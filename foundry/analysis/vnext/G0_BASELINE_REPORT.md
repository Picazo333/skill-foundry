# G0 — V5 + Noema RC0 Baseline Report

Status: **PENDING_GATE_CI**
Gate: G0
Rollback anchor candidate: `365c62b58b70dea7aecd3ce4c7724ac6ce291353`

## Purpose
Seal the exact pre-implementation VNext starting point after the operator-authorized VNext plan and closed-loop eval amendment became canonical.

## Baseline lineage
- Foundry V5 reconciled foundation: `42fe23e5645facb1e132bbc2f9addfde49393e2e`
- Noema RC0 governance migration merged: `a471a1b9f82faf221eeb3d89aa06a828a9f3a0cc`
- VNext canonical execution program merged: `f7916abba33817536984ec8cd3b89d114ebb30cd`
- VNext gate-eval amendment merged: `365c62b58b70dea7aecd3ce4c7724ac6ce291353`

## Domain integrity
The following Foundry-domain blob SHAs remain identical to the Noema migration integrity review:
- `FOUNDRY_CANON.md` → `f72e2eba22706c0df2b704455a9c1ad91a6e6d07`
- `foundry/taxonomy/TAXONOMY.yaml` → `8b16ad655669f627315f0ef367b7fbd848ccdd12`
- `foundry/ontology/ONTOLOGY.yaml` → `621650353de50da7e47e49b63436ccc22c735413`
- `foundry/registry/SKILL_REGISTRY.yaml` → `a489eaa09ee98088d24c942c62e8e524a12f30ff`
- `foundry/workflows/SF-WF-001_SKILL_GENESIS.md` → `f96692fc183f5f63bf32fd117dfae81ea18374a1`
- `foundry/workflows/SF-WF-002_BOOTSTRAP_V5.md` → `b48161f90a00806373fbfa83f6a010f27d689105`
- `tools/validate_foundry.py` → `dade4d1e95a71811324a6793ea0c57a59a8be18d`
- `tests/test_validate_foundry.py` → `99bca7ec85004e412536c8684d762e2130e99d98`

## Baseline catalog
- registry version: 0.1
- baseline suite: agentic-skill-suite 1.0.1
- baseline published Skills: **15**
- baseline source: `baseline/agentic-skill-suite-v1/`

## Noema pin
`noema.project.yaml` pins protocol `0.1.0-rc.0`.

## Context measurements retained as baseline evidence
From `foundry/analysis/NOEMA_MIGRATION_REVIEW.md`:
- recover: ~1,428 NCU, -73.8% vs old static baseline
- patch/build/audit/research: ~3,243 NCU, -40.5%
- architect: ~7,623 NCU, +3.2% vs old architecture set

These are comparison evidence, not billing-token accounting.

## Required G0 claims
- baseline_reproducible: PENDING PR CI
- foundry_validation_green: PENDING PR CI
- foundry_unit_tests_green: PENDING PR CI
- v1_baseline_integrity: PENDING PR CI
- noema_conformance_green: PENDING PR CI
- rollback_anchor_recorded: PASS

## Exit
Update this report and `G0_GATE_CERTIFICATE.yaml` after the G0 PR checks complete. Do not advance to G1 while any mandatory claim is not PASS.
