# Claude adapter — Rapid Capture & Triage

## Invocation
Runs as a native Claude Skill: this directory (`SKILL.md` + `schemas/` +
`templates/` + `references/`) is loaded when invoked by name or
auto-triggered by the `Trigger` conditions in `SKILL.md`. In Claude Code,
this is commonly triggered right after a voice-dictated or pasted note is
dropped into the conversation with an instruction like "triage this."

Native registration (auto-triggering and invocation by name) depends on the
`name`/`description` YAML frontmatter at the top of `SKILL.md`; without it the
skill can still be run by loading `SKILL.md` directly.

## File I/O
- **Claude Code / agentic environments:** reads the raw capture and any
  snapshot/existing JSON directly from the working directory or the
  conversation, writes the four required artifacts as real files (default:
  a `capture/` directory the user specifies, or the repo root).
- **claude.ai (no filesystem):** user pastes/uploads the raw capture (and
  optional snapshot); the four artifacts are returned as file attachments
  or delimited blocks per `adapters/generic.md`.

## Environment constraints
When run as an autonomous agent, follow `/shared/policies/AUTONOMY.md`: do
not ask "should I continue" mid-triage once given a clear `RUN_REQUEST`;
run the full procedure and stop only per `SKILL.md`'s stop conditions. Do
not ask the user to disambiguate every `AMBIGUITIES.md` entry before
finishing the run — surface them in the artifact and stop there; that is
completion, not a blocker requiring a mid-run question.

## Fallback
In a surface without a native Skill primitive (e.g. claude.ai without
filesystem access, or a harness that does not parse `SKILL.md` frontmatter),
load `SKILL.md` as a plain instruction document and follow
`adapters/generic.md` for artifact input/output.
