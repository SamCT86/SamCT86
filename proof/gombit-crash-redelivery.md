# When a crashing worker bypassed its retry limit

A job that took its worker down never returned an error. When its queue lease expired, another worker picked up the same job. With `MaxAttempts: 3`, the reported system reached attempt 21. A single job could keep taking workers down once per lease period. [Original Gombit issue #494](https://github.com/gombit-dev/gombit/issues/494)

## The change

Gombit now records whether a reservation reclaimed an expired lease. The worker uses that evidence to put an over-budget delivery into failed jobs before it calls the handler. With a budget of three, reservation four can still appear in the failed record. The fourth handler call is prevented. Explicit release and postponement go back to the pending queue, which preserves the existing shutdown behavior. [Exact PR diff](https://github.com/gombit-dev/gombit/pull/525/files) · [Merged worker code](https://github.com/gombit-dev/gombit/blob/8734759cd6664246f391484c357f1f8364856d96/jobs/worker.go#L205-L248)

## What the checks proved

- The regression simulates three leases that expire without settlement, then starts a worker. It checks for zero extra handler calls and a failed record marked `ReasonExhausted`. The test was introduced on its own before the implementation. [Test-only commit](https://github.com/gombit-dev/gombit/commit/c6afa1b9d9228fe78d1b22c4c03cdb0bb6e1c1ce) · [Final test](https://github.com/gombit-dev/gombit/blob/bfa7775e0b72c53e90e590b2f38b2323e2f7c264/jobs/worker_test.go#L254-L309)
- The queue conformance test checks that explicit release and postponement still report `LeaseExpired == false`. The exact PR head passed 26 hosted jobs, including the Redis queue tests. [Conformance cases](https://github.com/gombit-dev/gombit/blob/bfa7775e0b72c53e90e590b2f38b2323e2f7c264/jobs/queue_test.go#L123-L160) · [Hosted run](https://github.com/gombit-dev/gombit/actions/runs/36563135325) · [Redis job](https://github.com/gombit-dev/gombit/actions/runs/36563135325/job/109392835088)
- An independent contributor approved that head and the PR was merged. The same reviewer later requested changes on a separate failure-classification problem. [Approval](https://github.com/gombit-dev/gombit/pull/525#pullrequestreview-5355526242) · [Merge commit](https://github.com/gombit-dev/gombit/commit/8734759cd6664246f391484c357f1f8364856d96) · [Later review](https://github.com/gombit-dev/gombit/pull/525#pullrequestreview-5376994985)

## Where the evidence stopped

The exhausted delivery is still labeled `handler` in the inspected v0.9.0 source, even though the handler did not return an error. This can send an operator toward the wrong cause. The test checks the retry ceiling, failure reason and log attempt count. It leaves the failure kind unasserted. Before using that label for alert routing, I would test the failed record and log fields together on the lease-expiry path. [Tagged worker](https://github.com/gombit-dev/gombit/blob/dbf4d5b3a3f0788befa61882278e741376b8627d/jobs/worker.go#L215-L248) · [Failed-record construction](https://github.com/gombit-dev/gombit/blob/dbf4d5b3a3f0788befa61882278e741376b8627d/jobs/worker.go#L420-L434) · [Kind contract](https://github.com/gombit-dev/gombit/blob/dbf4d5b3a3f0788befa61882278e741376b8627d/jobs/errors.go#L20-L33)

The case uses public source, review and hosted CI. Production incident, adoption and financial outcomes are unknown. Sarmad scoped the contribution, directed the AI-assisted implementation and evaluated the evidence.
