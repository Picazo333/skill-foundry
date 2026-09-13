# Cursor adapter — Brand Verbal Identity

## Invocation
Add as a `.cursor/rules` entry (or project doc referenced from one) that
points at `skills/08-brand-verbal-identity/SKILL.md`: "When asked to build
or update brand verbal identity/voice from a locked brand strategy, follow
this file's procedure exactly." Unlike Codex's explicit-mention pattern, a
Cursor rule can auto-attach based on file-path glob (e.g. edits under a
`brand/` directory) or manual `@`-mention, per the project's rule
configuration.

## File I/O
Reads `BRAND_STRATEGY.md` and optional source artifacts from the repo
working tree (same as `codex.md`). Writes the three required artifacts as
real files in the repo.

## Environment constraints
Same as `codex.md`: only derive voice from a strategy the repo treats as
locked/approved, not an in-progress draft.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
