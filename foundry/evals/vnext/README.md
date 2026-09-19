# Skill Foundry VNext Gate Eval Loop

Status: **CANONICAL PROGRAM AMENDMENT — PRE-G0**

Purpose: make every VNext gate evidence-driven and closed-loop.

A gate advances only when all mandatory claims for that gate are evidenced as PASS. Missing evidence is UNASSESSED, never PASS. A failed claim generates a defect routed to the responsible owner/stage, followed by selective rework and selective re-evaluation.

## Evaluation order

1. deterministic evidence
2. runtime / behavioral evidence
3. independent audit evidence
4. adversarial / Shadow evidence
5. model judgment
6. narrative assertion

Lower-priority evidence cannot override higher-priority contradictory evidence.

## Verdicts

- PASS
- FAIL
- UNASSESSED
- BLOCKED

No aggregate score can convert a mandatory FAIL or UNASSESSED into PASS.

## Loop

WORK → EVAL SUITE → CLAIMS → PASS? → CERTIFICATE → NEXT GATE

If not:
FAIL → DEFECT → OWNER/STAGE → REWORK → SELECTIVE RE-EVAL → CERTIFICATE

## Certificate levels

- WORK_UNIT_CERTIFICATE
- GATE_CERTIFICATE
- WAVE_CERTIFICATE
- RELEASE_CERTIFICATE

## Noema boundary

Noema governs repository conformance, context, authority, executor descriptors/routing and coordination evidence envelopes. Skill Foundry owns the semantic quality claims and PASS/FAIL meaning for Skill/Factory behavior.

NOEMA PASS never equals FOUNDRY PASS.
