# Binlayout · One release run should show whether publishing succeeded

An operator starts a GitHub release and sees a green run. Can they tell whether the crate was published? In Binlayout's original flow, the release job launched a separate workflow and finished. Its green result covered the launch. The publishing result lived in a second run. The upstream maintainer requested a single view of the requested tag and its downstream outcome. [Original issue #23](https://github.com/LunaStev/binlayout/issues/23)

## What changed

The manual workflow already verified the release before creating or reusing the GitHub release. The patch exposes the resolved tag as an output, then calls the existing publishing workflow as a dependent job. That workflow checks out the selected tag, resolves the commit, verifies it and checks the registry before publishing. The initiating run now contains the publishing jobs for that tag. The tag-push and standalone manual entry points remain in place, and an already-published crate version still skips the publishing step. [Reviewed PR #39](https://github.com/LunaStev/binlayout/pull/39) · [Initiating workflow at the merge](https://github.com/LunaStev/binlayout/blob/b2a825b6ee9f2e9f6a93f346ab442b4b7047065f/.github/workflows/github-release.yml) · [Publishing workflow at the merge](https://github.com/LunaStev/binlayout/blob/b2a825b6ee9f2e9f6a93f346ab442b4b7047065f/.github/workflows/release.yml)

## What the evidence supports

| Question | Observed evidence |
|---|---|
| Did the old workflow split the evidence? | In the recorded pre-change release, the [initiating run](https://github.com/LunaStev/binlayout/actions/runs/36326644015) listed verification and GitHub release jobs. The separate [publishing run](https://github.com/LunaStev/binlayout/actions/runs/36327486327) carried the publishing result. |
| Do the tests distinguish those two topologies? | On the merge commit, the offline suite passed 11/11. With only the two workflow definitions replaced by their exact parent versions, 9/11 passed and the two workflow-connection checks failed. Local Python 3.12, original test code and helper bytes held fixed, no credentials used. [Tests at merge](https://github.com/LunaStev/binlayout/blob/b2a825b6ee9f2e9f6a93f346ab442b4b7047065f/.github/scripts/test_release_workflows.py) · [Parent](https://github.com/LunaStev/binlayout/commit/a17c121985bb851cdd189afbd047d4b6dfbbfe85) |
| Did independent review and hosted CI pass? | Repository maintainer LunaStev approved #39, then it merged as `b2a825b6ee9f2e9f6a93f346ab442b4b7047065f`. All four jobs passed in the [PR-head fork run](https://github.com/SamCT86/binlayout/actions/runs/36461761154) and the [upstream merge run](https://github.com/LunaStev/binlayout/actions/runs/36504021539). |
| Did the new path publish a real release? | The two visible manual runs predate the merge. GitHub's latest tagged release at the time of this review, [v0.1.0](https://github.com/LunaStev/binlayout/releases/tag/v0.1.0), points to a commit eight commits before the merge. Hosted failure, cancellation and real publication under the merged flow remain unverified. |

The PR author is `SamCT86`. Sarmad directed the AI-assisted engineering work and is accountable for the findings and evidence presented here. LunaStev independently reviewed the change.

## What I would check in your workflow

Pick one handoff where green can mean “request accepted.” Trace the exact run, artifact or request ID to the final effect. Then exercise the downstream failure case in a permitted test environment and check that the report exposes it without counting a retry twice. For a release pipeline, start with the run URL and one version tag. [Describe a workflow where the final outcome is unclear](mailto:sarmadtawfeek@gmail.com?subject=AI%20agent%20reliability%20or%20CI%20evidence%20discussion).
