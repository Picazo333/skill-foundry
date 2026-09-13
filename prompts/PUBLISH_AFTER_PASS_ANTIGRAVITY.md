# G10 — PUBLISH AFTER PASS — ANTIGRAVITY

Run only after the G9 audit verdict is `PASS` **and the passed Cursor implementation has been merged to `main`**.

1. Sync `agent/antigravity` from latest `origin/main` and verify the passed implementation exists there.
2. Update `foundry/registry/SKILL_REGISTRY.yaml` for the published Skill/change without duplicate IDs.
3. Update taxonomy/ontology only if the published capability introduces a genuinely necessary new classification concept.
4. Update routing/handoff data and integration evals only where the catalog graph materially changed.
5. Record candidate final state `PUBLISHED`, version/provenance and exact canonical path.
6. Update `foundry/state/CHECKPOINT.md` with completed work and next exact action.
7. Run Foundry validator and baseline validator; repair any canonical consistency defect.
8. Commit/push the small G10 canon update.
9. End `READY_FOR_MERGE`. After human merge, the cycle is complete and the new published capability becomes baseline evidence for future overlap analysis.
