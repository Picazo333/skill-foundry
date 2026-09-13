# Codex adapter — Brand Verbal Identity

## Invocation
Reference this skill from the repo's agent-instructions file (e.g.
`AGENTS.md`) as: "For brand verbal identity work, read
`skills/08-brand-verbal-identity/SKILL.md` and follow it exactly." The
coding agent loads `SKILL.md` on demand rather than keeping it permanently
in context.

## File I/O
Reads `BRAND_STRATEGY.md` (and any optional existing copy/customer
language/compliance docs) from the repo working tree. Writes the three
required artifacts as real files in the repo — default: alongside
`BRAND_STRATEGY.md`, or wherever the repo's brand-canon convention places
them.

## Environment constraints
Treat a locked/merged `BRAND_STRATEGY.md` as the authoritative source; if the
repo has a draft strategy still under review, flag that in `unresolved`
rather than deriving voice from a not-yet-locked positioning statement.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
