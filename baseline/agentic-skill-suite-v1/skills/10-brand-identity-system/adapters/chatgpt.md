# ChatGPT adapter — Brand Identity System

No native multi-file skill primitive, so this ships as a portable
instruction wrapper.

## Invocation
Custom GPT / Project instructions field:
> "You are the Brand Identity System skill. Follow the procedure in the
> attached `SKILL.md` exactly. On each run, expect a RUN_REQUEST
> (objective, source artifacts — minimum `BRAND_STRATEGY.md` and
> `APPROVED_VISUAL_DIRECTION.md` — mode). Define logo architecture with
> derived (not invented) clear-space/minimum-size values, color roles with
> computed WCAG contrast ratios, a typography scale, grid/spacing/shape
> rules, iconography/imagery rules, and motion principles. Produce all
> three required artifacts (`IDENTITY_SYSTEM.md`, `DESIGN_TOKENS.json`,
> `APPLICATION_RULES.md`) as separate, clearly labeled sections, with
> token values identical to the prose. Never invent a value with no trace
> to the approved direction or a stated derivation method."

Attach `SKILL.md`, `references/`, and `templates/` as Custom GPT knowledge
files.

## File I/O
`BRAND_STRATEGY.md`, `APPROVED_VISUAL_DIRECTION.md`, and any optional
context are attached as Project/Custom-GPT knowledge files or pasted
inline. Outputs return as labeled markdown/JSON sections in the chat
response; the user saves them as separate files for handoff to
`brand-book-builder`.

## Environment constraints
Custom GPT knowledge files are read-only context, not a live filesystem —
a `mode: UPDATE` run needs the prior `IDENTITY_SYSTEM.md`/
`DESIGN_TOKENS.json` re-attached explicitly.

## Fallback
This entire adapter is the fallback: ChatGPT has no native "skill folder"
primitive, so `SKILL.md`'s procedure is reproduced as system instructions.
