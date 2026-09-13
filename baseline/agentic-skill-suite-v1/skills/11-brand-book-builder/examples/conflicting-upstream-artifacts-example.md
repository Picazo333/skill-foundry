# Worked example — brand book with conflicting upstream artifacts

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "compile operational brand book"
  source_artifacts:
    - "VERBAL_IDENTITY.md (principle: 'we are the calm, expert friend' — audience explicitly stated as risk-averse, first-time buyers seeking reassurance)"
    - "MESSAGE_HIERARCHY.md (master message: 'buying your first home without the panic')"
    - "VOICE_EXAMPLES.md (DO/DON'T consistent with calm/reassuring tone)"
    - "IDENTITY_SYSTEM.md (color system built around high-saturation red/black, typography described in the artifact's own rationale as 'urgent, high-energy, built for a fast-moving audience that wants excitement, not hand-holding')"
    - "DESIGN_TOKENS.json (matches IDENTITY_SYSTEM.md prose)"
    - "APPLICATION_RULES.md (ad templates built around countdown/urgency motifs: 'act now', flashing accent color on CTAs)"
  known_context: null
  constraints: []
  desired_output: full_book
  mode: STANDARD
  prior_run: null
```

## Output (abridged)

**BRAND_BOOK.md** (excerpt, section 6, Governance):
```
## 6. Governance
Flagged coherence gaps:
- VERBAL_IDENTITY.md's audience (risk-averse, first-time buyers wanting
  reassurance) and stated principle ("the calm, expert friend") directly
  conflict with IDENTITY_SYSTEM.md's own stated rationale (urgent,
  high-energy visual system "for a fast-moving audience that wants
  excitement, not hand-holding") and APPLICATION_RULES.md's urgency/
  countdown ad motifs. These describe two different audiences and two
  different emotional registers, not one brand.
- This book is compiled with both sides shown as-is (see sections 3 and 4)
  because this skill does not resolve upstream positioning conflicts. A
  designer/writer executing from this book as written would produce
  materially inconsistent output depending on which section they read.
```

**RUN_RESULT** (abridged):
```yaml
RUN_RESULT:
  status: PARTIAL
  summary: "Brand book compiled; voice and visual canon describe two
    different audiences/registers — flagged, not resolved."
  artifacts: [BRAND_BOOK.md, BRAND_BOOK_OUTLINE.md, BRAND_BOOK_ASSET_CHECKLIST.md]
  decisions: ["depth: operational", "both conflicting sections compiled as-is per source, neither edited to match the other"]
  unresolved:
    - "Audience/register conflict between VERBAL_IDENTITY.md (calm,
       reassuring, risk-averse first-time buyers) and IDENTITY_SYSTEM.md +
       APPLICATION_RULES.md (urgent, high-energy, excitement-seeking
       audience) — needs resolution from brand-verbal-identity and/or
       brand-identity-system, likely against BRAND_STRATEGY.md if one exists."
  handoff:
    next_skill: "brand-identity-system"
    reason: "Visual system's own stated rationale conflicts with the
      audience in the locked verbal canon; recommend re-checking the visual
      direction against BRAND_STRATEGY.md before treating this book as
      execution-ready."
  quality:
    all_rules_traced_to_source: true
    no_unflagged_contradictions: true
    coherence_check_run: true
    asset_checklist_complete: true
    usability_test_passed: false
```

Note what did NOT happen: the skill did not soften "urgent, high-energy" in
`IDENTITY_SYSTEM.md`'s rationale to sound less contradictory, did not drop
the reassuring tone from `VERBAL_IDENTITY.md` to make the two sides agree,
and did not pick one side as "the real brand." The usability test in step 9
is correctly marked failed — a book that would produce inconsistent output
depending on which section a reader followed is not yet execution-ready,
and that is reported honestly rather than marked COMPLETE.
