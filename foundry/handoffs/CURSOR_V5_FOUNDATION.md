# CURSOR V5 FOUNDATION

Status: RECONCILED after Antigravity merge. Deterministic substrate remains compatible with the now-canonical lifecycle. No production Skill was built. Baseline was not modified. Canonical Foundry checkpoint was not edited.

Branch: `agent/cursor` (synced to `origin/agent/cursor`, then `origin/main` integrated; already contained via PR #2)

## Mission
One-time G8-style audit/hardening of V5 Foundry tooling against the V1 15-Skill precedent and the G0–G10 contract. Independent of Antigravity’s architecture audit.

## Files inspected
- `AGENTS.md`, `FOUNDRY_CANON.md`, `FOUNDRY_OPERATING_MODEL.md`, `COLLABORATION_PROTOCOL.md`
- `foundry/workflows/SF-WF-001_SKILL_GENESIS.md`, `foundry/workflows/SF-WF-002_BOOTSTRAP_V5.md`
- Compact registry/taxonomy/ontology: `foundry/registry/SKILL_REGISTRY.yaml`, `foundry/taxonomy/TAXONOMY.yaml`, `foundry/ontology/ONTOLOGY.yaml`
- Foundry contracts: `foundry/contracts/candidate.schema.json`, `skill-spec.schema.json`, `registry-entry.schema.json`
- Catalog template: `catalog/_template/**`
- Lifecycle templates under `foundry/templates/`
- `tools/validate_foundry.py`, `tests/test_validate_foundry.py`, `requirements-dev.txt`
- Relevant V1 precedent only: `baseline/agentic-skill-suite-v1/scripts/validate_suite.py`, `shared/contracts/skill-manifest.schema.json`, `shared/templates/EVAL_TEMPLATE.md`, and Skill `01` `SKILL.md`/`manifest.json` as package evidence
- `foundry/queue/CANDIDATES.yaml`, `foundry/specs/README.md`, `foundry/state/CHECKPOINT.md` (read only)

## Files changed
- `catalog/_template/SKILL.md` — added required `## Autonomy` (quality floor / canon §4 / G7–G8). Working headings were not restyled.
- `foundry/contracts/skill-manifest.schema.json` — Foundry-owned reuse of the V1 portable manifest contract for published catalog packages.
- `foundry/templates/04_RESEARCH_PLAN.template.md` — missing G4 authoring template.
- `foundry/templates/04_RESEARCH_FINDINGS.template.md` — missing G4 authoring template, including `RESEARCH_SKIPPED`.
- `tools/validate_foundry.py` — concrete defect repairs (see below).
- `tests/test_validate_foundry.py` — negative tests now assert the intended FAIL reason; extra fixtures cover silent-skip and crash paths.
- `foundry/handoffs/CURSOR_V5_FOUNDATION.md` — this file.

## Contracts reused
- V1 `skill-manifest.schema.json` required fields (`id`, `name`, `version`, `category`, `purpose`, `triggers`, `non_triggers`, `outputs`) plus V1 optional arrays.
- V1 eval case sections: Scenario, Input, Expected behavior, Expected artifacts, Forbidden behavior, Pass criteria.
- Existing Foundry `candidate.schema.json`, `skill-spec.schema.json`, `registry-entry.schema.json`.
- Taxonomy quality floor headings for published `SKILL.md` / template.
- `skill-spec.schema.json` `if/then` rule: `EXTEND`/`MODE`/`DEPENDENT_SKILL` require `target_skill_id`.

No new production Skill IDs. No baseline files edited.

## Defects repaired
1. Template `SKILL.md` lacked `## Autonomy` while the quality floor and approved-spec contract require it.
2. `registry-entry.schema.json` was not required and schema validation was skipped when absent (same class of silent-pass defect V1 recorded as P1-6).
3. Missing candidate/spec schemas could crash `validate()` instead of returning FAIL.
4. Published catalog packages were not checked for quality-floor headings, eval-case sections, or manifest schema.
5. Registry `canonical_path` existence was not checked.
6. Negative unit tests accepted any error containing `"candidate"` / `"catalog skill"` and would not distinguish crash, skip, or the intended reason.
7. G4 had no lifecycle templates while G0–G3/G5–G7/G9 did.

## Validation run

Launcher: `py -3`. Dev deps from `requirements-dev.txt` were already present (`jsonschema`, `PyYAML`); reinstalled/confirmed.

### 1. Foundry validator
```
py -3 tools/validate_foundry.py
Skill Foundry validation PASS.
```

### 2. Unit tests
```
py -3 -m unittest tests.test_validate_foundry -v
Ran 10 tests in 12.122s
OK
```

### 3. Baseline suite validator
Unmodified `baseline/agentic-skill-suite-v1/scripts/validate_suite.py` uses locale `read_text()` (no encoding). On this Windows host that is cp1252 and crashes with `UnicodeDecodeError`. Required invocation of the available launcher:

```
py -3 -X utf8 baseline/agentic-skill-suite-v1/scripts/validate_suite.py
Checked 15 skill directories.
All skills pass structural validation (...).
```

Baseline not modified. 15-Skill suite remains intact.

### 4. Negative unit tests — intended reasons (not crash/skip)

**invalid candidate** (`status: BOGUS`, `treatment: WRONG`):
- `candidate 0 invalid: 'BOGUS' is not one of [legal states...]`
- `candidate 0 illegal state: BOGUS`
- `candidate 0 illegal treatment: WRONG`

**malformed approved spec** (valid NEW_SKILL frontmatter, body `# Bad` only):
- `approved spec bad.md missing section: ## Identity` … through `## Explicit out-of-scope` (19 section FAILs including `## Autonomy`)
- spec schema check ran; no skip

**malformed skill package** (`SKILL.md` only):
- `catalog skill bad-skill missing manifest.json`
- `catalog skill bad-skill missing evals`
- `catalog skill bad-skill missing section: ## Autonomy` (and the rest of the quality floor)

Additional targeted FAILs covered by unittest: EXTEND without `target_skill_id`; empty eval cases missing required sections; template Autonomy removed; missing registry/candidate schema reported rather than crash or silent PASS; missing registry `canonical_path`.

## Reconciliation with Antigravity (`origin/main` @ `a757755`)

Inspected after fast-forward of local `agent/cursor` to `origin/agent/cursor` and merge of `origin/main` (already up to date):
- `foundry/handoffs/ANTIGRAVITY_V5_FOUNDATION.md`
- `foundry/analysis/V1_CAPABILITY_COVERAGE.md`
- `foundry/analysis/FOUNDATION_GAP_MAP.md`
- `foundry/analysis/FOUNDRY_LIFECYCLE_AUDIT.md`
- `foundry/analysis/FOUNDRY_EVAL_RESULTS.md`
- `foundry/state/CHECKPOINT.md` (read only; Antigravity-owned)
- Compact registry/taxonomy/ontology (unchanged by Antigravity; still 15 baseline entries, quality floor 13, lifecycle states 1:1 with `ALLOWED_STATES`)

Compatibility verdict: **no contract/template/validator contradiction**. Required code fixes: **none**.

Evidence:
- Registry/taxonomy/ontology were not modified in the Antigravity merge. Cursor still validates `registry-entry.schema.json`, canonical paths, and taxonomy quality-floor headings.
- G7 “19 mandatory sections” matches `SPEC_SECTIONS` in `tools/validate_foundry.py` and `APPROVED_SKILL_SPEC.template.md`.
- G8 remains `catalog/_template/` + `validate_foundry.py`; Cursor’s Autonomy heading, manifest schema, and eval-case checks implement the mechanical package gate Antigravity mapped as `REUSE`.
- G4 gap (distinguish `RESEARCH_SKIPPED` vs investigation) is covered by the existing G4 templates; not a meta-Skill. Aligns with Antigravity’s `REUSE` + skip-reason decision.
- Proposed `sf-genesis-assistant` and `sf-foundry-orchestrator` stay **PROPOSED** only. Not packaged, not self-approved.
- Lifecycle eval cases 01–05 are architecture evidence, not production Skills; validator correctly ignores them as catalog packages.

Re-validation after reconciliation:
- `py -3 tools/validate_foundry.py` → PASS
- `py -3 -m unittest tests.test_validate_foundry -v` → 10 tests OK
- `py -3 -X utf8 baseline/agentic-skill-suite-v1/scripts/validate_suite.py` → 15 Skills PASS

## Unresolved assumptions
- `foundry/state/CHECKPOINT.md` still says Cursor reconciliation is pending the Antigravity merge. That merge is already on `main`. Cursor did not edit the checkpoint (collision rule). Antigravity should refresh it at G10 / next steward pass.
- Running the baseline validator on Windows without UTF-8 mode will still crash inside unmodified V1 `read_text()`. That is a baseline encoding bug; Foundry now always reads UTF-8.
- G4 templates exist for authors but are not in `REQUIRED_CORE`; an empty queue remains valid.
- No `APPROVED_FOR_BUILD` spec and no `catalog/skills/` package exist yet; catalog checks are enforced by tests against cloned fixtures.

## Status
Deterministic V5 substrate reconciled with canonical Antigravity audit. Exact next action: human/GitHub review and merge of `agent/cursor` to `main`.
