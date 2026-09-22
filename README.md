# Sarmad Tawfeek

**Applied AI / Agentic Systems Builder — Stockholm, Sweden / Remote**

Most of the AI problems I enjoy start after the first demo works. An API times out. Evidence is incomplete. Two systems disagree about state. A model sounds confident, but the surrounding workflow still has no good reason to trust the result.

That is the kind of engineering I keep coming back to: explicit state, evidence, failure handling, evals, and automation that knows when to stop instead of inventing certainty.

I use AI tools every day. They make implementation faster, but they do not get the final vote. I own the problem framing, constraints, debugging, tests, and release decision.

**Open to:** bounded Applied AI contract work, AI integrations, evaluation/reliability work, technical consulting, and selective Applied AI roles.

[Portfolio](https://sarmadtawfeek.se) · [LinkedIn](https://www.linkedin.com/in/sarmad-lundberg-tawfeek-496197207/) · [Email](mailto:sarmadtawfeek@gmail.com)

## Start here

### [Agent Forecast Foundry](https://github.com/SamCT86/agent-forecast-foundry-case-study)

If you want to understand how I think about AI systems, this is the repo I would open first.

It asks a simple question: **when a model returns an answer, what still has to be true before the surrounding system should trust the run?**

The public reference covers structured output, evidence binding, explicit abstention, provider-state checks, cost/latency limits, sanitized persistence, replay/concurrency boundaries, tests, and offline evals.

I kept it bounded on purpose so another engineer can follow the execution path and challenge the assumptions without having to take a production-scale claim on faith.

If you only have a few minutes, start with the runtime path and its tests rather than the prose.

## Other work

| Project | The problem I was trying to make explicit |
| --- | --- |
| [MachineOutcome](https://github.com/SamCT86/machineoutcome-case-study) | An API timeout does not prove that an external action failed. Read back reality before retrying. |
| [Billable Meetings](https://github.com/SamCT86/billable-meetings-os-case-study) | Commercial rules become messy when evidence is incomplete or contradictory. Preserve a real review state instead of forcing a yes/no answer. |
| [ReleaseProof](https://github.com/SamCT86/releaseproof-case-study) | “Tests passed” is weak evidence if you cannot prove those tests belong to the exact artifact being shipped. |
| [PriceBriefs](https://github.com/SamCT86/pricebriefs-case-study) | A price difference is not useful until the product, source, currency, availability, and freshness are trustworthy enough to compare. |

These are intentionally bounded public engineering references with synthetic data. They are there to make specific decisions and failure boundaries inspectable — not to pretend that five full production systems are open-source. Private product code, credentials, customer/operational data, and proprietary workflows stay private.

## Things I care about in code

- If an external action times out, do not assume nothing happened.
- If the evidence is incomplete, do not turn uncertainty into success because the workflow wants an answer.
- If a system says something passed, be able to show exactly what was tested and what the result belongs to.
- Make important failure states visible enough that another engineer can challenge the decision without trusting the author’s confidence.

Those principles are not unique to AI. I have found them useful anywhere software crosses a boundary into another system or into a decision that matters.

## How I got here

Before my current Applied AI work, I built and operated automated FX trading systems in live markets from 2015–2020. That work involved execution logic and portfolio-risk decisions where software behavior had direct financial consequences. It is probably one reason I care so much about observed state, explicit risk boundaries, and knowing what actually happened instead of what a system hoped happened.

There is a historical third-party performance record on [Myfxbook](https://www.myfxbook.com/members/GloryForex). I include it as background, not as a claim about my current AI work.

## Tools I use

TypeScript / Node.js · Python / FastAPI · React / Next.js · Postgres / Supabase · OpenAI APIs · GitHub Actions

Tools change. The part I try to keep consistent is the reasoning around state, evidence, failure, and verification.

If you are working on an AI or automation problem where “probably worked” is not a good enough answer, [send me the problem](mailto:sarmadtawfeek@gmail.com).
