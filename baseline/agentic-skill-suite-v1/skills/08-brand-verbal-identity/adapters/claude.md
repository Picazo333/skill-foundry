# Claude adapter — Brand Verbal Identity

## Invocation
Runs as a native Claude Skill: this directory (`SKILL.md` + `schemas/` +
`templates/` + `references/`) is loaded when the skill is invoked by name or
auto-triggered by the stated `Trigger` conditions in `SKILL.md`.

Native registration (auto-triggering and invocation by name) depends on the
`name`/`description` YAML frontmatter at the top of `SKILL.md`; without it the
skill can still be run by loading `SKILL.md` directly.

## File I/O
- **Claude Code / agentic environments:** reads `BRAND_STRATEGY.md` (and any
  optional source artifacts) directly from the working directory/repo,
  writes the three required artifacts as real files (default: repo root or
  the same directory as `BRAND_STRATEGY.md`).
- **claude.ai (no filesystem):** user uploads/pastes `BRAND_STRATEGY.md`;
  the three artifacts are returned as file attachments or delimited
  markdown blocks per `adapters/generic.md`.

## Environment constraints
When run as an autonomous agent, follow `/shared/policies/AUTONOMY.md`: do
not ask "should I continue" once given a clear `RUN_REQUEST`; proceed through
the full procedure and stop only per `SKILL.md`'s stop conditions (including
returning `BLOCKED` on a thin strategy rather than asking whether to proceed
with filler).

## Fallback
In a surface without a native Skill primitive (e.g. claude.ai without
filesystem access, or a harness that does not parse `SKILL.md` frontmatter),
load `SKILL.md` as a plain instruction document and follow
`adapters/generic.md` for artifact input/output.
