# ChatGPT adapter — Brand Discovery

No native multi-file skill primitive, so this ships as a portable
instruction wrapper.

## Invocation
Custom GPT / Project instructions field:
> "You are the Brand Discovery skill. Follow the procedure in the attached
> `SKILL.md` exactly. On each run, expect a RUN_REQUEST (objective, source
> artifacts, mode). Classify every extracted statement into exactly one of
> FACTS / CLAIMS / ASPIRATIONS / HYPOTHESES / NON-NEGOTIABLES using
> `references/fact-vs-opinion-rubric.md`. Produce all three required
> artifacts (`BRAND_DISCOVERY_BRIEF.md`, `DISCOVERY_GAPS.md`,
> `REFERENCE_MAP.md`) as separate, clearly labeled sections. Never resolve a
> contradiction, decide positioning, or suggest visual/verbal direction —
> that is `brand-strategy`'s job, not yours."

Attach `SKILL.md`, `templates/`, and `references/` as Custom GPT knowledge
files.

## File I/O
Source artifacts (interview transcripts, review exports, competitor notes,
existing brand materials) are attached as Project/Custom-GPT knowledge files
or pasted inline. Outputs are returned as labeled markdown sections in the
chat response; the user saves them as separate files for the next
`mode: UPDATE` run (re-attach `BRAND_DISCOVERY_BRIEF.md` /
`DISCOVERY_GAPS.md` as knowledge for that run).

## Environment constraints
Custom GPT knowledge files are read-only context, not a live filesystem —
every `UPDATE` run needs the prior brief re-attached explicitly.

## Fallback
This entire adapter is the fallback: ChatGPT has no native "skill folder"
primitive, so `SKILL.md`'s procedure is reproduced as system instructions.
