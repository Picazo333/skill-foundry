# Gemini adapter — Brand Visual Direction

Same portable-instruction-wrapper pattern as `adapters/chatgpt.md`; notes
below cover only where Gemini differs.

## Invocation
Gem / system-instructions field:
> "You are the Brand Visual Direction skill. Follow `SKILL.md` exactly.
> Expect a RUN_REQUEST (objective, source artifacts — minimum
> `BRAND_STRATEGY.md` — mode). Generate 3-5 territories across all 8 axes,
> run the divergence audit before scoring, flag category clichés/AI-slop
> defaults against `references/ai-slop-and-cliche-checklist.md`, then
> produce the four required artifacts as separate labeled sections. Never
> present color-swapped territories as materially distinct."

Attach `SKILL.md`, `references/`, and `templates/` as Gem knowledge files
(or paste inline if the surface has no persistent file attachment).

## File I/O
`BRAND_STRATEGY.md` and optional references/anti-references are attached
as knowledge files or pasted inline, subject to that Gemini surface's
context-window and file-count limits — for a large strategy doc plus
multiple visual references, prefer summarized/excerpted source artifacts
over the full raw files if the context window is constrained. Outputs
return as labeled markdown sections.

## Note on image generation
If Gemini's native image generation is used to visualize a territory or
the approved direction, treat it as illustration only — the canonical,
required artifacts remain the written `APPROVED_VISUAL_DIRECTION.md` and
`GENERATION_LANGUAGE.md`.

## Environment constraints
No guaranteed persistent filesystem across sessions — a `mode: UPDATE` run
needs the prior canonical artifacts re-supplied explicitly each session.

## Fallback
This entire adapter is the fallback: `SKILL.md`'s procedure is reproduced
as system instructions, same as `adapters/chatgpt.md`.
