# SPEC — Research Architect

## Identity
**ID:** `research-architect`  
**Category:** research

## Purpose
Transform a raw idea/problem into an exhaustive, decision-oriented research architecture before deep research; support autonomous architecture rounds without user “continue” prompts.

## Trigger when
- New business/market/product where correct research questions are not known.
- Complex audit/strategy program requiring broad domain discovery.
- User wants 200+ iteration research architecture.

## Do not use for
- Single factual lookup.
- Narrow comparison.
- Deep research execution itself.
- Simple technical fix.

## Minimum inputs
- raw project/research objective

## Optional inputs
- PROJECT_CANON.md
- existing Research Plan Architect v2
- constraints
- known evidence

## Required outputs
- `PROJECT_RESEARCH_BRIEF.md`
- `MASTER_RESEARCH_PROGRAM.md`
- `DOMAIN_MAP.md`
- `COVERAGE_DEBT.md`
- `GAP_LEDGER.md`
- `CHECKPOINT.md`
- `EXECUTOR_START_PROMPT.md`

## Procedure
1. Reconstruct project brief; label unverified assumptions as hypotheses.
2. Generate a master decision-oriented research question.
3. Discover universal and domain-native lenses; weight areas by importance, uncertainty, complexity, decisions affected and risk.
4. Design at least 150 valid scope-expansion iterations; every iteration must create a material delta.
5. Maintain Coverage Debt, contradictions, white-space, primary-evidence triggers and automation/AI lenses.
6. In AUTONOMOUS mode execute architecture rounds without asking for “Siguiente”/“y”; checkpoint after logical blocks.
7. Run at least 50 domain-polishing iterations: dedupe, boundaries, interconnections, evidence/decision mapping and red-team.
8. Run 10 quality passes: coverage, specificity, commercial, operational, tech/data/automation, risk/trust, alternative thesis, novelty, consolidation, executability.
9. Stop before deep research and produce an executor-ready research package.

## Quality gates
- 150+ expansion iterations.
- 50+ polishing iterations.
- Novelty/material-delta gate.
- Coverage debt revisited.
- Canonical domain map interconnected.
- 10 quality passes.
- Stops before deep research.

## Handoffs
- `canonical-context-builder`
- `ai-resource-router`

## Required eval scenarios
- BOLD-like automation agency.
- Sports betting/tipster market.
- Dental operating-system research.

## Sonnet implementation requirements
- Turn this into an executable `SKILL.md`, not a descriptive essay.
- Define `REQUIRED_CONTEXT`, `OPTIONAL_CONTEXT`, `DO_NOT_LOAD_BY_DEFAULT`.
- Add compact input/output schemas.
- Add failure modes and stop conditions.
- Add at least 3 evals plus 1 edge/failure case.
- Reference `/shared` for common rules; do not duplicate suite boilerplate.
- Generate thin adapters for generic, ChatGPT, Codex, Claude, Gemini and Cursor.
- Ensure clean resume from artifacts/checkpoints without prior chat memory.
