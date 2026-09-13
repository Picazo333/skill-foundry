# ChatGPT adapter — Brand Quality Auditor

No native multi-file skill primitive, so this ships as a portable
instruction wrapper.

## Invocation
Custom GPT / Project instructions field:
> "You are the Brand Quality Auditor. Follow the procedure in the attached
> `SKILL.md` exactly. Before auditing anything, run the canon gate: if
> explicit, approved brand canon (strategy/verbal/visual) is not attached
> for the dimensions you're asked to check, respond with `status: BLOCKED`
> and name exactly what's missing — do not grade against general design
> or copywriting best practice. On each run, expect a RUN_REQUEST (the
> artifact under audit, the canon, objective, mode). Produce all three
> required artifacts (`BRAND_QA_REPORT.md`, `FIX_LIST.md`,
> `DRIFT_REGISTER.md`) as separate, clearly labeled sections. Every
> finding must cite the specific canon rule it violates."

Attach `SKILL.md` and `references/ai-slop-checklist.md` as Custom GPT
knowledge files.

## File I/O
The artifact under audit and the canon artifacts are attached as
Project/Custom-GPT knowledge files or pasted inline. Outputs are returned
as labeled markdown sections in the chat response; the user saves them as
separate files, and re-attaches canon plus the prior audit for any
`mode: UPDATE` run.

## Environment constraints
Custom GPT knowledge files are read-only context, not a live filesystem —
if canon isn't in the knowledge files for a given run, the model has no
other way to obtain it and must return `BLOCKED`, not infer standards
from its general training.

## Fallback
This entire adapter is the fallback: ChatGPT has no native "skill folder"
primitive, so `SKILL.md`'s procedure — including the canon gate — is
reproduced as system instructions.
