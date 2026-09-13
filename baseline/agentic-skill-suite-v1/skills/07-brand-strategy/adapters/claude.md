# Claude adapter — Brand Strategy

## Invocation
Runs as a native Claude Skill: this directory (`SKILL.md` + `schemas/` +
`templates/` + `references/`) is loaded when the skill is invoked by name or
auto-triggered by the stated `Trigger` conditions in `SKILL.md` — typically
right after `brand-discovery` produces `BRAND_DISCOVERY_BRIEF.md`, or when
routed here by `brand-skill-orchestrator`.

Native registration (auto-triggering and invocation by name) depends on the
`name`/`description` YAML frontmatter at the top of `SKILL.md`; without it the
skill can still be run by loading `SKILL.md` directly.

## File I/O
- **Claude Code / agentic environments:** reads `source_artifacts`
  (`BRAND_DISCOVERY_BRIEF.md` and any optional inputs) directly from the
  working directory/repo, writes the three required artifacts as real files
  (default: alongside the discovery brief, or a `brand/` directory the user
  specifies).
- **claude.ai (no filesystem):** user uploads/pastes source artifacts; the
  three artifacts are returned as file attachments or delimited markdown
  blocks per `adapters/generic.md`.

## Environment constraints
When run as an autonomous agent, follow `/shared/policies/AUTONOMY.md` (or
`/TOKEN_EFFICIENCY.md`'s autonomous-execution rule if that policy file is
absent): do not ask "should I continue" once given a clear `RUN_REQUEST`;
proceed through the full procedure and stop only per `SKILL.md`'s stop
conditions. Because this skill's completion fans out to two downstream
skills (`brand-verbal-identity` and `brand-visual-direction`), surface both
in `RUN_RESULT.handoff` rather than picking one.

## Fallback
In a surface without a native Skill primitive (e.g. claude.ai without
filesystem access, or a harness that does not parse `SKILL.md` frontmatter),
load `SKILL.md` as a plain instruction document and follow
`adapters/generic.md` for artifact input/output.
