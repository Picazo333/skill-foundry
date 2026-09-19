# Skill Foundry checkpoint

phase: vnext_g5_pass_pending_merge

completed:
- G0 baseline sealed and reproducible
- G1 authority/contracts/non-regression PASS
- G2 targeted research PASS
- G3 minimal VNext architecture + red-team PASS
- G4 real single-capability vertical slice PASS and published
- G5 R4/R5/R8 Factory research decisions completed
- SF-WF-003 Portfolio Factory implemented
- Factory schemas, policy, deterministic validator and mutation tests implemented
- skill-foundry extended to v1.1.0 with operational FACTORY routing
- mixed synthetic Factory smoke PASS with 100% source accounting
- Noema Conformance PASS
- Foundry Validation + V1 regression PASS
- G5 independent audit PASS
- G5 CompletionCertificate derives PASS
- observed G5 defects D001-D003 routed through explicit rework and closed

partial:
- G5 implementation and extension are READY_FOR_MERGE
- candidate publication state changes to PUBLISHED only after merge to main

blocked: []

active_candidate_id: sf-cand-20260919-skill-foundry-factory-mode

active_program:
- id: skill-foundry-vnext
- plan: foundry/plans/VNEXT_MASTER_PLAN.md
- manifest: foundry/plans/VNEXT_EXECUTION_MANIFEST.yaml
- acceptance: foundry/plans/VNEXT_ACCEPTANCE_GATES.md
- deviations: foundry/plans/VNEXT_DEVIATIONS.md

next_exact_action:
- Revalidate the current PR #13 head.
- Merge PR #13 only if Foundry Validation and Noema Conformance are green.
- Create a G5 close branch from latest main, mark the extension PUBLISHED, mark G5 PASS, issue terminal G5 gate certificate, validate and merge.
- Then execute G6 double canary + hardening.
