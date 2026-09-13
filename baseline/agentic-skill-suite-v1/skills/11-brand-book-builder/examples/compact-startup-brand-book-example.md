# Worked example — compact startup brand book (executive depth)

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "compile executive-depth brand book for founder deck / investor use"
  source_artifacts:
    - "VERBAL_IDENTITY.md (3 principles: 'name the number, skip the adjective'; 'answer before pleasantry'; 'never apologize for being small'; all traced, all with DO/DON'T)"
    - "MESSAGE_HIERARCHY.md (master message: 'the bookkeeping tool that never guesses'; 2 pillars, both traced)"
    - "VOICE_EXAMPLES.md (DO/DON'T across support, social, product/UI, sales)"
    - "IDENTITY_SYSTEM.md (single wordmark, no separate icon; 2 core colors with contrast behavior defined; 1 typeface family, 2 weights)"
    - "DESIGN_TOKENS.json (matches IDENTITY_SYSTEM.md prose)"
    - "APPLICATION_RULES.md (web, product/UI, deck only — 3 surfaces, startup has no print/social presence yet)"
  known_context: "10-person startup, book is for founder + design contractor, not external agency"
  constraints: ["executive depth only", "must fit a single deck appendix, no governance section needed"]
  desired_output: full_book
  mode: QUICK
  prior_run: null
```

## Output (abridged)

**BRAND_BOOK_OUTLINE.md** (excerpt):
```
Depth chosen: executive (mode: QUICK, explicit constraint)
Sections included: Essence, Strategy snapshot, Voice snapshot, Visual
snapshot, 1-page do/don't.
Excluded: Governance (constraint: "no governance section needed" — a
10-person startup doesn't need versioning/ownership process yet), Appendix
token table (executive depth doesn't require it; full DESIGN_TOKENS.json
still delivered as BRAND_BOOK_ASSET_CHECKLIST.md notes if a contractor needs
it later).
```

**BRAND_BOOK.md** (excerpt):
```
## 3. Voice snapshot [CANON]
Principles: "Name the number, skip the adjective" · "Answer before
pleasantry" · "Never apologize for being small"
Elevator pitch: "The bookkeeping tool that never guesses."

## 4. Visual snapshot [CANON]
Wordmark only, no icon mark. Two core colors (primary, accent) with defined
contrast pairs. One typeface, two weights (regular, bold) — no italic
defined.

## 5. 1-page do/don't
Voice — DO: "Yes, refunds land in 3-5 business days." DON'T: "Thanks so much
for reaching out! We'd be happy to help..."
Visual — DO: primary color on white background only (contrast-checked).
DON'T: accent-on-accent text (fails the defined contrast pair).
```

**BRAND_BOOK_ASSET_CHECKLIST.md** (excerpt):
```
## Coherence gaps
Coherence check run per SKILL.md step 6; no gaps found — voice (direct,
plainspoken, small-and-proud) and visual (minimal, two colors, one typeface)
read as one brand.

## Thin/underspecified upstream artifacts
None — all 6 source artifacts were sufficiently complete for executive
depth.
```

Note what did NOT happen: the skill did not add a governance section despite
`full`/`operational`-depth templates having one — the constraint explicitly
excluded it, and the outline records why. It also did not pad the book with
a social-media application section — APPLICATION_RULES.md only covers 3
surfaces because the startup doesn't have a social presence yet, and no
surface was invented to look more complete.
