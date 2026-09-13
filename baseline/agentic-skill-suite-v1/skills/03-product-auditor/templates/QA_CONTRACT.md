# QA CONTRACT — <product name>
_Run date: <date> · Built by: product-auditor v1.0.0_
_Binds: IMPLEMENTATION_PLAN.md items <range/list>_

> The acceptance contract an execution agent and a later QA-mode run are
> both bound to. "Done" means exactly this — nothing implied, nothing
> reinterpreted at QA time.

## Definition of done, per item

### Item <N> — <short title>
- **Acceptance criteria (from IMPLEMENTATION_PLAN.md):** <copied verbatim>
- **Verification method:** <how QA will check this — route walk, test suite,
  data inspection, screenshot diff>
- **Evidence required for `done`:** <what must be shown/cited — not just
  "looks right">
- **Explicitly out of scope for this item:** <what QA should NOT flag as
  incomplete because it was never in scope>

<repeat per item>

## Global constraints QA checks for
- No item in "Do NOT touch" (`IMPLEMENTATION_PLAN.md`) was altered.
- No migration ran without its stated rollback path existing.
- `REGRESSION_MATRIX.md` checks all executed, not sampled.
- No new regression introduced outside the plan's stated scope, or if one
  was, it is logged as a new finding — not silently absorbed into "done".
