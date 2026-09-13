# ChatGPT adapter — Creative Brief Generator

No native multi-file skill primitive, so this ships as a portable
instruction wrapper.

## Invocation
Custom GPT / Project instructions field:
> "You are the Creative Brief Generator. Follow the procedure in the
> attached `SKILL.md` exactly. On each run, expect a RUN_REQUEST (objective,
> canon source artifacts, known_context, constraints, mode). Produce all
> three required artifacts (`CREATIVE_BRIEF.md`, `ASSET_REQUIREMENTS.md`,
> `PRODUCTION_HANDOFF.md`) as separate, clearly labeled sections. Go BLOCKED
> if canon doesn't cover the deliverable; never invent brand rules. If the
> request conflicts with a locked canon rule, flag it explicitly — never
> silently comply or silently drop it."

Attach `SKILL.md`, `templates/`, and `references/` as Custom GPT knowledge
files.

## File I/O
Canon source artifacts are attached as Project/Custom-GPT knowledge files or
pasted inline. Outputs are returned as labeled markdown sections in the
chat response; the user saves them as separate files for the next
`mode: UPDATE` run (re-attach `CREATIVE_BRIEF.md` etc. as knowledge for that
run, alongside the same canon or its updated version).

## Environment constraints
Custom GPT knowledge files are read-only context, not a live filesystem —
every `UPDATE` run needs the prior brief set (and current canon) re-attached
explicitly.

## Fallback
This entire adapter is the fallback: ChatGPT has no native "skill folder"
primitive, so `SKILL.md`'s procedure is reproduced as system instructions.
