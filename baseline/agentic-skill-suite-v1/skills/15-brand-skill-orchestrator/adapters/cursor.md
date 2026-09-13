# Cursor adapter — Brand Skill Orchestrator

## Invocation
Add as a `.cursor/rules` entry pointing at
`skills/15-brand-skill-orchestrator/SKILL.md`: "When asked what's next on a
brand project, or to continue/resume a brand workflow, follow this file's
procedure exactly. It only routes — it does not do brand work itself."

## File I/O
Reads the suite's `skills/*/` output/run directories from the repo working
tree, same as `codex.md`. Writes state/handoff files as real files in the
repo.

## Environment constraints
Same as `codex.md`: prefer version-controlled artifacts and their commit/PR
approval state as the authoritative inventory source.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
