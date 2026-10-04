# Yukon QSB pinning benchmark — verified external result

Snapshot date: **2026-10-04**

This note records one externally evaluated CUDA optimization result from the Yukon / Eigen Labs Quantum Safe Bitcoin (QSB) pinning benchmark.

## Result

- Submission: `802024df-81f2-4377-9716-025f32f8eaaa`
- Track: `pinning`
- Hardware: **RTX 4090**
- Official score: **1,015,429,342 verified candidates/s**
- Provider verification: **verified = true**
- Terminal status: **rejected**
- Rejection reason: `score did not improve current best`
- Promoted best at the same readback: **1,020,930,406 verified candidates/s**
- Delta to promoted best: **-5,501,064 (-0.5388%)**

The submission was therefore a valid, independently verified benchmark run that missed the promotion threshold on performance. It was **not** rejected for incorrect results.

## Ranking snapshot

At the same 2026-10-04 public-history readback:

- total submissions: **2,591**
- submissions with an official score: **1,515**
- scored submissions above this result: **46**
- rank among scored submissions: **#47 / 1,515**
- rank percentile: **top 3.1%**
- scored submissions strictly below this result: **96.9%**

This is a **submission ranking**, not a unique-participant ranking. The public readback used for this calculation did not expose enough owner identity to deduplicate multiple submissions from the same participant.

## Claim boundary

What this supports:

> Official Yukon QSB pinning benchmark result: **1.015B verified candidates/s on RTX 4090, #47 of 1,515 scored submissions (top 3.1%) at the 2026-10-04 readback, 0.54% below the promoted best.**

What it does **not** support:

- winning the benchmark;
- promotion to the record;
- a top-3.1% claim among unique human participants;
- bounty payment or commercial acceptance.

## Public benchmark references

- Yukon QSB benchmark: https://www.yukon.org/qsb
- Benchmark source and verifier: https://github.com/Layr-Labs/quantum-safe-bitcoin-challenge

The benchmark repository describes the score as verified candidate throughput and independently re-derives submitted hits on CPU.
