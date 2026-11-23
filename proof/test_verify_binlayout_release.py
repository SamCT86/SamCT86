from contextlib import redirect_stderr, redirect_stdout
from hashlib import sha256
import io
import json
import tarfile
import unittest
from unittest.mock import patch

import verify_binlayout_release as verifier


def attempt(label, job_ids, publish_conclusion=None):
    run_id, number, commit, workflow = verifier.EXACT_ATTEMPTS[label]
    source = {"run_attempt": number, "head_sha": commit}
    run = dict(source, id=run_id, path=workflow, status="completed", conclusion="success",
               repository={"full_name": verifier.REPOSITORY})
    jobs = [
        dict(source, id=job_id, run_id=run_id, status="completed", conclusion="success",
             steps=[{"name": "Check evidence", "status": "completed", "conclusion": "success"}])
        for job_id in job_ids
    ]
    if label == "tested":
        named_steps = (
            ("test (stable)", ("Run python3 -m unittest discover -s .github/scripts -p 'test_*.py'",
                               "Run cargo test --locked", "Run cargo test --locked --no-default-features")),
            ("test (1.85.0)", ("Run cargo test --locked", "Run cargo test --locked --no-default-features")),
            ("test-32-bit", ("Run cargo test --locked --target i686-unknown-linux-gnu",
                             "Run cargo test --locked --target i686-unknown-linux-gnu --no-default-features")),
            ("lint", ("Run cargo fmt --check",
                      "Run cargo clippy --locked --all-targets --all-features -- -D warnings",
                      "Run cargo clippy --locked --all-targets --no-default-features -- -D warnings")),
        )
        for job, (name, steps) in zip(jobs, named_steps):
            job["name"] = name
            job["steps"] = [
                {"name": step, "status": "completed", "conclusion": "success"} for step in steps
            ]
    if publish_conclusion is not None:
        jobs[0]["steps"].append({
            "name": verifier.PUBLISH_STEP,
            "number": 5,
            "status": "completed",
            "conclusion": publish_conclusion,
            "started_at": "2026-09-27T14:53:00Z",
            "completed_at": "2026-09-27T14:53:02Z",
        })
    return {label + "_attempt": run, label + "_jobs": {"total_count": len(jobs), "jobs": jobs}}


def registry_fixture(*, embedded_commit=verifier.SOURCE):
    record = json.dumps({"git": {"sha1": embedded_commit}}).encode()
    payload = io.BytesIO()
    with tarfile.open(fileobj=payload, mode="w:gz") as archive:
        member = tarfile.TarInfo(f"{verifier.CRATE}-{verifier.VERSION}/.cargo_vcs_info.json")
        member.size = len(record)
        archive.addfile(member, io.BytesIO(record))

    blob = payload.getvalue()
    digest = sha256(blob).hexdigest()
    index = [{"name": verifier.CRATE, "vers": verifier.VERSION, "cksum": digest, "yanked": False}]
    version = {
        "crate": verifier.CRATE,
        "num": verifier.VERSION,
        "checksum": digest,
        "created_at": "2026-09-27T14:53:01Z",
        "yanked": False,
    }
    tag = {"ref": f"refs/tags/v{verifier.VERSION}", "object": {"type": "commit", "sha": verifier.SOURCE}}
    return index, blob, version, tag


class RegistryEvidenceTest(unittest.TestCase):
    def test_archive_bytes_and_source_match(self):
        index, blob, version, tag = registry_fixture()
        result = verifier.registry_evidence(index, blob, version, tag)
        self.assertEqual(result["sha256"], sha256(blob).hexdigest())
        self.assertEqual(result["source_commit"], verifier.SOURCE)

    def test_registry_index_checksum_conflicts(self):
        index, blob, version, tag = registry_fixture()
        index[0]["cksum"] = "0" * 64
        with self.assertRaisesRegex(verifier.EvidenceError, "Registry digest mismatch"):
            verifier.registry_evidence(index, blob, version, tag)

    def test_registry_api_checksum_conflicts(self):
        index, blob, version, tag = registry_fixture()
        version["checksum"] = "0" * 64
        with self.assertRaisesRegex(verifier.EvidenceError, "Registry digest mismatch"):
            verifier.registry_evidence(index, blob, version, tag)

    def test_valid_checksum_cannot_prove_a_different_embedded_commit(self):
        index, blob, version, tag = registry_fixture(embedded_commit="f" * 40)
        with self.assertRaisesRegex(verifier.EvidenceError, "Archive provenance differs"):
            verifier.registry_evidence(index, blob, version, tag)


class AuditExitStatusTest(unittest.TestCase):
    def run_audit(self, *, historical_publish="success", tested_publish=None,
                  created_at="2026-09-27T14:53:01Z", tested_ids=(1, 2, 3, 4),
                  tested_conclusion="success", mutate_jobs=None, historical_run="success", historical_job="success"):
        data = {
            **attempt("historical", (108643013538,), historical_publish),
            **attempt("tested", tested_ids, tested_publish),
            "registry_index": b"",
            "registry_archive": b"",
            "registry_version": {"version": {}},
            "release_tag": {},
        }
        data["tested_attempt"]["conclusion"] = tested_conclusion
        data["historical_attempt"]["conclusion"] = historical_run
        data["historical_jobs"]["jobs"][0]["conclusion"] = historical_job
        if mutate_jobs is not None:
            mutate_jobs(data["tested_jobs"]["jobs"])
        stdout, stderr = io.StringIO(), io.StringIO()
        with (
            patch("sys.argv", ["verify_binlayout_release.py"]),
            patch.object(verifier, "request", side_effect=lambda entry: entry),
            patch.object(verifier, "parse_sources", return_value=data),
            patch.object(verifier, "registry_evidence", return_value={"created_at": created_at}),
            redirect_stdout(stdout),
            redirect_stderr(stderr),
        ):
            status = verifier.main()
        return status, stdout.getvalue(), stderr.getvalue()

    def test_both_expected_outcomes_exit_zero(self):
        status, stdout, stderr = self.run_audit()
        self.assertEqual((status, stderr), (0, ""))
        report = json.loads(stdout)
        self.assertTrue(report["historical"]["registry_created_during_step"])
        self.assertEqual(report["tested"]["publish"], "NO_PUBLISH_STEP_IN_OBSERVED_ATTEMPT")

    def test_green_job_totals_do_not_prove_the_expected_work_ran(self):
        def drop_job_identity(jobs):
            jobs[0]["name"] = "Unrelated job"

        def skip_core_step(jobs):
            jobs[0]["steps"][0]["conclusion"] = "skipped"

        def omit_core_step(jobs):
            jobs[0]["steps"].pop(0)

        def duplicate_core_step(jobs):
            jobs[0]["steps"].append(dict(jobs[0]["steps"][0]))

        for change in (drop_job_identity, skip_core_step, omit_core_step, duplicate_core_step):
            with self.subTest(change=change.__name__):
                status, stdout, stderr = self.run_audit(mutate_jobs=change)
                self.assertEqual((status, stdout), (2, ""))
                self.assertTrue(stderr.startswith("UNVERIFIED: "))

    def test_failed_historical_run_or_job_cannot_exit_zero(self):
        for case in ({"historical_run": "failure"}, {"historical_job": "failure"}):
            with self.subTest(**case):
                status, stdout, stderr = self.run_audit(**case)
                self.assertEqual((status, stdout), (2, ""))
                self.assertIn("UNVERIFIED:", stderr)

    def test_changed_evidence_exits_unverified(self):
        cases = {
            "missing historical step": {"historical_publish": None},
            "skipped historical step": {"historical_publish": "skipped"},
            "registry timestamp outside the step": {"created_at": "2026-09-27T15:00:00Z"},
            "failed merge CI": {"tested_conclusion": "failure"},
            "missing merge job": {"tested_ids": (1, 2, 3)},
            "unexpected merge publish step": {"tested_publish": "skipped"},
        }
        for label, inputs in cases.items():
            with self.subTest(label=label):
                status, stdout, stderr = self.run_audit(**inputs)
                self.assertEqual((status, stdout), (2, ""))
                self.assertTrue(stderr.startswith("UNVERIFIED: "))
