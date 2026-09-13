# Codex adapter — Brand Skill Orchestrator

## Invocation
Reference from the repo's agent-instructions file (e.g. `AGENTS.md`): "For
brand workflow routing, read `skills/15-brand-skill-orchestrator/SKILL.md`
and its `references/` and follow it exactly. It only decides what to run
next — it does not perform brand work itself."

## File I/O
Reads the suite's `skills/*/` output/run directories from the repo working
tree to build the artifact inventory directly (existence, git history for
recency, any approval markers committed alongside artifacts). Writes
`BRAND_WORKFLOW_STATE.md`, `NEXT_SKILL_RUN.json`, `HANDOFF_PACKAGES/`,
`COMPLETION_REPORT.md` as real files in the repo. Can invoke the routed
skill's own procedure as a follow-up agent task within the same repo
session when the coding agent supports task chaining.

## Environment constraints
Prefer commit history/PR approval state over asking the user to restate
approval status — version-controlled artifacts are the authoritative
inventory source, consistent with skill 01's authority/recency reference.

## Fallback
N/A — repo filesystem access covers this skill's I/O and (optionally)
dispatch needs directly.
