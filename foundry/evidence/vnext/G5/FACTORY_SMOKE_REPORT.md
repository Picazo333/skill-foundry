# G5 Factory Smoke Report

Status: **PASS**

## Scope
This is a synthetic mixed-portfolio control-plane proof, not a production Skill portfolio and not a substitute for real human Plan Lock.

## Results

| Check | Evidence | Result |
|---|---|---|
| Raw/source coverage | 10 raw sources, 10 ledger sources, validator source_coverage=1.0 | PASS |
| UNKNOWN quarantine | i7 remains UNKNOWN + UNRESOLVED | PASS |
| Semantic dedup | s2→i1 and s8→i6 without duplicate Skill candidates | PASS |
| Catalog reuse | i1→canonical-context-builder; i3→skill-foundry; i5→brand-skill-orchestrator | PASS |
| NO_SKILL routing | deterministic checksum stays utility/no-Skill | PASS |
| Plan Lock fidelity | all 8 items covered by fixture Plan Lock; architecture changes require exception | PASS |
| Dependency DAG | i1→i6→i8, no cycle | PASS |
| Wave order | i6=w1, i8=w2 | PASS |
| Shared canon protection | shared_canon_write=false; serialized publisher required | PASS |
| Architecture exception | ex-001 keeps i4 deferred and unscheduled | PASS |
| Policy enforcement | >2 builders, non-buildable scheduling, blocked exception scheduling all fail mutation tests | PASS |
| Baseline integrity | V1 validator remains green | PASS |
| Noema boundary | Noema conformance green; Factory-specific quality meaning remains Foundry-owned | PASS |

## Closed-loop rework observed

Three real defects were caught by the gate loop and repaired rather than rationalized:
- G5-D001 validator crashed on an unscheduled buildable instead of returning a defect.
- G5-D002 Foundry-domain quality claims were incorrectly placed in Noema's protocol-governed claim vocabulary.
- G5-D003 a synthetic downstream item missed the newly-required lifecycle field.

All three have explicit evidence and acceptance criteria in `DEFECTS.yaml`.

## Synthetic execution
Two buildable fixture items progress through dependency-safe synthetic work receipts:
- i6 in w1 → SIMULATED_READY_FOR_PUBLISH
- i8 in w2 only after i6 → SIMULATED_READY_FOR_PUBLISH

No fake Skill packages or registry entries are created. G5 proves Factory control-plane semantics; real manufacturing is exercised in G6.

## CI evidence
- Skill Foundry Validation: `github-actions://35468943739` — PASS
- Noema Conformance: `github-actions://35468944034` — PASS
