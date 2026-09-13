# Cursor adapter — Brand Identity System

## Invocation
Skill lives as a `.cursor/rules` entry or a project doc the agent is
pointed at, same file-I/O pattern as `adapters/codex.md` but with
Cursor's invocation style: either an always-attached rule referencing
`skills/10-brand-identity-system/SKILL.md`, or an explicit `@` mention of
the file in chat to invoke it for a given run.

## File I/O
Reads `BRAND_STRATEGY.md` and `APPROVED_VISUAL_DIRECTION.md` (and optional
context) from the repo working tree. Writes the three required artifacts
as real files in the same location as the rest of this repo's canonical
brand artifacts, so `brand-book-builder` — and any component-library or
CSS-variable build step that consumes `DESIGN_TOKENS.json` directly — can
pick them up from the working tree without re-supplying context.

## Environment constraints
Same as `adapters/codex.md`: no native color-rendering UI inside the
editor agent — contrast ratios must be computed per
`references/contrast-verification-method.md`'s formula, not estimated by
eye. If the rule is auto-attached, confirm the loaded
`APPROVED_VISUAL_DIRECTION.md` is the current *approved* version (not a
stale territory-comparison draft) before running.

## Fallback
N/A — the `.cursor/rules` / `@`-mention pattern above is used directly.
