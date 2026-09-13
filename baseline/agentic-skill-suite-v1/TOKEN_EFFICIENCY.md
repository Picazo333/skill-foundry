# TOKEN EFFICIENCY & AUTONOMY

## Goal
Maximize useful output per token without lowering quality.

## Rules
1. Plan once, then execute without mechanical confirmation prompts.
2. Use canonical artifacts instead of full transcripts.
3. Load context progressively.
4. Centralize shared policies instead of duplicating them across 15 skills.
5. Use structured artifact handoffs.
6. Update by delta when a stable canonical artifact already exists.
7. Checkpoint after every phase and every 2–3 skills.
8. Resume from checkpoints without re-deriving completed work.
9. Separate architecture from execution.
10. Separate audit from implementation.
11. Build orchestrators last.
12. Run narrow evals incrementally.
13. Retry only failed components.
14. Never maintain five divergent platform implementations.
15. Keep logs compact: decisions, deltas, failures, next action.

## Autonomous execution
After Claude creates `EXECUTION_PLAN.md`, it must continue automatically. It must not ask the user to approve each phase or say “continue?”. Stop only on a genuine blocker that cannot be resolved locally.

## Checkpoint contract
Keep `CHECKPOINT.md` compact and recovery-oriented:
```yaml
phase:
completed:
partially_completed:
files_created:
tests_passed:
tests_failed:
known_issues:
decisions_locked:
next_exact_action:
resume_command:
```
