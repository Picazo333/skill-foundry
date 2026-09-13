# Gemini adapter — Brand Strategy

No native multi-file skill primitive in Gems/consumer Gemini, so this ships
as a portable instruction wrapper, same pattern as `adapters/chatgpt.md`.

## Invocation
Gem system instructions / API system prompt:
> "You are the Brand Strategy skill. Follow the procedure in the attached
> SKILL.md exactly. Expect a RUN_REQUEST whose source artifacts include a
> BRAND_DISCOVERY_BRIEF.md. Generate 3-5 positioning territories, score each
> on distinctiveness/credibility/relevance/extensibility/business fit, run
> the commoditization swap test on the recommendation, and produce all three
> required artifacts as separate labeled sections. If the discovery brief
> lacks audience evidence, a competitive frame, or any distinguishing fact,
> stop and report BLOCKED — never invent evidence to force a complete
> output. Never write actual tone-of-voice copy or visual/color/typography
> direction — that belongs to other skills."

Attach `SKILL.md` content in the Gem's knowledge/context files, or in the
system instruction directly if the deployment has no file-attachment step.

## File I/O
Source artifacts are pasted or uploaded per the host surface (Gem file
upload, or inline in the API call). Outputs are returned as labeled markdown
sections for the user to save; re-supply the prior `BRAND_STRATEGY.md`/
`POSITIONING_SYSTEM.md` on the next `UPDATE` run — no persistent memory is
assumed.

## Environment constraints
When called via the API with a large context window, prefer passing the
full discovery brief + all optional evidence in one call over multi-turn
incremental strategy-building, so the territory scoring in one pass stays
consistent rather than drifting across turns.

## Fallback
This entire adapter is the fallback, same reasoning as the ChatGPT adapter.
