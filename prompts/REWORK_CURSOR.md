# G8 REWORK — CURSOR

An independent audit returned `REWORK` for an approved build.

1. Sync `agent/cursor` from latest `origin/main` and fetch/read the cited audit.
2. Fix **only** the listed defects plus directly necessary consequences; do not redesign or expand scope.
3. Satisfy every acceptance criterion explicitly.
4. Rerun Skill evals, structural checks and `tools/validate_foundry.py`.
5. Update builder handoff with defect→fix→evidence mapping.
6. Commit/push.
7. End `BUILD_COMPLETE` and request a new independent G9 audit. Do not self-declare PASS.
