# G9 — INDEPENDENT AUDIT OF CURSOR BUILD

Audit the specified Cursor branch/commit against its approved spec.

1. Sync `agent/antigravity` from latest `origin/main`; fetch the Cursor branch/commit read-only.
2. Inspect diff + built artifacts.
3. Audit spec compliance, package structure, eval quality, portability, token/context discipline, handoffs/shared contracts, compatibility for EXTEND/MODE, overlap regression and scope creep.
4. Run available validators/evals relevant to the build.
5. Write `foundry/reviews/<skill_id>_AUDIT.md`.
6. Verdict exactly `PASS` or `REWORK`.
7. Every REWORK defect gets a concrete acceptance criterion; do not redesign the Skill silently.
8. Commit/push audit on `agent/antigravity`.
9. End with exact verdict and next action: REWORK → Cursor correction prompt; PASS → human may merge the passed Cursor implementation, then run publish prompt.
