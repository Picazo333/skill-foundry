# Claude adapter — Brand Book Builder

## Invocation
Runs as a native Claude Skill: this directory (`SKILL.md` + `schemas/` +
`templates/` + `references/`) is loaded when the skill is invoked by name or
auto-triggered by the stated `Trigger` conditions in `SKILL.md`.

Native registration (auto-triggering and invocation by name) depends on the
`name`/`description` YAML frontmatter at the top of `SKILL.md`; without it the
skill can still be run by loading `SKILL.md` directly.

## File I/O
- **Claude Code / agentic environments:** reads all 6 required canon
  artifacts (and optional `BRAND_STRATEGY.md`) directly from the working
  directory/repo, writes the three required artifacts as real files
  (default: repo root or the same directory the verbal/identity-system
  artifacts live in).
- **claude.ai (no filesystem):** user uploads/pastes the 6 canon artifacts;
  the three artifacts are returned as file attachments or delimited
  markdown blocks per `adapters/generic.md`.

## Environment constraints
When run as an autonomous agent, follow `/shared/policies/AUTONOMY.md`: do
not ask "should I continue" once given a clear `RUN_REQUEST`; proceed
through the full procedure and stop only per `SKILL.md`'s stop conditions —
including returning `BLOCKED` when a required canon artifact is missing, or
`PARTIAL` when step 6's coherence check finds a gap serious enough to
misrepresent the brand as aligned, rather than asking whether to proceed.

## Fallback
In a surface without a native Skill primitive (e.g. claude.ai without
filesystem access, or a harness that does not parse `SKILL.md` frontmatter),
load `SKILL.md` as a plain instruction document and follow
`adapters/generic.md` for artifact input/output.
