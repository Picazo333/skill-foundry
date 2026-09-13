# Worked example — dental clinic discovery

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "build discovery brief for a 3-location dental clinic rebrand"
  source_artifacts:
    - "founder_interview_2026-06.txt (founder: Dr. Amara Osei, practicing 11 years, 3 locations)"
    - "google_reviews_export.csv (312 reviews, avg 4.6 stars)"
    - "current_website_copy.txt ('Gentle, judgment-free dental care for the whole family')"
    - "competitor_notes.txt (2 nearby corporate chains, 1 boutique 'spa dentistry' practice)"
  known_context: null
  constraints: ["brand-only scope"]
  desired_output: full_discovery_set
  mode: STANDARD
  prior_run: null
```
Founder interview excerpts: "We've grown from one chair to three locations
in 11 years." "Patients tell us all the time they've never been to a dentist
that doesn't make them feel judged about their teeth." "I want us to feel
like the friendly neighbor, not a clinic." "I refuse to ever do those
fear-based before/after ads the corporate chains run." "Honestly I think
we're already the most trusted name in the area."

## Output (abridged)

**BRAND_DISCOVERY_BRIEF.md**
```
## FACTS
- 3 locations, operating 11 years — source: founder_interview_2026-06.txt
- Average review rating 4.6/5 across 312 reviews — source: google_reviews_export.csv

## CLAIMS
- "We're already the most trusted name in the area" — asserted by: Dr. Osei
  (founder), source: founder_interview_2026-06.txt — no market-share/survey
  data supplied to verify.

## ASPIRATIONS
- Wants the brand to "feel like the friendly neighbor, not a clinic" —
  source: founder_interview_2026-06.txt

## NON-NEGOTIABLES
- Will not use fear-based before/after advertising — source: founder,
  founder_interview_2026-06.txt

## Discovery axes
### Customer language
- "never been to a dentist that doesn't make them feel judged" (founder
  paraphrasing repeated patient feedback) — source: founder_interview_2026-06.txt
  — flagged for a follow-up: pull 2-3 verbatim review quotes to confirm this
  is patient language, not founder paraphrase, before treating it as
  customer language proper.

### Current perception
- 4.6/5 average rating suggests generally positive experience, but no
  qualitative theme analysis of reviews was done in source material —
  logged as a gap, not inferred.

### Business objective
- Not explicitly stated in source material — HYPOTHESIS (unconfirmed):
  likely differentiation from 2 nearby corporate chains ahead of a possible
  4th location, inferred from competitor_notes.txt + growth trajectory in
  FACTS. Needs founder confirmation.

## Contradictions
- None identified with current material — "friendly neighbor, judgment-free"
  aspiration and "no fear-based ads" non-negotiable are consistent, not in
  tension.
```

**DISCOVERY_GAPS.md**
```
| Gap | Blocks | Closing question | Owner |
|---|---|---|---|
| Business objective for rebrand timing | business objective | "What's driving the rebrand now — new location, competitive pressure, something else?" | Dr. Osei |
| No qualitative review-theme analysis | current perception (evidence for target audience decision) | "Can we get a theme pull from the 312 reviews (top 5 recurring positives/negatives)?" | founder/ops, or research-architect if not feasible from raw export |
```

**REFERENCE_MAP.md**
```
## Unclassified / needs follow-up
- "spa dentistry" boutique competitor — named in competitor_notes.txt with
  no stated quality (positive or negative reference?) — needs follow-up
  question before mapping.
```

Note what did NOT happen: the skill did not decide whether "friendly
neighbor" beats "spa dentistry" positioning, did not promote the "most
trusted name" claim to a fact despite the founder's confidence, and did not
draft any messaging — all of that is `brand-strategy`'s job.
