# Gemini adapter — Brand Identity System

Same portable-instruction-wrapper pattern as `adapters/chatgpt.md`; notes
below cover only where Gemini differs.

## Invocation
Gem / system-instructions field:
> "You are the Brand Identity System skill. Follow `SKILL.md` exactly.
> Expect a RUN_REQUEST (objective, source artifacts — minimum
> `BRAND_STRATEGY.md` and `APPROVED_VISUAL_DIRECTION.md` — mode). Derive
> logo clear-space/minimum-size from supplied mark geometry, compute every
> color-contrast ratio per `references/contrast-verification-method.md`,
> and produce the three required artifacts as separate labeled sections
> with token values identical to the prose. Never invent an untraceable
> value."

Attach `SKILL.md`, `references/`, and `templates/` as Gem knowledge files
(or paste inline if the surface has no persistent file attachment).

## File I/O
`BRAND_STRATEGY.md`, `APPROVED_VISUAL_DIRECTION.md`, and optional context
are attached as knowledge files or pasted inline, subject to that Gemini
surface's context-window and file-count limits — for a large strategy doc
plus multiple reference files, prefer summarized/excerpted source
artifacts over the full raw files if the context window is constrained.
Outputs return as labeled markdown/JSON sections.

## Environment constraints
No guaranteed persistent filesystem across sessions — a `mode: UPDATE` run
needs the prior canonical artifacts (`IDENTITY_SYSTEM.md`,
`DESIGN_TOKENS.json`) re-supplied explicitly each session.

## Fallback
This entire adapter is the fallback: `SKILL.md`'s procedure is reproduced
as system instructions, same as `adapters/chatgpt.md`.
