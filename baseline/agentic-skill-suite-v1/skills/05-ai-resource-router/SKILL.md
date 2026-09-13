---
name: ai-resource-router
description: Chooses the best available AI tool or account for a task using capability fit, quota, reset urgency and cost, then outputs a routing plan and dispatch prompt without doing the routed work itself; use when multiple AI subscriptions/tools are available and it's unclear which should take which task, not for abstract tool benchmarking with no real task to route.
---

# AI Resource Router

> Canonical skill definition. Adapters in `adapters/` are thin wrappers over
> this file — they may not change purpose, procedure, outputs, quality gates
> or stop conditions. See `/PORTABILITY.md` and `/shared/adapters/README.md`.

## Identity
- **ID:** `ai-resource-router`
- **Category:** ai-operations
- **Version:** `1.0.0`
- **Purpose:** Given a set of tasks and a snapshot of available AI tools/
  accounts and their capacity, produce a routing plan — which tool handles
  which task, in what order, with a ready-to-use dispatch prompt for each —
  without performing any of the routed tasks itself.

## Trigger
Use this skill when:
- More than one AI subscription/tool/account is available and it is unclear
  which should take which task.
- A quota reset, extra-reset expiry, or renewal boundary is approaching and
  unused capacity is at risk of being wasted.
- A batch of tasks (research, synthesis, code, audit, agentic, creative,
  long-context, QA) needs to be assigned across tools before work starts.
- A daily/weekly AI deployment plan is needed.

## Non-trigger
Do not use this skill for:
- Abstract tool benchmarking with no actual task to route — there is nothing
  to route; this skill only routes real, stated tasks.
- Producing quota, cost, reset-date, or capability data that was not
  supplied — if capacity data is missing, say so in `unresolved`/`BLOCKED`,
  never invent a number.
- Doing the domain work itself. If given "route this task" and the router
  ends up drafting the research/code/copy instead of a dispatch prompt for
  another tool to do it, that is a failure of this skill, not a shortcut.
  This is the suite's load-bearing rule for this skill
  (`QUALITY_GATES.md` suite-level gate 3).
- Deep implementation planning (`product-auditor`), exhaustive research
  itself (`research-architect`), or multi-skill brand workflow sequencing
  (`brand-skill-orchestrator`) — this skill hands off to those, it doesn't
  replace them.

## Context policy
- **REQUIRED_CONTEXT:** the task list to route, and a current snapshot of
  available tools/accounts with whatever capacity data is actually known
  (even if partial).
- **OPTIONAL_CONTEXT:** reset times, extra/bonus resets and their expiry,
  per-tool cost, renewal/subscription status, per-project urgency, known
  tool-strength notes, per-task context-window/tool-access constraints.
- **DO_NOT_LOAD_BY_DEFAULT:** full conversational history of how each task
  came to be (route from the task statement + canonical artifacts it
  references, not the chat that produced it); other projects' capacity
  snapshots; unrelated skills' canon. If a canonical artifact (e.g.
  `PROJECT_CANON.md`, an `IMPLEMENTATION_PLAN.md`) is the task's source,
  reference it by path in the dispatch prompt — do not inline its full
  contents into the routing plan.

Prefer canonical artifacts over conversational memory (`ARCHITECTURE.md`).

## Inputs

### Minimum inputs
- Tasks/projects to route (each with at least: what kind of work, and what
  "done" looks like).
- Available tool/capacity snapshot (which tools/accounts exist right now —
  even a partial or stale snapshot is a valid minimum input; gaps become
  `unresolved`, not blockers, unless capacity is unknown for every option).

### Optional inputs
- Reset times (per tool/account).
- Extra/bonus resets and their expiry.
- Costs (subscription, per-token, or opportunity cost notes).
- Renewal status (renewing, lapsing, trial ending).
- Project/task urgency or deadlines.
- Tool strength notes (e.g. "X is strong at long-context synthesis").
- Context constraints (context-window limits, tool/file access a task
  requires that not every tool has).

### RUN_REQUEST envelope
```yaml
RUN_REQUEST:
  objective:            # e.g. "route today's task list across available AI tools before Tuesday reset"
  source_artifacts:      # canonical docs the tasks reference (plans, canon, briefs) — referenced, not inlined
  known_context:         # e.g. prior routing decisions, standing tool-assignment rules
  constraints:            # e.g. "no more than 2 simultaneous agents", "X account context-window <= 32k"
  desired_output:        # full_routing_set | queue_only | single_task_dispatch
  mode: STANDARD          # QUICK | STANDARD | AUDIT (see below; this skill does not use DEEP/UPDATE/AUTONOMOUS)
  prior_run:              # path to prior ROUTING_PLAN.md / CAPACITY_RISK.md, if resuming a rolling capacity plan
```
Supported modes for this skill: `QUICK` (single task, one obvious best tool —
skip the full scoring pass), `STANDARD` (full task batch, full procedure),
`AUDIT` (re-check an existing `ROUTING_PLAN.md` against updated capacity
data without re-deriving task-type normalization from scratch).

## Procedure
1. **Normalize tasks.** For each task, classify its type — one or more of:
   research, synthesis, code, audit, agentic, creative, long-context, QA —
   and state what "done" looks like and any hard requirement (tool/file
   access, context length, must-run-unattended, etc.).
2. **Normalize resources.** For each available tool/account, record: what's
   actually known (availability window, capability strengths if supplied),
   and what's supplied vs. unknown for: reset date/time, extra resets and
   their expiry, cost, renewal status, and account relationships (e.g. two
   accounts of the same provider with different reset clocks are two
   separate resources, not one). Never fabricate a value for an unsupplied
   field — mark it `unknown` and carry it into `CAPACITY_RISK.md`.
3. **Score capability fit first.** For each task, rank the tools that can
   actually do it well, independent of quota pressure. A tool that cannot
   competently do the task is excluded from consideration for that task
   regardless of how much unused quota it has — never route a task to a
   poor-fit tool just to burn quota (quality gate).
4. **Calculate opportunity pressure.** For each remaining candidate tool,
   compute a qualitative pressure signal from: unused capacity × reset
   proximity × extra-reset expiry risk × renewal status (lapsing capacity
   is more urgent to use than renewing capacity). Use this to break ties
   among tools that are roughly equal on capability fit — never to override
   a clear capability-fit winner.
5. **Weigh time horizon correctly.** When a task could reasonably wait,
   prefer the routing that protects capacity with weekly/monthly reset
   windows over one that burns a tool with a tight, less-relevant short
   window — unless the task itself is urgent enough that the short window
   is the actual constraint (quality gate).
6. **Account for supervision/switching cost.** More simultaneously-dispatched
   agentic tasks means more human attention split across them. Apply any
   stated cap on simultaneous agents; if none is stated, do not recommend
   more concurrent unattended agentic dispatches than the task list and
   context plausibly support, and say so in `decisions`.
7. **Assign primary + fallback.** Each task gets exactly one primary tool.
   Add a fallback only where it's genuinely useful (e.g. primary tool's
   quota is at real risk of running out mid-task, or primary has a known
   reliability gap for this task type) — do not pad every task with a
   fallback by default.
8. **Generate dispatch prompts.** For each routed task, write one concise,
   task-specific, ready-to-paste prompt for the assigned tool. Each prompt
   references canonical artifacts by path/name (not full inlined content)
   and states the task's definition of done. Generic, interchangeable
   prompts ("please help with this task") fail the quality gate.
9. **Build the queue.** Sort routed tasks into `use-now` (should be dispatched
   immediately — capability-critical or high opportunity pressure),
   `next` (queued behind current dispatch-cap, dispatch as slots free up),
   and `reserve` (capacity intentionally held back — e.g. for a
   higher-priority task expected soon, or because dispatching now would
   exceed a stated simultaneous-agent cap). Briefly explain each high-impact
   placement decision (why a task is `use-now` and not `next`, or vice
   versa).
10. **Surface no-fit tasks.** Any task with no tool that meets its hard
    requirements is NOT force-routed. It is listed explicitly as unroutable
    in `ROUTING_PLAN.md` and `RUN_RESULT.unresolved`, with the missing
    capability/constraint stated.
11. **Stop after routing.** Do not begin performing any routed task. The run
    ends at a complete dispatch plan + prompts, not at task execution.

### Checkpoints
For a large task batch (many tasks × many tools), checkpoint after step 2
(normalized task list + normalized resource snapshot, before scoring) and
after step 7 (assignments locked, before prompt generation), recording
counts of tasks routed/unroutable so a resumed `AUDIT`-mode run re-scores
only what changed in the capacity snapshot rather than re-normalizing
everything.

## Outputs

### Required output artifacts
- `ROUTING_PLAN.md` — per-task: type, assigned primary (+ fallback if any),
  rationale, queue placement (use-now/next/reserve).
- `DISPATCH_QUEUE.json` — the same routing decisions in machine-readable
  form, ordered by queue placement, per `schemas/output.schema.json`.
- `PROMPTS/` — one file per routed task, the ready-to-paste dispatch prompt
  for that task's assigned tool.
- `CAPACITY_RISK.md` — per-tool: known vs. unknown capacity fields, reset/
  expiry/renewal risk notes, and any tool excluded from all routing due to
  insufficient capacity data.

### RUN_RESULT envelope
```yaml
RUN_RESULT:
  status:      # COMPLETE | PARTIAL | BLOCKED
  summary:
  artifacts: [ROUTING_PLAN.md, DISPATCH_QUEUE.json, PROMPTS/, CAPACITY_RISK.md]
  decisions:    # high-impact routing calls and why (e.g. weekly window protected over daily one)
  unresolved:   # unroutable tasks, unknown capacity fields, ties not confidently broken
  handoff:      # recommended next skill(s) + why
  quality:      # gate results
```

### Output schema
See `schemas/output.schema.json` for the machine-checkable shape of
`DISPATCH_QUEUE.json` / `RUN_RESULT`, and `schemas/input.schema.json` for
`RUN_REQUEST`.

## Handoffs
- → `product-auditor` — when a routed task's dispatch prompt is itself an
  implementation/audit task; the router passes the dispatch prompt + source
  artifacts, not a redone analysis.
- → `research-architect` — when a routed task is open-ended research that
  needs research architecture before it can even be dispatched as one prompt.
- → `brand-skill-orchestrator` — when the task batch spans a multi-stage
  brand workflow and sequencing (not just tool assignment) is also needed.

## Failure modes
- **Doing the task instead of routing it.** Detect: `ROUTING_PLAN.md` or a
  `PROMPTS/` entry contains the actual research/code/copy output rather than
  a prompt describing the task. Fix: replace with a dispatch prompt; the
  domain work happens on the receiving tool, not here.
- **Fabricating capacity data.** Detect: a reset time, quota amount, or cost
  appears in `CAPACITY_RISK.md`/`ROUTING_PLAN.md` that was not in the
  `RUN_REQUEST`. Fix: mark the field `unknown`, route around it or flag the
  tool as low-confidence, never invent the number.
- **Burning quota on a poor capability fit.** Detect: a task is routed to a
  tool that cannot do it well, justified by "it had quota available." Fix:
  re-run capability-fit scoring (step 3) as the primary filter; opportunity
  pressure only breaks ties among already-qualified tools.
- **Force-routing an unroutable task.** Detect: every candidate tool fails a
  task's hard requirement, but the plan assigns one anyway. Fix: list it as
  unroutable in `unresolved`, state the missing capability, do not force a
  match.
- **Generic, copy-pasted dispatch prompts.** Detect: two different tasks'
  prompts in `PROMPTS/` are near-identical templates with only the task name
  swapped. Fix: rewrite each prompt to be specific to that task's definition
  of done and referenced artifacts.

## Quality gates
Must satisfy `/QUALITY_GATES.md` skill-level gates 1–10, plus:
- Suite-level gate 3: routes but does not execute unrelated domain work — no
  `ROUTING_PLAN.md`/`PROMPTS/` entry contains completed domain work.
- Weekly/monthly capacity is prioritized over an irrelevant short window when
  the task doesn't require the short window's urgency.
- Extra-reset expiry is considered wherever supplied.
- No fabricated quota, reset, or cost data.
- Capability fit beats token/quota burning as the primary routing filter.
- Every dispatch prompt is task-specific, not a generic template.

## Stop conditions
- Normal completion: all tasks are either routed (with a dispatch prompt) or
  explicitly listed unroutable with a stated reason; all four required
  artifacts produced; `status: COMPLETE`.
- Blocked: no capacity data exists for any available tool (not even partial)
  → `status: BLOCKED`, state exactly what capacity snapshot is needed.
- Partial: some tasks routed, others blocked on missing capability/capacity
  data → `status: PARTIAL`, list which tasks and what's missing.
- Never continue past producing a dispatch plan into performing the routed
  work itself — that always ends the run and hands off instead.

## Examples
See `examples/` for at least one worked input → output pair.

## Evals
See `evals/` — minimum 3 scenarios + 1 edge/failure case, using
`shared/templates/EVAL_TEMPLATE.md`.
