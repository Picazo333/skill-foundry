# Eval Case — Compact startup brand book

## Scenario
A 10-person startup has locked, complete verbal and visual canon but only 3
production surfaces (web, product/UI, deck) and no social/print presence
yet. The founder wants a small, investor-deck-appendix-ready book, not a
full agency manual. Tests that depth selection actually changes what's
included, not just a label.

## Input
```yaml
RUN_REQUEST:
  objective: "compile executive-depth brand book for founder deck / investor use"
  source_artifacts:
    - "VERBAL_IDENTITY.md (3 traced principles, DO/DON'T present)"
    - "MESSAGE_HIERARCHY.md (master message, 2 traced pillars)"
    - "VOICE_EXAMPLES.md (DO/DON'T across support, social, product/UI, sales)"
    - "IDENTITY_SYSTEM.md (wordmark only, 2 core colors with contrast behavior, 1 typeface)"
    - "DESIGN_TOKENS.json (matches IDENTITY_SYSTEM.md)"
    - "APPLICATION_RULES.md (web, product/UI, deck only — 3 surfaces)"
  known_context: "10-person startup, founder + one design contractor"
  constraints: ["executive depth only", "no governance section needed"]
  desired_output: full_book
  mode: QUICK
  prior_run: null
```

## Expected behavior
1. Step 1 gate passes — all 6 artifacts present and sufficient.
2. Step 2 selects `executive` depth (mode: QUICK plus explicit constraint).
3. Step 3 builds essence/strategy/voice-snapshot/visual-snapshot/1-page
   do-don't only — no governance section, no appendix token table.
4. Step 5 pairs applications only for the 3 surfaces `APPLICATION_RULES.md`
   actually covers — does not invent a social or print application section
   to look more complete.
5. Step 6 coherence check runs and is recorded even though no gap is found.
6. `BRAND_BOOK_OUTLINE.md` states why governance/appendix were excluded
   (constraint + depth, not "forgot").

## Expected artifacts
- `BRAND_BOOK.md` — executive depth, 5 sections only, no governance/appendix.
- `BRAND_BOOK_OUTLINE.md` — explicit depth rationale and excluded-sections list.
- `BRAND_BOOK_ASSET_CHECKLIST.md` — coherence-check-run-no-gaps-found stated
  explicitly; no fabricated missing-surface entries for social/print (they
  were never in scope, not "missing").

## Forbidden behavior
- Must NOT add a social or print application section since none exists in
  `APPLICATION_RULES.md`.
- Must NOT add a full governance section despite it existing in the template
  — the constraint explicitly excludes it.
- Must NOT omit stating that the coherence check ran, even though it found
  nothing.

## Pass criteria
- [ ] `BRAND_BOOK.md` contains no governance or appendix section.
- [ ] Applications section covers exactly the 3 surfaces in
      `APPLICATION_RULES.md`, no more.
- [ ] `BRAND_BOOK_OUTLINE.md` explains the depth choice and each excluded
      section.
- [ ] `RUN_RESULT.quality.coherence_check_run` is `true`.
