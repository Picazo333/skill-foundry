# Claude adapter — Brand Identity System

## Invocation
Runs as a native Claude Skill: this directory (`SKILL.md` + `schemas/` +
`templates/` + `references/`) loads when the skill is invoked by name or
auto-triggered by the `Trigger` conditions in `SKILL.md`.

Native registration (auto-triggering and invocation by name) depends on the
`name`/`description` YAML frontmatter at the top of `SKILL.md`; without it the
skill can still be run by loading `SKILL.md` directly.

## File I/O
- **Claude Code / agentic environments:** reads `BRAND_STRATEGY.md` and
  `APPROVED_VISUAL_DIRECTION.md` (and optional context) directly from the
  working directory/repo, writes the three required artifacts as real
  files (default: repo root, or an `identity-system/` directory the user
  specifies). Prefer `templates/IDENTITY_SYSTEM.md`,
  `templates/DESIGN_TOKENS.json`, and `templates/APPLICATION_RULES.md` as
  the starting shape for each artifact rather than freeform structure.
- **claude.ai (no filesystem):** user uploads/pastes the source artifacts;
  the three artifacts are returned as file attachments or delimited
  markdown/JSON blocks per `adapters/generic.md`.

## Environment constraints
When run as an autonomous agent, follow `/shared/policies/AUTONOMY.md` (or
`TOKEN_EFFICIENCY.md`'s autonomous-execution rule if that policy file does
not exist in this checkout): do not ask "should I continue" mid-procedure;
run the full architecture → color → typography → grid/shape → motion →
application-rules → exceptions → tokens → audit sequence and stop only per
`SKILL.md`'s stop conditions.

## Fallback
In a surface without a native Skill primitive (e.g. claude.ai without
filesystem access, or a harness that does not parse `SKILL.md` frontmatter),
load `SKILL.md` as a plain instruction document and follow
`adapters/generic.md` for artifact input/output.
