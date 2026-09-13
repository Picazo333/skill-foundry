# Cursor adapter — Creative Brief Generator

## Invocation
Add as a `.cursor/rules` entry (or project doc referenced from one) that
points at `skills/12-creative-brief-generator/SKILL.md`: "When asked to
produce a creative brief for a deliverable, follow this file's procedure
exactly." Unlike Codex's explicit-mention pattern, a Cursor rule can
auto-attach based on file-path glob (e.g. edits under `briefs/` or
`marketing/`) or manual `@`-mention, per the project's rule configuration.

## File I/O
Reads canon `source_artifacts` from the repo working tree (same as
`codex.md`) — typically `brand-book-builder`'s output. Writes the three
required artifacts as real files in the repo.

## Environment constraints
Same as `codex.md`: prefer version-controlled canon over pasted/ad-hoc brand
descriptions, and check for staleness against recent canon commits before
treating a cached read as current.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
