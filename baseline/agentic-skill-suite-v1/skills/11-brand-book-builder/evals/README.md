# Evals — Brand Book Builder

4 cases in `cases/`: 3 core scenarios (from `SPEC.md`'s required eval
scenarios) + 1 edge/failure case. Each follows
`/shared/templates/EVAL_TEMPLATE.md`.

| Case | Type | Tests |
|---|---|---|
| `01-compact-startup-brand-book.md` | core | executive depth selection, correct exclusion of governance/appendix, no padding of missing surfaces |
| `02-full-client-manual.md` | core | full depth, all 6 surfaces paired, asset checklist catches a genuinely missing example instead of inventing one |
| `03-conflicting-upstream-artifacts.md` | core | explicit contradiction between verbal and visual canon is flagged, not silently resolved; status PARTIAL |
| `04-edge-subtle-positioning-misalignment.md` | edge/failure | canon that is internally consistent on its own but subtly misaligned in audience/positioning between verbal and visual — must be caught by the coherence check, not waved through as "no contradiction found" |
