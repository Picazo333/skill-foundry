# Cursor × Antigravity — Collaboration Protocol V5

`FOUNDRY_OPERATING_MODEL.md` owns the process. Agent roles are assignments inside G0–G10, not the architecture itself.

## Antigravity — Miner / Architect / Steward / Independent Auditor
Primary write areas:
- `foundry/candidates/`
- `foundry/analysis/`
- `foundry/specs/`
- `foundry/reviews/`
- `foundry/registry/`
- `foundry/taxonomy/`
- `foundry/ontology/`
- `foundry/state/`
- architecture-side handoffs

Primary responsibility:
G0–G7, G9, and canonical stewardship in G10.

## Cursor — Builder / Contract-Eval Implementer / Packager
Primary write areas:
- `catalog/skills/`
- `catalog/_template/`
- `foundry/contracts/`
- `foundry/templates/`
- `tools/`
- `tests/`
- builder-side handoffs

Primary responsibility:
G8 plus deterministic Foundry tooling.

## Human
Primary responsibility:
G6 architecture decision and GitHub merge approvals. Human should not perform mechanical repo work that either agent can safely perform.

## Branches
- `main` = stable canon.
- Cursor = `agent/cursor`.
- Antigravity = `agent/antigravity`.
- Each work unit begins by integrating latest `origin/main` into the agent's own branch.
- No force-push/destructive history rewrite.
- Cross-agent artifacts become canonical only after merge to `main`, except explicit branch-diff audit.

## Collision rule
The non-owner proposes rather than silently edits the other role's canonical area. Antigravity owns `foundry/state/CHECKPOINT.md`; Cursor reports state in builder handoffs.

## Initial bootstrap integration
Both initial missions are independent. Merge Antigravity first. Then Cursor must run `prompts/RECONCILE_CURSOR_AFTER_ANTIGRAVITY.md`, sync the new `main`, rerun Foundry validation/tests and only then become merge-ready.

## Steady-state handoff
1. Antigravity G0–G5 → G6 human.
2. Human decision → Antigravity G7 or closure.
3. Approved spec merged to `main` → Cursor G8.
4. Antigravity G9 audit of Cursor build.
5. REWORK → Cursor correction prompt → G9 again.
6. PASS → implementation merged → Antigravity G10 publish/canon update → final small merge.

Parallelism is allowed only for independent candidates or stages whose dependencies are already canonical.
