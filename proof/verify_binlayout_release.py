"""Reproduce the two exact public Binlayout release-audit findings."""

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from hashlib import sha256
from io import BytesIO
from urllib.request import Request, urlopen
import argparse
import json
import sys
import tarfile

REPOSITORY = "LunaStev/binlayout"
CRATE = "binlayout"
VERSION = "0.1.0"
SOURCE = "6cf1500c6f570ca42e7540e5c497fb6c4872efff"
PUBLISH_STEP = "Publish to crates.io"

SOURCES = {
    "historical_attempt": "https://api.github.com/repos/LunaStev/binlayout/actions/runs/36327486327/attempts/1",
    "historical_jobs": "https://api.github.com/repos/LunaStev/binlayout/actions/runs/36327486327/attempts/1/jobs",
    "tested_attempt": "https://api.github.com/repos/LunaStev/binlayout/actions/runs/36504021539/attempts/1",
    "tested_jobs": "https://api.github.com/repos/LunaStev/binlayout/actions/runs/36504021539/attempts/1/jobs",
    "release_tag": "https://api.github.com/repos/LunaStev/binlayout/git/ref/tags/v0.1.0",
    "registry_version": "https://crates.io/api/v1/crates/binlayout/0.1.0",
    "registry_index": "https://index.crates.io/bi/nl/binlayout",
    "registry_archive": "https://static.crates.io/crates/binlayout/binlayout-0.1.0.crate",
}
EXACT_ATTEMPTS = {
    "historical": (36327486327, 1, "9a6e8ef942564d9444223835012e1aa13823d225", ".github/workflows/release.yml"),
    "tested": (36504021539, 1, "b2a825b6ee9f2e9f6a93f346ab442b4b7047065f", ".github/workflows/ci.yml"),
}


# The recorded merge attempt has four distinct jobs. Bind each job to the
# verification it ran, since a successful job can contain skipped steps.
CARGO_TESTS = (
    "Run cargo test --locked",
    "Run cargo test --locked --no-default-features",
)
MERGE_CI_STEPS = {
    "test (stable)": (
        "Run python3 -m unittest discover -s .github/scripts -p 'test_*.py'",
        *CARGO_TESTS,
    ),
    "test (1.85.0)": CARGO_TESTS,
    "test-32-bit": (
        "Run cargo test --locked --target i686-unknown-linux-gnu",
        "Run cargo test --locked --target i686-unknown-linux-gnu --no-default-features",
    ),
    "lint": (
        "Run cargo fmt --check",
        "Run cargo clippy --locked --all-targets --all-features -- -D warnings",
        "Run cargo clippy --locked --all-targets --no-default-features -- -D warnings",
    ),
}


class EvidenceError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise EvidenceError(message)


def date(value):
    require(isinstance(value, str), "Missing event timestamp")
    moment = datetime.fromisoformat(value)
    require(moment.tzinfo is not None, "Event timestamp has no timezone")
    return moment


def exact_jobs(run, listing, expected):
    run_id, attempt, revision, _ = expected
    actual = (run["id"], run["run_attempt"], run["head_sha"], run["path"])
    require(run["repository"]["full_name"] == REPOSITORY and actual == expected, "Unexpected workflow run, attempt or source")
    require(run["status"] == "completed", "Workflow attempt is not complete")
    jobs = listing["jobs"]
    require(isinstance(jobs, list) and len(jobs) == listing["total_count"] > 0, "Incomplete workflow job listing")
    require(len({job["id"] for job in jobs}) == len(jobs), "Duplicate job records")
    require(all((job["run_id"], job["run_attempt"], job["head_sha"]) == (run_id, attempt, revision) for job in jobs), "Job belongs to a different attempt")
    for job in jobs:
        require(job["status"] == "completed", "Job is not terminal")
        steps = job.get("steps")
        require(isinstance(steps, list) and (steps or job["conclusion"] == "skipped"), "Missing step records for an executed job")
        require(all(step["status"] == "completed" for step in steps), "Job has nonterminal steps")
    return jobs


def registry_evidence(index, blob, version, tag):
    entries = [entry for entry in index if entry["name"] == CRATE and entry["vers"] == VERSION]
    require(len(entries) == 1, "Expected a unique registry index entry")
    require((version["crate"], version["num"]) == (CRATE, VERSION), "Unexpected registry version")
    digest = sha256(blob).hexdigest()
    require(digest == entries[0]["cksum"] == version["checksum"], "Registry digest mismatch")
    require(tag["ref"] == f"refs/tags/v{VERSION}" and tag["object"]["type"] == "commit", "Unexpected tag object")
    with tarfile.open(fileobj=BytesIO(blob), mode="r:gz") as archive:
        name = f"{CRATE}-{VERSION}/.cargo_vcs_info.json"
        matches = [member for member in archive.getmembers() if member.name == name]
        require(len(matches) == 1 and matches[0].isfile() and matches[0].size <= 4096, "Missing unambiguous archive provenance record")
        with archive.extractfile(matches[0]) as record:
            vcs = json.load(record)
    require(vcs["git"]["sha1"] == tag["object"]["sha"] == SOURCE, "Archive provenance differs from exact release tag")
    require(isinstance(version["yanked"], bool) and version["yanked"] == entries[0]["yanked"], "Registry reports conflict on yanked state")
    return {"version": VERSION, "sha256": digest, "source_commit": SOURCE, "created_at": version["created_at"], "yanked": version["yanked"]}


def publish_evidence(run, jobs, registry):
    steps = [(job, step) for job in jobs for step in job["steps"] if step["name"] == PUBLISH_STEP]
    if not steps:
        return {"publish": "NO_PUBLISH_STEP_IN_OBSERVED_ATTEMPT", "jobs": len(jobs)}
    require(len(steps) == 1, "Ambiguous publish step")
    job, step = steps[0]
    result = {"job_id": job["id"], "step_number": step["number"], "jobs": len(jobs)}
    if step["conclusion"] == "skipped":
        return {**result, "publish": "SKIPPED", "new_publication_established": False}
    if step["conclusion"] != "success":
        return {**result, "publish": step["conclusion"], "new_publication_established": False}

    started, ended, created = (date(value) for value in (step["started_at"], step["completed_at"], registry["created_at"]))
    require(started <= ended, "Publish step interval out of order")
    return {**result, "publish": "SUCCESS_RECORDED", "registry_created_during_step": started <= created <= ended,
            "run_conclusion": run["conclusion"], "job_conclusion": job["conclusion"]}


def require_merge_ci(run, jobs):
    job_names = {job["name"] for job in jobs}
    require(len(jobs) == len(MERGE_CI_STEPS) and job_names == MERGE_CI_STEPS.keys(),
            "Merge CI does not contain the four expected verification jobs")
    require(run["conclusion"] == "success", "Merge CI did not succeed")
    for job in jobs:
        name = job["name"]
        require(job["conclusion"] == "success", f"Merge CI job did not succeed: {name}")
        for required_step in MERGE_CI_STEPS[name]:
            conclusions = [step["conclusion"] for step in job["steps"] if step["name"] == required_step]
            require(conclusions == ["success"], f"Merge CI {name}: expected one successful {required_step}")


def inspect(data):
    registry = registry_evidence(
        [json.loads(line) for line in data["registry_index"].splitlines() if line.strip()],
        data["registry_archive"], data["registry_version"]["version"], data["release_tag"],
    )
    report = {"registry": registry}
    for label, identity in EXACT_ATTEMPTS.items():
        run = data[label + "_attempt"]
        jobs = exact_jobs(run, data[label + "_jobs"], identity)
        report[label] = {"run_id": run["id"], "attempt": run["run_attempt"], "workflow_commit": run["head_sha"],
                         "workflow": run["path"], **publish_evidence(run, jobs, registry)}

    historical = report["historical"]
    require(historical["publish"] == "SUCCESS_RECORDED" and historical["job_id"] == 108643013538,
            "Historical publish job no longer shows the recorded successful step")
    require(historical["registry_created_during_step"], "Registry creation falls outside the historical publish step")

    tested = report["tested"]
    require(tested["publish"] == "NO_PUBLISH_STEP_IN_OBSERVED_ATTEMPT",
            "Merge CI unexpectedly contains a publish step")
    require_merge_ci(data["tested_attempt"], data["tested_jobs"]["jobs"])
    return report


def parse_sources(entries):
    raw_keys = {"registry_index", "registry_archive"}
    return {name: raw if name in raw_keys else json.loads(raw) for name, raw in entries}


def request(entry):
    name, url = entry
    try:
        with urlopen(Request(url, headers={"User-Agent": "SamCT86-binlayout-release-audit"}), timeout=20) as response:
            raw = response.read(1_000_001)
    except OSError as error:
        raise EvidenceError(f"Could not read {name}: {error}") from error
    require(len(raw) <= 1_000_000, f"Response too large: {name}")
    return name, raw


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    try:
        with ThreadPoolExecutor(max_workers=len(SOURCES)) as pool:
            report = inspect(parse_sources(pool.map(request, SOURCES.items())))
    except (OSError, KeyError, TypeError, ValueError, tarfile.TarError) as error:
        print(f"UNVERIFIED: {error}", file=sys.stderr)
        return 2
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
