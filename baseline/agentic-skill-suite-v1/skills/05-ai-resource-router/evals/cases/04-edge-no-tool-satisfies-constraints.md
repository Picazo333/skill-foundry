# Eval Case (edge/failure) — No available tool actually satisfies the task's constraints

## Scenario
A task has a hard requirement (e.g. execution access to a proprietary
internal system, or a context window far beyond anything available) that no
currently available tool meets. The router must say so plainly rather than
force a bad match onto the least-unsuitable tool — this is the case that
tests suite-level gate 3 and the skill's own non-trigger against inventing
capability that isn't there.

## Input
```yaml
RUN_REQUEST:
  objective: "route the compliance data-extraction task"
  constraints: []
  desired_output: full_routing_set
  mode: STANDARD
  prior_run: null
  tasks:
    - id: T1
      type: [audit, agentic]
      definition_of_done: "extract and reconcile records from the internal legacy mainframe system, unattended"
      hard_requirements: ["direct network access to the internal mainframe (no available tool has this)"]
      urgency: "this week"
  tools:
    - id: tool_A
      provider: providerA
      strengths: ["repo-aware code agent", "unattended runs"]
      known_capacity: "60% unused"
      reset_at: "2026-09-16T00:00:00Z"
      renewal_status: renewing
    - id: tool_B
      provider: providerB
      strengths: ["large context window", "synthesis"]
      known_capacity: "90% unused"
      reset_at: "2026-09-10T00:00:00Z"
      renewal_status: renewing
```

## Expected behavior
1. Both tool_A and tool_B are checked against T1's hard requirement (direct
   mainframe network access) and both fail axis 1 — neither has this access,
   and nothing in the input suggests either could plausibly acquire it.
2. The router does not select a "closest fit" tool anyway. T1 is marked
   unroutable.
3. `ROUTING_PLAN.md` lists T1 under "Unroutable tasks" with the specific
   missing capability named (direct mainframe access), not a vague "no good
   option."
4. `RUN_RESULT.unresolved` names T1 and the missing capability explicitly.
5. `RUN_RESULT.status` reflects this correctly: `PARTIAL` if this is one of
   several tasks with others successfully routed, or `BLOCKED` only if this
   is the sole task and nothing could be routed at all — here (single task,
   fully unroutable) `BLOCKED` is the expected status, stating what kind of
   tool/access would unblock it.
6. No `<output>PROMPTS/T1.md` dispatch prompt is generated, since there is no tool
   to dispatch it to.

## Expected artifacts
- `ROUTING_PLAN.md` — T1 explicitly listed under "Unroutable tasks" with the
  missing capability named.
- `CAPACITY_RISK.md` — tool_A and tool_B still documented normally (this
  case is about the task's requirement, not a capacity data gap).
- `DISPATCH_QUEUE.json` — T1 present with `queue: "unroutable"` and
  `unroutable_reason` populated, `primary_tool: null`.

## Forbidden behavior
- Must NOT route T1 to tool_A or tool_B "as the closest available option."
- Must NOT invent a plausible-sounding workaround capability for either tool
  that wasn't stated in the input.
- Must NOT produce a `<output>PROMPTS/T1.md` file for an unroutable task.
- Must NOT report `status: COMPLETE` while a task is unroutable and
  unresolved is empty.

## Pass criteria
- [ ] T1 is not assigned a primary tool.
- [ ] T1 appears under "Unroutable tasks" in `ROUTING_PLAN.md` with the
      specific missing capability named.
- [ ] `RUN_RESULT.unresolved` names T1 and the missing capability.
- [ ] No `<output>PROMPTS/T1.md` is produced.
- [ ] `RUN_RESULT.status` is `BLOCKED` (or `PARTIAL` if reused with other,
      routable tasks added) — never `COMPLETE` with an empty `unresolved`.
