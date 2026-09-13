# Gemini adapter — Brand Skill Orchestrator

No native multi-file skill/dispatch primitive in Gems/consumer Gemini, so
this ships as a portable instruction wrapper, same pattern as
`adapters/chatgpt.md`.

## Invocation
Gem system instructions / API system prompt:
> "You are the Brand Skill Orchestrator. Follow SKILL.md exactly, using the
> routed-skill-contracts.md and stage-detection-rules.md reference docs.
> You determine and report only the single next skill to run — you never
> perform its work yourself."

Attach `SKILL.md` and the two reference docs as Gem knowledge/context files.

## File I/O
User reports artifact inventory each run (upload or inline). Orchestrator
returns `BRAND_WORKFLOW_STATE.md`/`NEXT_SKILL_RUN.json`/handoff package
contents as labeled sections; the user runs the recommended skill separately
and returns with its output for the next orchestrator turn.

## Environment constraints
When called via the API, prefer passing the full current
`BRAND_WORKFLOW_STATE.md` in one call over incremental multi-turn state
building, to avoid inventory drift across turns.

## Fallback
This entire adapter is the fallback, same reasoning as the ChatGPT adapter.
