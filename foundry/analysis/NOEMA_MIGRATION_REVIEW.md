# Noema migration review — Skill Foundry

**Status:** HOLD FOR HUMAN REVIEW — do not merge automatically  
**Baseline:** `42fe23e5645facb1e132bbc2f9addfde49393e2e`  
**Migration branch:** `migration/noema-rc0`

## Outcome
Skill Foundry is Noema-conformant on the migration branch without transferring Foundry-domain authority into Noema.

## Before / after context measurement
Metric: **Noema Context Units v1** (`characters / 4`). Dynamic current task/handoff/candidate content is excluded on both sides.

### Before
The pre-migration agent entry rules universally required:
`AGENTS.md + FOUNDRY_CANON.md + FOUNDRY_OPERATING_MODEL.md + COLLABORATION_PROTOCOL.md`.

- static baseline: **4 files / 21,796 chars / ~5,449 NCU**
- architecture/overlap baseline after Registry + Taxonomy + Ontology: **7 files / 29,548 chars / ~7,387 NCU**

### After, by mode
| Mode | Cold-start files | Chars | NCU | Change vs old static baseline |
|---|---:|---:|---:|---:|
| recover | 3 | 5,710 | 1,428 | **-73.8%** |
| patch | 3 | 12,971 | 3,243 | **-40.5%** |
| build | 3 | 12,971 | 3,243 | **-40.5%** |
| audit | 3 | 12,971 | 3,243 | **-40.5%** |
| research | 3 | 12,971 | 3,243 | **-40.5%** |
| architect | 7 | 30,489 | 7,623 | **+3.2% vs old architecture set** |

The architect mode deliberately pays full architecture context only when architecture is actually requested. Ordinary work no longer pays that cost.

## Domain-authority integrity check
The following files have identical blob SHA on baseline and migration branch:

- `FOUNDRY_CANON.md` → `f72e2eba22706c0df2b704455a9c1ad91a6e6d07`
- `foundry/taxonomy/TAXONOMY.yaml` → `8b16ad655669f627315f0ef367b7fbd848ccdd12`
- `foundry/ontology/ONTOLOGY.yaml` → `621650353de50da7e47e49b63436ccc22c735413`
- `foundry/registry/SKILL_REGISTRY.yaml` → `a489eaa09ee98088d24c942c62e8e524a12f30ff`
- `foundry/workflows/SF-WF-001_SKILL_GENESIS.md` → `f96692fc183f5f63bf32fd117dfae81ea18374a1`
- `foundry/workflows/SF-WF-002_BOOTSTRAP_V5.md` → `b48161f90a00806373fbfa83f6a010f27d689105`
- `tools/validate_foundry.py` → `dade4d1e95a71811324a6793ea0c57a59a8be18d`
- `tests/test_validate_foundry.py` → `99bca7ec85004e412536c8684d762e2130e99d98`

No taxonomy, ontology, registry, workflow, validator, test or V1 baseline content moved.

## Changes that did occur
1. Added `noema.project.yaml` as repository governance/context manifest.
2. Reduced `AGENTS.md` to an entry map instead of a mandatory architecture preload.
3. Reduced Cursor/Antigravity rules to thin platform adapters that delegate static context routing to Noema.
4. Changed only the **Context discipline** section of `FOUNDRY_OPERATING_MODEL.md` so repository cold-start is not duplicated there; Foundry process authority remains explicit.
5. Refreshed stale `foundry/state/CHECKPOINT.md` to reflect that both V5 foundation branches were already merged and this migration is awaiting review.
6. Marked `00_START_HERE.md` and `EXECUTE_THIS.md` as historical bootstrap/provenance instead of current agent state; neither was deleted.
7. Added immutable Noema conformance CI and separate Foundry-native validation CI.
8. Added the pre-migration baseline and this review evidence.

## Adversarial finding during migration
The first Noema run **correctly failed** because the migration initially invented:
- project type `agentic-capability-foundry`;
- traits `multi-agent`, `eval-backed`, and `portable`.

Noema's composition registry already had the appropriate `agentic-capability-library` profile. The migration was corrected to:
- `type: library`;
- traits `agentic`, `reusable`, `research-heavy`, `human-gated`;
- existing quality claims including capability trigger accuracy and portability.

**Decision:** reuse protocol vocabulary; do not expand Noema for one consumer.

## CI evidence
On migration commit `ea0f3eb49e54aa93ae2c2a8ee51b90602ed29e75`:
- Noema Conformance run `35294543837` → **PASS**
- Skill Foundry Validation run `35294543219` → **PASS**
  - Foundry validator → PASS
  - 10 unit tests → PASS
  - immutable V1 15-Skill baseline validator → PASS

Noema PASS remains separate from Foundry quality/eval PASS.

## Remaining observations
- The architect mode is slightly larger than the old architecture preload because it now includes the explicit Noema manifest. This is accepted because only architecture tasks pay it.
- Dynamic candidate/spec/handoff context is intentionally not encoded as static Noema paths; the current task selects those artifacts after the stable mode context loads.
- Historical bootstrap docs remain in place to preserve provenance. They are no longer startup authority.
- Agency Foundation was not touched.

## Merge recommendation
Technically **merge-ready**, but intentionally held for human inspection.

Merge only if the reviewer agrees that:
1. the ~74% recovery and ~40% ordinary-mode context reductions justify the governance additions;
2. explicit architecture mode paying ~3% extra is acceptable;
3. Foundry authority boundaries are unchanged;
4. the new CI workflows should remain permanent.
