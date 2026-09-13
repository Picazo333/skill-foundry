# Claude adapter — Product Auditor

## Invocation
Runs as a native Claude Skill: this directory (`SKILL.md` + `schemas/` +
`templates/` + `references/`) is loaded when the skill is invoked by name or
auto-triggered by the stated `Trigger` conditions in `SKILL.md`.

Native registration (auto-triggering and invocation by name) depends on the
`name`/`description` YAML frontmatter at the top of `SKILL.md`; without it the
skill can still be run by loading `SKILL.md` directly.

## File I/O
- **Claude Code / agentic environments:** reads the repo/app directly from
  the working directory, can run the app/tests to reproduce findings. Writes
  the five required artifacts as real files (default: repo root or an
  `audit/` directory the user specifies). Even though this environment has
  full write access to product files, `mode: AUDIT` and `mode: QA` must not
  use it to edit product code/config/data — only to read, run tests, and
  write the five audit artifacts. Treat this as a hard tool-use restriction
  for the duration of the run, not a suggestion.
- **claude.ai (no filesystem):** user uploads/pastes source artifacts and
  screenshots; the five artifacts are returned as file attachments or
  delimited markdown blocks per `adapters/generic.md`.

## Environment constraints
When run as an autonomous agent, proceed through the full procedure without
asking "should I continue" once given a clear `RUN_REQUEST` — but the
autonomy grant never extends to writing/editing product code during AUDIT
or QA mode; that boundary is a stop condition, not a pacing choice.

## Fallback
In a surface without a native Skill primitive (e.g. claude.ai without
filesystem access, or a harness that does not parse `SKILL.md` frontmatter),
load `SKILL.md` as a plain instruction document and follow
`adapters/generic.md` for artifact input/output.
