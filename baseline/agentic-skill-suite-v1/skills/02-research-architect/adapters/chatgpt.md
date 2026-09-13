# ChatGPT adapter — Research Architect

No native multi-file skill primitive, so this ships as a portable
instruction wrapper.

## Invocation
Custom GPT / Project instructions field:
> "You are the Research Architect. Follow the procedure in the attached
> `SKILL.md` exactly, including the 150+ scope-expansion / 50+
> domain-polishing minimums, the material-delta/novelty test on every
> iteration, key-area weighting (never equal distribution), Coverage Debt,
> the contradiction/white-space/primary-evidence ledgers, the workflow-first
> automation/AI lens, and the 10-pass final QA. Produce all 7 required
> artifacts as separate labeled sections. In `mode: AUTONOMOUS`, do not pause
> to ask 'should I continue' between iterations — checkpoint after each
> logical block instead. In every mode, stop after producing the package —
> never answer the research questions yourself."

Attach `SKILL.md` and `templates/` as Custom GPT knowledge files.

## File I/O
Source artifacts (`PROJECT_CANON.md`, prior `CHECKPOINT.md`, etc.) are
attached as knowledge files or pasted inline. Outputs are returned as
labeled markdown sections; because a 200+iteration program is long, expect
multiple responses — the user saves each `CHECKPOINT.md` update and
re-attaches it if a new chat session is needed to continue (Custom GPT
knowledge files are read-only context per session, not live state).

## Environment constraints
No live filesystem; every resumed session needs the prior `CHECKPOINT.md`
and artifacts re-attached explicitly, same pattern as
`canonical-context-builder`'s ChatGPT adapter. Long outputs may need to be
split across turns — checkpoint before the split, not mid-iteration.

## Fallback
This entire adapter is the fallback: ChatGPT has no native "skill folder"
primitive, so `SKILL.md`'s procedure is reproduced as system instructions.
