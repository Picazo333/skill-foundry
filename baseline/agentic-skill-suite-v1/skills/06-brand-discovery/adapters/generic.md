# Generic adapter — Brand Discovery

For any chat-based LLM interface with file upload or paste support.

## Invocation
Paste or reference `SKILL.md` as a system/instruction message, then supply
the `RUN_REQUEST` fields as a message (objective, source artifacts, mode).
If the interface has no persistent memory, re-paste `BRAND_DISCOVERY_BRIEF.md`
(and `DISCOVERY_GAPS.md`) at the start of any `mode: UPDATE` session — they
are the required `prior_run` input, not something to reconstruct from
memory.

## File I/O
- **Reading sources:** paste interview transcripts, notes, review exports,
  etc. directly, or upload files if supported.
- **Writing outputs:** the assistant returns the three required artifacts
  (`BRAND_DISCOVERY_BRIEF.md`, `DISCOVERY_GAPS.md`, `REFERENCE_MAP.md`) as
  separate, clearly delimited markdown blocks so they can be saved as
  separate files by the user.

## Environment constraints
No filesystem access assumed. The user is responsible for saving the
returned artifacts and re-supplying `BRAND_DISCOVERY_BRIEF.md` /
`DISCOVERY_GAPS.md` on the next `UPDATE` run.

## Fallback
N/A — this is the baseline all other adapters specialize.
