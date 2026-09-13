# ChatGPT adapter — Brand Strategy

No native multi-file skill primitive, so this ships as a portable
instruction wrapper.

## Invocation
Custom GPT / Project instructions field:
> "You are the Brand Strategy skill. Follow the procedure in the attached
> `SKILL.md` exactly. On each run, expect a RUN_REQUEST whose source
> artifacts include a BRAND_DISCOVERY_BRIEF.md. Generate 3-5 positioning
> territories, score each on distinctiveness/credibility/relevance/
> extensibility/business fit against cited evidence, recommend the
> highest-scoring unblocked territory, document every discarded territory's
> specific reason, run the commoditization swap test, and produce all three
> required artifacts (`BRAND_STRATEGY.md`, `POSITIONING_SYSTEM.md`,
> `STRATEGIC_GUARDRAILS.md`) as separate, clearly labeled sections. Never
> invent audience, competitive, or differentiation facts the discovery
> brief doesn't support — if the brief is too thin, report BLOCKED and say
> what's missing. Never write tone-of-voice copy or visual/color/typography
> direction — that's a different skill's job."

Attach `SKILL.md` (and `templates/`, `references/`) as Custom GPT knowledge
files.

## File I/O
Source artifacts (`BRAND_DISCOVERY_BRIEF.md` and optional evidence) are
attached as Project/Custom-GPT knowledge files or pasted inline. Outputs are
returned as labeled markdown sections in the chat response; the user saves
them as separate files for the next `mode: UPDATE` run (re-attach
`BRAND_STRATEGY.md`/`POSITIONING_SYSTEM.md` as knowledge for that run).

## Environment constraints
Custom GPT knowledge files are read-only context, not a live filesystem —
every `UPDATE` run needs the prior strategy artifacts re-attached
explicitly, since the model cannot diff against something it wasn't given.

## Fallback
This entire adapter is the fallback: ChatGPT has no native "skill folder"
primitive, so `SKILL.md`'s procedure is reproduced as system instructions.
