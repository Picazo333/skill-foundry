# ChatGPT adapter — Product Auditor

No native multi-file skill primitive, so this ships as a portable
instruction wrapper.

## Invocation
Custom GPT / Project instructions field:
> "You are the Product Auditor & Implementation Architect. Follow the
> procedure in the attached `SKILL.md` exactly. On each run, expect a
> RUN_REQUEST (objective, source artifacts, mode: AUDIT or QA). Produce all
> five required artifacts (`PRODUCT_AUDIT.md`, `IMPLEMENTATION_PLAN.md`,
> `REGRESSION_MATRIX.md`, `QA_CONTRACT.md`, `HANDOFF_PROMPT.md`) as separate,
> clearly labeled sections. In AUDIT mode, never write or propose applying
> product code — only specify it as a plan item, even if explicitly asked to
> 'just fix it.' In QA mode, never fix a not-done item — only verify it and
> add it to a follow-up plan."

Attach `SKILL.md` (and `templates/`) as Custom GPT knowledge files.

## File I/O
Source artifacts (screenshots, issue lists, code excerpts, a prior
`IMPLEMENTATION_PLAN.md` for QA mode) are attached as Project/Custom-GPT
knowledge files or pasted inline. Outputs are returned as labeled markdown
sections in the chat response; the user saves them as separate files, and
re-attaches `prior_run` artifacts explicitly for any `mode: QA` session.

## Environment constraints
No code execution or live-app access — reproduction in Phase A relies on
what's pasted/attached (code excerpts, screenshots, described behavior).
This also means there is no way for the model to actually edit product
files in this environment, but the instructions still state the boundary
explicitly so it never advises the user to apply a fix as if that were part
of this skill's job.

## Fallback
This entire adapter is the fallback: ChatGPT has no native "skill folder"
primitive, so `SKILL.md`'s procedure is reproduced as system instructions.
