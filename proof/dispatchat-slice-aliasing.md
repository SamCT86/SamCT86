# Case study 01 — A scheduler that silently rewrote its caller's options

**Problem class:** Go slice aliasing / concurrency / background-job correctness  
**Buyer relevance:** Shared configuration and retry/uniqueness invariants can fail silently in an otherwise green automation pipeline.

## Context and observed failure

Gombit `Dispatcher.DispatchAt(ctx, job, when, opts...)` appended an `At(when)` option directly to the variadic `opts` slice. If the slice had spare capacity, `append` could reuse the **caller's** backing array. A sibling option slice occupying that spare slot—for example, `Unique("report:42", time.Hour)`—could be overwritten with `At(when)`. The original issue also describes a concurrent-use data race. See [original issue #496](https://github.com/gombit-dev/gombit/issues/496).

## Minimal code change

**Before:** `append(opts, At(when))`  
**After:** `append(opts[:len(opts):len(opts)], At(when))`

The full slice expression caps capacity at length, causing `append` to allocate rather than overwrite caller-owned spare capacity. One line of production code changed in `jobs/dispatcher.go`.

**Exact contribution:** [PR #521](https://github.com/gombit-dev/gombit/pull/521) · head SHA [`10d9e3a9dbb4071376040d6a2c93343ba74723eb`](https://github.com/gombit-dev/gombit/commit/10d9e3a9dbb4071376040d6a2c93343ba74723eb).

## Adversarial evidence

- **Original upstream issue:** contains a failing reproduction where the `Unique` option disappears and both dispatches are accepted. This is upstream-issue evidence, not our locally run Gombit suite.
- **Regression in merged patch:** `TestDispatchAtDoesNotMutateCallerOptions` constructs sibling slices sharing one backing array and asserts the second unique dispatch gets `jobs.ErrDuplicateDispatch`.
- **Local independent semantics probe, 13 Nov 2026:** `aliasing_probe.go` showed `OLD sibling option: schedule`, `FIXED sibling option: unique:welcome:1` and exited 0. This tests Go slice semantics in isolation, **not the Gombit project/runtime**.
- **Review:** maintainer `leo-aa88` commented on the exact capacity-bound fix and submitted `APPROVED` on 29 Sep 2026. PR is independently merged.

## Outcome and limits

**VERIFIED:** merged upstream fix and maintainer approval; exact patch and regression source; independent local Go semantic probe PASS.  
**REPORTED:** PR author said package tests passed and the regression failed pre-fix.  
**NOT VERIFIED HERE:** freshly rerun full Gombit CI, production adoption, end-user metrics, revenue.

## What a buyer can infer

The portfolio shows a specific failure mode—shared mutable option storage—with a compact mechanistic correction and a falsifiable test. It **does not** prove broad individual Go expertise or production reliability without further assessment. AI agents performed implementation coding under Sarmad's direction; attribution and claims remain explicit.
