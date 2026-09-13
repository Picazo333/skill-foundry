# Codex adapter — Brand Book Builder

## Invocation
Reference this skill from the repo's agent-instructions file (e.g.
`AGENTS.md`) as: "For compiling a brand book from locked verbal and visual
identity canon, read `skills/11-brand-book-builder/SKILL.md` and follow it
exactly." The coding agent loads `SKILL.md` on demand rather than keeping it
permanently in context.

## File I/O
Reads the 6 required canon artifacts (and optional `BRAND_STRATEGY.md`)
from the repo working tree — typically wherever `brand-verbal-identity` and
`brand-identity-system` wrote their outputs. Writes the three required
artifacts as real files in the repo (default: alongside the source canon,
or wherever the repo's brand-canon convention places compiled artifacts).

## Environment constraints
Treat canon artifacts under version control (committed/merged) as
authoritative; if either the verbal or visual canon is still an open draft
PR, flag that in `unresolved` rather than compiling against a not-yet-locked
source. Use `git log`/`git diff` to confirm which version of each source
artifact is current before compiling, especially on `mode: UPDATE`.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
