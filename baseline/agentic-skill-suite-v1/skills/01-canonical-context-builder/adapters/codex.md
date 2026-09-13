# Codex adapter — Canonical Context Builder

## Invocation
Reference this skill from the repo's agent-instructions file (e.g.
`AGENTS.md`) as: "For canonical context work, read
`skills/01-canonical-context-builder/SKILL.md` and follow it exactly." The
coding agent loads `SKILL.md` on demand rather than keeping it permanently
in context.

## File I/O
Reads `source_artifacts` from the repo working tree (docs, commit history,
prior canon files). Writes the five required artifacts as real files in the
repo (default: repo root, or wherever the repo's convention places canonical
docs — check for an existing `PROJECT_CANON.md` location first).

## Environment constraints
Prefer `git log`/`git diff` and existing docs over asking the user to
re-paste history — the repo itself is the source-artifact inventory. Treat
files under version control as higher-authority than untracked scratch
notes, consistent with `references/authority-and-recency-ranking.md`.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
