# SPEC — Product Auditor & Implementation Architect

## Identity
**ID:** `product-auditor`  
**Category:** product

## Purpose
Inspect an existing app/repo/product, verify issues and opportunities, and produce an implementation plan precise enough for an execution agent without implementing during audit mode.

## Trigger when
- User dictates UX bugs/features while navigating an app.
- Need Astra-style product audit.
- Need agent-ready implementation plan.
- Need QA against a prior plan.

## Do not use for
- Writing production code in AUDIT mode.
- Generic ideation without inspecting current state.
- Replacing approved design direction without evidence.

## Minimum inputs
- repo/app/artifacts
- audit objective

## Optional inputs
- PROJECT_CANON.md
- screenshots
- issue list
- prior audit
- JSON/data model
- mobile build

## Required outputs
- `PRODUCT_AUDIT.md`
- `IMPLEMENTATION_PLAN.md`
- `REGRESSION_MATRIX.md`
- `QA_CONTRACT.md`
- `HANDOFF_PROMPT.md`

## Procedure
1. Inspect current product across routes, states and relevant data.
2. Reproduce/verify reported issues where possible; separate confirmed vs suspected.
3. Compare behavior with canonical requirements and prior audits.
4. Identify regressions, missing features, redundant UI, data risks, mobile parity issues and simplification opportunities.
5. Classify P0–P3 and complexity; split implement-now vs backlog vs discard.
6. For each approved change specify problem, target, affected components/data, dependencies, risks, what not to touch, tests and acceptance.
7. Sequence implementation to protect data safety and prevent rework.
8. Define desktop/mobile parity and no-regression tests.
9. Generate execution handoff and stop before implementation in AUDIT mode.

## Quality gates
- Confirmed vs inferred issues separated.
- Executor need not reinterpret product intent.
- Migrations explicit.
- Mobile parity explicit.
- Approved existing features protected.

## Handoffs
- `ai-resource-router`
- `canonical-context-builder`

## Required eval scenarios
- Regula-style local-first app audit.
- Responsive brand site audit.
- Partial implementation versus an existing plan.

## Sonnet implementation requirements
- Turn this into an executable `SKILL.md`, not a descriptive essay.
- Define `REQUIRED_CONTEXT`, `OPTIONAL_CONTEXT`, `DO_NOT_LOAD_BY_DEFAULT`.
- Add compact input/output schemas.
- Add failure modes and stop conditions.
- Add at least 3 evals plus 1 edge/failure case.
- Reference `/shared` for common rules; do not duplicate suite boilerplate.
- Generate thin adapters for generic, ChatGPT, Codex, Claude, Gemini and Cursor.
- Ensure clean resume from artifacts/checkpoints without prior chat memory.
