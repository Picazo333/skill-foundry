# Claude adapter — Research Architect

## Invocation
Runs as a native Claude Skill: this directory (`SKILL.md` + `schemas/` +
`templates/` + `references/`) loads when invoked by name or auto-triggered
by the `Trigger` conditions in `SKILL.md`.

Native registration (auto-triggering and invocation by name) depends on the
`name`/`description` YAML frontmatter at the top of `SKILL.md`; without it the
skill can still be run by loading `SKILL.md` directly.

## File I/O
- **Claude Code / agentic environments:** reads `source_artifacts` directly
  from the working directory/repo, writes the 7 required artifacts as real
  files (default: a `research/<project>/` directory). `CHECKPOINT.md` is
  overwritten in place at each logical-block boundary so resuming a long
  autonomous run is a normal file read, not a re-paste.
- **claude.ai (no filesystem):** user uploads/pastes source artifacts; the
  7 artifacts are returned as file attachments or delimited markdown blocks
  per `adapters/generic.md`.

## Environment constraints
When `mode: AUTONOMOUS`, follow `/shared/policies/AUTONOMY.md`: proceed
through Phases 0-4 without asking "should I continue," and checkpoint after
every logical block named in `SKILL.md`'s AUTONOMOUS-mode section (not only
at phase boundaries) — a 200+iteration run is exactly the long-running case
that policy anticipates. In Claude Code, prefer writing `CHECKPOINT.md` to
disk after each block over holding state only in the conversation, so a
container restart or context compaction loses at most one block of work.
Still stop before deep research in every mode, per `SKILL.md`'s stop
conditions — this is never relaxed for autonomy or for agentic tool access.

## Fallback
In a surface without a native Skill primitive (e.g. claude.ai without
filesystem access, or a harness that does not parse `SKILL.md` frontmatter),
load `SKILL.md` as a plain instruction document and follow
`adapters/generic.md` for artifact input/output.
