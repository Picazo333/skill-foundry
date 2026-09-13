# Claude adapter — Brand Skill Orchestrator

## Invocation
Native Claude Skill. In an agentic environment (Claude Code / Claude
agents), this skill can actually invoke the routed skill's own SKILL.md as
a sub-task/sub-agent call after producing `NEXT_SKILL_RUN.json` — closing
the loop within one session rather than requiring manual hand-carry between
sessions, when the harness supports it.

Native registration (auto-triggering and invocation by name) depends on the
`name`/`description` YAML frontmatter at the top of `SKILL.md`; without it the
skill can still be run by loading `SKILL.md` directly.

## File I/O
- **Agentic environments:** reads the suite's `skills/*/` output directories
  directly from the working tree to build the artifact inventory, writes
  `BRAND_WORKFLOW_STATE.md`/`NEXT_SKILL_RUN.json`/`HANDOFF_PACKAGES/`/
  `COMPLETION_REPORT.md` as real files (default: a `runs/<project>/` dir the
  user specifies, kept separate from the suite's own `skills/` source tree).
- **claude.ai (no filesystem):** falls back to `adapters/generic.md`'s
  upload/paste pattern.

## Environment constraints
Per `/shared/policies/AUTONOMY.md`: once given a clear objective and
artifact inventory, proceed through routing decisions without asking
"should I continue" at each stage transition — only stop per `SKILL.md`'s
own stop conditions (objective fulfilled, or a genuine `BLOCKED` conflict).

## Fallback
In a surface without a native Skill primitive (e.g. claude.ai without
filesystem access, or a harness that does not parse `SKILL.md` frontmatter),
load `SKILL.md` as a plain instruction document and follow
`adapters/generic.md` for artifact input/output. This skill additionally
supports an optional sub-agent auto-dispatch extension when the harness
supports it, independent of this fallback.
