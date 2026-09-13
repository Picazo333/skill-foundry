# START V5 — CURSOR

Execute the one-time deterministic foundation audit/hardening. Do not wait for `APPROVED_FOR_BUILD`, Antigravity, or a candidate. Do not stop after inspection.

## Read first
`AGENTS.md` → `FOUNDRY_CANON.md` → `FOUNDRY_OPERATING_MODEL.md` → `COLLABORATION_PROTOCOL.md` → `foundry/workflows/SF-WF-001_SKILL_GENESIS.md` → `foundry/workflows/SF-WF-002_BOOTSTRAP_V5.md` → compact registry/taxonomy/ontology → relevant V1 contracts/validator/template only.

## Branch
Work only on `agent/cursor`, created/synced from latest `origin/main`. Handle normal Git yourself. Never force-push. Stop only for authentication or genuine unresolved conflict.

## Mission
V5 already contains `catalog/_template/`, Foundry contracts, `tools/validate_foundry.py`, tests and practical lifecycle templates. Audit them against the V1 precedent and the G0–G10 contract. **Fix concrete defects; do not rebuild working files for style.**

Mandatory validation:
1. Ensure the local dev dependencies in `requirements-dev.txt` are available. If they are missing, install them yourself using the available Python launcher; do not ask the human to do it.
2. Run `tools/validate_foundry.py` using the available Python launcher (`python`, `py`, or equivalent).
3. Run `tests/test_validate_foundry.py` through unittest.
4. Run the baseline suite validator at `baseline/agentic-skill-suite-v1/scripts/validate_suite.py`.
5. Prove each negative unit test fails for its intended reason, not because the validator crashes or skips the check.

Create `foundry/handoffs/CURSOR_V5_FOUNDATION.md` with files inspected/changed, contracts reused, exact tests and results, and unresolved assumptions. Do not edit the canonical Foundry checkpoint and do not modify baseline.

Repair failures autonomously until all required validation passes. Commit/push. Final response: concise artifacts + tests + branch/commit; final line exactly `READY_FOR_REVIEW`.
