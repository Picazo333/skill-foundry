# REGRESSION MATRIX — <product name>
_Mode: <AUDIT (defined) | QA (executed)> · Run date: <date> · Built by: product-auditor v1.0.0_

> Desktop/mobile parity and no-regression checks derived from what Phase A
> inspection actually found working — not a generic checklist. If the
> product has no mobile surface, state that explicitly rather than omitting
> the section.

## No-regression checks
Existing behavior that implementation must not break.

| # | Check | Route/component | Desktop result | Mobile result | Notes |
|---|---|---|---|---|---|
| R1 | <behavior that must still work> | <route> | pass \| fail \| n/a (AUDIT: blank) | pass \| fail \| n/a | <notes> |

## Parity checks
Desktop/mobile behavioral parity required by the plan's new/changed items.

| # | Check | Related plan item | Desktop result | Mobile result | Notes |
|---|---|---|---|---|---|
| P1 | <parity requirement> | <IMPLEMENTATION_PLAN.md item #> | pass \| fail \| n/a | pass \| fail \| n/a | <notes> |

## Mobile applicability
- <"Product has a mobile surface: <platform/build>, all rows above apply." |
  "Product has no mobile surface as of <date> — mobile columns are
  explicitly not-applicable, not omitted.">
