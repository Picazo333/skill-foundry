# Evals — Rapid Capture & Triage

4 cases in `cases/`: 3 core scenarios (from `SPEC.md`'s required eval
scenarios) + 1 edge/failure case. Each follows
`/shared/templates/EVAL_TEMPLATE.md`.

| Case | Type | Tests |
|---|---|---|
| `01-long-chaotic-mobile-dictation.md` | core | segmentation of a long unpunctuated dump, recurrent-vs-supervision distinction, priority/time-signal detection, backlog vs. idea handling |
| `02-task-reprioritization-with-renames.md` | core | duplicate/rename matching against a snapshot, preserving unmentioned fields, capture-order vs. invented priority |
| `03-partial-json-update.md` | core | `mode: UPDATE` against a supplied existing JSON, delta scoped to only what changed, no silent overwrite of untouched fields |
| `04-edge-self-contradictory-no-action-items.md` | edge/failure | input with a genuine internal contradiction and no clear action items — must NOT force false structure or invent a resolution |
