# Case study 03 — One SQL wildcard broke the schema-reset contract

**Problem class:** Database semantics / migration safety / negative-control testing  
**Buyer relevance:** Cleanup and recovery routines must distinguish user-owned objects from reserved system objects.

## Context and defect

Gombit's SQLite schema reset selected objects to drop with `name NOT LIKE 'sqlite_%'`. In SQL `LIKE`, `_` matches any single character, not a literal underscore. The query wrongly preserved user tables such as `sqlitex_cache` and `sqlite3_import` and caused later migration replay to fail with "table already exists". See [original issue #491](https://github.com/gombit-dev/gombit/issues/491).

## Minimal fix

**Before:** `name NOT LIKE 'sqlite_%'`  
**After:** `name NOT LIKE 'sqlite\_%' ESCAPE '\'`

One production SQL line changed. The patch added a native SQLite regression test that verifies user tables and a user view are dropped, while the built-in `sqlite_sequence` table survives.

**Exact contribution:** [PR #651](https://github.com/gombit-dev/gombit/pull/651) · head SHA [`e4431f4249870899f6ed9f7cbff072fcbba9c27d`](https://github.com/gombit-dev/gombit/commit/e4431f4249870899f6ed9f7cbff072fcbba9c27d).

## Falsifiable evidence

- **Original GitHub patch:** exactly `migrations/reset.go` and `migrations/reset_sqlite_prefix_test.go` changed. The test is against native SQLite, not a mocked string predicate.
- **Local isolated reproduction, 13 Nov 2026:** `independent_probes.py` ran both SQL predicates against an in-memory SQLite fixture. The old query selected just `normal_table` and `reserved_anchor`; the corrected query also selected `sqlitex_cache`, `sqlite3_import` and `sqlitex_view`, while excluding `sqlite_sequence`. `PASS`, exit 0.
- **Maintainer review:** `leo-aa88` submitted `APPROVED` (4 Nov 2026); PR merged upstream on 5 Nov 2026.
- **Reported:** original PR author recorded a native SQLite RED→GREEN replay and local focused tests. This document's local reproduction verifies the query semantics, **not Gombit's entire migration pipeline**.

## Outcome and limitations

**VERIFIED:** precise upstream one-line fix, native regression source, maintainer approval, merged PR, independent isolated SQL red/green probe.  
**NOT VERIFIED HERE:** complete SQLite/PostgreSQL/MySQL matrix on the final head, current downstream installations, customer effects or revenue.

## What a buyer can infer

A small syntactic detail can invert a destructive cleanup contract. This contribution demonstrates testing both the intended deletion set **and** the reserved negative control. AI agents performed implementation coding under Sarmad's direction; the evidence is the submitted diff and accepted upstream review, not an unsupported personal coding claim.
