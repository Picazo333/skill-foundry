# Generic adapter — AI Resource Router

For any chat-based LLM interface with file upload or paste support.

## Invocation
Paste or reference `SKILL.md` as a system/instruction message, then supply
the `RUN_REQUEST` fields as a message: objective, the task list (each with
type, definition of done, hard requirements), and the tool/capacity
snapshot (each tool with whatever fields are actually known — leave the
rest unstated rather than guessed).

## File I/O
- **Reading sources:** paste the task list and capacity snapshot directly,
  or upload files if supported. Reference canonical source artifacts
  (plans, canon) by name rather than pasting them in full unless they're
  short.
- **Writing outputs:** the assistant returns the four required artifacts —
  `ROUTING_PLAN.md`, `DISPATCH_QUEUE.json`, one `PROMPTS/<task_id>.md` per
  routed task, and `CAPACITY_RISK.md` — as separate, clearly delimited
  markdown/JSON blocks so they can be saved as separate files.

## Environment constraints
No filesystem access assumed. The user saves the returned artifacts and
re-supplies the prior `ROUTING_PLAN.md`/`CAPACITY_RISK.md` as `prior_run` if
running this skill again in `AUDIT` mode against updated capacity data.

## Fallback
N/A — this is the baseline all other adapters specialize.
