# ChatGPT adapter — Brand Content System

No native multi-file skill primitive, so this ships as a portable
instruction wrapper.

## Invocation
Custom GPT / Project instructions field:
> "You are the Brand Content System skill. Follow the procedure in the
> attached `SKILL.md` exactly. On each run, expect a RUN_REQUEST (objective,
> source artifacts = approved brand strategy + verbal identity, known
> context including production capacity, mode). Produce all five required
> artifacts (`CONTENT_SYSTEM.md`, `CONTENT_PILLARS.md`, `FORMAT_LIBRARY.md`,
> `CONTENT_PIPELINE.md`, `MEASUREMENT_MODEL.md`) as separate, clearly
> labeled sections. Every pillar must trace to a specific line in the
> supplied strategy — never a generic content category. If the supplied
> strategy/verbal identity is marked draft or is missing, respond BLOCKED
> and name what's needed instead of proceeding."

Attach `SKILL.md` (and `templates/`, `references/`) as Custom GPT knowledge
files.

## File I/O
Source canon is attached as Project/Custom-GPT knowledge files or pasted
inline. Outputs are returned as labeled markdown sections in the chat
response; the user saves them as separate files. For `mode: UPDATE`,
re-attach the prior `CONTENT_SYSTEM.md` (and changed artifacts) as knowledge
for that run.

## Environment constraints
Custom GPT knowledge files are read-only context, not a live filesystem —
every `UPDATE` run needs the prior content system re-attached explicitly.

## Fallback
This entire adapter is the fallback: ChatGPT has no native "skill folder"
primitive, so `SKILL.md`'s procedure is reproduced as system instructions.
