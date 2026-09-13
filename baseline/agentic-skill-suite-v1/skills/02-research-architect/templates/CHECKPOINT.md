# CHECKPOINT — <project name>
_Written: <date/time> · Mode: <STANDARD | AUTONOMOUS | UPDATE>_

```yaml
phase: <0-Brief | 1-Domain-Discovery | 2-Scope-Expansion | 3-Domain-Polishing | 4-Final-QA | Packaged>
completed:
  - <block completed, e.g. "Phase 1: domain map + weighting locked">
partially_completed:
  - <in-progress block, e.g. "Phase 2: 87/150 scope-expansion iterations">
files_created:
  - <artifact paths written so far>
tests_passed: []          # applicable QA passes completed, by number/name
tests_failed: []          # QA passes that failed and were fixed, or remain open
known_issues:
  - <e.g. "Domain 4 still below weighted iteration allocation">
decisions_locked:
  - <weighting/scoping decisions that should not be re-derived on resume>
next_exact_action: "<precise next step, e.g. 'continue scope-expansion at iteration 88, Domain 4 (Distribution)'>"
resume_command: "Resume research-architect with RUN_REQUEST.mode: <mode>, prior_run: CHECKPOINT.md"
```

## Iteration counts at this checkpoint
- Scope-expansion valid: <N> / 150
- Domain-polishing valid: <N> / 50
- Discarded (no material delta): <N>

## Coverage Debt snapshot
- Open: <N> domains — see `COVERAGE_DEBT.md`

## Resume instructions
On resume, load this file plus `DOMAIN_MAP.md`, `MASTER_RESEARCH_PROGRAM.md`,
`COVERAGE_DEBT.md`, and `GAP_LEDGER.md` — do not re-derive iterations already
counted above, and do not re-run the material-delta test against them.
