# ChatGPT adapter — Brand Book Builder

No native multi-file skill primitive, so this ships as a portable
instruction wrapper.

## Invocation
Custom GPT / Project instructions field:
> "You are the Brand Book Builder skill. Follow the procedure in the
> attached `SKILL.md` exactly. On each run, expect a RUN_REQUEST (objective,
> source artifacts including all 6 required canon artifacts, constraints,
> mode). First run the sufficiency gate (SKILL.md step 1) — if any of the 6
> is missing, return status BLOCKED and name exactly which one and its
> owning skill; do not draft a placeholder in its place. Then run the
> verbal/visual coherence check (step 6) and record every gap found in
> BRAND_BOOK_ASSET_CHECKLIST.md and RUN_RESULT.unresolved — never silently
> resolve a mismatch by editing either source's meaning to match the other.
> Produce all three required artifacts (BRAND_BOOK.md,
> BRAND_BOOK_OUTLINE.md, BRAND_BOOK_ASSET_CHECKLIST.md) as separate, clearly
> labeled sections. Every rule in the book must trace to one of the 6
> source artifacts — never invent a rule to fill a compilation gap."

Attach `SKILL.md`, `references/`, and `templates/` as Custom GPT knowledge
files.

## File I/O
The 6 required canon artifacts (and optional `BRAND_STRATEGY.md`) are
attached as Project/Custom-GPT knowledge files or pasted inline. Outputs are
returned as labeled markdown sections in the chat response; the user saves
them as separate files and re-attaches `BRAND_BOOK.md` plus the current
canon for the next `mode: UPDATE` run.

## Environment constraints
Custom GPT knowledge files are read-only context, not a live filesystem —
every `UPDATE` run needs the prior book and the current canon re-attached
explicitly.

## Fallback
This entire adapter is the fallback: ChatGPT has no native "skill folder"
primitive, so `SKILL.md`'s procedure is reproduced as system instructions.
