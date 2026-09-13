# Claude adapter — Brand Discovery

## Invocation
Runs as a native Claude Skill: this directory (`SKILL.md` + `schemas/` +
`templates/` + `references/`) is loaded when the skill is invoked by name or
auto-triggered by the `Trigger` conditions stated in `SKILL.md`.

Native registration (auto-triggering and invocation by name) depends on the
`name`/`description` YAML frontmatter at the top of `SKILL.md`; without it the
skill can still be run by loading `SKILL.md` directly.

## File I/O
- **Claude Code / agentic environments:** reads `source_artifacts` directly
  from the working directory/repo (interview notes, review exports,
  existing brand materials, a prior `PROJECT_CANON.md`), writes the three
  required artifacts as real files (default: repo root or a `discovery/`
  directory the user specifies).
- **claude.ai (no filesystem):** user uploads/pastes source artifacts; the
  three artifacts are returned as file attachments or delimited markdown
  blocks per `adapters/generic.md`.

## Environment constraints
When run as an autonomous agent, follow `/shared/policies/AUTONOMY.md`: do
not ask "should I continue" once given a clear `RUN_REQUEST`; proceed
through the full procedure and stop only per `SKILL.md`'s stop conditions.
If `canonical-context-builder` has already produced a `PROJECT_CANON.md` for
this project, read it as `OPTIONAL_CONTEXT` rather than re-deriving general
project facts from scratch.

## Fallback
In a surface without a native Skill primitive (e.g. claude.ai without
filesystem access, or a harness that does not parse `SKILL.md` frontmatter),
load `SKILL.md` as a plain instruction document and follow
`adapters/generic.md` for artifact input/output.
