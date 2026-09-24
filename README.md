# Sarmad Tawfeek

**AI-Native Product & Systems Builder — Stockholm, Sweden / Remote**

I turn expensive, manual or unreliable workflows into working AI systems.

I use AI agents and software tools as the implementation layer. My role is to frame the problem, set the constraints, direct the build, test the system and decide what is good enough to ship.

I am **not positioning myself as a traditional hand-coding software engineer**. The work below shows systems and mechanisms I can direct, inspect, test and defend — not a claim that I manually authored every line.

**Start small:** [AI Workflow Audit](mailto:sarmadtawfeek@gmail.com?subject=AI%20Workflow%20Audit&body=Hi%20Sarmad%2C%0A%0AThe%20workflow%20I%20want%20to%20improve%20is%3A%20) — one workflow, one real constraint, one prioritized improvement path.

[Website](https://sarmadtawfeek.se) · [LinkedIn](https://www.linkedin.com/in/sarmad-lundberg-tawfeek-496197207/) · [Email](mailto:sarmadtawfeek@gmail.com)

## Selected proof

### [MachineOutcome](https://github.com/SamCT86/machineoutcome-case-study) — verify what actually happened before retrying

An API timeout does not prove that an external action failed. This public reference binds task, attempt and observed state before allowing `VERIFIED`, `FAILED` or `UNKNOWN` — and blocks blind retry when reality is still ambiguous.

**Shows:** state verification · reconciliation before retry · fail-closed evidence boundaries

### [Billable Meetings](https://github.com/SamCT86/billable-meetings-os-case-study) — turn meeting evidence into defensible billing decisions

A live product plus a bounded public decision-engine reference. Agreement rules and meeting evidence become `BILLABLE`, `NON_BILLABLE` or `REVIEW`; missing or contradictory evidence stays visible instead of being forced into a yes/no answer.

[Live product](https://billablemeetings.com) · [Public reference](https://github.com/SamCT86/billable-meetings-os-case-study)

**Shows:** commercial rule modeling · evidence traceability · explicit review states

### [ReleaseProof](https://github.com/SamCT86/releaseproof-case-study) — verify the exact artifact that will ship

A release check should not say `PASS` unless its evidence belongs to the exact artifact and environment being judged. The public reference fails closed on cross-artifact, incomplete or mismatched evidence.

**Shows:** artifact identity · evidence binding · explicit `INCONCLUSIVE`

### More public references

- [Agent Forecast Foundry](https://github.com/SamCT86/agent-forecast-foundry-case-study) — checks evidence, structured output, provider state, cost, latency and persistence boundaries before accepting an AI run.
- [PriceBriefs](https://github.com/SamCT86/pricebriefs-case-study) — refuses weak competitive-price comparisons until identity, currency, availability, source qualification and freshness are good enough for the decision.

## What these repositories are

These case studies are intentionally bounded, runnable references. They use synthetic data where appropriate and expose mechanisms, tests and failure boundaries so the work can be inspected directly.

They are AI-assisted implementations. They are **not** dumps of private product code, customer data or proprietary workflows, and they are not presented as proof of product-market fit, customer ROI or personal hand-authorship of every line.

That boundary is deliberate: **proof before social proof, and evidence before stronger claims.**

## What I help with

- **AI Workflow Audit** — map one workflow, find where time, cost or reliability leaks, and identify the smallest useful improvement path.
- **AI-native systems** — use agents and software tools to create automations, integrations and internal systems around a real operational constraint.
- **Verification & reliability** — add tests, evals, readback and explicit failure states when “probably worked” is not good enough.

## How I work

1. Frame the real business or operational problem.
2. Set constraints, acceptance criteria and failure boundaries.
3. Direct AI agents and tools to implement the system.
4. Test and inspect the result against reality.
5. Iterate or reject until the outcome is useful enough to ship.

AI gives me implementation leverage. My value is in the **problem framing, system direction, orchestration, verification and final judgment**.

## Background

Before my current AI work, I built and operated automated FX trading systems in live markets from 2015–2020. That work involved execution and risk decisions where software behavior had direct financial consequences, which is one reason I care about observed state and explicit risk boundaries. A historical third-party performance record is available on [Myfxbook](https://www.myfxbook.com/members/GloryForex); I include it as background, not as a claim about my current AI work.

## Implementation environment

AI agents & coding tools · TypeScript / Node.js · Python / FastAPI · React / Next.js · Postgres / Supabase · OpenAI APIs · GitHub Actions

If you have one AI or automation workflow where cost, manual work or reliability is becoming a problem, [send me the workflow](mailto:sarmadtawfeek@gmail.com?subject=AI%20Workflow%20Audit&body=Hi%20Sarmad%2C%0A%0AThe%20workflow%20I%20want%20to%20improve%20is%3A%20).