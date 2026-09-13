# DOMAIN MAP — <project name>
_Built: <date> · Built by: research-architect v1.0.0_

Weighted, interconnected canonical domain map. Every domain must have at
least one explicit link to another domain (see `SKILL.md` Phase 1 step 4) —
a domain with no `Interconnects with` entries fails the interconnection gate.

## Weighting method
Each domain scored 1-5 on: **importance** (to the master decision),
**uncertainty** (how unknown), **complexity**, **risk/decisions affected**.
Weight = sum (not average) — higher weight drives proportionally more
Phase 2 iterations. See `references/key-area-weighting-and-qa-checklist.md`.

## Domains

### <Domain 1 name> — weight: <N>/20
- Importance: <1-5> · Uncertainty: <1-5> · Complexity: <1-5> · Risk: <1-5>
- Lens type: <universal | domain-native>
- Scope (in): <what this domain covers>
- Scope (out): <explicit boundary, set during Phase 3 polishing>
- Interconnects with: <Domain X> (via <shared variable/decision>), <Domain Y>
- Scope-expansion iterations allocated: <N> (of 150+ total)
- Workflow/automation-AI lens applied: <yes/no + iteration ref, if this domain touches an operational/delivery workflow>

### <Domain 2 name> — weight: <N>/20
...

## Weight → allocation check
| Domain | Weight | Iterations allocated | Proportional? |
|---|---|---|---|
| <Domain 1> | <N> | <N> | <yes/no + note if not> |

Blind equal distribution across domains regardless of weight is a defect —
flag and correct before Phase 2 closes.
