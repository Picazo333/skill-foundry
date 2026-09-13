# Codex adapter — Creative Brief Generator

## Invocation
Reference this skill from the repo's agent-instructions file (e.g.
`AGENTS.md`) as: "For creative brief work, read
`skills/12-creative-brief-generator/SKILL.md` and follow it exactly." The
coding agent loads `SKILL.md` on demand rather than keeping it permanently
in context.

## File I/O
Reads canon `source_artifacts` from the repo working tree (typically
`brand-book-builder`'s output — `BRAND_BOOK.md` or the strategy/verbal/
visual set). Writes the three required artifacts as real files in the repo
(default: alongside the canon, or wherever the repo's convention places
brief deliverables — check for an existing `briefs/` or `creative/`
directory first).

## Environment constraints
Treat canon files under version control as authoritative; if a deliverable
request comes in as an issue/PR description, extract the objective and
known_context from it rather than asking the requester to re-type the
RUN_REQUEST fields verbatim. Prefer `git log` on the canon files to spot a
recent update the brief should reflect before treating canon as stale.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
