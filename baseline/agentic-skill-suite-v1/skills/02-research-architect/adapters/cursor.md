# Cursor adapter — Research Architect

## Invocation
Add as a `.cursor/rules` entry (or a project doc referenced from one)
pointing at `skills/02-research-architect/SKILL.md`: "When asked to build a
research architecture (not execute research), follow this file's procedure
exactly, including the iteration minimums and the stop-before-execution
rule." A Cursor rule can auto-attach via file-path glob or manual
`@`-mention, per the project's rule configuration — unlike Codex's
explicit-mention pattern.

## File I/O
Reads `source_artifacts` from the repo working tree (same as `codex.md`).
Writes the 7 required artifacts as real files in the repo, updating
`CHECKPOINT.md` in place at each logical-block boundary.

## Environment constraints
Same as `codex.md`: run `mode: AUTONOMOUS` across multiple agent turns
without per-iteration confirmation, per `/shared/policies/AUTONOMY.md`,
checkpointing to disk so an interrupted session resumes from the working
tree rather than lost context. The stop-before-execution rule is never
relaxed regardless of what browsing/execution tools Cursor has available in
the session.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
