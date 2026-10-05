# Yukon / Eigen Labs QSB pinning — independently verified CUDA result

> **1.015B verified candidates/s · NVIDIA RTX 4090 · #47 / 1,515 scored submissions · top 3.1%**
>
> Official Yukon evaluation at the **2026-10-04** snapshot — **0.5388% below the then-promoted best**.

This page preserves the evidence for one externally evaluated CUDA optimization submission to the Yukon / Eigen Labs **Quantum Safe Bitcoin (QSB) pinning** benchmark.

## Result at a glance

| Metric | Verified result |
|---|---:|
| Track | `pinning` |
| Submission | `802024df-81f2-4377-9716-025f32f8eaaa` |
| Hardware | **NVIDIA RTX 4090** |
| Official score | **1,015,429,342 verified candidates/s** |
| Provider verification | **`verified = true`** |
| Verified hits | **145,470** |
| Provider-scored candidates | **1,220,290,805,760** |
| Ranked elapsed time | **1,201.7486 s** |
| Then-promoted best | **1,020,930,406 verified candidates/s** |
| Gap to promoted best | **5,501,064 candidates/s (0.5388%)** |
| Snapshot rank | **#47 / 1,515 scored submissions** |
| Snapshot percentile | **top 3.1%** |

The benchmark accepted the run as **correct and scorable**. Every credited hit was subject to the benchmark's independent verification path.

## Engineering delta

The submitted change was a narrow GPU memory-policy experiment rather than a change to the benchmark or correctness rules.

It introduced `QSB_HOT_DENSE32`, changing the **L2 cache-priority classification** for the lower-density 16 MiB table bank while leaving table addresses, sign extraction, arithmetic and candidate enumeration unchanged.

The exact upstream validation commit is public:

- [Layr-Labs/quantum-safe-bitcoin-challenge @ `bd5b7f4`](https://github.com/Layr-Labs/quantum-safe-bitcoin-challenge/commit/bd5b7f433a125db8ed9333952475e374832b9aaa)

That commit records the submitted source delta and the Yukon validation submission ID.

## Why the score is meaningful

The QSB benchmark is designed so the ranked number is not just a self-reported GPU counter:

1. **Every reported hit is independently re-derived on CPU.** Invalid or duplicate hits do not contribute to the score.
2. **The harness owns the clock.** Ranked throughput is recomputed from verified hits and harness-controlled wall time, not from the candidate's own throughput report.
3. **Ranked runs use a fresh unpredictable problem instance.** The seed is generated after the submission is fixed, preventing precomputed hits from being replayed for score.

See the public benchmark specification:

- [QSB benchmark repository](https://github.com/Layr-Labs/quantum-safe-bitcoin-challenge)
- [Scoring & verification specification](https://github.com/Layr-Labs/quantum-safe-bitcoin-challenge/blob/main/spec/SCORING.md)
- [Machine-readable benchmark contract](https://github.com/Layr-Labs/quantum-safe-bitcoin-challenge/blob/main/benchmark.json)

## Ranking snapshot

At the 2026-10-04 public-history snapshot:

- **1,515** submissions had an official score.
- **46** scored submissions were above this result.
- **1,468** scored submissions were below it.
- The resulting rank was **#47 / 1,515**.
- That is **top 3.1%**, with this score above **96.9%** of scored submissions.

> **Ranking unit:** submissions. The public history available for this snapshot did not expose enough owner identity to deduplicate multiple submissions from the same participant.

<details>
<summary><strong>Provider terminal status</strong></summary>

Yukon recorded:

`rejected — score did not improve current best`

This was a **performance/promotion outcome, not a correctness failure**. The run was verified and scored successfully, but its official throughput was **0.5388% below** the then-promoted best, so it did not replace the record.

</details>

## Portfolio-safe citation

> **Yukon / Eigen Labs QSB pinning:** **1.015B verified candidates/s on NVIDIA RTX 4090**, ranked **#47 / 1,515 scored submissions (top 3.1%)** at the 2026-10-04 snapshot, **0.54% below the then-promoted best**.

## Public references

- [Yukon QSB benchmark](https://www.yukon.org/qsb)
- [Benchmark source](https://github.com/Layr-Labs/quantum-safe-bitcoin-challenge)
- [Exact upstream validation commit](https://github.com/Layr-Labs/quantum-safe-bitcoin-challenge/commit/bd5b7f433a125db8ed9333952475e374832b9aaa)

---

*The rank and frontier values above are intentionally tied to the 2026-10-04 snapshot. Live leaderboard positions can change as later submissions are evaluated.*
