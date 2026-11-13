# Work with Sarmad — AI-native delivery with inspectable evidence

If your automation can act twice, your CI can turn green without proving the important behavior, or your AI-assisted implementation is hard to review, I can help you frame a **small, testable technical engagement**.

My role is to define the problem, direct AI-agent implementation, establish acceptance criteria, challenge results with negative controls, and account for what evidence actually supports. AI agents write hands-on implementation code. Independent qualified reviewers should assess security-critical code where warranted. No previous paid engagement, customer result or particular response time is implied here.

## Option A — Reliability / CI evidence audit

**Best for:** a team unsure whether CI/release checks or an agent workflow actually enforce its stated safeguards.

**Bounded scope:** one repository or one clearly identified workflow, agreed upfront. Read-only source/evidence review by default; any live exploit reproduction or privileged configuration change requires separate authorized scope.

**Proposed deliverable:**

- A map of the claimed trust boundary and the exact source/checks that implement it.
- Two or three high-impact falsifiers grounded in real failure modes, such as PR-editable workflow trust, skipped/neutral jobs, lost acknowledgements and duplicate effects.
- A prioritized findings register: confirmed defect vs plausible risk vs unknown, with reproducible steps when safe.
- An owner-facing decision: repair now, accept documented risk, or stop under-evidenced claims.

**Acceptance:** the client can reproduce each confirmed finding, trace it to source and understand the remaining unknowns. This is not a security certification or penetration-test guarantee.

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
