# Sarmad Tawfeek

**AI-Native Product & Systems Builder | Stockholm, Sweden / Remote**

I build and operate AI-native systems with an evidence-first approach: explicit acceptance criteria, real provider readback, fail-closed behavior, and verified outcomes instead of activity claims.

**Commercial product focus:** MachineOutcome and Agent Cash Cow OS.

Other internal products and experiments are intentionally kept private and used as indie-hacking / R&D assets rather than presented as commercial portfolio products.

[Website](https://sarmadtawfeek.se) · [LinkedIn](https://www.linkedin.com/in/sarmad-lundberg-tawfeek-496197207/) · [Email](mailto:sarmadtawfeek@gmail.com)

## Commercial products

### [MachineOutcome](https://github.com/SamCT86/machineoutcome-case-study)

MachineOutcome focuses on a critical automation problem: an attempted action is not the same thing as a verified outcome.

The public reference demonstrates reconciliation before retry, task/attempt-bound evidence, explicit `VERIFIED | FAILED | UNKNOWN` states, and refusal to blindly replay ambiguous external mutations.

**Public proof:** [machineoutcome-case-study](https://github.com/SamCT86/machineoutcome-case-study)

### [Agent Cash Cow OS](https://github.com/SamCT86/agent-forecast-foundry-case-study)

Agent Cash Cow OS is the second commercial product track. Its current product hypothesis centers on forecast evidence and measurable decision advantage for autonomous agents.

The public reference exposes only a bounded engineering pattern for evidence, structured output, provider-state checks, cost/latency limits and fail-closed acceptance. The production OS, orchestration, benchmark logic, live evidence and commercial controls remain private.

**Public proof:** [Agent Cash Cow OS — Forecast Evidence reference](https://github.com/SamCT86/agent-forecast-foundry-case-study)

## External open-source proof

Merged contributions to third-party repositories remain part of the engineering track record, but they are not commercial products.

- **gombit-dev/gombit — [PR #534](https://github.com/gombit-dev/gombit/pull/534):** fixed `jobs retry --all` reprocessing live re-failures, then addressed a maintainer-found peak-read regression with bounded pagination + regression coverage.
- **gombit-dev/gombit — [PR #525](https://github.com/gombit-dev/gombit/pull/525):** fixed unbounded crash redelivery so a poison job cannot keep rerunning past `MaxAttempts`.
- **gombit-dev/gombit — [PR #521](https://github.com/gombit-dev/gombit/pull/521):** fixed `Dispatcher.DispatchAt` mutating caller-owned option storage and added regression coverage.
- **LunaStev/binlayout — [PR #39](https://github.com/LunaStev/binlayout/pull/39):** connected the publishing result to the manual release flow.
- **LunaStev/binlayout — [PR #35](https://github.com/LunaStev/binlayout/pull/35):** added offline release-workflow regression coverage.

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
