# Sarmad Tawfeek

**AI-Native Product & Systems Builder | Stockholm, Sweden / Remote**

I build and operate AI-native systems with an evidence-first approach: explicit acceptance criteria, real provider readback, fail-closed behavior, and verified outcomes instead of activity claims.

> 🏆 **External performance proof — Yukon / Eigen Labs QSB**<br>
> **1.015B verified candidates/s on NVIDIA RTX 4090 · #47/1,515 scored submissions (top 3.1%) · 0.54% from the then-promoted best** at the 2026-10-04 snapshot.<br>
> [Inspect the upstream-verifiable benchmark evidence →](proof/yukon-qsb-benchmark.md)

> ⚙️ **External performance proof — Paradigm / ScoreBench Anthropic Take-Home**<br>
> **1,113 cycles · 132.7× cycle speedup vs the freshly verified starter · official provider rank #86 · ~top 15% of 565 participants** at the 2026-10-05 snapshot.<br>
> [Inspect the spoiler-safe official-score evidence →](proof/scorebench-anthropic-vliw.md)

**Commercial product focus:** MachineOutcome and Agent Cash Cow OS.

## Start here if you're evaluating my work

- **MachineOutcome** — inspect how I handle ambiguous external side effects before retrying. Relevant to agent/workflow systems that can create duplicate writes, deployments, payments or other irreversible effects.
- **Agent Cash Cow OS** — start with the interactive Transaction Lab's buyer-first 15-second timeout walkthrough and guided failure run, inspect the public transaction-reliability source proof, then use the Forecast Evidence reference for the separate verification/runtime pattern behind the broader product direction.
- **Current engagement fit / next step** — if one workflow is slow, expensive or unreliable, send 2–3 sentences by [email](mailto:sarmadtawfeek@gmail.com). No technical brief or meeting is required to start, and no sensitive data should be sent yet. I return the next useful step; scope and price are agreed before anything is ordered. I do not claim paid adoption, customer ROI or market traction for MachineOutcome or Agent Cash Cow OS unless it is independently verified.

Other internal products and experiments are intentionally kept private and used as indie-hacking / R&D assets rather than presented as commercial portfolio products.

## Current ways to start

These are the same bounded entry points presented on the live portfolio:

- **Workflow check** — when you need to know whether a workflow problem is worth solving. You get a baseline, the biggest leak, estimated potential and a recommended next step.
- **Fix sprint** — when the right problem is already clear. One bounded change is implemented against a pre-agreed metric and the outcome is verified.
- **Reliability review** — when AI or integrations already run but you do not fully trust them. You get failure, duplicate-action and handoff testing plus a prioritized action list.

Start with 2–3 sentences about what is slow, expensive or unreliable. [Portfolio](https://www.sarmadtawfeek.com) · [Email](mailto:sarmadtawfeek@gmail.com)


[LinkedIn](https://www.linkedin.com/in/sarmad-lundberg-tawfeek-496197207/) · [Email](mailto:sarmadtawfeek@gmail.com)

## Commercial products

### [MachineOutcome](https://github.com/SamCT86/machineoutcome-case-study)

[![MachineOutcome CI](https://github.com/SamCT86/machineoutcome-case-study/actions/workflows/verify-reference.yml/badge.svg)](https://github.com/SamCT86/machineoutcome-case-study/actions/workflows/verify-reference.yml)

MachineOutcome focuses on a critical automation problem: an attempted action is not the same thing as a verified outcome.

The public reference demonstrates reconciliation before retry, task/attempt-bound evidence, explicit `VERIFIED | FAILED | UNKNOWN` states, and refusal to blindly replay ambiguous external mutations.

**Public proof:** [machineoutcome-case-study](https://github.com/SamCT86/machineoutcome-case-study)

### [Agent Cash Cow OS](https://github.com/SamCT86/agent-forecast-foundry-case-study)

[![Agent Cash Cow OS CI](https://github.com/SamCT86/agent-forecast-foundry-case-study/actions/workflows/reference-tests.yml/badge.svg)](https://github.com/SamCT86/agent-forecast-foundry-case-study/actions/workflows/reference-tests.yml)

Agent Cash Cow OS is the second commercial product track. Its public proof now covers two bounded surfaces: synthetic agent-commerce failure handling and forecast-evidence discipline for autonomous agents.

**Interactive proof:** [Agent Cash Cow OS — Transaction Lab](https://www.sarmadtawfeek.com/agent-cash-cow) — a synthetic browser-only lab for timeout/readback, replay, authorization and outcome/settlement decisions. No account or real money is required.

The GitHub reference exposes a separate bounded engineering pattern for evidence, structured output, provider-state checks, cost/latency limits and fail-closed acceptance. The production OS, orchestration, payment/provider integrations, benchmark logic, live evidence and commercial controls remain private.

**Public source proof:** [Agent Cash Cow OS — Transaction reliability proof](https://github.com/SamCT86/agent-cash-cow-os) — synthetic failure handling, proof receipts, deterministic tests and explicit public/private boundaries.

**GitHub proof:** [Agent Cash Cow OS — Forecast Evidence reference](https://github.com/SamCT86/agent-forecast-foundry-case-study)

## External open-source proof

Merged contributions to third-party repositories remain part of the engineering track record, but they are not commercial products.

- **gombit-dev/gombit — [PR #541](https://github.com/gombit-dev/gombit/pull/541):** made three test-only nil guards explicit so staticcheck could prove the following pointer dereferences unreachable; upstream CI passed, the maintainer reviewed the process contract, then approved and merged it.
- **gombit-dev/gombit — [PR #534](https://github.com/gombit-dev/gombit/pull/534):** fixed `jobs retry --all` reprocessing live re-failures, then addressed a maintainer-found peak-read regression with bounded pagination + regression coverage.
- **gombit-dev/gombit — [PR #525](https://github.com/gombit-dev/gombit/pull/525):** fixed unbounded crash redelivery so a poison job cannot keep rerunning past `MaxAttempts`.
- **gombit-dev/gombit — [PR #521](https://github.com/gombit-dev/gombit/pull/521):** fixed `Dispatcher.DispatchAt` mutating caller-owned option storage and added regression coverage.
- **LunaStev/binlayout — [PR #39](https://github.com/LunaStev/binlayout/pull/39):** connected the publishing result to the manual release flow.
- **LunaStev/binlayout — [PR #35](https://github.com/LunaStev/binlayout/pull/35):** added offline release-workflow regression coverage.

## External benchmark proof

- **Yukon / Eigen Labs QSB pinning — independently verified RTX 4090 evaluation:** **1,015,429,342 verified candidates/s**. At the 2026-10-04 snapshot, the result ranked **#47 of 1,515 scored submissions (top 3.1%)**, **0.54% below the then-promoted best**. Yukon verified and scored the run successfully; it simply did not replace the promoted record. [Inspect the evidence chain and exact upstream validation commit](proof/yukon-qsb-benchmark.md) · [Official benchmark](https://www.yukon.org/qsb)
- **Paradigm / ScoreBench — Anthropic Take-Home:** official **1,113-cycle** result, **132.7×** cycle speedup versus a freshly reproduced 147,734-cycle starter, provider rank **#86** at the 2026-10-05 snapshot. The leaderboard contained 565 actual participant rows after excluding five reference baselines; ordered participant position was **85 / 565 (~top 15%)**. [Inspect the spoiler-safe score, rank and verification evidence](proof/scorebench-anthropic-vliw.md) · [Official challenge](https://www.paradigm.xyz/puzzles/anthropic-challenge)

## How I work

1. Define the real outcome and the evidence needed to prove it.
2. Bound authority, side effects and failure states before execution.
3. Use AI agents and software tools to implement the smallest causal solution.
4. Test adversarially and read back the state that actually matters.
5. Ship, reject or retry only from verified evidence.

AI gives me implementation leverage. I remain accountable for **problem framing, system direction, orchestration, verification and final judgment**.

## Background

Before my current AI work, I spent years in investigation and evidence-heavy operational roles, with earlier studies in IT forensics and information security.

From 2015 to 2020, I also built and operated automated FX trading systems in live markets, where software behavior had direct financial consequences. A historical third-party performance record is available on [Myfxbook](https://www.myfxbook.com/members/GloryForex).

## Implementation environment

AI agents and coding tools · TypeScript / Node.js · Python / FastAPI · React / Next.js · Postgres / Supabase · OpenAI APIs · GitHub Actions
