# SF-WF-002 — V5 FOUNDATION AUDIT / HARDENING

Status: ONE-TIME ACTIVE WORKFLOW

V5 already contains the deterministic substrate. Initial agents must **audit and harden**, not invent a second Foundry.

## Antigravity mandatory deliverables
1. `foundry/analysis/V1_CAPABILITY_COVERAGE.md` — all 15 baseline Skills: purpose/boundary, key I/O, actual handoffs, Genesis coverage, explicit non-coverage.
2. `foundry/analysis/FOUNDATION_GAP_MAP.md` — map G0–G10 to existing coverage/missing functions and decide REUSE/EXTEND/MODE/DEPENDENT_SKILL/NEW_SKILL/NO_SKILL without mirroring stages into meta-Skills.
3. `foundry/analysis/FOUNDRY_LIFECYCLE_AUDIT.md` — audit operating model, registry, taxonomy, ontology and closure paths.
4. `foundry/analysis/FOUNDRY_EVAL_RESULTS.md` — run the five cases under `foundry/evals/cases/` as architecture evals and record PASS/FAIL with evidence.
5. Modify registry/taxonomy/ontology only when the audit proves a deficiency.
6. `foundry/handoffs/ANTIGRAVITY_V5_FOUNDATION.md` with findings, exact edits, proposed meta-capabilities (PROPOSED only), next action.
7. Update `foundry/state/CHECKPOINT.md` accurately.
8. Commit/push `agent/antigravity`; end exactly `READY_FOR_REVIEW`.

## Cursor mandatory deliverables
1. Inspect `catalog/_template/`, Foundry contracts, `tools/validate_foundry.py` and tests against the V1 precedent.
2. Fix only concrete defects; do not replace working substrate for style.
3. Run `python tools/validate_foundry.py` and `python -m unittest tests/test_validate_foundry.py`.
4. Run the baseline validator and confirm the 15-Skill baseline remains intact.
5. Verify intentionally invalid tests fail for the intended reason rather than a generic crash.
6. Create `foundry/handoffs/CURSOR_V5_FOUNDATION.md` with files changed, tests, results and any remaining assumptions.
7. Do not invent production Skills or modify the baseline.
8. Commit/push `agent/cursor`; end exactly `READY_FOR_REVIEW`.

## Acceptance criteria
Foundation is ready only when both missions are substantive, Foundry validator/tests pass, baseline validator passes, G0–G10 are covered in Antigravity's audit, lifecycle evals are evaluated, no meta-Skill is self-approved, and no unrelated project context leaks into new operational artifacts.
