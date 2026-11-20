# Binlayout · One release run should show whether publishing succeeded

An operator starts a GitHub release and sees a green run. Can they tell whether the crate was published? The recorded v0.1.0 release used two manual runs. The later workflow version immediately before the fix triggered publishing in a separate run and could finish while publishing was pending. The maintainer requested a single view of the requested tag and its downstream outcome. [Original issue #23](https://github.com/LunaStev/binlayout/issues/23)

## What changed

The manual workflow already verified the release before creating or reusing the GitHub release. The patch exposes the resolved tag as an output, then calls the existing publishing workflow as a dependent job. That workflow checks out the selected tag, resolves the commit, verifies it and checks the registry before publishing. The initiating run now contains the publishing jobs for that tag. The workflow keeps the tag-push and standalone manual entry points. Its registry check skips the publish step when it finds the version. [Reviewed PR #39](https://github.com/LunaStev/binlayout/pull/39) · [Initiating workflow at the merge](https://github.com/LunaStev/binlayout/blob/b2a825b6ee9f2e9f6a93f346ab442b4b7047065f/.github/workflows/github-release.yml) · [Publishing workflow at the merge](https://github.com/LunaStev/binlayout/blob/b2a825b6ee9f2e9f6a93f346ab442b4b7047065f/.github/workflows/release.yml)

## What the evidence supports

| Question | Observed evidence |
|---|---|
| Did the old workflow split the evidence? | The [GitHub release job](https://github.com/LunaStev/binlayout/actions/runs/36326644015/job/108640668072) ended at 14:39:11 UTC. A separate [manual publishing job](https://github.com/LunaStev/binlayout/actions/runs/36327486327/job/108643013538) recorded a successful `Publish to crates.io` step at 14:53:02 UTC. The [later pre-fix source](https://github.com/LunaStev/binlayout/blob/a17c121985bb851cdd189afbd047d4b6dfbbfe85/.github/workflows/github-release.yml) dispatched a separate workflow. |
| Do the tests distinguish those two topologies? | On the merge commit, the offline suite passed 11/11. With only the two workflow definitions replaced by their exact parent versions, 9/11 passed and the two workflow-connection checks failed. Local Python 3.12, original test code and helper bytes held fixed, no credentials used. [Tests at merge](https://github.com/LunaStev/binlayout/blob/b2a825b6ee9f2e9f6a93f346ab442b4b7047065f/.github/scripts/test_release_workflows.py) · [Parent](https://github.com/LunaStev/binlayout/commit/a17c121985bb851cdd189afbd047d4b6dfbbfe85) |
| Did independent review and hosted CI pass? | Repository maintainer [LunaStev approved #39](https://github.com/LunaStev/binlayout/pull/39#pullrequestreview-5346324297), then it merged as `b2a825b6ee9f2e9f6a93f346ab442b4b7047065f`. All four jobs passed in the [PR-head fork run](https://github.com/SamCT86/binlayout/actions/runs/36461761154) and the [upstream merge run](https://github.com/LunaStev/binlayout/actions/runs/36504021539). |
| What package reached the registry? | [crates.io records v0.1.0](https://crates.io/crates/binlayout/0.1.0) at 14:53:01 UTC on 27 September 2026. The downloaded crate matched the [registry index checksum](https://index.crates.io/bi/nl/binlayout). Its embedded Git SHA matches the [release tag](https://github.com/LunaStev/binlayout/releases/tag/v0.1.0) at `6cf1500`, eight commits before #39 merged. |
| Did the new path publish a release? | The v0.1.0 publication predates the merge. The upstream merge run contains four verification jobs. Hosted failure, cancellation and first-time publication under the merged flow remain unverified. |

### A retry can fail before the registry check

At the merge, the resolve job checks out the requested tag and then runs `.github/scripts/resolve_release.py` from that checkout. The historical [v0.1.0 tree](https://github.com/LunaStev/binlayout/tree/6cf1500c6f570ca42e7540e5c497fb6c4872efff/.github) predates the helper. Running the first helper command against the tag's files failed locally because the file was missing. A hosted retry remains unverified. [Resolve job at the merge](https://github.com/LunaStev/binlayout/blob/b2a825b6ee9f2e9f6a93f346ab442b4b7047065f/.github/workflows/release.yml#L35-L44)

The PR author is `SamCT86`. Sarmad directed the AI-assisted engineering work and is accountable for the findings and evidence presented here. LunaStev independently reviewed the change.

## What I would check in your workflow

For a release review, send the initiating run URL and one version tag. On Binlayout, the [registry check and publish steps](https://github.com/LunaStev/binlayout/blob/b2a825b6ee9f2e9f6a93f346ab442b4b7047065f/.github/workflows/release.yml#L62-L69) give three materially different answers.

| What the run shows | What I would report |
|---|---|
| `Publish to crates.io` ran and succeeded | GitHub recorded a successful publish step. Read back that exact crate version from the registry. |
| `Publish to crates.io` was skipped after the registry check found the version | The version already existed. A green run here is a successful no-op. |
| Publishing failed, was cancelled, or was skipped without confirmed registry existence | The run leaves publication unconfirmed. Check the registry independently before deciding whether to retry. |

For source provenance, compare the downloaded archive's SHA-256 with the registry index and the commit reported in `.cargo_vcs_info.json` with the GitHub tag target. For `v0.1.0`, the checksum was `f350bdd1984438a38e9559075e1573fbb4278670d04348e7dc7b5081553de08d` and both commit references resolved to `6cf1500c6f570ca42e7540e5c497fb6c4872efff`. [See the scope of a one-workflow review](../WORK_WITH_ME.md#option-a--reliability--ci-evidence-audit).

## Run the audit yourself

Open the [pinned verifier](https://raw.githubusercontent.com/SamCT86/SamCT86/bc85b205f0ce8995ba0a219696de3ce396b44f12/proof/verify_binlayout_release.py) and save it as `verify_binlayout_release.py`. Run it from that folder with Python 3.11 or later.

On Linux or macOS, run

```sh
python3 verify_binlayout_release.py
```

In Windows PowerShell, run

```powershell
py -3 verify_binlayout_release.py
```

If Windows has Python installed without the `py` launcher, use `python verify_binlayout_release.py`.

The verifier reads eight public GitHub and crates.io sources, pins both run attempts to their workflow revisions, and compares the crate checksum and embedded commit with the registry records and release tag. It uses the Python standard library, needs no credentials, and reads the crate metadata without installing it.

| Check | Expected evidence |
|---|---|
| Historical publish attempt `36327486327/1` | `SUCCESS_RECORDED`. The registry's creation timestamp falls within the recorded publish step. The original [publish job](https://github.com/LunaStev/binlayout/actions/runs/36327486327/job/108643013538) also logs the publication. |
| Merge CI attempt `36504021539/1` | `NO_PUBLISH_STEP_IN_OBSERVED_ATTEMPT`. Four verification jobs ran. A hosted publication from the changed release workflow still needs its own receipt. |

The result covers these recorded attempts. Missing, inconsistent or inaccessible sources produce `UNVERIFIED` and exit code 2. If an upstream API rate-limits the request, retry after its limit resets.
