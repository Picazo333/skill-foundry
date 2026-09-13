# Gemini adapter — Brand Discovery

No native multi-file skill primitive in Gems/consumer Gemini, so this ships
as a portable instruction wrapper, same pattern as `adapters/chatgpt.md`.

## Invocation
Gem system instructions / API system prompt:
> "You are the Brand Discovery skill. Follow the procedure in the attached
> SKILL.md exactly. Expect a RUN_REQUEST (objective, source artifacts,
> mode) and produce all three required artifacts
> (BRAND_DISCOVERY_BRIEF.md, DISCOVERY_GAPS.md, REFERENCE_MAP.md) as
> separate labeled sections. Classify every statement into FACTS / CLAIMS /
> ASPIRATIONS / HYPOTHESES / NON-NEGOTIABLES; never promote an unverified
> claim to a fact; never resolve a contradiction or suggest a strategic/
> visual direction — log contradictions and material gaps instead."

Attach `SKILL.md` content in the Gem's knowledge/context files, or in the
system instruction directly if the deployment has no file-attachment step.

## File I/O
Source artifacts are pasted or uploaded per the host surface (Gem file
upload, or inline in the API call). Outputs are returned as labeled markdown
sections for the user to save; re-supply the prior brief on the next
`UPDATE` run — no persistent memory is assumed.

## Environment constraints
When called via the API with a large context window, prefer passing the
full set of source artifacts (interviews, reviews, competitor notes) in one
call over multi-turn incremental extraction, to avoid drift in how
statements get classified across turns.

## Fallback
This entire adapter is the fallback, same reasoning as the ChatGPT adapter.
