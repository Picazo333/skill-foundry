# Walkthrough 3 — Existing app → Product Auditor → implementation handoff

## Starting state
An existing local-first app (matching skill 03's own eval scenario) needs an
audit before a new feature phase. Canon exists but is a few months stale.

## Sequence
1. **`canonical-context-builder`** run (`mode: UPDATE`) against the current
   repo state and any drift since the last canon build.
   - Output: refreshed `PROJECT_CANON.md`.
   - `RUN_RESULT.handoff.next_skill: product-auditor`.
2. **`product-auditor`** run in `mode: AUDIT` (per skill 03's two-mode
   design — AUDIT only, never implements) with
   `source_artifacts: [PROJECT_CANON.md, repo]`.
   - Output: `PRODUCT_AUDIT.md`, `IMPLEMENTATION_PLAN.md`,
     `REGRESSION_MATRIX.md`, `QA_CONTRACT.md`, `HANDOFF_PROMPT.md`. No code
     is touched — the hard AUDIT/QA boundary from skill 03's failure modes
     holds even if asked mid-run to "just fix it" (per its own edge eval).
   - `RUN_RESULT.handoff.next_skill: ai-resource-router`.
3. **`ai-resource-router`** run with `source_artifacts: [IMPLEMENTATION_PLAN.md, HANDOFF_PROMPT.md]`,
   a capacity/quota snapshot.
   - Output: `ROUTING_PLAN.md`, `DISPATCH_QUEUE.json`, `PROMPTS/`,
     `CAPACITY_RISK.md` — a ready-to-dispatch prompt for an external
     execution agent. The router does not implement the plan itself (per
     skill 05's own non-trigger).
4. *(external, out of suite scope)* An execution agent implements the plan.
5. **`product-auditor`** run again, this time in `mode: QA`, with
   `source_artifacts: [IMPLEMENTATION_PLAN.md, REGRESSION_MATRIX.md, delivered work]`.
   - Verifies delivered work against the original plan; does not fix
     anything itself, only reports.
   - `RUN_RESULT.handoff.next_skill: canonical-context-builder`.
6. **`canonical-context-builder`** run (`mode: UPDATE`) to fold the completed
   phase into canon.

## What must hold
- Step 2 and step 5 are the same skill in two different modes — neither mode
  ever writes/changes product code.
- Step 3's router never performs the actual implementation domain work.
- The loop closes back into canon (step 6), matching `WORKFLOW_MAP.md`'s
  "existing product/app" diagram exactly.

## Failure signature
Any step where `product-auditor` or `ai-resource-router` produces a code
diff instead of a plan/dispatch artifact is a boundary violation both
skills' `SKILL.md` explicitly forbid.
