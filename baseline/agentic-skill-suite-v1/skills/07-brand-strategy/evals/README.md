# Evals — Brand Strategy

4 cases in `cases/`: 3 core scenarios (the exact eval scenarios required by
`SPEC.md`) + 1 edge/failure case. Each follows
`/shared/templates/EVAL_TEMPLATE.md`.

| Case | Type | Tests |
|---|---|---|
| `01-orthodontic-brand.md` | core | finding real differentiation in a commoditized local-market category; regulatory guardrails as operational rules |
| `02-ai-consulting-agency.md` | core | scoring/tiebreaking between multiple credible evidence-backed territories; no-benchmark-claim constraint |
| `03-consumer-apparel-brand.md` | core | `mode: UPDATE` repositioning against a prior strategy; strict non-trigger boundary (no visual/verbal leakage) |
| `04-edge-weak-generic-discovery-input.md` | edge/failure | must stop at `BLOCKED` rather than invent differentiation from a discovery brief with no real evidence |
