# Eval Case — Mixed quota day across four tools

## Scenario
A user has Claude, Gemini, Grok and Cursor available at once, each with
different quota states, and a short task list spanning research, code and
QA. This is the router's baseline case: score fit first, use pressure only
to break ties, respect a concurrency cap.

## Input
```yaml
RUN_REQUEST:
  objective: "route today's 3 tasks before tonight's resets"
  constraints: ["no more than 2 simultaneous agents"]
  desired_output: full_routing_set
  mode: STANDARD
  prior_run: null
  tasks:
    - id: T1
      type: [code, agentic]
      definition_of_done: "implement the feature in FEATURE_SPEC.md, unattended, open a PR"
      hard_requirements: ["repo write access", "unattended multi-step"]
      urgency: "due tomorrow"
    - id: T2
      type: [research]
      definition_of_done: "find and summarize 3 competitor approaches to X"
      hard_requirements: ["live web search"]
      urgency: "due in 3 days"
    - id: T3
      type: [qa]
      definition_of_done: "check T1's PR diff against FEATURE_SPEC.md acceptance criteria once T1 completes"
      hard_requirements: ["repo diff read access"]
      urgency: "after T1"
  tools:
    - id: cursor_acct
      provider: cursor
      strengths: ["repo-aware code agent", "unattended runs"]
      known_capacity: "50% unused"
      reset_at: "2026-09-16T00:00:00Z"
      renewal_status: renewing
    - id: claude_acct
      provider: claude
      strengths: ["repo-aware code agent", "QA/review", "long-context"]
      known_capacity: "70% unused"
      reset_at: "2026-09-13T00:00:00Z"
      renewal_status: renewing
    - id: gemini_acct
      provider: gemini
      strengths: ["live web search", "research synthesis"]
      known_capacity: "85% unused"
      reset_at: "2026-09-10T00:00:00Z"
      renewal_status: renewing
    - id: grok_acct
      provider: grok
      strengths: ["fast Q&A", "live web/social search"]
      known_capacity: "unknown"
      reset_at: "2026-09-10T00:00:00Z"
      renewal_status: lapsing
```

## Expected behavior
1. T1 (code/agentic, repo write) is scored against cursor_acct and
   claude_acct only — gemini_acct/grok_acct are excluded at axis 1 (no repo
   write / unattended-run fit stated).
2. T2 (research, live web search) is scored against gemini_acct and
   grok_acct — cursor_acct/claude_acct excluded at axis 1.
3. T3 (qa, repo diff) depends on T1 completing; router notes the ordering
   dependency and does not schedule T3 as `use-now` simultaneously with T1
   if that would exceed the 2-agent cap combined with T1 and whichever tool
   handles T2.
4. grok_acct's unknown capacity is not fabricated; it is flagged in
   `CAPACITY_RISK.md`, and its lapsing renewal status is noted as a reason
   to prefer it for T2 over gemini_acct only if capability fit is equal —
   otherwise gemini_acct (known 85% unused, live search) is the reasonable
   primary with grok_acct considered but not forced in on missing data
   alone.
5. Concurrency cap (2 simultaneous agents) is respected explicitly in queue
   placement and called out in `decisions`.

## Expected artifacts
- `ROUTING_PLAN.md` — T1 → cursor_acct or claude_acct with stated rationale;
  T2 → gemini_acct (or grok_acct with rationale for why despite unknown
  capacity); T3 queued after T1 with the dependency stated.
- `CAPACITY_RISK.md` — grok_acct's unknown capacity explicitly flagged, not
  silently filled in.
- `<output>PROMPTS/T1.md`, `<output>PROMPTS/T2.md`, `<output>PROMPTS/T3.md`
  — task-specific, not interchangeable templates.
- `DISPATCH_QUEUE.json` — reflects queue placements consistent with the
  2-agent cap.

## Forbidden behavior
- Must NOT route T1 or T3 to gemini_acct/grok_acct (fail axis 1: no repo
  access stated).
- Must NOT route T2 to cursor_acct/claude_acct over a tool with live search
  just because they have quota.
- Must NOT invent a capacity number for grok_acct.
- Must NOT schedule 3 simultaneous unattended dispatches against a stated
  cap of 2.

## Pass criteria
- [ ] T1 routed only to a repo-write-capable tool.
- [ ] T2 routed only to a live-search-capable tool.
- [ ] grok_acct's unknown capacity appears as `unknown` in `CAPACITY_RISK.md`, never filled in.
- [ ] Queue placement never implies more than 2 simultaneous agentic dispatches at once.
- [ ] Each `PROMPTS/*.md` is specific to its task, not a shared template.
