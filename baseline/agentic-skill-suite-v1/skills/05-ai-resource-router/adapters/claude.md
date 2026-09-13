# Claude adapter — AI Resource Router

## Invocation
Runs as a native Claude Skill: this directory (`SKILL.md` + `schemas/` +
`templates/` + `references/`) is loaded when the skill is invoked by name or
auto-triggered by the stated `Trigger` conditions in `SKILL.md`.

Native registration (auto-triggering and invocation by name) depends on the
`name`/`description` YAML frontmatter at the top of `SKILL.md`; without it the
skill can still be run by loading `SKILL.md` directly.

## File I/O
- **Claude Code / agentic environments:** reads the task list and tool/
  capacity snapshot directly from the working directory/repo or from the
  `RUN_REQUEST` message, writes the four required artifacts as real files
  (default: repo root or a `routing/` directory the user specifies).
- **claude.ai (no filesystem):** user pastes/uploads the task list and
  capacity snapshot; the four artifacts are returned as file attachments or
  delimited markdown/JSON blocks per `adapters/generic.md`.

## Environment constraints
When run as an autonomous agent, follow `/shared/policies/AUTONOMY.md`: do
not ask "should I continue" once given a clear `RUN_REQUEST`; proceed
through the full procedure and stop only per `SKILL.md`'s stop conditions —
specifically, stop at the dispatch plan and never drift into performing a
routed task itself, even when running in an environment (Claude Code) that
is fully capable of doing that task directly.

## Fallback
In a surface without a native Skill primitive (e.g. claude.ai without
filesystem access, or a harness that does not parse `SKILL.md` frontmatter),
load `SKILL.md` as a plain instruction document and follow
`adapters/generic.md` for artifact input/output.
