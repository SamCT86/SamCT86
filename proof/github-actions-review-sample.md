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

## GitHub release and registry evidence

SeraPlot's [v2.8.7 release job](https://github.com/feur25/Sera/actions/runs/40190234399/job/121163246988) passed. Its [GitHub release](https://github.com/feur25/Sera/releases/tag/v2.8.7) contains a Linux wheel and a macOS wheel. Both wheels report `seraplot 2.8.7.post1` in their embedded package metadata. On 22 November 2026, the [exact PyPI version](https://pypi.org/project/seraplot/2.8.7.post1/#files) listed a Windows CPython 3.11 wheel and a source distribution. The [maintainer's issue](https://github.com/feur25/Sera/issues/22) tracks the missing PyPI step.

For the next release, check the tag against the wheel version before upload. Then compare the published filenames and SHA-256 digests with the staged wheels.

## Keep release notes tied to the shipped package

A failed [Gutenberg release job](https://github.com/WordPress/gutenberg/actions/runs/31575283775/job/94046967379) had already published packages before a Git backport stopped. The npm archives for [Components 39.0.0](https://registry.npmjs.org/@wordpress%2fcomponents/39.0.0) and [DataViews 18.0.0](https://registry.npmjs.org/@wordpress%2fdataviews/18.0.0) matched the registry hashes and contained the exact changelog bytes from the [published commit](https://github.com/WordPress/gutenberg/commit/989764d42ff93e33684aaf0b96a5b7f3d9bbff52).

**Finding.** The [first correction attempt](https://github.com/WordPress/gutenberg/commit/d36bccf8ca2069f0e058feb36c88e2840eeb414c) changed the released sections in four of 125 package changelogs. The [merged correction](https://github.com/WordPress/gutenberg/pull/81502) restored those sections. The failure and proposed check were previously documented in [Gutenberg #81506](https://github.com/WordPress/gutenberg/issues/81506).

**Decision.** Compare released sections with the published commit before pushing a backport. Push the exact revision that passed. An AI-assisted local prototype rejected a clean cherry-pick that silently moved an unreleased entry into a shipped version. It also pushed the verified revision when a synthetic local branch moved after inspection. Upstream review and hosted testing would precede adoption.


## What I would examine in an agent workflow

I would trace the trigger and data sources through the job's token, secrets, runtime and outbound actions. For any step that reads issue text or web pages, I would trace where that content can affect commands, file writes or external actions. Each finding would cite the workflow and step, explain the observed impact and give a way to verify the proposed change.
