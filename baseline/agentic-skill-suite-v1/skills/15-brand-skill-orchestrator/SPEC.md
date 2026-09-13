# SPEC — Brand Skill Orchestrator

## Identity
**ID:** `brand-skill-orchestrator`  
**Category:** brand-orchestration

## Purpose
Route a brand project through only the necessary skills, in the correct order, using existing artifacts and approvals; prevent restarts, duplicated work and manual coordination.

## Trigger when
- Multi-stage brand project.
- Existing partial brand system needs continuation.
- Need automate brand workflow across agents/tools.

## Do not use for
- Doing deep brand strategy itself.
- Replacing child skills.
- Forcing every project through every stage.

## Minimum inputs
- brand project objective
- available artifacts

## Optional inputs
- PROJECT_CANON.md
- approval states
- tool availability
- deadlines

## Required outputs
- `BRAND_WORKFLOW_STATE.md`
- `NEXT_SKILL_RUN.json`
- `HANDOFF_PACKAGES/`
- `COMPLETION_REPORT.md`

## Procedure
1. Inventory brand artifacts and validate status/version.
2. Determine stage; detect completed, incomplete, conflicting or missing upstream work.
3. Route to Discovery only if discovery gaps block Strategy.
4. Invoke Research Architect only when market/category/customer uncertainty materially blocks Strategy.
5. Route Strategy → Verbal/Visual; allow parallel work when dependencies permit.
6. Route approved Visual + Strategy into Identity System.
7. Route validated canon into Brand Book, Creative Briefs and Content System as needed.
8. Invoke Quality Auditor at meaningful gates, not after every trivial action.
9. Use AI Resource Router when execution environment/model allocation matters.
10. Maintain workflow state/checkpoint and stop when project objective is fulfilled.

## Quality gates
- Never reruns completed stage without cause.
- Never substitutes orchestration for domain work.
- Uses artifact versions.
- Approval gates explicit.
- Partial projects resume cleanly.

## Handoffs
- `all brand skills`
- `research-architect`
- `ai-resource-router`
- `canonical-context-builder`

## Required eval scenarios
- Brand from zero to brand book.
- Partial brand with approved strategy but no visual system.
- Existing brand needing content only.

## Sonnet implementation requirements
- Convert this into executable `SKILL.md`.
- Define required/optional/do-not-load context.
- Add compact I/O schemas, failure modes, stop conditions.
- Add 3+ evals plus an edge/failure case.
- Keep shared rules in `/shared`.
- Generate thin generic/ChatGPT/Codex/Claude/Gemini/Cursor adapters.
- Support artifact/checkpoint resume without prior chat memory.
