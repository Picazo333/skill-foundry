# Cursor adapter — Brand Strategy

## Invocation
Add as a `.cursor/rules` entry (or project doc referenced from one) that
points at `skills/07-brand-strategy/SKILL.md`: "When asked to define or
update brand positioning/strategy, follow this file's procedure exactly,
using the project's `BRAND_DISCOVERY_BRIEF.md` as required input." Unlike
Codex's explicit-mention pattern, a Cursor rule can auto-attach based on
file-path glob (e.g. any `brand/` directory) or manual `@`-mention, per the
project's rule configuration.

## File I/O
Reads `source_artifacts` from the repo working tree (same as `codex.md`).
Writes the three required artifacts as real files in the repo, checking for
an existing `BRAND_STRATEGY.md` first when the request implies
repositioning (`mode: UPDATE`).

## Environment constraints
Same as `codex.md`: prefer version-controlled discovery/research files as
source evidence over untracked scratch notes, and treat an existing
tracked `BRAND_STRATEGY.md` as the `prior_run` baseline rather than
regenerating from nothing.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
