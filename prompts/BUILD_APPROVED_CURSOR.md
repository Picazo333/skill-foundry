# G8 — BUILD APPROVED SPECS — CURSOR

1. Sync `agent/cursor` from latest `origin/main`.
2. Inspect `foundry/specs/` for explicitly `APPROVED_FOR_BUILD` items in scope.
3. For each, implement exactly the approved `change_kind` and boundaries.
4. Reuse V1/shared contracts and `catalog/_template/`; do not clone boilerplate blindly.
5. Produce canonical `SKILL.md`, manifest, only useful schemas/templates/references/examples/adapters, and required evals.
6. For EXTEND/MODE, preserve compatibility/migration constraints from spec; do not silently fork a duplicate Skill.
7. Run relevant structural/behavioral checks plus `tools/validate_foundry.py`.
8. Repair failures autonomously.
9. Create/update builder handoff with exact artifacts, tests, results and any blocker.
10. Commit/push `agent/cursor`; end `BUILD_COMPLETE` only when spec + eval + validation requirements are satisfied.

Do not redesign approved architecture or add unapproved Skills.
