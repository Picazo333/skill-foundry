# Claude adapter — Creative Brief Generator

## Invocation
Runs as a native Claude Skill: this directory (`SKILL.md` + `schemas/` +
`templates/` + `references/`) is loaded when the skill is invoked by name or
auto-triggered by the stated `Trigger` conditions in `SKILL.md`.

Native registration (auto-triggering and invocation by name) depends on the
`name`/`description` YAML frontmatter at the top of `SKILL.md`; without it the
skill can still be run by loading `SKILL.md` directly.

## File I/O
- **Claude Code / agentic environments:** reads canon `source_artifacts`
  directly from the working directory/repo (e.g. output of
  `brand-book-builder`), writes the three required artifacts as real files
  (default: alongside the canon, or a `briefs/<deliverable>/` directory the
  user specifies).
- **claude.ai (no filesystem):** user uploads/pastes canon artifacts; the
  three required artifacts are returned as file attachments or delimited
  markdown blocks per `adapters/generic.md`.

## Environment constraints
When run as an autonomous agent, follow `/shared/policies/AUTONOMY.md`: do
not ask "should I continue" once given a clear `RUN_REQUEST`; proceed
through the full procedure and stop only per `SKILL.md`'s stop conditions
(including going `BLOCKED` on missing/insufficient canon or an unresolved
canon conflict — that is a genuine stop, not something to ask permission to
skip).

## Fallback
In a surface without a native Skill primitive (e.g. claude.ai without
filesystem access, or a harness that does not parse `SKILL.md` frontmatter),
load `SKILL.md` as a plain instruction document and follow
`adapters/generic.md` for artifact input/output.
