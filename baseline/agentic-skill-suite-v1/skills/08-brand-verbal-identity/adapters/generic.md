# Generic adapter — Brand Verbal Identity

For any chat-based LLM interface with file upload or paste support.

## Invocation
Paste or reference `SKILL.md` as a system/instruction message, then supply
the `RUN_REQUEST` fields as a message (objective, source artifacts including
`BRAND_STRATEGY.md`, constraints, mode). If the interface has no persistent
memory, re-paste `VERBAL_IDENTITY.md` at the start of any `mode: UPDATE`
session — it is the required `prior_run` input, not something to reconstruct
from memory.

## File I/O
- **Reading sources:** paste `BRAND_STRATEGY.md` text directly, or upload if
  supported; same for optional existing copy/customer language/compliance
  docs.
- **Writing outputs:** the assistant returns the three required artifacts
  (`VERBAL_IDENTITY.md`, `MESSAGE_HIERARCHY.md`, `VOICE_EXAMPLES.md`) as
  separate, clearly delimited markdown blocks so they can be saved as
  separate files.

## Environment constraints
No filesystem access assumed. The user is responsible for saving the
returned artifacts and re-supplying them on the next `UPDATE` run.

## Fallback
N/A — this is the baseline all other adapters specialize.
