# Cursor adapter — Canonical Context Builder

## Invocation
Add as a `.cursor/rules` entry (or project doc referenced from one) that
points at `skills/01-canonical-context-builder/SKILL.md`: "When asked to
build or update project canon, follow this file's procedure exactly."
Unlike Codex's explicit-mention pattern, a Cursor rule can auto-attach based
on file-path glob or manual `@`-mention, per the project's rule
configuration.

## File I/O
Reads `source_artifacts` from the repo working tree (same as `codex.md`).
Writes the five required artifacts as real files in the repo.

## Environment constraints
Same as `codex.md`: prefer version-controlled files over untracked scratch
as higher-authority sources.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
