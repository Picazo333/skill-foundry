# Evals — Brand Skill Orchestrator

4 cases in `cases/`: 3 core scenarios (matching `SPEC.md`'s required eval
scenarios) + 1 edge/failure case. Each follows
`/shared/templates/EVAL_TEMPLATE.md`.

| Case | Type | Tests |
|---|---|---|
| `01-zero-to-brand-book.md` | core | full stage sequence from nothing to a completed brand book, no stage skipped or rerun without cause |
| `02-partial-brand-approved-strategy-no-visual.md` | core | resumes correctly mid-workflow, routes only to what's missing (visual direction), doesn't re-run discovery/strategy |
| `03-existing-brand-content-only.md` | core | narrow objective on an already-approved brand routes directly to brand-content-system, skips discovery/strategy/verbal/visual/identity/book entirely with stated reasons |
| `04-edge-conflicting-strategy-versions.md` | edge/failure | two contradictory BRAND_STRATEGY.md versions with no clear authority — must BLOCK and name the conflict, never silently pick one or route forward |
