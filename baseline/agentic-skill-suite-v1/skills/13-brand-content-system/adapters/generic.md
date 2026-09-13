# Generic adapter — Brand Content System

For any chat-based LLM interface with file upload or paste support.

## Invocation
Paste or reference `SKILL.md` as a system/instruction message, then supply
the `RUN_REQUEST` fields as a message (objective, source artifacts, known
context — especially production capacity, since cadence must be
arithmetic-backed, not invented — and mode).

## File I/O
- **Reading sources:** paste `BRAND_STRATEGY.md` and `VERBAL_IDENTITY.md`
  (or `BRAND_BOOK.md`) directly, or upload if supported. Confirm they are
  marked approved, not draft — the skill blocks otherwise (`SKILL.md` step 1
  / stop conditions).
- **Writing outputs:** the assistant returns the five required artifacts
  (`CONTENT_SYSTEM.md`, `CONTENT_PILLARS.md`, `FORMAT_LIBRARY.md`,
  `CONTENT_PIPELINE.md`, `MEASUREMENT_MODEL.md`) as separate, clearly
  delimited markdown blocks so each can be saved as its own file.

## Environment constraints
No filesystem access assumed. The user saves the five returned artifacts.
For `mode: UPDATE`, re-paste the prior `CONTENT_SYSTEM.md` (and whichever of
the other four changed) at the start of the session — they are the required
`prior_run` input, not something to reconstruct from memory.

## Fallback
N/A — this is the baseline all other adapters specialize.
