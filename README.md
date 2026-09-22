# Sarmad Tawfeek

**Applied AI / Agentic Systems Builder — Stockholm, Sweden / Remote**

I’m interested in the part of AI work that starts after the demo looks good: what the system is allowed to trust, what happens when evidence is missing, how it behaves after an API timeout, and how you prove that an action actually happened.

I build small, inspectable systems around those problems. I care about clear failure states, useful tests, observable behavior, and software that can say “I don’t know” when the evidence is not good enough.

I use AI tools heavily in my day-to-day implementation work. They make me faster, but I do not treat their output as authority. I define the problem, set the constraints, inspect failures, test the edge cases, and decide what ships.

**Open to:** bounded Applied AI contract work, AI integrations, evaluation/reliability work, technical consulting, and selective Applied AI roles.

[Portfolio](https://sarmadtawfeek.se) · [LinkedIn](https://www.linkedin.com/in/sarmad-lundberg-tawfeek-496197207/) · [Email](mailto:sarmadtawfeek@gmail.com)

## Start here

### [Agent Forecast Foundry](https://github.com/SamCT86/agent-forecast-foundry-case-study)

This is the repo I would open first if you want to understand how I think.

It is a runnable reference for a simple question: **when an AI model returns an answer, what still has to be true before the surrounding system should trust the run?**

The reference covers structured output, evidence binding, explicit abstention, provider-state checks, cost/latency limits, sanitized persistence, replay/concurrency boundaries, tests, and offline evals.

The code is intentionally bounded enough to review rather than dressed up as a production-scale platform.

## Other work

| Project | The problem I was trying to make explicit |
| --- | --- |
| [MachineOutcome](https://github.com/SamCT86/machineoutcome-case-study) | An API timeout does not prove that an external action failed. Read back reality before retrying. |
| [Billable Meetings](https://github.com/SamCT86/billable-meetings-os-case-study) | Commercial rules become messy when the evidence is incomplete or contradictory. Preserve a real review state instead of forcing a yes/no answer. |
| [ReleaseProof](https://github.com/SamCT86/releaseproof-case-study) | “Tests passed” is weak evidence if you cannot prove those tests belong to the exact artifact being shipped. |
| [PriceBriefs](https://github.com/SamCT86/pricebriefs-case-study) | A price difference is not useful until the product, source, currency, availability, and freshness are trustworthy enough to compare. |

These repositories are public engineering references with synthetic data. I keep private product code, credentials, customer/operational data, and proprietary workflows out of the public surface.

## A few rules I keep coming back to

- If an external action times out, do not assume nothing happened.
- If the evidence is incomplete, do not turn uncertainty into success just because the workflow wants an answer.
- If a system says something passed, be able to show exactly what was tested and what the result belongs to.
- Make important failure states visible enough that another engineer can reason about them without trusting the author’s confidence.

Those ideas show up repeatedly in my work because I have found them useful across agent workflows, integrations, decision systems, and automation.

## Earlier systems work

Before my current Applied AI work, I built and operated automated FX trading systems in live markets from 2015–2020. That work involved execution logic and portfolio-risk decisions where software behavior had direct financial consequences.

There is a historical third-party performance record on [Myfxbook](https://www.myfxbook.com/members/GloryForex). I include it as background, not as a claim about my current AI work.

## Tools I use

TypeScript / Node.js · Python / FastAPI · React / Next.js · Postgres / Supabase · OpenAI APIs · GitHub Actions

Tools change. The part I try to keep consistent is the reasoning around state, evidence, failure, and verification.

If you are working on an AI or automation problem where “probably worked” is not a good enough answer, [send me the problem](mailto:sarmadtawfeek@gmail.com).
