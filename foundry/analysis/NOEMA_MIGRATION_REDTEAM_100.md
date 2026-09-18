# Noema migration red-team — 100-round pre-merge audit

**Scope:** PR #4, `migration/noema-rc0` vs baseline `42fe23e5645facb1e132bbc2f9addfde49393e2e`  
**Objective:** verify that Noema adoption did not delete, absorb, silently weaken, or orphan important Skill Foundry behavior.

## Method
100 adversarial rounds grouped into ten lenses:
1. repository tree / deletion / rename;
2. constitutional and domain authority;
3. G0–G10 lifecycle integrity;
4. decision semantics and human gates;
5. platform-agent role/branch behavior;
6. progressive context and token discipline;
7. V1 baseline, contracts, evals and package substrate;
8. CI, validator separation and immutable Noema pinning;
9. checkpoint/provenance/recovery;
10. merge durability, cross-project leakage and future-staleness.

Each round asks whether an old behavior still exists in one authoritative place, whether a new rule conflicts with Foundry, and whether the resulting tree remains valid before and after merge.

## First pass result
99/100 substantive controls passed. One deterministic failure:
- the migration checkpoint encoded “unmerged pending human review”, which would become false immediately after merge.

Manual semantic review found three additional weaknesses not caught by simple path/content assertions:
- `noema.project.yaml` unnecessarily named `agency-domain-rules` in `does_not_own`, coupling an autonomous Foundry repo to an unrelated consumer;
- the lightweight `AGENTS.md` no longer stated explicitly that the existing Operating Model + Skill Genesis workflow must not be replaced during ordinary work;
- the cold-start entrypoint no longer explicitly repeated “workflow/capability != Skill”, “new Skill is not default”, and “reuse proven shared contracts first”, although deeper canonical docs still contained them.

## Corrections made before merge
- checkpoint rewritten to remain true both before and after merge; Git/PR state is authoritative for merge state;
- removed Agency-specific authority leakage from the Foundry manifest;
- replaced transient `x-migration-stage: pre-merge-review` with stable `x-noema-adoption: rc0-conformant`;
- restored the lost high-value guardrails to the lightweight `AGENTS.md` while keeping progressive context.

## Integrity facts
No tracked file is deleted or renamed by the migration.

These domain-critical blobs remain byte-for-byte identical to baseline:
- `FOUNDRY_CANON.md`
- `foundry/taxonomy/TAXONOMY.yaml`
- `foundry/ontology/ONTOLOGY.yaml`
- `foundry/registry/SKILL_REGISTRY.yaml`
- `foundry/workflows/SF-WF-001_SKILL_GENESIS.md`
- `foundry/workflows/SF-WF-002_BOOTSTRAP_V5.md`
- `tools/validate_foundry.py`
- `tests/test_validate_foundry.py`

The V1 baseline tree remains present and is executed by CI.

## Removed checkpoint detail
The shortened checkpoint no longer enumerates every historical completion line. Those facts remain evidenced by their canonical artifacts:
- candidate ID/path, decision ladder, closure paths, G8 REWORK and G10 publish semantics: Operating Model + SF-WF-001;
- lifecycle eval PASS results: `foundry/analysis/FOUNDRY_EVAL_RESULTS.md`;
- 15-Skill coverage: `foundry/analysis/V1_CAPABILITY_COVERAGE.md`;
- gap map: `foundry/analysis/FOUNDATION_GAP_MAP.md`;
- lifecycle/taxonomy/ontology audit: `foundry/analysis/FOUNDRY_LIFECYCLE_AUDIT.md`;
- Antigravity/Cursor reconciliation detail: handoff reports.

This is compression of a derived state projection, not deletion of evidence.

## Merge gate
Remain in HOLD until:
- post-correction 100-round audit has no material failure;
- Noema Conformance passes;
- Foundry validator passes;
- 10 Foundry unit tests pass;
- V1 15-Skill baseline validator passes;
- human approves the PR diff.

No merge is authorized by this document.
