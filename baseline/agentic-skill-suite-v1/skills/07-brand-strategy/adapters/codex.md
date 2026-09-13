# Codex adapter — Brand Strategy

## Invocation
Reference this skill from the repo's agent-instructions file (e.g.
`AGENTS.md`) as: "For brand positioning/strategy work, read
`skills/07-brand-strategy/SKILL.md` and follow it exactly, using the
project's `BRAND_DISCOVERY_BRIEF.md` as the required input." The coding
agent loads `SKILL.md` on demand rather than keeping it permanently in
context.

## File I/O
Reads `source_artifacts` (`BRAND_DISCOVERY_BRIEF.md`, and any optional
research/competitor-map/VoC/business-model files) from the repo working
tree. Writes the three required artifacts as real files in the repo
(default: alongside the discovery brief, or wherever the repo's convention
places brand canon — check for an existing `BRAND_STRATEGY.md` location
first, especially in `mode: UPDATE`).

## Environment constraints
Treat any existing `BRAND_STRATEGY.md`/`POSITIONING_SYSTEM.md` under version
control as the authoritative `prior_run` for `mode: UPDATE` — do not
regenerate strategy from scratch when a prior version exists in the repo.
Prefer repo-tracked discovery/research files over untracked scratch notes
as source evidence.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
