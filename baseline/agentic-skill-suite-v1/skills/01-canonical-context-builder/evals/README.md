# Evals — Canonical Context Builder

4 cases in `cases/`: 3 core scenarios (from `SPEC.md`'s required eval
scenarios) + 1 edge/failure case. Each follows
`/shared/templates/EVAL_TEMPLATE.md`.

| Case | Type | Tests |
|---|---|---|
| `01-multi-rename-project.md` | core | authority/recency ranking, deprecated register, delta on rename |
| `02-brand-with-rejected-directions.md` | core | deprecated vs. current separation for creative work |
| `03-sparse-project-unresolved-hypotheses.md` | core | doesn't invent facts when evidence is thin |
| `04-edge-contradictory-equal-authority.md` | edge/failure | must NOT auto-resolve a same-tier same-recency conflict |
