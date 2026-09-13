# Evals — Research Architect

4 cases in `cases/`: 3 core scenarios (from `SPEC.md`'s required eval
scenarios) + 1 edge/failure case. Each follows
`/shared/templates/EVAL_TEMPLATE.md`.

| Case | Type | Tests |
|---|---|---|
| `01-bold-automation-agency.md` | core | key-area weighting on an operations/automation-heavy business; workflow-first AI lens applied per domain |
| `02-sports-betting-tipster-market.md` | core | domain-native lens discovery vs. generic filler; primary-evidence triggers; AUTONOMOUS mode with no "continue?" prompts |
| `03-dental-operating-system.md` | core | multi-stakeholder regulated market; interconnected domain map across clinical/ops/compliance; ≥150/≥50 iteration minimums with real material-delta discipline |
| `04-edge-stops-before-execution-and-rejects-padding.md` | edge/failure | must stop before deep research even when asked to also execute; must reject padded/duplicate iterations that don't pass the material-delta test |
