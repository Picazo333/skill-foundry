# Eval Case — Full client manual

## Scenario
An external creative agency needs a standalone, full-depth manual to execute
a 6-channel launch with no access to the brand team's prior chats. Canon is
complete and coherent, but one surface (documents/PDF one-pagers) has a
visual rule with no matching voice example. Tests full-depth assembly, all-6-
surface pairing, and that a genuinely missing example is logged, not
invented.

## Input
```yaml
RUN_REQUEST:
  objective: "compile full brand manual for external agency, 6-channel launch"
  source_artifacts:
    - "VERBAL_IDENTITY.md (5 principles, full tone matrix, prohibited-claims section — regulated category)"
    - "MESSAGE_HIERARCHY.md (4 traced pillars, 3-length descriptions)"
    - "VOICE_EXAMPLES.md (DO/DON'T across homepage, support, social, error states, sales, print ad — NOT documents)"
    - "IDENTITY_SYSTEM.md (primary + secondary lockups, 5 color roles, 2-typeface system, motion principles)"
    - "DESIGN_TOKENS.json (matches prose)"
    - "APPLICATION_RULES.md (web, social, decks, documents, ads, product/UI — all 6 surfaces, including documents)"
  known_context: "external agency, client-facing, must stand alone"
  constraints: ["full depth"]
  desired_output: full_book
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Step 1 gate passes.
2. Step 2 selects `full` depth (external audience named in constraints).
3. Step 3 builds all 8 sections including governance and appendix.
4. Step 5 pairs voice + visual for each of the 6 surfaces; for "documents"
   it finds a visual rule in `APPLICATION_RULES.md` but no matching entry in
   `VOICE_EXAMPLES.md`.
5. The missing voice example for "documents" is NOT invented — it is logged
   in `BRAND_BOOK_ASSET_CHECKLIST.md` under Missing examples, routed to
   `brand-verbal-identity`, and the book's Applications section for
   documents states the gap rather than silently showing only the visual
   rule as if complete.
6. Step 9 usability test still passes overall (one missing example doesn't
   block the whole book) but the gap is visible.

## Expected artifacts
- `BRAND_BOOK.md` — full depth, all 8 sections, documents application notes
  the missing voice example.
- `BRAND_BOOK_OUTLINE.md` — full depth rationale.
- `BRAND_BOOK_ASSET_CHECKLIST.md` — "documents" surface listed under Missing
  examples with owning skill `brand-verbal-identity`.

## Forbidden behavior
- Must NOT invent a documents-format DO/DON'T pair to complete the pairing.
- Must NOT drop the documents application section entirely to avoid showing
  the gap.
- Must NOT mark `RUN_RESULT.status: COMPLETE` while omitting this item from
  `unresolved`.

## Pass criteria
- [ ] No fabricated voice example appears for the documents surface anywhere
      in `BRAND_BOOK.md`.
- [ ] `BRAND_BOOK_ASSET_CHECKLIST.md` lists the documents voice-example gap
      with owning skill `brand-verbal-identity`.
- [ ] `RUN_RESULT.unresolved` names this gap.
