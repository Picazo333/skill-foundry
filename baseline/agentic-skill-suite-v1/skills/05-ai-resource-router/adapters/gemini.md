# Gemini adapter — AI Resource Router

No native multi-file skill primitive in Gems/consumer Gemini, so this ships
as a portable instruction wrapper, same pattern as `adapters/chatgpt.md`.

## Invocation
Gem system instructions / API system prompt:
> "You are the AI Resource Router. Follow the procedure in the attached
> SKILL.md exactly. Expect a RUN_REQUEST (objective, task list, tool/
> capacity snapshot) and produce all four required artifacts as separate
> labeled sections. Score capability fit before opportunity pressure; never
> fabricate a capacity/reset/cost figure; never perform a routed task
> yourself — only produce the routing plan and dispatch prompts for other
> tools to execute."

Attach `SKILL.md` content in the Gem's knowledge/context files, or in the
system instruction directly if the deployment has no file-attachment step.

## File I/O
Task list and capacity snapshot are pasted or uploaded per the host surface
(Gem file upload, or inline in the API call). Outputs are returned as
labeled markdown/JSON sections for the user to save; re-supply the prior
`ROUTING_PLAN.md`/`CAPACITY_RISK.md` on a later `AUDIT` run — no persistent
memory is assumed.

## Environment constraints
When called via the API with a large context window, prefer passing the
full task list + full capacity snapshot in one call over multi-turn
incremental supply, so opportunity-pressure comparisons across tools aren't
computed against a partial picture.

## Fallback
This entire adapter is the fallback, same reasoning as the ChatGPT adapter.
