from contextlib import redirect_stderr, redirect_stdout
import io
import json
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


class AuditExitStatusTest(unittest.TestCase):
    def run_audit(self, *, historical_publish="success", tested_publish=None,
                  created_at="2026-09-27T14:53:01Z", tested_ids=(1, 2, 3, 4),
                  tested_conclusion="success"):
        data = {
            **attempt("historical", (108643013538,), historical_publish),
            **attempt("tested", tested_ids, tested_publish),
            "registry_index": b"",
            "registry_archive": b"",
            "registry_version": {"version": {}},
            "release_tag": {},
        }
        data["tested_attempt"]["conclusion"] = tested_conclusion
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
