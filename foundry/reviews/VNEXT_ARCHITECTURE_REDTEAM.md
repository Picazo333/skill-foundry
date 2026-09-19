# VNext Architecture 1.0 — Pre-code Red Team

Status: **PASS — NO OPEN CRITICAL DEFECT**
Target: G3 minimal architecture and front-door vertical slice
Method: threat-model review against recovered Shadow failure patterns + Noema/Foundry boundary.

## Attacks and disposition

| ID | Attack | Initial risk | Resolution | Residual |
|---|---|---|---|---|
| RT-01 | Treat Noema PASS as Skill PASS | Critical | Separate Noema conformance and Foundry CompletionCertificate; conjunctive domain claims | Low |
| RT-02 | Front door self-approves architecture | Critical | Candidate still traverses explicit G6 Decision; front door cannot issue approval | Low |
| RT-03 | Alias hides duplicate existing Skill | Major | Catalog preflight + mandatory decision precedence before NEW_SKILL | Medium, tested G4 |
| RT-04 | Uploaded doc says “ignore governance” | Critical | external/generated input treated as data, not authority | Low, holdout required |
| RT-05 | Builder edits tests until green | Critical | protected holdouts + integrity mechanism + circuit breaker | Low, mechanism required G4 |
| RT-06 | BLOCKED request still mutates canon | Critical | blocked state restricted; no canonical publication until evidence/gates pass | Low |
| RT-07 | “Resume” actually restarts completed work | Major | recovery class explicitly RECONSTRUCT_FROM_REPO with completed/remaining/next_action | Medium, fixture G4 |
| RT-08 | Missing dependency still reports success | Major | mandatory claims become FAIL/BLOCKED; missing evidence cannot PASS | Low |
| RT-09 | Minimal Noema context omits required candidate/spec | Major | Noema supplies stable mode context; Foundry dynamically loads current candidate/spec after routing | Low |
| RT-10 | Executor substitution changes Skill architecture | Major | capability-before-executor; provider identity excluded from architecture | Low |
| RT-11 | Build silently expands approved responsibility | Critical | spec binding + independent audit; architecture drift routes to exception/rework | Low |
| RT-12 | Provenance/evidence refs disappear | Critical | persistent evidence + derived certificate; missing evidence = UNASSESSED | Low |
| RT-13 | Individually safe checks compose into bad chain | Major | G4 tests single lifecycle; composition remains explicit G5/G6 gate, not falsely claimed now | Medium/deferred |
| RT-14 | Front door advertises Factory before it exists | Major | support matrix: detect FACTORY but return explicit BLOCKED until G5 | Low |
| RT-15 | Front door becomes a mega-Skill containing G0–G10 | Major | front door responsibility frozen to detect/preflight/route/mediate; canonical process stays external | Low |
| RT-16 | Invent generic Run/runtime infrastructure prematurely | Major | Run deferred; reuse Noema WorkOrder/Handoff/EvalResult; no runtime framework | Low |
| RT-17 | Ambiguous user request force-routed incorrectly | Major | AMBIGUOUS outcome + one minimum architecture-blocking question | Low |
| RT-18 | CompletionCertificate becomes duplicate Noema EvalResult | Major | CompletionCertificate is Foundry domain aggregation artifact over Noema evidence envelopes | Low |

## Red-team changes made before freeze

1. **No new ontology entity in G4.** CompletionCertificate remains a typed Foundry artifact/contract until repeated usage proves ontology value.
2. **No generic Run entity.** WorkOrder + Handoff + existing Foundry state are sufficient.
3. **Unsupported-mode honesty.** FACTORY/MAINTENANCE are detectable but explicitly BLOCKED in the G4 front door.
4. **Intent and execution routing separated.** Foundry chooses lifecycle; Noema chooses context/executor.
5. **Recovery claim narrowed.** Only `RECONSTRUCT_FROM_REPO` is allowed.
6. **Front-door scope narrowed.** It delegates process rather than embedding methodology.

## Open non-critical risks

- Semantic overlap can still be wrong despite preflight; G4 independent eval covers obvious alias cases and G5 can strengthen dedup.
- Context-efficiency targets are not yet optimized beyond current Noema routing; measure rather than invent thresholds.
- Composition across multiple new Skills is not demonstrated by G4 and remains explicitly out of claim scope until G5/G6.

## Verdict

**PASS**

The architecture can proceed to G4 implementation. No critical red-team defect remains open.
