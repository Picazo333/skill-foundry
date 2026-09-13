# Codex adapter — Brand Discovery

## Invocation
Reference this skill from the repo's agent-instructions file (e.g.
`AGENTS.md`) as: "For brand discovery work, read
`skills/06-brand-discovery/SKILL.md` and follow it exactly." The coding
agent loads `SKILL.md` on demand rather than keeping it permanently in
context.

## File I/O
Reads `source_artifacts` from the repo working tree (interview notes,
review/analytics exports, competitor notes, existing brand materials, a
prior `PROJECT_CANON.md` or `BRAND_DISCOVERY_BRIEF.md`). Writes the three
required artifacts as real files in the repo (default: repo root, or
wherever the repo's convention places brand/discovery docs — check for an
existing `BRAND_DISCOVERY_BRIEF.md` location first).

## Environment constraints
Prefer repo-tracked source material (docs, prior briefs) over asking the
user to re-paste context — the repo itself is the source-artifact
inventory. Treat files under version control as higher-authority than
untracked scratch notes, consistent with the FACTS/CLAIMS boundary in
`references/fact-vs-opinion-rubric.md` (a committed brief outranks a loose
note, but neither outranks what a source actually verifies).

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
