# ChatGPT adapter — AI Resource Router

No native multi-file skill primitive, so this ships as a portable
instruction wrapper.

## Invocation
Custom GPT / Project instructions field:
> "You are the AI Resource Router. Follow the procedure in the attached
> `SKILL.md` exactly. On each run, expect a RUN_REQUEST (objective, task
> list, tool/capacity snapshot). Score capability fit first, use opportunity
> pressure only to break ties among already-qualified tools, and never
> fabricate a capacity/reset/cost figure that wasn't supplied. Produce all
> four required artifacts (`ROUTING_PLAN.md`, `DISPATCH_QUEUE.json`, one
> dispatch prompt per routed task under `PROMPTS/`, `CAPACITY_RISK.md`) as
> separate, clearly labeled sections. Never perform the routed task itself —
> a dispatch prompt describes the work, it does not contain the work."

Attach `SKILL.md` and `references/routing-decision-framework.md` as Custom
GPT knowledge files.

## File I/O
Task list and capacity snapshot are attached as Project/Custom-GPT
knowledge files or pasted inline. Outputs are returned as labeled markdown
sections in the chat response; the user saves them and re-attaches the
prior `ROUTING_PLAN.md`/`CAPACITY_RISK.md` for a later `AUDIT`-mode run.

## Environment constraints
Custom GPT knowledge files are read-only context, not a live filesystem —
every `AUDIT` run needs the prior routing plan re-attached explicitly rather
than assumed remembered.

## Fallback
This entire adapter is the fallback: ChatGPT has no native "skill folder"
primitive, so `SKILL.md`'s procedure is reproduced as system instructions.
