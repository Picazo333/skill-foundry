# AFTER G6 HUMAN DECISION — ANTIGRAVITY

Apply the human's immediately preceding decision to the active candidate. If more than one candidate is in `AWAITING_HUMAN_DECISION` and the decision does not uniquely identify one, ask only for the candidate ID.

1. Record the decision exactly in the candidate `DECISION.md`; do not infer approval for omitted items.
2. If `RESEARCH_MORE` or `CORRECT`, return to the appropriate earlier gate, update artifacts, and return to G6.
3. If `REJECT`, mark `REJECTED`, update checkpoint, commit/push and close without build.
4. If approved outcome is only `REUSE` and/or `NO_SKILL`, mark `CLOSED_REUSE` / `CLOSED_NO_SKILL`, document exact existing Skill/utility usage, update checkpoint, commit/push and close. Do not manufacture a spec.
5. For each approved `EXTEND`, `MODE`, `DEPENDENT_SKILL` or `NEW_SKILL`, run G7 and create `foundry/specs/<skill_id>.md` using the approved spec template/frontmatter.
6. Re-run overlap reasoning after any human scope change.
7. Validate specs mechanically where possible, commit/push, and end `READY_FOR_REVIEW` with exact specs Cursor may build after merge to `main`.
