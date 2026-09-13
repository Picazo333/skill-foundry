# Evals — Product Auditor & Implementation Architect

4 cases in `cases/`: 3 core scenarios (from `SPEC.md`'s required eval
scenarios) + 1 edge/failure case. Each follows
`/shared/templates/EVAL_TEMPLATE.md`.

| Case | Type | Mode | Tests |
|---|---|---|---|
| `01-regula-local-first-audit.md` | core | AUDIT | confirmed vs. suspected separation, migration explicitness, canon-contradiction detection, no code written |
| `02-responsive-brand-site-audit.md` | core | AUDIT | mobile parity explicitness, protecting locked/approved content, severity triage (implement-now vs. backlog) |
| `03-partial-implementation-qa.md` | core | QA | evidence-based verdicts, partial vs. done distinction, unscoped-change detection, follow-up plan generation without fixing |
| `04-edge-refuses-to-implement-when-asked.md` | edge/failure | AUDIT | must refuse to write/edit product code even when explicitly asked mid-run |
