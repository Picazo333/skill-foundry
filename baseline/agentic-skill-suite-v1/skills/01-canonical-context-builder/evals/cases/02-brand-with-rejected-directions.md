# Eval Case — Brand project with rejected visual directions

## Scenario
A brand project explored 3 visual directions; 2 were explicitly rejected by
the stakeholder in review notes, 1 was approved. Tests that rejected
creative work is preserved (for institutional memory / avoiding re-pitching
the same rejected idea) but never presented as live or current.

## Input
```yaml
RUN_REQUEST:
  objective: "build canon after visual direction review"
  source_artifacts:
    - "visual_direction_brief.md (3 directions: Minimal, Bold, Playful)"
    - "review_notes.md (Minimal: rejected — 'too generic'; Bold: APPROVED; Playful: rejected — 'off-brand tone')"
  known_context: null
  constraints: ["brand-only scope"]
  desired_output: full_canon_set
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Only "Bold" appears in LOCKED DECISIONS as the current visual direction.
2. "Minimal" and "Playful" both appear in `DEPRECATED_REGISTER.md`, each with
   its stated rejection reason preserved verbatim/near-verbatim.
3. No fabricated reasoning is added beyond what the review notes stated.

## Expected artifacts
- `PROJECT_CANON.md` — LOCKED DECISIONS: visual direction = Bold only.
- `DEPRECATED_REGISTER.md` — Minimal ("too generic") and Playful ("off-brand
  tone"), each with source = review_notes.md.

## Forbidden behavior
- Must not merge or blend the rejected directions into the current one.
- Must not invent a rejection reason beyond what review_notes.md states.
- Must not leave Minimal/Playful unmentioned (silent loss of why they were
  rejected would let someone re-pitch them later).

## Pass criteria
- [ ] Exactly one visual direction is current in canon.
- [ ] Both rejected directions are in `DEPRECATED_REGISTER.md` with their
      real stated reasons.
- [ ] No invented rationale appears anywhere.
