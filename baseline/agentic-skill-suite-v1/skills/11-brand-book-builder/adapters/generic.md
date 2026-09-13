# Generic adapter — Brand Book Builder

For any chat-based LLM interface with file upload or paste support.

## Invocation
Paste or reference `SKILL.md` as a system/instruction message, then supply
the `RUN_REQUEST` fields as a message (objective, all 6 source artifacts,
constraints, mode). If the interface has no persistent memory, re-paste
`BRAND_BOOK.md` at the start of any `mode: UPDATE` session — it is the
required `prior_run` input, not something to reconstruct from memory.

## File I/O
- **Reading sources:** paste the text of `VERBAL_IDENTITY.md`,
  `MESSAGE_HIERARCHY.md`, `VOICE_EXAMPLES.md`, `IDENTITY_SYSTEM.md`,
  `DESIGN_TOKENS.json`, and `APPLICATION_RULES.md` directly, or upload if
  supported; same for optional `BRAND_STRATEGY.md`/assets.
- **Writing outputs:** the assistant returns the three required artifacts
  (`BRAND_BOOK.md`, `BRAND_BOOK_OUTLINE.md`, `BRAND_BOOK_ASSET_CHECKLIST.md`)
  as separate, clearly delimited markdown blocks so they can be saved as
  separate files.

## Environment constraints
No filesystem access assumed. The user is responsible for saving the
returned artifacts and re-supplying all 6 source canon artifacts (plus
`BRAND_BOOK.md` if `mode: UPDATE`) on the next run — this skill does not
retain context between sessions.

## Fallback
N/A — this is the baseline all other adapters specialize.
