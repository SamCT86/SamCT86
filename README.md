# Sarmad Tawfeek

**AI-native product builder · Agent orchestration · Reliability and evidence-first delivery**

Stockholm, Sweden

**Does a green CI run prove your release actually shipped?** I review one workflow, trace what happened, and show the first gap worth fixing. [See the reviewed release case](proof/binlayout-release-evidence.md). [Email one workflow and the result you need to verify](mailto:sarmadtawfeek@gmail.com?subject=One-workflow%20CI%20evidence%20review&body=Public%20workflow%20or%20run%20URL%20%28or%20short%20description%29%3A%0AExpected%20result%3A%0A%0APlease%20leave%20out%20credentials%20and%20confidential%20material.) or [see a sample audit](WORK_WITH_ME.md#ci-audit-sample).

**I turn AI-assisted software work into technical outcomes that other engineers can inspect, test and challenge.** I define the problem and acceptance criteria, orchestrate AI agents that write implementation code, evaluate evidence and failure modes, and take responsibility for technical-product decisions and the claims I publish.

## Three independently reviewed engineering outcomes

I have **11 merged upstream pull requests across three independently maintained open-source projects** (verified against GitHub on 17 November 2026). These selected examples show specific problems, changes and maintainer decisions—not a claim that I personally typed the code.

**1. A green release run could finish before package publishing did.** The upstream fix puts the requested tag and its publishing jobs in one GitHub Actions run. The [historical publish job](https://github.com/LunaStev/binlayout/actions/runs/36327486327/job/108643013538) and [registry v0.1.0](https://crates.io/api/v1/crates/binlayout/0.1.0) predate the fix. [Binlayout #39 — approved and merged](https://github.com/LunaStev/binlayout/pull/39#pullrequestreview-5346324297) · [Release evidence](proof/binlayout-release-evidence.md).

**2. A crashing worker could send the same job past its retry limit.** The upstream fix stops an over-budget crash redelivery before the handler runs again. The fix ships in the public Gombit Go module. The case shows the tagged-module test, hosted Redis checks and a separate replay where three workers were terminated. [Gombit #525 — approved and merged](https://github.com/gombit-dev/gombit/pull/525#pullrequestreview-5355526242) · [Crash redelivery evidence](proof/gombit-crash-redelivery.md).

**3. SQLite schema reset could leave user tables behind.** `_` in SQL `LIKE` is a wildcard, so an unsafe filter treated names such as `sqlitex_cache` as reserved. A precise escape and native SQLite test check both user objects and `sqlite_sequence`. [Gombit #651 — approved and merged](https://github.com/gombit-dev/gombit/pull/651) · [How it was tested](proof/sqlite-schema-reset.md).

<details>
<summary>All 11 merged upstream pull requests</summary>

**Gombit**

- [#521 — fix: preserve caller options in DispatchAt](https://github.com/gombit-dev/gombit/pull/521) · [How it was tested](proof/dispatchat-slice-aliasing.md)
- [#525 — fix: stop crash redelivery after MaxAttempts](https://github.com/gombit-dev/gombit/pull/525)
- [#534 — fix: retry each failed job once per invocation](https://github.com/gombit-dev/gombit/pull/534)
- [#535 — fix: treat dev null stdin as non-interactive](https://github.com/gombit-dev/gombit/pull/535)
- [#541 — test: make staticcheck nil guards explicit](https://github.com/gombit-dev/gombit/pull/541)
- [#563 — fix(scaffold): validate Go module paths before generation](https://github.com/gombit-dev/gombit/pull/563) · [How it was tested](proof/go-module-validation.md)
- [#651 — fix(migrations): preserve only reserved sqlite_ objects during reset for SQLite](https://github.com/gombit-dev/gombit/pull/651)

**Binlayout**

- [#35 — test(ci): add offline release workflow regression coverage](https://github.com/LunaStev/binlayout/pull/35)
- [#39 — ci: connect publishing result to manual release flow](https://github.com/LunaStev/binlayout/pull/39)

**OpenMuse**

- [#40 — Add runnable typed tool example](https://github.com/tahodev/openmuse/pull/40)
- [#46 — Add credential-free documentation link checker](https://github.com/tahodev/openmuse/pull/46)

</details>

## Try the three pinned projects

**[Agent Forecast Foundry](https://github.com/SamCT86/agent-forecast-foundry-case-study) — check an agent's answer before accepting it.** Run synthetic cases with unbound evidence, incomplete provider output and abstention. [Run the local tests and evals](https://github.com/SamCT86/agent-forecast-foundry-case-study#try-it-locally).

**[MachineOutcome](https://github.com/SamCT86/machineoutcome-case-study) — read back the outcome before retrying.** In the synthetic demo, compare a timeout with confirmed state, missing readback, and evidence from the wrong attempt. [Open the browser demo](https://machineoutcome.com/#lab).

**[TrustPR](https://github.com/SamCT86/trustpr-action) — inspect what a pull-request check actually observed.** The read-only Action reports diff and check evidence. The maintainer-run example shows why the collector can finish green while test execution is still unknown. v0.1.1 is a prerelease. [See the hosted example](https://github.com/SamCT86/trustpr-action/blob/main/REAL-PUBLIC-EXAMPLE.md) · [Install guide](https://github.com/SamCT86/trustpr-action/blob/main/START-HERE.md) · [Merge-gate limitation](https://github.com/SamCT86/trustpr-action/issues/53).

Related reference: [Transaction Lab](https://github.com/SamCT86/agent-cash-cow-os) uses synthetic payment timeouts to illustrate when a retry could duplicate an effect.

## How I approach a technical problem

**Reproduce the failure → choose the smallest testable change → challenge the fix with negative controls → run the relevant checks → seek independent review → state the exact outcome and remaining risk.**

My contribution is **problem framing, AI-agent direction, acceptance criteria, evidence evaluation, technical-product judgment and delivery accountability**. AI agents perform hands-on implementation coding. For risk-critical code or security-sensitive changes, qualified independent code review remains important; successful tests alone are not a safety certificate.

## Work with me

**Potential starting points:** an Agent Reliability/CI Evidence Audit, a tightly scoped bug-fix sprint, or an AI-native product trial with measurable acceptance criteria. The right scope and commercial terms depend on your problem; I do not imply previous paid engagements or customer adoption without evidence.

**[Compare three bounded engagement options](WORK_WITH_ME.md)** · [Try the agent evidence trial](WORK_WITH_ME.md#try-the-evidence-trial) · **[Email a concrete problem](mailto:sarmadtawfeek@gmail.com?subject=Scope%20a%20technical%20engagement)** · [LinkedIn](https://www.linkedin.com/in/sam-tawfeek-496197207/) · [Website](https://sarmadtawfeek.se/)
