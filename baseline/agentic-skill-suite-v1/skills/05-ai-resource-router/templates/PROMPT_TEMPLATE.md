# Dispatch prompt — <task_id>

> One file per routed task, saved under `PROMPTS/<task_id>.md`. This is
> pasted directly into the assigned tool — it must be self-sufficient and
> task-specific, never a generic template with the task name swapped in.

**Assigned tool:** <tool id>
**Task type:** <research | synthesis | code | audit | agentic | creative | long_context | qa>

---

<Task-specific prompt body. Must include, in the tool's own words:>
- What the task is, concretely (not "help with X" — the actual work).
- The definition of done, so the receiving tool/human knows when to stop.
- Canonical source artifacts to use, referenced by path/name (e.g.
  `PROJECT_CANON.md`, `IMPLEMENTATION_PLAN.md §3`) — not inlined in full
  unless the tool has no file access and the content is short enough to
  paste directly.
- Any hard constraint that shaped the routing (context limit, must run
  unattended, output format expected downstream).
- What to return and to whom / where (e.g. "return findings as
  RESEARCH_PACKAGE.md for handoff back to canonical-context-builder").

---

**Do not** include this router's own reasoning about *why* this tool was
chosen — that belongs in `ROUTING_PLAN.md`, not in the dispatch prompt
itself.
