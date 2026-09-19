# R1 — Behavioral completion / false-PASS evidence

Status: **DECIDED**
Gate: G2
Decision owner: Skill Foundry architecture
Date: 2026-09-19

## Decision question

What minimum evidence is required before VNext may claim that a Skill/Foundry work unit is behaviorally complete, rather than merely structurally present?

## Existing project evidence

Shadow recovered a dominant false-positive risk class: artifacts, eval files, validator exit codes, or narrative statements can all exist while behavior is wrong. VNext therefore already requires evidence-backed gate claims, independent audit, holdouts, and circuit breakers.

Noema RC0 explicitly separates conformance from quality. Noema PASS proves governability/conformance only; it cannot prove Foundry semantic correctness.

## External evidence

1. Anthropic, **Demystifying evals for AI agents** (2026-01-09)
   - https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
   - Agent evals need grading logic matched to multi-turn/tool/state behavior.
   - Effective agent evaluation combines code-based, model-based and human graders as appropriate.

2. OpenAI Agents SDK, **Testing**
   - https://openai.github.io/openai-agents-python/testing/
   - Deterministic/provider-neutral tests are appropriate for orchestration owned by the application: tools, handoffs, guardrails, retries and session behavior.
   - Behavior owned by real models/external providers requires real integration/provider evaluation.

3. OpenAI Agents SDK, **Tracing**
   - https://openai.github.io/openai-agents-python/tracing/
   - End-to-end workflow traces distinguish model turns, tools, guardrails and handoffs, demonstrating that a final output alone is insufficient evidence of execution path.

4. Anthropic, **Building Effective AI Agents**
   - https://www.anthropic.com/engineering/building-effective-agents
   - Evaluator-optimizer loops are useful when evaluation criteria are clear and iterative feedback measurably improves outputs.

## Alternatives considered

### A. Structural completion only
Definition: required files exist + validator passes.

Rejected. It directly reproduces Shadow paper-PASS failure modes.

### B. Single model evaluator
Definition: independent model reads artifacts and returns PASS/FAIL.

Rejected as sole authority. It remains a correlated semantic judgment and may rubber-stamp convincing artifacts.

### C. Conjunctive evidence model
Definition: completion requires all applicable structural, runtime/behavioral, independent and adversarial evidence.

**Chosen.**

## Decision

VNext completion is **conjunctive**, not score-based.

For the G4 vertical slice, minimum completion evidence is:

1. **architecture/spec binding**
   - output traces to the approved decision/spec;
2. **deterministic integrity**
   - schemas, required artifacts, references, ownership and regressions pass;
3. **runtime/behavioral evidence**
   - the capability is exercised on representative behavior, not only inspected statically;
4. **trigger/non-trigger/failure behavior**
   - at least one expected activation, one expected refusal/non-trigger, and one failure/edge case where applicable;
5. **independent audit**
   - evaluator separate from builder confirms spec fidelity and scope;
6. **false-completion holdout**
   - at least one protected case designed to catch premature/unsupported completion;
7. **baseline non-regression**
   - V1 and existing Foundry validation remain green;
8. **derived certificate**
   - completion verdict is derived from evidence references; free-form builder text cannot issue PASS.

No aggregate score may offset a mandatory failed or unassessed claim.

## Architecture implication

G3 must define a Foundry-owned `CompletionCertificate` and evidence references that can reuse Noema `EvalResult`, `Artifact`, `Handoff`, and `StorageRef` envelopes without redefining them.

A full tracing framework is **not** required. VNext needs only enough durable execution evidence to prove relevant events/outputs. OpenAI tracing is architectural evidence for observability granularity, not a dependency recommendation.

## Confidence

High.

## Revisit trigger

Reopen if G4 demonstrates that the minimum evidence cannot detect a known Shadow false-PASS, or if the evidence burden materially exceeds the value for simple E1/R0 Skills.
