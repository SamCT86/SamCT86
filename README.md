# Sarmad Tawfeek

**Self-taught software builder · AI-assisted engineering · open-source reliability**

Stockholm, Sweden

I build and review software that must **prove what happened before taking the next action**: agent workflows, safe retries, GitHub Actions, and evidence-first delivery. I use AI-assisted development, but take human responsibility for problem definition, acceptance criteria, tests, code review, and what I publish.

**Open to:** engineering roles, paid technical trials, focused consulting, and open-source collaboration in AI agent engineering, developer tools, reliability, and CI evidence. [Connect on LinkedIn](https://www.linkedin.com/in/sarmad-lundberg-tawfeek-496197207/) or [visit my website](https://www.sarmadtawfeek.com).

## Evidence of engineering work — independently merged upstream

**11 merged pull requests in 3 independently maintained open-source projects** (verified 11 November 2026). These are accepted code contributions, **not** customer results, formal certifications, or endorsements of my own products.

| Problem | What changed | Independent evidence |
|---|---|---|
| SQLite schema reset missed user-owned tables because `_` in `LIKE` is a wildcard | Narrowly scoped escaping fix and native SQLite regression test, including a reserved internal-table negative control | [gombit PR #651](https://github.com/gombit-dev/gombit/pull/651) · maintainer-approved and merged |
| Invalid Go module paths could be accepted before scaffold generation | Go-native validation before writing files, with valid/invalid-path tests | [gombit PR #563](https://github.com/gombit-dev/gombit/pull/563) · two rounds of requested changes → approval → merge |
| Crash-reclaimed jobs risked running past `MaxAttempts` | Preserve lease-expiry provenance and distinguish crash retry from voluntary release; regression coverage | [gombit PR #525](https://github.com/gombit-dev/gombit/pull/525) · merged |

Other accepted contributions: [gombit](https://github.com/gombit-dev/gombit/pulls?q=is%3Apr+author%3ASamCT86+is%3Amerged), [binlayout](https://github.com/LunaStev/binlayout/pulls?q=is%3Apr+author%3ASamCT86+is%3Amerged), [openmuse](https://github.com/tahodev/openmuse/pulls?q=is%3Apr+author%3ASamCT86+is%3Amerged). The PR discussions show how fixes were reviewed; some tests described in PR bodies are author-reported, not independent benchmark results.

## Tools and public engineering references

### [TrustPR](https://github.com/SamCT86/trustpr-action) — understand PR evidence without guessing

Free, MIT-licensed GitHub Action producing a readable receipt of observed changes, checks, and unknowns. [Install guide](https://github.com/SamCT86/trustpr-action/blob/main/START-HERE.md) · [Marketplace](https://github.com/marketplace/actions/trustpr-evidence-receipt) · [first-party example](https://github.com/SamCT86/trustpr-consumer-canary/actions/runs/39475939069).

**Scope:** v0.1.1 is a prerelease. TrustPR does not run PR tests, certify code safety, or authorize a merge. [Required-check workflow trust boundary remains open (#53)](https://github.com/SamCT86/trustpr-action/issues/53). No independent third-party adoption is claimed.

### [MachineOutcome](https://github.com/SamCT86/machineoutcome-case-study) — reconcile before retry

A public, MIT-licensed **synthetic** case study of the ambiguous-timeout problem: a request can fail locally after the external effect already succeeded. [Try the browser demo](https://samct86.github.io/machineoutcome-case-study/). The private runtime is separate and not publicly released; the reference is not offered as a commercial product.

### [Transaction Lab](https://github.com/SamCT86/agent-cash-cow-os) — duplicate-action failure modes

An inspectable **synthetic evaluation** of payment timeouts, provider readback, and retry decisions. [Try the lab](https://www.sarmadtawfeek.com/agent-cash-cow). Not a production payment service or a claimed live customer deployment.

## Work with me

If you have an AI workflow that occasionally retries the wrong thing, an automation that reports success without proof, or CI checks with unclear trust boundaries, I can discuss a **scoped engineering review or focused fix**, subject to technical fit and agreed terms. I am also interested in real coding challenges, OSS maintenance and agent/developer-tool engineering roles.

**[LinkedIn — contact](https://www.linkedin.com/in/sarmad-lundberg-tawfeek-496197207/)** · **[Website](https://www.sarmadtawfeek.com)** · [TrustPR feedback](https://github.com/SamCT86/trustpr-action/issues/11)

*Public examples and synthetic demos are labeled. No unverified paid clients, external installations, commercial revenue, or engineering certifications are implied.*
