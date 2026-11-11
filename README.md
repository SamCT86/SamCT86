# Sarmad Tawfeek

**AI-native product builder · AI-agent orchestration · evidence-first delivery**

Stockholm, Sweden

I lead AI agents to turn product ideas and reliability problems into inspectable technical results. I define the goal, scope and acceptance criteria, evaluate demos, test outcomes and original-source evidence, and decide what is ready to publish. **AI agents perform the hands-on coding**; I do not claim to independently write or review implementation code as a conventional software engineer. I take responsibility for the direction, decisions and claims.

**Open to:** AI-native product-building work, agent orchestration, technical product ownership, outcome-driven collaborations, and paid trials where AI-assisted coding is explicitly acceptable. [Connect on LinkedIn](https://www.linkedin.com/in/sarmad-lundberg-tawfeek-496197207/) or [visit my website](https://www.sarmadtawfeek.com).

## Evidence of AI-assisted technical delivery — independently merged upstream

**11 merged pull requests in 3 independently maintained open-source projects** (verified 11 November 2026). These are real upstream-accepted results from AI-assisted work under my GitHub account; they do **not** prove that I personally wrote the implementation code, passed a coding interview, delivered paid client work or hold an engineering certification.

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

If you need someone to define an AI-native product, direct agent-assisted implementation, or make automation results auditable, I can discuss a **bounded discovery, prototype or delivery engagement** with clear acceptance criteria. Code-level assurance and security decisions require appropriately qualified human review when the risk calls for it. I am also interested in paid AI-agent/product challenges that permit AI-assisted implementation.

**[LinkedIn — contact](https://www.linkedin.com/in/sarmad-lundberg-tawfeek-496197207/)** · **[Website](https://www.sarmadtawfeek.com)** · [TrustPR feedback](https://github.com/SamCT86/trustpr-action/issues/11)

*Public examples and synthetic demos are labeled. No unverified paid clients, external installations, commercial revenue, or engineering certifications are implied.*
