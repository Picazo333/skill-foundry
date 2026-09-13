# Claude adapter — Brand Quality Auditor

## Invocation
Runs as a native Claude Skill: this directory (`SKILL.md` + `schemas/` +
`templates/` + `references/`) is loaded when the skill is invoked by name
or auto-triggered by the stated `Trigger` conditions in `SKILL.md`.

Native registration (auto-triggering and invocation by name) depends on the
`name`/`description` YAML frontmatter at the top of `SKILL.md`; without it the
skill can still be run by loading `SKILL.md` directly.

## File I/O
- **Claude Code / agentic environments:** reads the artifact under audit
  and the canon artifacts directly from the working directory/repo (or a
  linked brand-book location), writes the three required artifacts as
  real files (default: repo root or an `audits/<artifact-name>/`
  directory the user specifies). If canon files cannot be located in the
  expected location, treat this the same as canon not being supplied —
  run the canon gate (`SKILL.md` step 1) and return `BLOCKED` rather than
  proceeding without them.
- **claude.ai (no filesystem):** user uploads/pastes the artifact and
  canon; the three artifacts are returned as file attachments or
  delimited markdown blocks per `adapters/generic.md`.

## Environment constraints
When run as an autonomous agent, follow `/shared/policies/AUTONOMY.md`: do
not ask "should I continue" once given a clear `RUN_REQUEST` with
sufficient canon; proceed through the full procedure and stop only per
`SKILL.md`'s stop conditions. Do not treat "canon file not found on disk"
as a reason to silently skip the canon gate and grade anyway — surface the
`BLOCKED` result immediately.

## Fallback
In a surface without a native Skill primitive (e.g. claude.ai without
filesystem access, or a harness that does not parse `SKILL.md` frontmatter),
load `SKILL.md` as a plain instruction document and follow
`adapters/generic.md` for artifact input/output.
