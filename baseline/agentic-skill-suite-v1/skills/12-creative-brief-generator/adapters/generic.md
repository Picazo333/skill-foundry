# Generic adapter — Creative Brief Generator

For any chat-based LLM interface with file upload or paste support.

## Invocation
Paste or reference `SKILL.md` as a system/instruction message, then supply
the `RUN_REQUEST` fields as a message (objective, canon source artifacts,
known_context, constraints, mode). If the interface has no persistent
memory, re-paste `CREATIVE_BRIEF.md` (and the other two artifacts) at the
start of any `mode: UPDATE` session — they are the required `prior_run`
input, not something to reconstruct from memory.

## File I/O
- **Reading canon:** paste the relevant canon sections directly, or upload
  `BRAND_BOOK.md` / `STRATEGY.md` + `VERBAL_IDENTITY.md` (+
  `VISUAL_IDENTITY.md`) if supported. Do not paste the entire brand book by
  default — per `SKILL.md` step 3, only sections relevant to the deliverable
  are needed; more can be requested if the run flags it's missing something.
- **Writing outputs:** the assistant returns the three required artifacts
  (`CREATIVE_BRIEF.md`, `ASSET_REQUIREMENTS.md`, `PRODUCTION_HANDOFF.md`) as
  separate, clearly delimited markdown blocks so they can be saved as
  separate files by the user.

## Environment constraints
No filesystem access assumed. The user is responsible for saving the
returned artifacts and re-supplying them (plus updated canon, if it
changed) on the next run.

## Fallback
N/A — this is the baseline all other adapters specialize.
