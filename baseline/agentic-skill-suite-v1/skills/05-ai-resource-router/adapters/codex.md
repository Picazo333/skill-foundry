# Codex adapter — AI Resource Router

## Invocation
Reference this skill from the repo's agent-instructions file (e.g.
`AGENTS.md`) as: "For deciding which AI tool/account should take a task,
read `skills/05-ai-resource-router/SKILL.md` and follow it exactly. Do not
perform the routed tasks yourself — only produce the routing plan and
dispatch prompts." The coding agent loads `SKILL.md` on demand rather than
keeping it permanently in context.

## File I/O
Reads the task list from the repo (issue trackers exported to files, an
`IMPLEMENTATION_PLAN.md`, a TODO list) and the tool/capacity snapshot from
wherever the user tracks it (a checked-in `capacity.yaml`, or supplied
inline in the prompt). Writes the four required artifacts as real files in
the repo (default: alongside other canonical docs, or a `routing/`
directory if the repo has a convention for it).

## Environment constraints
This adapter is especially prone to the skill's core failure mode — a
coding agent asked to "route this task" may reflexively start implementing
it instead. Treat step 11 of `SKILL.md` ("stop after routing") as a hard
boundary: the run ends at `PROMPTS/<task_id>.md`, never at an actual diff,
PR, or code change for the routed task itself.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
