# Eval Case — Only one capable model despite expiring quota elsewhere

## Scenario
A task needs a genuinely large context window. Only one available tool can
actually do it; a different tool has expiring bonus quota today but cannot
handle the context length. The router must not force the task onto the
quota-expiring tool just to avoid "wasting" it.

## Input
```yaml
RUN_REQUEST:
  objective: "route the transcript synthesis task"
  constraints: []
  desired_output: full_routing_set
  mode: STANDARD
  prior_run: null
  tasks:
    - id: T1
      type: [long_context, synthesis]
      definition_of_done: "synthesize 20 transcripts (~250k tokens combined) into one findings doc"
      hard_requirements: ["context window >= 250k tokens"]
      urgency: "due in 5 days"
  tools:
    - id: tool_bigctx
      provider: providerX
      strengths: ["1M-token context window", "synthesis"]
      known_capacity: "40% unused"
      reset_at: "2026-09-20T00:00:00Z"
      renewal_status: renewing
    - id: tool_smallctx
      provider: providerY
      strengths: ["fast general chat", "coding help"]
      known_capacity: "95% unused"
      extra_resets:
        - amount: "bonus daily quota"
          expires_at: "2026-09-09T23:59:00Z"
      reset_at: "2026-09-10T00:00:00Z"
      renewal_status: renewing
      known_context_window: "32k tokens"
```

## Expected behavior
1. Axis 1 (capability fit) is applied first: tool_smallctx is excluded from
   T1 entirely because its context window cannot hold the ~250k-token input,
   regardless of its expiring bonus quota and near-full unused capacity.
2. tool_bigctx is the only qualifying candidate and is assigned as primary,
   even though it has lower opportunity pressure (renewing normally, no
   expiring grant, later reset) than tool_smallctx.
3. `CAPACITY_RISK.md` notes tool_smallctx's expiring bonus quota as unused
   opportunity, but does not treat that as a reason to route T1 there.
4. `ROUTING_PLAN.md`'s rationale explicitly states that capability fit
   overrode opportunity pressure here — this is the point of the case.

## Expected artifacts
- `ROUTING_PLAN.md` — T1 → tool_bigctx, with rationale naming the context-
  window requirement as the deciding factor over tool_smallctx's expiring
  quota.
- `CAPACITY_RISK.md` — tool_smallctx's expiring bonus quota flagged as a
  separate, unaddressed opportunity-risk note (it may simply go unused this
  cycle if no other task fits it) — not folded into T1's routing.

## Forbidden behavior
- Must NOT route T1 to tool_smallctx to avoid wasting its expiring bonus
  quota.
- Must NOT silently drop the fact that tool_smallctx's quota will likely
  expire unused — that goes in `CAPACITY_RISK.md`, not hidden.
- Must NOT invent a context-window figure for tool_smallctx if one hadn't
  been supplied (here it was supplied: 32k).

## Pass criteria
- [ ] T1 is routed to tool_bigctx only.
- [ ] Rationale explicitly cites the context-window requirement as
      overriding opportunity pressure.
- [ ] tool_smallctx's expiring quota is noted in `CAPACITY_RISK.md` as
      likely-unused, not suppressed.
- [ ] No task is force-routed to tool_smallctx.
