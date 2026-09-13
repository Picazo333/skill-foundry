# Reference: routing decision framework

Used in `SKILL.md` steps 3–6 (scoring, opportunity pressure, time horizon,
supervision cost). Deliberately generic on tool names/prices — plug in
whatever tools/accounts the `RUN_REQUEST` actually supplies. Do not hardcode
a specific vendor's model lineup or pricing here; those go stale and belong
in the per-run `RUN_REQUEST.tools` data instead.

## The four axes, in priority order

### 1. Capability fit (primary filter — always first)
Can this tool actually do this task well? This is a gate, not a score to
average against the others: a tool that fails it is removed from
consideration for that task before axis 2–4 are even computed.

Ask, per task type:
- **research** — can it browse/search or was it given the source material?
- **synthesis** — does it handle the input length without truncation?
- **code** — does it have the repo/tool access the task needs (execution,
  file edits, test running)?
- **audit** — can it see the actual artifact being audited, not just a
  description of it?
- **agentic** — can it run multi-step and unattended, or does it need a
  human in the loop at each step?
- **creative** — does a stated tool-strength note favor it for this kind of
  output?
- **long_context** — does its context window actually cover the material?
- **qa** — does it have (or can it be given) the acceptance criteria to
  check against?

A tool that is merely "available" is not a candidate until it clears this
gate for the specific task.

### 2. Opportunity pressure (tie-break among qualified tools)
Among tools that already passed axis 1, compute a qualitative pressure
signal:

```
pressure ≈ unused_capacity × reset_proximity × expiry_risk × renewal_status
```

- **unused_capacity** — how much of this tool's window is sitting idle.
- **reset_proximity** — how soon the window resets (closer reset = capacity
  not carried forward = higher pressure to use it now).
- **expiry_risk** — extra/bonus resets or trial capacity that expires and
  does not renew; this is the highest-pressure case when present.
- **renewal_status** — lapsing/non-renewing capacity is more urgent to use
  than steadily renewing capacity, which can absorb next week's tasks too.

High pressure breaks a tie toward using that tool now. It never overrides a
clear capability-fit winner (an ill-fitting tool with expiring quota is
still not the right routing — see failure modes in `SKILL.md`).

### 3. Time horizon (weekly/monthly vs. short windows)
Prefer routing that protects longer-cycle capacity (weekly/monthly resets)
for tasks that can plausibly wait, and reserves tight short-window capacity
for tasks that actually need that urgency. Routing an easily-deferred task
into a scarce short window just because it's "available right now" wastes
the window on the wrong task later. Only override this when the task itself
carries the urgency (a real deadline, blocking downstream work).

### 4. Supervision / switching cost
Every simultaneously-dispatched agentic task adds attention overhead for
whoever is supervising them. Respect any stated cap on concurrent agents. In
its absence, use judgment: routing five unattended agentic tasks at once
when there's no way to check in on any of them is a real cost even though no
tool axis flags it — note it explicitly in `decisions` rather than silently
maxing out concurrency.

## Worked illustration (generic tool names)

Two tools, one task:

- **Task:** long-context synthesis of a 150-page source set, due in 4 days,
  not urgent beyond that.
- **Tool A:** long-context capable, weekly reset in 2 days, 70% capacity
  unused, renewing normally.
- **Tool B:** long-context capable, daily reset tonight, 90% capacity
  unused, has a bonus-reset grant expiring in 24 hours.

Axis 1: both pass (both handle the context length).
Axis 2: Tool B has higher opportunity pressure (expiring bonus grant, daily
reset tonight).
Axis 3: the task can wait 4 days, so protecting Tool A's weekly window isn't
necessary here — but Tool B's expiring grant means using B costs nothing
extra to Tool A's future availability.
Axis 4: single task, no concurrency concern.

**Routing:** Tool B, primary — captures the expiring bonus capacity that
would otherwise be lost; Tool A stays available for whatever comes up before
its own reset. If Tool B lacked long-context capability (failed axis 1),
this would flip immediately to Tool A regardless of B's expiring grant —
capability fit always wins over unused-quota pressure.

## When no tool clears axis 1
Do not lower the bar. Report the task as unroutable with the specific
missing capability named (`SKILL.md` step 10) — this is a correct, expected
outcome of the framework, not a failure to route harder.
