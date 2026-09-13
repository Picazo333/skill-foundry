# Evals — Brand Quality Auditor

4 cases in `cases/`: 3 core scenarios (from `SPEC.md`'s required eval
scenarios) + 1 edge/failure case. Each follows
`/shared/templates/EVAL_TEMPLATE.md`.

| Case | Type | Tests |
|---|---|---|
| `01-website-drift.md` | core | regression detection against explicit canon; strategy left ungraded when not supplied |
| `02-ai-generated-social-creative.md` | core | operationalized AI-slop detection, every hit tied to a canon citation |
| `03-brand-book-self-audit.md` | core | audits a section of canon-adjacent material without collapsing canon vs. artifact distinction, defers ambiguous canon-vs-violation cases |
| `04-edge-missing-canon-must-block.md` | edge/failure | must return BLOCKED, not grade against implicit/assumed standards — the suite-level "requires explicit canon" gate |
