# Cursor adapter — AI Resource Router

## Invocation
Add as a `.cursor/rules` entry (or project doc referenced from one) that
points at `skills/05-ai-resource-router/SKILL.md`: "When deciding which
available AI tool/account should take a task, follow this file's procedure
exactly — produce a routing plan and dispatch prompts, do not perform the
task in this session." Unlike Codex's explicit-mention pattern, a Cursor
rule can auto-attach based on file-path glob or manual `@`-mention, per the
project's rule configuration.

## File I/O
Reads the task list and tool/capacity snapshot from the repo working tree
or the current chat context (same as `codex.md`). Writes the four required
artifacts as real files in the repo.

## Environment constraints
Same as `codex.md`: the biggest risk on this platform is the agent sliding
from "route this" into "just do it since I'm already in the repo." Enforce
`SKILL.md` step 11 (stop after routing) explicitly — a routed coding task's
`PROMPTS/<task_id>.md` is the deliverable, not an implemented diff.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
