# SPEC — AI Resource Router

## Identity
**ID:** `ai-resource-router`  
**Category:** ai-operations

## Purpose
Choose the best AI/tool for a task using capability fit, available quota, reset urgency, cost/opportunity, context needs and execution mode; output a dispatch plan and prompt.

## Trigger when
- Multiple AI subscriptions/tools are available.
- Need decide what to use before reset.
- Need task-to-model routing.
- Need daily AI deployment plan.

## Do not use for
- Abstract benchmarking with no task.
- Inventing quota data.
- Executing domain work instead of routing it.

## Minimum inputs
- tasks/projects
- available tool/capacity snapshot

## Optional inputs
- reset times
- extra resets
- costs
- renewal status
- project urgency
- tool strengths
- context constraints

## Required outputs
- `ROUTING_PLAN.md`
- `DISPATCH_QUEUE.json`
- `PROMPTS/`
- `CAPACITY_RISK.md`

## Procedure
1. Normalize tasks by type: research, synthesis, code, audit, agentic, creative, long-context, QA.
2. Normalize resources: availability, windows, reset date/time, extra resets/expiry, cost, renewal and account relationships.
3. Score capability fit first; never route poorly just to burn quota.
4. Calculate opportunity pressure from unused capacity × reset proximity × expiry risk × renewal status.
5. Account for supervision/switching cost and cap simultaneous agents.
6. Assign one primary tool and fallback only where useful.
7. Generate concise dispatch prompts referencing canonical artifacts.
8. Produce use-now/next/reserve queue and explain high-impact choices.
9. Stop after routing.

## Quality gates
- Weekly/monthly capacity prioritized over irrelevant short windows when appropriate.
- Extra reset expiry considered.
- No fabricated quotas.
- Model fit beats token burning.
- Prompts are task-specific.

## Handoffs
- `product-auditor`
- `research-architect`
- `brand-skill-orchestrator`

## Required eval scenarios
- Claude/Gemini/Grok/Cursor mixed quota day.
- Only one capable model despite expiring quota elsewhere.
- Two accounts of same provider with different resets.

## Sonnet implementation requirements
- Turn this into an executable `SKILL.md`, not a descriptive essay.
- Define `REQUIRED_CONTEXT`, `OPTIONAL_CONTEXT`, `DO_NOT_LOAD_BY_DEFAULT`.
- Add compact input/output schemas.
- Add failure modes and stop conditions.
- Add at least 3 evals plus 1 edge/failure case.
- Reference `/shared` for common rules; do not duplicate suite boilerplate.
- Generate thin adapters for generic, ChatGPT, Codex, Claude, Gemini and Cursor.
- Ensure clean resume from artifacts/checkpoints without prior chat memory.
