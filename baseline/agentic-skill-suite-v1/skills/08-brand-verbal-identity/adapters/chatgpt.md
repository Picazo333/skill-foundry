# ChatGPT adapter — Brand Verbal Identity

No native multi-file skill primitive, so this ships as a portable
instruction wrapper.

## Invocation
Custom GPT / Project instructions field:
> "You are the Brand Verbal Identity skill. Follow the procedure in the
> attached `SKILL.md` exactly. On each run, expect a RUN_REQUEST (objective,
> source artifacts including BRAND_STRATEGY.md, constraints, mode). First
> run the sufficiency gate (SKILL.md step 1) — if positioning, value
> proposition, audience, or a differentiator is missing or too vague, return
> status BLOCKED and say exactly what's missing; do not produce a generic
> adjective-only voice to fill the gap. Otherwise produce all three required
> artifacts (VERBAL_IDENTITY.md, MESSAGE_HIERARCHY.md, VOICE_EXAMPLES.md) as
> separate, clearly labeled sections. Every voice principle must trace to a
> specific BRAND_STRATEGY.md line and include a DO/DON'T pair."

Attach `SKILL.md`, `references/`, and `templates/` as Custom GPT knowledge
files.

## File I/O
`BRAND_STRATEGY.md` and any optional source artifacts are attached as
Project/Custom-GPT knowledge files or pasted inline. Outputs are returned as
labeled markdown sections in the chat response; the user saves them as
separate files for the next `mode: UPDATE` run (re-attach
`VERBAL_IDENTITY.md` etc. as knowledge for that run).

## Environment constraints
Custom GPT knowledge files are read-only context, not a live filesystem —
every `UPDATE` run needs the prior artifacts re-attached explicitly.

## Fallback
This entire adapter is the fallback: ChatGPT has no native "skill folder"
primitive, so `SKILL.md`'s procedure is reproduced as system instructions.
