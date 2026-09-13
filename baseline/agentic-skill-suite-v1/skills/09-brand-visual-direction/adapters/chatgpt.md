# ChatGPT adapter — Brand Visual Direction

No native multi-file skill primitive, so this ships as a portable
instruction wrapper.

## Invocation
Custom GPT / Project instructions field:
> "You are the Brand Visual Direction skill. Follow the procedure in the
> attached `SKILL.md` exactly. On each run, expect a RUN_REQUEST
> (objective, source artifacts — minimum `BRAND_STRATEGY.md` — mode).
> Generate 3-5 territories across all 8 axes (composition, materiality,
> type logic, color behavior, image language, motion, density, UI/system
> implications), run the divergence audit before scoring, flag category
> clichés and AI-slop defaults, then produce all four required artifacts
> (`VISUAL_TERRITORIES.md`, `APPROVED_VISUAL_DIRECTION.md`,
> `VISUAL_ANTI_PATTERNS.md`, `GENERATION_LANGUAGE.md`) as separate, clearly
> labeled sections. Never present territories that only differ by accent
> color as materially distinct."

Attach `SKILL.md`, `references/`, and `templates/` as Custom GPT knowledge
files.

## File I/O
`BRAND_STRATEGY.md` and any optional references/anti-references are
attached as Project/Custom-GPT knowledge files or pasted inline. Outputs
return as labeled markdown sections in the chat response; the user saves
them as separate files for handoff to `brand-identity-system`.

## Note on image generation
If the platform's native image generation is used to *visualize* a
territory or the approved direction for stakeholder review, treat the
generated image as an illustration of the written grammar, not a
replacement for it. `APPROVED_VISUAL_DIRECTION.md` and
`GENERATION_LANGUAGE.md` remain the canonical artifacts handed to
`brand-identity-system` — a generated image is not itself a required
output artifact of this skill.

## Environment constraints
Custom GPT knowledge files are read-only context, not a live filesystem —
a `mode: UPDATE` run needs `BRAND_STRATEGY.md` and the prior
`VISUAL_TERRITORIES.md`/`APPROVED_VISUAL_DIRECTION.md` re-attached
explicitly.

## Fallback
This entire adapter is the fallback: ChatGPT has no native "skill folder"
primitive, so `SKILL.md`'s procedure is reproduced as system instructions.
