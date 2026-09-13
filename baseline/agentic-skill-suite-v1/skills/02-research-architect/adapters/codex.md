# Codex adapter — Research Architect

## Invocation
Reference this skill from the repo's agent-instructions file (e.g.
`AGENTS.md`) as: "For research-architecture work, read
`skills/02-research-architect/SKILL.md` and follow it exactly, including
the iteration minimums, material-delta test, and the stop-before-execution
rule." The coding agent loads `SKILL.md` on demand.

## File I/O
Reads `source_artifacts` (`PROJECT_CANON.md`, prior program/checkpoint)
from the repo working tree. Writes the 7 required artifacts as real files
(default: a `research/<project>/` directory, or wherever the repo already
places research docs). `CHECKPOINT.md` is committed/updated in place at
each logical-block boundary so a long autonomous run surfaces its progress
in the working tree, not only in agent memory.

## Environment constraints
For `mode: AUTONOMOUS`, run the full multi-phase procedure across as many
agent turns as needed without asking for per-iteration confirmation, per
`/shared/policies/AUTONOMY.md` — this is exactly the long-horizon,
checkpoint-driven task that policy is written for. Never let "autonomous"
extend into actually running searches or writing findings against the
program: the coding-agent environment's ability to browse/execute does not
change the stop-before-execution rule in `SKILL.md`.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
