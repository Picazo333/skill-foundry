# Generic adapter — Canonical Context Builder

For any chat-based LLM interface with file upload or paste support.

## Invocation
Paste or reference `SKILL.md` as a system/instruction message, then supply
the `RUN_REQUEST` fields as a message (objective, source artifacts, mode).
If the interface has no persistent memory, re-paste `PROJECT_CANON.md` (and
the other canonical artifacts) at the start of any `mode: UPDATE` session —
they are the required `prior_run` input, not something to reconstruct from
memory.

## File I/O
- **Reading sources:** paste text directly, or upload files if supported.
- **Writing outputs:** the assistant returns the five required artifacts as
  separate, clearly delimited markdown blocks (one per artifact) so they can
  be saved as separate files by the user.

## Environment constraints
No filesystem access assumed. The user is responsible for saving the
returned artifacts and re-supplying them on the next `UPDATE` run.

## Fallback
N/A — this is the baseline all other adapters specialize.
