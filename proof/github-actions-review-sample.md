# GitHub Actions review sample

**Decision.** Use the Binlayout check to verify the audit script's behavior. Confirm the actual release through the publishing run and the package registry. A reviewer can reproduce both decisions from public sources.

**Scope.** One workflow in this portfolio, its offline tests, and the two public Binlayout runs the audit examines. Sarmad sets the scope for the AI-assisted portfolio work. The sources below show the checks behind the findings.

| Priority | Finding | Evidence and action |
| --- | --- | --- |
| High for an automated consumer | The audit could exit successfully when a recorded publish step was missing or skipped, or when the registry timestamp fell outside the step. A script that only looked at the exit code could accept the wrong conclusion. | [PR #28](https://github.com/SamCT86/SamCT86/pull/28) makes exit 0 contingent on both expected results. Six changed-evidence cases now exit 2 with `UNVERIFIED`. [Regression cases](https://github.com/SamCT86/SamCT86/blob/bc85b205f0ce8995ba0a219696de3ce396b44f12/proof/test_verify_binlayout_release.py#L57-L77) · [GitHub Actions job](https://github.com/SamCT86/SamCT86/actions/runs/44787182263/job/136465012710). |
| Reviewed control | The workflow runs offline checks on pull requests and pushes to main. It declares `contents: read`, pins Checkout to a full commit SHA, and disables credential persistence. The job has no publish step. | [Workflow at the tested commit](https://github.com/SamCT86/SamCT86/blob/bc85b205f0ce8995ba0a219696de3ce396b44f12/.github/workflows/binlayout-audit.yml#L3-L25). Retain those permissions for the offline check. Review the approval and workflow ownership separately before relying on it for a protected merge. |
| Evidence limit | The hosted tests confirm how the verifier classifies selected inputs. The actual publishing claim comes from a different job and the registry. | The [historical job](https://github.com/LunaStev/binlayout/actions/runs/36327486327/job/108643013538) records publishing v0.1.0. The [registry version](https://crates.io/api/v1/crates/binlayout/0.1.0) and archive checksum support that claim. The [later Binlayout run](https://github.com/LunaStev/binlayout/actions/runs/36504021539) contains four verification jobs. None of them published a package. |

## Reproduce the result

[Run the pinned verifier](binlayout-release-evidence.md#run-the-audit-yourself). A successful run reports `SUCCESS_RECORDED` for the historical publish and `NO_PUBLISH_STEP_IN_OBSERVED_ATTEMPT` for the later verification run.

## A successful evidence collector with a partial report

In [TrustPR's first-party consumer PR](https://github.com/SamCT86/trustpr-consumer-canary/pull/6), a [read-only workflow at the PR commit](https://github.com/SamCT86/trustpr-consumer-canary/blob/b4a85b7c352d924b57d4ad0ddd9bc0db11c23d5b/.github/workflows/trustpr.yml) ran a pinned Action against the proposed change. The [GitHub-hosted collector job](https://github.com/SamCT86/trustpr-consumer-canary/actions/runs/39475939069/job/118811794878) succeeded and recorded `PARTIAL`, `UNAUTHENTICATED` and `POLICY_UNBOUND`. The [published example](https://github.com/SamCT86/trustpr-action/blob/6457de77ff1a3666674fac5e48dc6ec11f85186e/REAL-PUBLIC-EXAMPLE.md) explains which check it saw. The receipt records no established test execution or merge authorization. The PR was closed without merging.

## What I would examine in an agent workflow

I would trace the trigger and data sources through the job's token, secrets, runtime and outbound actions. For any step that reads issue text or web pages, I would trace where that content can affect commands, file writes or external actions. Each finding would cite the workflow and step, explain the observed impact and give a way to verify the proposed change.
