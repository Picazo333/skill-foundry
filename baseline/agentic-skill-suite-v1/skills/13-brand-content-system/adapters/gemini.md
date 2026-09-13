# Gemini adapter — Brand Content System

Same portable-instruction-wrapper pattern as `adapters/chatgpt.md`; note
Gemini-specific context/upload conventions where they differ.

## Invocation
Gem / system-instruction field:
> "You are the Brand Content System skill. Follow `SKILL.md`'s procedure
> exactly: derive content pillars only from lines traceable to the supplied
> brand strategy and verbal identity, set cadence only from stated
> production capacity, and produce all five required artifacts
> (`CONTENT_SYSTEM.md`, `CONTENT_PILLARS.md`, `FORMAT_LIBRARY.md`,
> `CONTENT_PIPELINE.md`, `MEASUREMENT_MODEL.md`). If strategy/verbal
> identity is missing or draft, return BLOCKED and name what's needed."

Attach `SKILL.md` (and `templates/`, `references/`) as Gem knowledge files.

## File I/O
Source canon is attached as Gem knowledge files or pasted inline (Gemini's
large context window can hold a full brand book pasted directly if no
upload is available). Outputs are returned as labeled markdown sections;
the user saves each as a separate file.

## Environment constraints
As with ChatGPT, Gem knowledge attachments are static per-session context —
`mode: UPDATE` runs need the prior `CONTENT_SYSTEM.md` re-supplied
explicitly rather than assumed to persist.

## Fallback
This entire adapter is the fallback: no native multi-file skill primitive,
so `SKILL.md`'s procedure is reproduced as system instructions.
