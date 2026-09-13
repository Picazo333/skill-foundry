# Evals — Creative Brief Generator

4 cases in `cases/`: 3 core scenarios (from `SPEC.md`'s required eval
scenarios) + 1 edge/failure case. Each follows
`/shared/templates/EVAL_TEMPLATE.md`.

| Case | Type | Tests |
|---|---|---|
| `01-landing-page-brief.md` | core | canon-cited mandatories, single message, checkable acceptance criteria |
| `02-reel-video-brief.md` | core | claims policy enforcement, does not invent a data point to strengthen the pitch |
| `03-executive-deck-brief.md` | core | format constraint (slide cap) honored, hype-language voice rule enforced |
| `04-edge-canon-conflict.md` | edge/failure | must flag a request that conflicts with a locked brand constraint, not silently comply |
