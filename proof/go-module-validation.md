# Case study 02 — Reject invalid Go modules before writing a scaffold

**Problem class:** Input validation / fail-before-write / user-owned file integrity  
**Buyer relevance:** A generator should reject invalid input before creating a broken working directory and forcing a destructive retry.

## Context and root cause

Gombit `gombit new --module` accepted module paths containing `@`, `;` or tabs, even though the Go toolchain rejects them. It could exit successfully after generating files that would not build; rerunning the generator could then require overwriting existing project files. See [original issue #515](https://github.com/gombit-dev/gombit/issues/515).

## Fix

`scaffold/options.go` now validates with Go's own `golang.org/x/mod/module` rules (`CheckImportPath`, reserved module path checks and `SplitPathVersion`) instead of relying on a small hand-written set of string exclusions. The validator runs before scaffold generation writes the destination tree.

**Exact contribution:** [PR #563](https://github.com/gombit-dev/gombit/pull/563) · head SHA [`5375e3006a2e4be183c84db84fd4a4a65d4eca82`](https://github.com/gombit-dev/gombit/commit/5375e3006a2e4be183c84db84fd4a4a65d4eca82).

## Independent review and verification

- Regression source covers valid and invalid module paths, including version suffixes and malformed characters.
- Maintainer `leo-aa88` requested changes twice (6 and 7 Oct 2026). The PR was subsequently `APPROVED` on 27 Oct and merged upstream.
- **Verified from original GitHub:** exact changed file paths, production code patch, upstream closed/merged state, independent reviews.
- **Reported, not rerun here:** the PR's original tests and CI on candidate commits. No full build/test environment has been reconstructed as part of this case-study writing.

## Outcome and limitation

**VERIFIED:** independently merged, test-backed fail-before-write bug fix following two adversarial review rounds.  
**NOT VERIFIED HERE:** newly reproduced baseline failure on an exact pristine Gombit checkout, currently deployed generated apps, customer impact or revenue.

## What a buyer can infer

The central engineering judgment is to validate external input with the **authoritative ecosystem parser**, and to put that validation before irreversible file effects. This is a useful pattern in code generators, agent tools and automation. AI agents wrote implementation code under Sarmad's direction.
