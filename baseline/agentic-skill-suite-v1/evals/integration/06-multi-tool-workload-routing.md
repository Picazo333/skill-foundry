# Walkthrough 6 — Multi-tool workload → AI Resource Router

## Starting state
A single operator has three pending tasks at once: a large refactor
(coding-heavy), a market research synthesis (reasoning-heavy, low urgency),
and a client-facing brand deck polish (fast turnaround, tomorrow morning).
Available tools/accounts have mixed quotas and reset times (matching skill
05's own "mixed quota day" eval scenario).

## Sequence
1. **`ai-resource-router`** run standalone (not downstream of any other
   skill in this walkthrough — it can be invoked "at any execution boundary"
   per `WORKFLOW_MAP.md`) with `RUN_REQUEST` listing all three tasks and the
   capacity/quota snapshot.
   - Procedure runs its 11-step scoring pipeline: normalize tasks → normalize
     resources → capability fit → opportunity pressure → time horizon →
     supervision cost → assign primary/fallback → generate prompts → build
     queue → surface unroutable tasks → stop.
   - Output: `ROUTING_PLAN.md` assigns each task a primary tool + fallback,
     `DISPATCH_QUEUE.json` orders them by opportunity pressure/time horizon
     (the deck, due tomorrow, is not starved behind the refactor even if the
     refactor was requested first), `CAPACITY_RISK.md` flags any tool nearing
     its reset window, `PROMPTS/` holds one ready-to-dispatch prompt per task.

## What must hold
- The router assigns tools/prompts; it does not itself perform the refactor,
  the research synthesis, or the deck polish.
- The urgent, lower-effort deck task is not silently deprioritized behind
  the higher-effort refactor purely by request order — opportunity
  pressure/time horizon scoring must surface this.
- If no available tool actually satisfies one task's constraints (e.g. the
  research task needs a capability nothing currently has quota for), that
  task is reported as unroutable/`BLOCKED` in `CAPACITY_RISK.md`, not forced
  onto a poor-fit tool.

## Failure signature
`DISPATCH_QUEUE.json` containing an actual code diff, research report, or
deck content (rather than a dispatch prompt referencing the task) means the
router crossed into doing the domain work itself.
