# Work with Sarmad — AI-native delivery with inspectable evidence

If your automation can act twice, your CI can turn green without proving the important behavior, or your AI-assisted implementation is hard to review, I can help you frame a **small, testable technical engagement**.

My role is to define the problem, direct AI-agent implementation, establish acceptance criteria, challenge results with negative controls, and account for what evidence actually supports. AI agents write hands-on implementation code. Independent qualified reviewers should assess security-critical code where warranted. No previous paid engagement, customer result or particular response time is implied here.

## Option A — Reliability / CI evidence audit

If a green run can mean only that a job started, I'll trace one workflow from the triggering commit to the result your team needs to verify, such as a package reaching its registry. The review starts with existing logs and source.

- **Send one example.** Share a public workflow or run URL and the result you expected it to prove. For a private workflow, start with a brief description and share access through your own approved route after we agree scope.
- **Get a decision you can act on.** You'll receive the exact commit, check and output examined, the most consequential gap and a prioritized fix. I include a repeatable check where the evidence permits it and identify any missing access or data separately.
- **Accept the review when your engineer can follow the evidence.** They can locate the source and runs behind each finding, repeat the check for a confirmed gap, and see the next change to make.

[**Send one workflow and the result you need to verify**](mailto:sarmadtawfeek@gmail.com?subject=One-workflow%20CI%20evidence%20review&body=Public%20workflow%20or%20run%20URL%20%28or%20short%20description%29%3A%0AExpected%20result%3A%0A%0APlease%20leave%20out%20credentials%20and%20confidential%20material.)

### CI audit sample

**Question:** Did Binlayout v0.1.0 reach crates.io, and what did CI on the newer revision prove?

| Verdict | Evidence | Decision |
| --- | --- | --- |
| Historical publication confirmed | The [release job](https://github.com/LunaStev/binlayout/actions/runs/36326644015/job/108640668072) created the tag and release. A separate [publish job](https://github.com/LunaStev/binlayout/actions/runs/36327486327/job/108643013538) succeeded, and the [registry](https://crates.io/crates/binlayout/0.1.0) lists the exact version. | Verify publication with the job and the received version. |
| New workflow reviewed and tested | The maintainer approved [PR #39](https://github.com/LunaStev/binlayout/pull/39). The new path connects the release and publishing jobs. [Merge CI](https://github.com/LunaStev/binlayout/actions/runs/36504021539) ran the release-workflow tests. | Verify publishing and registry readback on the next new version. Check whether old tags contain the release helpers before retrying. |

[Run the recorded audit yourself](proof/binlayout-release-evidence.md#run-the-audit-yourself) or [inspect the commit and negative controls](proof/binlayout-release-evidence.md).

## Option B — One-defect fix sprint

**Best for:** a narrow, high-impact reliability or security-adjacent bug with accessible code and clear ownership.

**Bounded scope:** one accepted issue, one agreed repository and explicit test/runtime access. A new feature, production credentials, schema migration or broad refactor is not silently included.

**Proposed deliverable:**

- The failing behavior reproduced on an exact baseline when feasible.
- A minimal, reviewable patch and at least one negative control that catches a misleading green result.
- Relevant tests and hosted CI; a source-bound report of failures and omissions.
- Review-ready PR or permitted handoff, with rollback plan; merge/deployment only under the owner's authority.

**Acceptance:** agreed target behavior demonstrably changes RED → GREEN, no named negative control regresses, and known limitations are explicit. An unreviewed patch does not equal production-safe delivery.

## Option C — AI-agent evidence trial

**Best for:** a founder or engineering team exploring one agent-mediated workflow without committing to a large architecture or automation platform.

**Bounded scope:** one workflow, one externally observable outcome, bounded test inputs and access. Start with a synthetic or isolated sandbox; production invocation and API spend need separate approval and measurable caps.

**Proposed deliverable:**

- A clear task → authorized action → original-provider evidence → decision diagram.
- A runnable prototype or evaluation harness using synthetic fixtures.
- Tests for ambiguous outcome, duplicate request, stale evidence and failed readback where relevant.
- A go/no-go statement stating what remains unverified before a live pilot.

**Acceptance:** the test harness can reproduce the agreed success and failure cases, with no unsupported claims of provider attestation or real customer outcomes.

## Why these are credible starting points

Independently accepted OSS contributions include [a job option aliasing fix](proof/dispatchat-slice-aliasing.md), [fail-before-write module validation](proof/go-module-validation.md), and [SQLite reset semantics](proof/sqlite-schema-reset.md). They prove specific reviewed work, not blanket expertise in every platform or claimed customer deployment.

## Contact

[**Email a focused engagement question**](mailto:sarmadtawfeek@gmail.com?subject=AI%20reliability%20engagement) or [contact me on LinkedIn](https://www.linkedin.com/in/sarmad-lundberg-tawfeek-496197207/) with the public repo/workflow, the failure or goal, and what acceptance would look like. Do **not** send credentials, customer data, private URLs or confidential source in an initial message.

Scope, permissions, terms, price, payment entity and timelines are agreed separately by the authorized owners. These options are examples, not binding offers or verified market demand.
