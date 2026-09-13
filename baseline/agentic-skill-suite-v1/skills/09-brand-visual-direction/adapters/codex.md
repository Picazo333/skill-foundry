# Codex adapter — Brand Visual Direction

## Invocation
Skill lives as a repo file the coding agent is told to read before
acting — either a section in `AGENTS.md` pointing at
`skills/09-brand-visual-direction/SKILL.md`, or a direct instruction:
> "Read `skills/09-brand-visual-direction/SKILL.md` and follow its
> procedure exactly for this Brand Visual Direction run."

## File I/O
Reads `BRAND_STRATEGY.md` (and optional context) from the repo working
tree — wherever the upstream `brand-strategy` skill wrote it (commonly a
`brand/` or project-root canonical-artifacts directory; follow this repo's
existing convention if one exists). Writes the four required artifacts as
real files in the same location, ready for `brand-identity-system` to read
next from the working tree without re-supplying context.

## Environment constraints
Codex runs as a coding agent, not a design tool — it has no native image
rendering. If a territory needs to be visualized, generate the written
grammar per `SKILL.md` and note in the handoff that a design tool or
`brand-identity-system` should render/visualize it; do not attempt to fake
visual output as code comments or ASCII art in place of the actual
grammar artifacts.

## Fallback
N/A — the repo-file-read pattern above is used directly; no additional
wrapper needed.
