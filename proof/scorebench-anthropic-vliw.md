# Paradigm / ScoreBench — Anthropic Take-Home performance proof

> **1,113 cycles · official provider rank #86 · 132.735× cycle speedup vs a freshly verified starter**
>
> Official Paradigm / ScoreBench evaluation on the **Anthropic Take-Home** challenge at the **2026-10-05** snapshot.

This page preserves the public, spoiler-safe evidence for one externally evaluated performance-engineering result. The optimized solution source is intentionally **not published**: the challenge permits modification and use but restricts publishing or redistributing solutions.

## Result at a glance

| Metric | Verified result |
|---|---:|
| Challenge | Paradigm Puzzles / ScoreBench — `Anthropic Take-Home` / `vliw` |
| Submission | `a5f41786-2817-46d9-a3a6-5d80649472ad` |
| Official score | **1,113 cycles** |
| Provider status | **`success`** |
| Retained | **`true`** |
| Official provider rank | **#86** |
| Fresh starter control | **147,734 cycles** |
| Cycle speedup vs starter | **132.73495×** |
| Previous official score | 1,140 cycles |
| Improvement vs previous official | **27 cycles / 2.3684%** |
| Leader at verified snapshot | 864 cycles |
| Scored leaderboard rows | 570, including 5 reference baselines |
| Actual participant rows | **565** |
| Ordered participant position | **85 / 565** |
| Participants strictly better | 83 |
| Tied at 1,113 | 2, including this result |
| Participants strictly worse | **480** |

The provider rank includes reference-baseline rows. Removing the five reference baselines gives an ordered participant position of **85 / 565** at the snapshot. That places the result at roughly the **top 15% of participants**. Rank is time-sensitive and may move as later submissions are scored.

## Verification evidence

The exact standalone candidate used for the official submission was verified before and after submission:

- **9 / 9** official public tests passed.
- **258** additional frozen-simulator seeds passed at exactly 1,113 cycles.
- **8** adversarial input patterns passed at exactly 1,113 cycles.
- Scratch usage: **1,536 / 1,536**.
- Independent ISA/resource and same-cycle destination-alias audits passed.
- Compile determinism and diff checks passed.
- A deliberately wrong path-mask negative control was rejected by the unchanged frozen oracle.
- `tests/submission_tests.py`, `tests/frozen_problem.py`, `problem.py` and `Readme.md` remained byte-identical to upstream.
- No other participant solution source or artifacts were used.

Exact candidate identities retained privately:

- candidate SHA256: `2dd2023ab8db896652cf654ab20a20bb67f261db2337856afeedf43092249a94`
- deterministic generated-program SHA256: `2f4b86a8bf5efb9a81422157e04b380230906ebbd3cd76fb50bba149d0d60c3b`
- ScoreBench bundle SHA256: `3b5993d6a675a8b087f8d2837eb52dc0d91f41dfcd20de4e9a7deda566f1a359`

## What the engineering work demonstrates

The work is best understood as **performance engineering under a constrained VLIW-style machine model**, not as a generic coding-speed benchmark.

The optimization process combined:

- resource-aware instruction scheduling;
- scratch-lifetime management under a hard memory budget;
- vector/scalar workload balancing;
- dependency-chain shortening;
- selective caching and address prefetching;
- exact arithmetic transformations that preserve benchmark semantics;
- adversarial correctness testing before stronger performance claims.

Across the final renewal, **1,408 configurations** were screened in ten experiment grids plus structural controls. The retained path improved the prior official result from 1,140 to **1,113 cycles**. The final design remained 42 cycles above its strongest measured slot lower bound; global optimality is not claimed.

## Why the score is meaningful

1. **The score is provider-evaluated, not self-reported.** Paradigm / ScoreBench returned the official 1,113-cycle score, `success` status and retained result.
2. **Correctness stayed coupled to performance.** Public tests, frozen-simulator seeds and adversarial patterns all passed on the exact retained candidate.
3. **The comparison baseline was freshly reproduced.** The upstream starter reproduced **147,734 cycles** with correct outputs.
4. **The result has a public competitive context.** Provider rank was **#86** at the verified snapshot, with 565 actual participant rows after excluding five reference baselines.

## Portfolio-safe citation

> **Paradigm / ScoreBench — Anthropic Take-Home:** official **1,113-cycle** result, **132.7×** cycle speedup versus the freshly verified 147,734-cycle starter, provider rank **#86** at the 2026-10-05 snapshot; **85 / 565** ordered participant position after excluding five reference baselines.

## Claim boundary

This proves performance and correctness on the official community benchmark workload used by the challenge.

It does **not** claim:

- Anthropic endorsement, certification, employment or hiring acceptance;
- a global optimum;
- a sub-1,000 or sub-900 score;
- that provider rank is permanent;
- broader production-system performance;
- payment or commercial acceptance.

The solution source remains private to respect the challenge's publication boundary.

## Public references

- [Paradigm Puzzles — Anthropic Challenge](https://www.paradigm.xyz/puzzles/anthropic-challenge)
- [ScoreBench](https://scorebench.dev/)

---

*Verified snapshot: 2026-10-05. Competitive ranks can change as later submissions are evaluated.*
