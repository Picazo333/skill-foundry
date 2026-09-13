# HANDOFF PROMPT — <product name>
_From: product-auditor (mode: <AUDIT | QA>) · Run date: <date>_

## Recommended next skill
`<ai-resource-router | canonical-context-builder>` — <one line why>

## What the next agent needs (artifacts only, not this conversation)
- `PRODUCT_AUDIT.md` — findings and verdicts.
- `IMPLEMENTATION_PLAN.md` — implement-now / follow-up items, ordered.
- `REGRESSION_MATRIX.md` — parity and no-regression checks (+ results if QA).
- `QA_CONTRACT.md` — definition of done per item.

## Exact next action
<e.g. "Dispatch IMPLEMENTATION_PLAN.md items 1–4 (blocked by migration in
item 1) to an execution agent via ai-resource-router. Do not start item 5
until item 1's migration is confirmed applied.">

## Constraints that carry forward
- <e.g. "no schema changes beyond migration in item 1">
- <e.g. "desktop-only this pass per RUN_REQUEST.constraints">

## Open items not blocking handoff
- <suspected findings / backlog items the next agent should know about but
  that don't block starting>

## Explicitly NOT done by this run
- No product code, config, or data was written or changed by this audit.
  <If mode: QA — "No not-done/partial item was fixed; only verified.">
