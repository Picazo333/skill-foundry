# Worked example — mixed-quota day, three tasks, three tools

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "route today's task list before tonight's resets"
  source_artifacts:
    - "IMPLEMENTATION_PLAN.md (Phase 2 tasks)"
  known_context: "cap of 2 simultaneous unattended agentic dispatches"
  constraints: ["no more than 2 simultaneous agents"]
  desired_output: full_routing_set
  mode: STANDARD
  prior_run: null
  tasks:
    - id: T1
      type: [audit]
      definition_of_done: "QA pass on Phase 2 diff against IMPLEMENTATION_PLAN.md §3 acceptance criteria"
      hard_requirements: ["needs read access to the repo diff"]
      urgency: "blocks merge today"
    - id: T2
      type: [long_context, synthesis]
      definition_of_done: "summarize 12 stakeholder interview transcripts (~180k tokens total) into a single findings doc"
      hard_requirements: ["context window >= 180k tokens"]
      urgency: "due in 4 days"
    - id: T3
      type: [agentic, code]
      definition_of_done: "implement Task 7 from IMPLEMENTATION_PLAN.md unattended, open a PR"
      hard_requirements: ["repo write access", "can run unattended"]
      urgency: "due in 2 days"
  tools:
    - id: tool_A
      provider: providerA
      strengths: ["repo-aware code agent", "unattended multi-step runs"]
      reset_at: "2026-09-16T00:00:00Z"
      extra_resets: []
      cost: "flat monthly subscription"
      renewal_status: renewing
      known_capacity: "60% unused this window"
    - id: tool_B
      provider: providerB
      strengths: ["very large context window", "strong synthesis"]
      reset_at: "2026-09-10T00:00:00Z"
      extra_resets:
        - amount: "one bonus long-context run"
          expires_at: "2026-09-09T23:59:00Z"
      cost: "usage-based"
      renewal_status: renewing
      known_capacity: "90% unused today"
    - id: tool_C
      provider: providerC
      strengths: ["fast QA/review pass", "repo diff aware"]
      reset_at: "2026-09-10T00:00:00Z"
      extra_resets: []
      cost: "flat monthly subscription"
      renewal_status: lapsing
      known_capacity: "unknown — not reported today"
```

## Output (abridged)

**CAPACITY_RISK.md** (excerpt):
```
### tool_C (providerC)
- Known capacity: unknown — not reported today
- Renewal status: lapsing
- Unknown fields: [known_capacity]
- Opportunity pressure: high — lapsing subscription, capacity unreported
  but assume it should be used before it lapses; routed cautiously given
  the missing capacity figure.

### tool_B (providerB)
- Extra/bonus resets: one bonus long-context run, expires 2026-09-09T23:59:00Z
- Opportunity pressure: high — bonus grant expires today, 90% unused.
```

**ROUTING_PLAN.md** (excerpt):
```
### T2 — synthesize 12 interview transcripts
- Type: long_context, synthesis
- Primary tool: tool_B
- Fallback tool: none — not needed
- Queue placement: use-now
- Rationale: only tool_B clears the >=180k context requirement (axis 1);
  its bonus long-context grant also expires tonight (axis 2), so routing
  now instead of later this week captures capacity that would otherwise
  be lost. Task's 4-day deadline alone would have allowed waiting, but the
  expiring grant makes "now" strictly better at no cost elsewhere.

### T1 — QA pass on Phase 2 diff
- Type: audit
- Primary tool: tool_C
- Fallback tool: tool_A (repo-aware, though not its core strength)
- Queue placement: use-now
- Rationale: tool_C fits the QA/review task directly; capacity is
  unreported (CAPACITY_RISK.md) but renewal is lapsing, so use-now is
  preferred over risking the account lapsing with capacity unused. Fallback
  to tool_A only if tool_C's actual capacity turns out insufficient — not
  pre-emptively split across both.

### T3 — implement Task 7, open PR (unattended)
- Type: agentic, code
- Primary tool: tool_A
- Fallback tool: none
- Queue placement: next
- Rationale: tool_A is the only tool with repo write access and unattended
  multi-step capability (axis 1). Queued as "next" rather than "use-now"
  only because dispatching it simultaneously with T1's fallback would risk
  the stated 2-agent concurrency cap if T1 needs both tool_C and tool_A at
  once; T1 is prioritized use-now since it blocks today's merge.
```

**PROMPTS/T2.md** (excerpt):
```
Assigned tool: tool_B
Task type: long_context, synthesis

Summarize the 12 stakeholder interview transcripts referenced in
IMPLEMENTATION_PLAN.md §Interviews into a single findings document.
Definition of done: one FINDINGS.md covering, per interview, the top 3
themes plus verbatim supporting quotes; cross-interview patterns called out
in a summary section at the top. Do not editorialize beyond what's in the
transcripts. Return FINDINGS.md for handoff back to canonical-context-builder.
```

Note what did NOT happen: the router did not draft the findings document,
the audit, or the code itself — each `PROMPTS/*.md` is an instruction for
the receiving tool to do that work, and `ROUTING_PLAN.md` states reasoning
about routing, not task content.
