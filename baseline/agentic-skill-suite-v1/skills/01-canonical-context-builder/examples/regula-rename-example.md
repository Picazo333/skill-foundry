# Worked example — multi-rename project

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "rebuild canon from scratch after project went through 3 names and 2 pivots"
  source_artifacts:
    - "chat_2024-01_initial_pitch.txt (project called 'Regula', compliance-tracking angle)"
    - "chat_2024-03_pivot_note.txt (renamed to 'Ledgerly', pivots to bookkeeping angle)"
    - "signed_brief_2024-05.pdf (final name 'Ledgerly', bookkeeping + compliance combined, APPROVED)"
    - "chat_2024-06_random_aside.txt (someone floats going back to compliance-only, never followed up)"
  known_context: null
  constraints: ["brand-only scope, no technical architecture"]
  desired_output: full_canon_set
  mode: STANDARD
  prior_run: null
```

## Output (abridged)

**PROJECT_CANON.md** (excerpt):
```
## FACTS
- Current project name is "Ledgerly" — source: signed_brief_2024-05.pdf (highest authority, most recent)
- Product combines bookkeeping and compliance tracking — source: signed_brief_2024-05.pdf

## LOCKED DECISIONS
- Name is "Ledgerly", not "Regula" or an earlier working name — locked 2024-05, source: signed_brief_2024-05.pdf

## OPEN LOOPS
- chat_2024-06 raised reverting to compliance-only positioning but no decision was made — see OPEN_LOOPS.md

## DEPRECATED
- "Regula" (original name, compliance-only angle) — superseded by "Ledgerly" bookkeeping+compliance combo, see DEPRECATED_REGISTER.md
```

**DEPRECATED_REGISTER.md** (excerpt):
```
| "Regula" name + compliance-only angle | superseded by "Ledgerly" combined angle per signed_brief_2024-05.pdf | chat_2024-01_initial_pitch.txt | 2024-01 |
```

**OPEN_LOOPS.md** (excerpt):
```
| Should compliance-only positioning be reconsidered? | question | chat_2024-06 raised it, no follow-up | no | needs a stakeholder decision, not inferable from sources |
```

Note what did NOT happen: the skill did not decide whether the 2024-06 aside
should override the approved brief — that is exactly the kind of conflict
that goes to `OPEN_LOOPS.md`, not to an inferred resolution.
