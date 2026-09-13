# Cursor adapter — Brand Book Builder

## Invocation
Add as a `.cursor/rules` entry (or project doc referenced from one) that
points at `skills/11-brand-book-builder/SKILL.md`: "When asked to compile a
brand book/manual from locked verbal and visual identity canon, follow this
file's procedure exactly." Unlike Codex's explicit-mention pattern, a Cursor
rule can auto-attach based on file-path glob (e.g. edits under a `brand/`
directory) or manual `@`-mention, per the project's rule configuration.

## File I/O
Reads the 6 required canon artifacts and optional `BRAND_STRATEGY.md` from
the repo working tree (same as `codex.md`). Writes the three required
artifacts as real files in the repo.

## Environment constraints
Same as `codex.md`: only compile against canon the repo treats as
locked/merged, not an in-progress draft; flag any not-yet-locked source in
`unresolved` instead of compiling against it silently.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
