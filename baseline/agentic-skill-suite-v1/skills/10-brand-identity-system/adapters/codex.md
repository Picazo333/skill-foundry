# Codex adapter — Brand Identity System

## Invocation
Skill lives as a repo file the coding agent is told to read before
acting — either a section in `AGENTS.md` pointing at
`skills/10-brand-identity-system/SKILL.md`, or a direct instruction:
> "Read `skills/10-brand-identity-system/SKILL.md` and follow its
> procedure exactly for this Brand Identity System run."

## File I/O
Reads `BRAND_STRATEGY.md` and `APPROVED_VISUAL_DIRECTION.md` (and optional
context) from the repo working tree — wherever `brand-visual-direction`
wrote its outputs (commonly a `brand/` or project-root canonical-artifacts
directory; follow this repo's existing convention if one exists). Writes
the three required artifacts as real files in the same location, including
`DESIGN_TOKENS.json` in the shape a downstream build pipeline (e.g. Style
Dictionary) could consume directly, ready for `brand-book-builder` to read
next from the working tree without re-supplying context.

## Environment constraints
Codex runs as a coding agent — it can validate `DESIGN_TOKENS.json` as
strict JSON and cross-check its values against `IDENTITY_SYSTEM.md`'s
prose programmatically as part of step 9's audit (e.g. a small script
diffing token values against cited prose values); use that capability
rather than eyeballing the parity check where the tooling is available. It
has no native color-rendering or contrast-calculator UI, so contrast
ratios must be computed per `references/contrast-verification-method.md`'s
formula (implement it as a short script if convenient) rather than
estimated.

## Fallback
N/A — the repo-file-read pattern above is used directly; no additional
wrapper needed.
