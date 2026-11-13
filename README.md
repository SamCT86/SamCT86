# Sarmad Tawfeek

**AI-native product builder · Agent orchestration · Reliability and evidence-first delivery**

Stockholm, Sweden

**I turn AI-assisted software work into technical outcomes that other engineers can inspect, test and challenge.** I define the problem and acceptance criteria, orchestrate AI agents that write implementation code, evaluate evidence and failure modes, and take responsibility for technical-product decisions and the claims I publish.

**I can help with a scoped agent-reliability review, CI evidence audit or review-ready fix sprint.** If your team has a workflow that might act twice, a merge check whose trust boundary is unclear, or an AI-assisted implementation that's hard to evaluate, [email me a short description](mailto:sarmadtawfeek@gmail.com?subject=AI%20agent%20reliability%20or%20CI%20evidence%20discussion), [connect on LinkedIn](https://www.linkedin.com/in/sarmad-lundberg-tawfeek-496197207/) or [visit my website](https://www.sarmadtawfeek.com). No credentials or confidential files in the initial message.

## Three independently reviewed engineering outcomes

I have **11 merged upstream pull requests across three independently maintained open-source projects** (verified against GitHub on 13 November 2026). These selected examples show specific problems, changes and maintainer decisions—not a claim that I personally typed the code.

**1. A scheduler silently lost a job uniqueness guard.** A shared Go option slice could be overwritten during scheduling. A one-line capacity-bound fix and regression test preserve the caller's `Unique` option. [Gombit #521 — approved and merged](https://github.com/gombit-dev/gombit/pull/521) · [How it was tested](proof/dispatchat-slice-aliasing.md).

**2. SQLite schema reset could leave user tables behind.** `_` in SQL `LIKE` is a wildcard, so an unsafe filter treated names such as `sqlitex_cache` as reserved. A precise escape and native SQLite test check both user objects and `sqlite_sequence`. [Gombit #651 — approved and merged](https://github.com/gombit-dev/gombit/pull/651) · [How it was tested](proof/sqlite-schema-reset.md).

**3. A generator accepted Go module paths that later failed to build.** Go-native module validation now runs before creating the destination; the patch passed two rounds of requested maintainer changes. [Gombit #563 — approved and merged](https://github.com/gombit-dev/gombit/pull/563) · [How it was tested](proof/go-module-validation.md).

[Browse all independently merged contributions](https://github.com/pulls?q=is%3Apr+author%3ASamCT86+is%3Amerged+-user%3ASamCT86) · [Gombit review history](https://github.com/gombit-dev/gombit/pulls?q=is%3Apr+author%3ASamCT86+is%3Amerged) · [Binlayout](https://github.com/LunaStev/binlayout/pulls?q=is%3Apr+author%3ASamCT86+is%3Amerged) · [OpenMuse](https://github.com/tahodev/openmuse/pulls?q=is%3Apr+author%3ASamCT86+is%3Amerged)

## Open engineering work you can inspect

**[TrustPR — evidence receipts for pull requests](https://github.com/SamCT86/trustpr-action).** A free MIT-licensed GitHub Action that reports observed diff/check evidence and what's unknown. [Install guide](https://github.com/SamCT86/trustpr-action/blob/main/START-HERE.md) · [Marketplace listing](https://github.com/marketplace/actions/trustpr-evidence-receipt). The current v0.1.1 prerelease is **not** an independent security gate: [PR-editable workflow and required-check trust remain unresolved](https://github.com/SamCT86/trustpr-action/issues/53).

**[MachineOutcome — reconcile before retry](https://github.com/SamCT86/machineoutcome-case-study).** Public MIT-licensed synthetic demo of a difficult distributed-systems case: a timeout does not prove that an external side effect failed. [Run the browser demo](https://samct86.github.io/machineoutcome-case-study/). The private runtime is separate; no live customer outcome is claimed.

**[Transaction Lab — unsafe retries and duplicate effects](https://github.com/SamCT86/agent-cash-cow-os).** An inspectable synthetic evaluation of payment-timeout scenarios, provider readback and replay decisions. [Open the lab](https://www.sarmadtawfeek.com/agent-cash-cow). It is not a production payment processor.

## How I approach a technical problem

**Reproduce the failure → choose the smallest testable change → challenge the fix with negative controls → run the relevant checks → seek independent review → state the exact outcome and remaining risk.**

My contribution is **problem framing, AI-agent direction, acceptance criteria, evidence evaluation, technical-product judgment and delivery accountability**. AI agents perform hands-on implementation coding. For risk-critical code or security-sensitive changes, qualified independent code review remains important; successful tests alone are not a safety certificate.

## Work with me

**Potential starting points:** an Agent Reliability/CI Evidence Audit, a tightly scoped bug-fix sprint, or an AI-native product trial with measurable acceptance criteria. The right scope and commercial terms depend on your problem; I do not imply previous paid engagements or customer adoption without evidence.

**[Compare three bounded engagement options](WORK_WITH_ME.md)** · **[Email a concrete problem](mailto:sarmadtawfeek@gmail.com?subject=Scope%20a%20technical%20engagement)** · [LinkedIn](https://www.linkedin.com/in/sarmad-lundberg-tawfeek-496197207/) · [Website](https://www.sarmadtawfeek.com)
