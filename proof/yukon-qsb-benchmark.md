# Yukon / Eigen Labs QSB pinning — verified RTX 4090 result

**Benchmark snapshot:** 2026-10-04  
**Track:** `pinning`  
**Hardware:** NVIDIA RTX 4090  
**Official score:** **1,015,429,342 verified candidates/s**  
**Snapshot rank:** **#47 / 1,515 scored submissions — top 3.1%**

> **Portfolio summary:** An externally evaluated CUDA optimization for the Yukon / Eigen Labs Quantum Safe Bitcoin pinning benchmark reached **1.015B verified candidates/s on RTX 4090**, placing **#47 of 1,515 scored submissions** at the 2026-10-04 public-history snapshot — **0.54% below the promoted best**.

## Verified result

| Metric | Result |
|---|---:|
| Submission | `802024df-81f2-4377-9716-025f32f8eaaa` |
| Official score | **1,015,429,342 candidates/s** |
| Provider verification | **true** |
| Verified hits | **145,470** |
| Candidates evaluated | **1,220,290,805,760** |
| Benchmark elapsed time | **1,201.7486 s** |
| Hardware | **RTX 4090** |
| Promoted best at readback | **1,020,930,406 candidates/s** |
| Gap to promoted best | **5,501,064 candidates/s (0.5388%)** |

The run completed successfully and the submitted hits were independently verified by the benchmark infrastructure. The result was therefore a **valid scored run**.

## Ranking snapshot

At the same public-history readback:

- **2,591** total submissions were visible.
- **1,515** submissions had an official score.
- **46** scored submissions were above this result.
- The resulting submission rank was **#47 / 1,515**.
- That corresponds to the **top 3.1% of scored submissions** at that snapshot.
- **96.9%** of scored submissions were below this score.

The ranking is a **time-stamped submission ranking**. It can move as new submissions are evaluated, and it should not be interpreted as a deduplicated ranking of unique participants.

## Why the provider status says `rejected`

Yukon returned the terminal status:

`rejected — score did not improve current best`

That status reflects the benchmark's **performance/promotion rule**, not a correctness failure.

The submission was:

- built and executed successfully;
- scored on the official RTX 4090 benchmark path;
- marked `verified = true`;
- independently checked against the benchmark verifier;
- **0.5388% below** the promoted best at the same readback.

So the accurate interpretation is:

> **Correct and independently verified, but not fast enough to replace the promoted record.**

## Reproducible citation

For a CV, portfolio, profile, or technical summary, the defensible compact claim is:

> **Yukon / Eigen Labs QSB pinning:** 1.015B verified candidates/s on RTX 4090; **#47 / 1,515 scored submissions (top 3.1%)** at the 2026-10-04 snapshot; **0.54% below the promoted best**.

## Public benchmark references

- Yukon QSB benchmark: https://www.yukon.org/qsb
- Benchmark source and verifier: https://github.com/Layr-Labs/quantum-safe-bitcoin-challenge

The benchmark repository defines the score in terms of verified candidate throughput and re-derives submitted hits on CPU for correctness verification.

---

*Ranking and frontier values above are intentionally tied to the 2026-10-04 snapshot so the historical result remains auditable even if the live leaderboard changes later.*
