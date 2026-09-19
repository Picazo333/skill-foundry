# Skill Foundry checkpoint

phase: vnext_g4_build_pass_pending_merge

completed:
- V5 + Noema RC0 baseline sealed through G0
- G1 Noema/Foundry authority and contract reconciliation PASS
- G2 targeted research PASS
- G3 minimal VNext architecture + pre-code red-team PASS
- front-door candidate completed G0–G7 with explicit G6 Decision
- G8 skill-foundry implementation complete
- G9 independent audit PASS
- G4 behavioral and protected holdout evidence PASS
- Foundry Validation and Noema Conformance green on implementation branch
- deterministic G4 CompletionCertificate derives PASS

partial:
- G4 candidate implementation is READY_FOR_MERGE
- G10 registry/canon publication must occur only after implementation merge

blocked: []

active_candidate_id: sf-cand-20260919-skill-foundry-front-door

active_program:
- id: skill-foundry-vnext
- plan: foundry/plans/VNEXT_MASTER_PLAN.md
- manifest: foundry/plans/VNEXT_EXECUTION_MANIFEST.yaml
- acceptance: foundry/plans/VNEXT_ACCEPTANCE_GATES.md
- deviations: foundry/plans/VNEXT_DEVIATIONS.md

next_exact_action:
- Merge PR #11 only if current head CI remains green.
- Create the G4 publish/canon follow-up from latest main.
- Add skill-foundry to Skill Registry, mark candidate PUBLISHED, finalize G4 gate certificate/manifest/checkpoint, validate, and merge.
- Then execute VNext G5.
