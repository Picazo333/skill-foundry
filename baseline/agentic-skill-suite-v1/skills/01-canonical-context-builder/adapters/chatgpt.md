# ChatGPT adapter — Canonical Context Builder

No native multi-file skill primitive, so this ships as a portable
instruction wrapper.

## Invocation
Custom GPT / Project instructions field:
> "You are the Canonical Context Builder. Follow the procedure in the
> attached `SKILL.md` exactly. On each run, expect a RUN_REQUEST (objective,
> source artifacts, mode). Produce all five required artifacts
> (`PROJECT_CANON.md`, `DECISION_REGISTER.md`, `OPEN_LOOPS.md`,
> `DEPRECATED_REGISTER.md`, `NEXT_START_PROMPT.md`) as separate, clearly
> labeled sections. Never invent facts; unresolved conflicts go to
> OPEN_LOOPS.md, never silently resolved."

Attach `SKILL.md` (and `templates/`) as Custom GPT knowledge files.

## File I/O
Source artifacts are attached as Project/Custom-GPT knowledge files or
pasted inline. Outputs are returned as labeled markdown sections in the
chat response; the user saves them as separate files for the next
`mode: UPDATE` run (re-attach `PROJECT_CANON.md` etc. as knowledge for that
run).

## Environment constraints
Custom GPT knowledge files are read-only context, not a live filesystem —
every `UPDATE` run needs the prior canon re-attached explicitly.

## Fallback
This entire adapter is the fallback: ChatGPT has no native "skill folder"
primitive, so `SKILL.md`'s procedure is reproduced as system instructions.
