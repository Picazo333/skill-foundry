# Gemini adapter — Brand Verbal Identity

No native multi-file skill primitive in Gems/consumer Gemini, so this ships
as a portable instruction wrapper, same pattern as `adapters/chatgpt.md`.

## Invocation
Gem system instructions / API system prompt:
> "You are the Brand Verbal Identity skill. Follow the procedure in the
> attached SKILL.md exactly. Expect a RUN_REQUEST (objective, source
> artifacts including BRAND_STRATEGY.md, mode). Run the sufficiency gate
> first; if strategy signal is too thin, return BLOCKED and name what's
> missing instead of producing generic voice adjectives. Otherwise produce
> all three required artifacts as separate labeled sections, each voice
> principle traced to strategy with a DO/DON'T pair."

Attach `SKILL.md` content in the Gem's knowledge/context files, or in the
system instruction directly if the deployment has no file-attachment step.

## File I/O
`BRAND_STRATEGY.md` and optional sources are pasted or uploaded per the host
surface. Outputs are returned as labeled markdown sections for the user to
save; re-supply the prior artifacts on the next `UPDATE` run — no persistent
memory is assumed.

## Environment constraints
When called via the API with a large context window, prefer passing the
full `BRAND_STRATEGY.md` plus any existing copy/customer language in one
call over multi-turn incremental building, to avoid principle drift across
turns.

## Fallback
This entire adapter is the fallback, same reasoning as the ChatGPT adapter.
