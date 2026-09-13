# Cursor adapter — Brand Visual Direction

## Invocation
Skill lives as a `.cursor/rules` entry or a project doc the agent is
pointed at, same file-I/O pattern as `adapters/codex.md` but with
Cursor's invocation style: either an always-attached rule referencing
`skills/09-brand-visual-direction/SKILL.md`, or an explicit `@` mention of
the file in chat to invoke it for a given run.

## File I/O
Reads `BRAND_STRATEGY.md` (and optional context) from the repo working
tree. Writes the four required artifacts as real files in the same
location as the rest of this repo's canonical brand artifacts, so
`brand-identity-system` can pick them up from the working tree directly.

## Environment constraints
Same as `adapters/codex.md`: no native image rendering inside the editor
agent — the deliverable is the written grammar (`APPROVED_VISUAL_DIRECTION.md`,
`GENERATION_LANGUAGE.md`), not a rendered image. If the rule is
auto-attached, confirm the loaded `BRAND_STRATEGY.md` is current before
running — Cursor rules can be stale if the file moved or was regenerated
since the rule was last attached.

## Fallback
N/A — the `.cursor/rules` / `@`-mention pattern above is used directly.
