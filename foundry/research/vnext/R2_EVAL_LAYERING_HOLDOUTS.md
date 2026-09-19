# R2 — Eval layering, holdouts and eval-gaming resistance

Status: **DECIDED**
Gate: G2
Date: 2026-09-19

## Decision question

How should VNext divide eval responsibility among the builder, independent auditor, deterministic tooling and protected holdouts without creating unnecessary cost?

## Existing project evidence

Shadow explicitly recovered eval-gaming strategies including weakening assertions, fixtures or test expectations. The VNext pre-G0 amendment already makes protected eval manipulation a circuit breaker and requires model-evaluator calibration.

## External evidence

1. Anthropic, **Demystifying evals for AI agents**
   - https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
   - Agent eval systems commonly combine code-based, model-based and human graders; grader choice should match what is being measured.

2. OpenAI Agents SDK, **Testing**
   - https://openai.github.io/openai-agents-python/testing/
   - Deterministic tests should cover orchestration the application owns.
   - Provider/model-owned behavior needs integration/provider evaluation rather than a fake deterministic substitute.

3. OpenAI Agents SDK, **Guardrails**
   - https://openai.github.io/openai-agents-python/guardrails/
   - Blocking checks can prevent expensive or unsafe downstream execution. This supports treating high-severity eval failures as gates rather than advisory scores.

4. Anthropic, **Building Effective AI Agents**
   - https://www.anthropic.com/engineering/building-effective-agents
   - Evaluator-optimizer patterns are justified when clear criteria exist and feedback measurably improves results.

## Alternatives considered

### A. Builder authors and runs all tests
Rejected: cheapest, but creates direct opportunity for test gaming and correlated blind spots.

### B. All tests hidden from builder
Rejected: wastes iteration budget and makes normal acceptance behavior unnecessarily opaque.

### C. Layered eval architecture
**Chosen.**

## Decision

Use three semantic layers plus deterministic infrastructure:

### L0 — Deterministic project checks
Owned by code/CI:
- schemas;
- references;
- IDs;
- ownership/write scope;
- baseline regression;
- dependency graph;
- protected suite integrity.

### L1 — Builder-visible acceptance evals
Purpose:
- make approved behavior implementable;
- encode spec examples;
- enable fast local iteration.

Builder may add cases but may not weaken protected existing cases.

### L2 — Independent auditor evals
Purpose:
- test spec fidelity, non-trigger behavior, scope creep, quality and failures from a perspective not authored by the builder.

Evaluator identity/tool should be independent where practical.

### L3 — Protected holdout / Shadow cases
Purpose:
- catch false completion, gaming, adversarial edge cases and known failure patterns.

The builder knows the quality contract but not all holdout fixtures.

## Holdout sizing

Do **not** define a universal large fixed count.

Depth is risk/effort-adaptive:
- simple/low-risk work: minimum targeted holdout(s) for false completion + any relevant failure surface;
- core/high-blast-radius work: broader protected suite;
- orchestrator/routing/system-critical work: composition/routing/adversarial holdouts.

Quality floor is constant; amount of evidence varies.

## Integrity rule

Protected suites require an integrity reference before and after build. Unauthorized mutation or weakening is a circuit breaker, not ordinary REWORK.

G4 should implement the smallest practical hash/integrity mechanism required for protected fixtures.

## Evaluator calibration

Critical model-based evaluators must pass known-good and known-bad calibration fixtures before their verdict is relied upon. Calibration failure invalidates the evaluator for the affected gate.

## Architecture implication

G3/G4 must distinguish:
- eval definition;
- eval execution result;
- protected fixture integrity;
- evaluator provenance/calibration;
- gate claim derivation.

No universal aggregate score is introduced.

## Confidence

High.

## Revisit trigger

Reopen after the real canary if holdout maintenance cost is high, calibration is unstable, or correlated failure remains visible despite independent layers.
