# VNext Gate Evaluation Model

## Claim model

Every gate declares mandatory claims. Each claim specifies:
- evaluator class;
- evidence type;
- owner;
- failure severity;
- rework destination;
- selective rerun scope.

Mandatory claim PASS requires positive evidence. Missing evidence = UNASSESSED.

## Evaluator classes

- deterministic
- behavioral
- independent_audit
- shadow_adversarial
- noema_conformance
- human_decision

## Severity

- CRITICAL — gate/wave stops immediately
- MAJOR — gate cannot pass; rework required
- MINOR — must be resolved or explicitly accepted by the relevant gate contract

## Anti-gaming

- builder-visible evals may guide implementation;
- auditor evals are independently authored/reviewed;
- holdout/adversarial fixtures may be hidden from the builder;
- protected test/holdout changes require explicit authorization;
- unauthorized weakening or mutation of protected evals = circuit breaker.

## Rework semantics

A defect must include:
- defect_id
- failed_claim
- severity
- owner_role
- return_to
- affected_artifacts
- problem
- acceptance_criteria
- rerun_scope

Re-evaluate only impacted checks plus any regression subset required by the gate contract.

## Evaluator calibration

Model-based evaluators must periodically be tested against:
- known-good fixture → expected PASS
- known-bad fixture → expected FAIL

Calibration failure invalidates that evaluator for the affected gate until repaired.
