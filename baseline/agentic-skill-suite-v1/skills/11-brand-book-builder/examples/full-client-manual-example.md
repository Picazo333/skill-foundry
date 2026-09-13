# Worked example — full client-facing brand manual

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "compile full brand manual for external agency to execute a 6-channel launch campaign"
  source_artifacts:
    - "VERBAL_IDENTITY.md (5 principles, full tone modulation matrix across 6 contexts, prohibited-claims section present — category is financial services)"
    - "MESSAGE_HIERARCHY.md (master message, 4 pillars, 3-length descriptions, 3 tagline territories)"
    - "VOICE_EXAMPLES.md (DO/DON'T across 6 formats: homepage, support, social, error states, sales, print ad)"
    - "IDENTITY_SYSTEM.md (primary + secondary logo lockups, 5 color roles with contrast behavior, 2-typeface system with fallback stack, grid/spacing rules, motion principles for UI)"
    - "DESIGN_TOKENS.json (matches prose, includes contrast ratios)"
    - "APPLICATION_RULES.md (web, social, decks, documents, ads, product/UI — all 6 surfaces, exceptions documented for co-branded partner placements)"
  known_context: "external creative agency, client-facing deliverable, governed rollout across 6 channels"
  constraints: ["full depth", "must stand alone for an agency team who never spoke to the brand team"]
  desired_output: full_book
  mode: STANDARD
  prior_run: null
```

## Output (abridged)

**BRAND_BOOK_OUTLINE.md** (excerpt):
```
Depth chosen: full (constraint: external agency audience).
All 8 sections included: Essence, Strategy snapshot, Voice (full),
Visual system (full), Applications (all 6 surfaces paired), Governance
(full — versioning, exceptions, forbidden combinations, change-request
process), Appendix (full DESIGN_TOKENS.json table + prohibited-claims
glossary).
```

**BRAND_BOOK.md** (excerpt, section 5, one surface):
```
### Social
- Visual rule: secondary lockup only below 400px width; accent color capped
  at 20% of frame area — source: APPLICATION_RULES.md
- Voice DO/DON'T: DO "Rates you can actually read before you sign anything."
  DON'T "Transparent, competitive rates you can trust!" — source:
  VOICE_EXAMPLES.md
```

**BRAND_BOOK.md** (excerpt, section 6, Governance):
```
## 6. Governance
Exceptions: co-branded partner placements may substitute partner's
secondary color in the accent role only, primary color and wordmark remain
fixed — source: IDENTITY_SYSTEM.md.
Flagged coherence gaps: Coherence check run per SKILL.md step 6; no gaps
found.
Change-request process: changes to any [CANON] rule route back to
brand-verbal-identity or brand-identity-system, not edited in this book.
```

**BRAND_BOOK_ASSET_CHECKLIST.md** (excerpt):
```
## Missing examples
| Surface | What's missing | Referenced in | Should come from |
|---|---|---|---|
| Documents (PDF one-pagers) | APPLICATION_RULES.md defines the visual rule but VOICE_EXAMPLES.md has no document-format example (only homepage/support/social/error/sales/print-ad) | 5. Applications | brand-verbal-identity |
```

Note what did NOT happen: the missing document-format voice example was not
invented to complete the pairing — it was logged in the asset checklist and
routed back to `brand-verbal-identity`, and section 5 states the gap
explicitly rather than silently showing only the visual rule as if it were
complete.
