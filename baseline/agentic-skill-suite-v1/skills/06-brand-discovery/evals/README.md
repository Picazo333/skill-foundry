# Evals — Brand Discovery

4 cases in `cases/`: 3 core scenarios (from `SPEC.md`'s required eval
scenarios) + 1 edge/failure case. Each follows
`/shared/templates/EVAL_TEMPLATE.md`.

| Case | Type | Tests |
|---|---|---|
| `01-dental-clinic-discovery.md` | core | FACT/CLAIM boundary, unstated business objective handled as flagged hypothesis, no premature positioning |
| `02-streetwear-aggressive-references.md` | core | reference mapping by underlying quality, contradiction detection (exclusive vs. accessible), no design work |
| `03-b2b-automation-agency-unclear-offer.md` | core | multi-stakeholder contradiction not resolved, materiality-filtered gap list, PARTIAL status when interviews are unavailable |
| `04-edge-contradictory-founder-input.md` | edge/failure | must NOT silently resolve or average a direct founder self-contradiction (premium vs. accessible on the same axis) |
