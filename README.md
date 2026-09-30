# Sarmad Tawfeek

**AI-Native Product & Systems Builder | Stockholm, Sweden / Remote**

I help turn expensive, manual or unreliable workflows into practical AI-assisted systems that are easier to operate, test and trust.

My role is to frame the business problem, set the constraints, direct AI and software execution, verify the result and decide what is ready to use.

**Open to:** outcome-based consulting · AI systems/integration roles · technical product/system ownership · remote collaboration.

This GitHub is evidence-first: public repositories and third-party contributions show mechanisms, tests, failure boundaries and review outcomes — not just a list of tools.

**Start small:** [AI Workflow Audit](mailto:sarmadtawfeek@gmail.com?subject=AI%20Workflow%20Audit&body=Hi%20Sarmad%2C%0A%0AThe%20workflow%20I%20want%20to%20improve%20is%3A%20). One workflow, one real constraint, one prioritized improvement path.

[Website](https://sarmadtawfeek.se) · [LinkedIn](https://www.linkedin.com/in/sarmad-lundberg-tawfeek-496197207/) · [Email](mailto:sarmadtawfeek@gmail.com)

## What I help with

- **AI Workflow Audits:** find where time, cost, manual work or reliability leaks, then identify the smallest useful fix.
- **AI automation and internal systems:** turn repeatable operational work into practical automations, integrations and agent-assisted workflows.
- **Verification and reliability:** add tests, evals, readback and explicit failure states when "probably worked" is not good enough.

## Paid client proof

- Completed 5-star client work in local SEO and website optimization.
- Completed paid advisory work focused on Google Page Speed and LCP performance.

I use paid work as commercial proof and the public repositories below as inspectable technical proof.

## External open-source proof

Merged contributions to third-party repositories:

- **gombit-dev/gombit — [PR #534](https://github.com/gombit-dev/gombit/pull/534):** fixed `jobs retry --all` reprocessing live re-failures, then addressed a maintainer-found peak-read regression with bounded pagination + regression coverage. Maintainer requested changes, verified the remediation, approved it, and merged after CI 26/26.
- **gombit-dev/gombit — [PR #525](https://github.com/gombit-dev/gombit/pull/525):** fixed unbounded crash redelivery so a poison job cannot keep rerunning past `MaxAttempts`. Code-owner approved; current-head CI passed 26/26 jobs.
- **gombit-dev/gombit — [PR #521](https://github.com/gombit-dev/gombit/pull/521):** fixed `Dispatcher.DispatchAt` mutating caller-owned option storage and added regression coverage. Code-owner approved; current-head CI passed 26/26 jobs.
- **LunaStev/binlayout — [PR #39](https://github.com/LunaStev/binlayout/pull/39):** connected the publishing result to the manual release flow.
- **LunaStev/binlayout — [PR #35](https://github.com/LunaStev/binlayout/pull/35):** added offline release-workflow regression coverage.

## Selected technical proof

### [MachineOutcome](https://github.com/SamCT86/machineoutcome-case-study)
A runnable reference for verifying what actually happened before an automated system retries or takes another action.

**Shows:** state verification · reconciliation before retry · explicit uncertainty

### [Billable Meetings](https://github.com/SamCT86/billable-meetings-os-case-study)
A bounded decision engine that turns agreement rules and meeting evidence into `BILLABLE`, `NON_BILLABLE` or `REVIEW`.

[Live product](https://billablemeetings.com) · [Public reference](https://github.com/SamCT86/billable-meetings-os-case-study)

**Shows:** commercial rule modeling · evidence traceability · review states

### [ReleaseProof](https://github.com/SamCT86/releaseproof-case-study)
A release-verification reference that binds evidence to the exact artifact and environment being judged.

**Shows:** artifact identity · evidence binding · explicit `INCONCLUSIVE`

### Additional public references

- [Agent Forecast Foundry](https://github.com/SamCT86/agent-forecast-foundry-case-study): verifies evidence, output structure, provider state, cost and latency before accepting an AI run.
- [PriceBriefs](https://github.com/SamCT86/pricebriefs-case-study): rejects weak competitive-price comparisons until identity, currency, availability, source quality and freshness are strong enough.

## How I work

1. Find the real operational or commercial constraint.
2. Define the evidence, acceptance criteria and failure boundaries.
3. Direct AI agents and software tools to implement the smallest useful system.
4. Test the result against the state that actually matters.
5. Iterate, reject or ship based on evidence.

AI gives me implementation leverage. I am accountable for **problem framing, system direction, orchestration, verification and final judgment**.

## Background

Before my current AI work, I spent years in investigation and evidence-heavy operational roles, with earlier studies in IT forensics and information security. That background shaped how I think about uncertainty, evidence quality and system failure boundaries.

From 2015 to 2020, I also built and operated automated FX trading systems in live markets, where software behavior had direct financial consequences. A historical third-party performance record is available on [Myfxbook](https://www.myfxbook.com/members/GloryForex).

## Implementation environment

AI agents and coding tools · TypeScript / Node.js · Python / FastAPI · React / Next.js · Postgres / Supabase · OpenAI APIs · GitHub Actions

If you have one workflow where cost, manual work or reliability is becoming a problem, [send me the workflow](mailto:sarmadtawfeek@gmail.com?subject=AI%20Workflow%20Audit&body=Hi%20Sarmad%2C%0A%0AThe%20workflow%20I%20want%20to%20improve%20is%3A%20).