# COVERAGE DEBT — <project name>
_Last updated: <date, and which Phase-2/3 checkpoint this reflects>_

Coverage Debt = domains whose iteration count is materially below what their
Phase 1 weight implies. Recomputed at every checkpoint (~every 10-15
iterations during expansion, and again at Phase 3 close) — not a one-time
snapshot.

| Domain | Weight | Expected iterations (proportional) | Actual iterations | Debt (expected − actual) | Status |
|---|---|---|---|---|---|
| <Domain 1> | <N> | <N> | <N> | <N> | open / paid down / carried forward |

## Debt paid down this run
- <domain> — <how it was addressed, which iterations closed the gap>

## Debt carried forward (still open at packaging)
- <domain> — <remaining gap> — <why it wasn't closed this run> — must appear
  in `RUN_RESULT.unresolved`.
