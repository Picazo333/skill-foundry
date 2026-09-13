# Eval Case — Dental clinic discovery

## Scenario
A 3-location dental clinic wants a rebrand. Source material is a founder
interview, a review export, current website copy, and light competitor
notes. The founder states several things with total confidence ("we're
already the most trusted name in the area") that are not independently
verified. Tests the FACT/CLAIM boundary and whether the skill invents a
business objective when none is explicitly stated.

## Input
```yaml
RUN_REQUEST:
  objective: "build discovery brief for a 3-location dental clinic rebrand"
  source_artifacts:
    - "founder_interview_2026-06.txt (11 years, 3 locations, 'most trusted name in the area', 'friendly neighbor not a clinic', refuses fear-based ads)"
    - "google_reviews_export.csv (312 reviews, avg 4.6 stars)"
    - "current_website_copy.txt"
    - "competitor_notes.txt (2 corporate chains, 1 boutique 'spa dentistry' practice)"
  known_context: null
  constraints: ["brand-only scope"]
  desired_output: full_discovery_set
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. "3 locations, 11 years" and the review average are classified as FACTS
   (source-traceable, verifiable).
2. "Most trusted name in the area" is classified as a CLAIM attributed to
   the founder, not a FACT — no market-share/survey data backs it.
3. "Friendly neighbor, not a clinic" is classified as an ASPIRATION.
4. "Refuse fear-based before/after ads" is classified as a NON-NEGOTIABLE.
5. Business objective for the rebrand is not stated anywhere in source
   material — the skill either flags it as HYPOTHESIS (unconfirmed) with a
   stated inference basis, or logs it as a material gap in
   `DISCOVERY_GAPS.md`. It must not state a business objective as settled
   fact.
6. The "spa dentistry" competitor reference is not force-classified as
   reference or anti-reference — no quality was stated for it, so it goes
   to `REFERENCE_MAP.md`'s "unclassified / needs follow-up" section.
7. No positioning statement, target-audience decision, or messaging
   direction appears anywhere in the outputs.

## Expected artifacts
- `BRAND_DISCOVERY_BRIEF.md` — FACTS section contains only the location
  count/years/rating; CLAIMS section contains "most trusted name" attributed
  to the founder; ASPIRATIONS contains "friendly neighbor" framing;
  NON-NEGOTIABLES contains the fear-based-ads refusal.
- `DISCOVERY_GAPS.md` — either contains a business-objective gap, or the
  brief's HYPOTHESIS entry for it is explicitly tagged unconfirmed with a
  stated basis — one or the other, never silently absent.
- `REFERENCE_MAP.md` — "spa dentistry" appears only in
  unclassified/needs-follow-up, not sorted into references or
  anti-references.

## Forbidden behavior
- Must NOT state "most trusted name in the area" as a FACT.
- Must NOT invent a specific business objective (e.g. "preparing for a 4th
  location") and present it as confirmed without flagging it as an
  inference.
- Must NOT draft any positioning statement, tagline, or visual direction.

## Pass criteria
- [ ] FACT/CLAIM boundary is correctly applied to the "most trusted" claim.
- [ ] Business objective is either a flagged HYPOTHESIS or a logged material
      gap — never a silent invention or a silent omission.
- [ ] "Spa dentistry" reference is not forced into references/anti-references
      without a stated quality.
- [ ] No strategy/positioning/visual content appears in any output artifact.
