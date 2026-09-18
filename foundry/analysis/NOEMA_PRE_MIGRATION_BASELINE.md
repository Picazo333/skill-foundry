# Noema pre-migration baseline — Skill Foundry

**Baseline commit:** `42fe23e5645facb1e132bbc2f9addfde49393e2e`  
**Purpose:** freeze measurable repository behavior before Noema governance is introduced.

## Authority baseline
Skill Foundry already owns and must continue to own:
- `FOUNDRY_CANON.md` and `FOUNDRY_OPERATING_MODEL.md`;
- taxonomy and ontology;
- Skill Registry;
- G0–G10 lifecycle/workflows;
- Foundry contracts and evals;
- candidate state, handoffs and published Skill packages;
- immutable V1 baseline precedent.

Noema must not absorb or duplicate these authorities.

## Cold-start baseline
The pre-migration `AGENTS.md` required every Foundry agent to read, before ordinary work:
1. `AGENTS.md`
2. `FOUNDRY_CANON.md`
3. `FOUNDRY_OPERATING_MODEL.md`
4. `COLLABORATION_PROTOCOL.md`

Measured with Noema Context Units v1 (`characters / 4`):
- static mandatory set: **4 files / 21,796 characters / ~5,449 NCU**;
- normal architecture/overlap work after adding Registry + Taxonomy + Ontology: **7 files / 29,548 characters / ~7,387 NCU**.

Both exclude the current task/handoff, candidate artifacts and any relevant baseline Skill, so real task startup is higher.

## Duplicate startup authority
Three platform-facing entry surfaces independently instructed agents to preload Canon/Operating Model:
- `AGENTS.md`;
- `.agents/rules/skill-foundry.md`;
- `.cursor/rules/skill-foundry.mdc`.

This creates instruction duplication and drift risk.

## Recovery drift found before migration
`foundry/state/CHECKPOINT.md` still stated that Cursor reconciliation was pending even though the reconciled Cursor foundation had already been merged to `main`. This confirms that checkpoint/state is a derived projection, not Git authority.

## Legacy bootstrap drift
`00_START_HERE.md` and `EXECUTE_THIS.md` still describe creating/cloning the repository from zero. They remain useful provenance/reinstallation documents but are not valid current agent startup state.

## Acceptance criteria for migration
The migration is acceptable only if:
- Noema conformance passes;
- existing Foundry validator/tests and V1 baseline validation still pass;
- Canon, taxonomy, ontology, registry, workflows, contracts, evals and baseline remain semantically unchanged;
- default recovery cold-start is materially below the pre-migration static baseline;
- architecture mode may be large when necessary, but ordinary modes stop preloading architecture context;
- no new runtime/service/database is introduced;
- the branch remains reviewable before merge.
