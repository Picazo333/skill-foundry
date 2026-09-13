# Eval Case — B2B founder-led content factory

## Scenario
A B2B SaaS founder wants a repeatable LinkedIn + newsletter content system
built around their own credibility as the differentiator. Tests that
pillars trace to specific founder-credibility and product-mechanism claims
(not generic "thought leadership"), that formats vary correctly across
LinkedIn vs. newsletter, and that the measurement model distinguishes
engagement vanity metrics from pipeline signal.

## Input
```yaml
RUN_REQUEST:
  objective: "build ongoing founder-led content system for demand gen"
  source_artifacts:
    - "BRAND_STRATEGY.md (approved): positioning = 'built by the person who
       spent 8 years running the ops team this replaces'; differentiator =
       founder's direct operational experience in the exact pain the
       product solves; audience pain = ops leaders drowning in manual
       reconciliation; proof point = documented before/after case studies
       from design partners"
    - "VERBAL_IDENTITY.md (approved): first-person founder voice, specific
       and numeric over vague, no generic SaaS jargon ('synergy',
       'game-changing'); banned: unverified customer metrics"
  known_context:
    offer_funnel: "LinkedIn/newsletter -> demo request"
    channels_in_use: ["LinkedIn", "email newsletter"]
    production_capacity: "founder only, ~4hrs/week"
    vertical_constraints: []
  constraints: []
  desired_output: full_system
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Pillars trace to the founder's operational-experience differentiator and
   the design-partner case studies — not a generic "thought leadership" or
   "industry tips" category.
2. Format library defines distinct LinkedIn vs. newsletter variants for the
   same pillar (e.g. LinkedIn = short pattern-interrupt hook; newsletter =
   longer narrative with data).
3. Cadence arithmetic reflects founder-only, 4hrs/week capacity.
4. Measurement model separates engagement metrics (Attention/Trust) from
   the actual conversion signal (demo requests attributed), and explicitly
   flags engagement/follower growth as not a revenue proxy.

## Expected artifacts
- `CONTENT_PILLARS.md` — pillars traced to founder operational experience
  and design-partner proof, distinct from generic thought-leadership framing.
- `FORMAT_LIBRARY.md` — at least one pillar with explicit LinkedIn vs.
  newsletter channel variants showing different hook/body structure.
- `MEASUREMENT_MODEL.md` — demo-request attribution as the conversion
  metric; engagement/reach explicitly listed as not-revenue.

## Forbidden behavior
- Must not produce a "thought leadership" or "industry insights" pillar
  with no traced source.
- Must not copy-paste the same format/length across LinkedIn and newsletter.
- Must not report engagement rate or follower growth as a pipeline/revenue
  metric.
- Must not invent a customer metric not present in source artifacts (banned
  per VERBAL_IDENTITY.md — unverified customer metrics).

## Pass criteria
- [ ] Every pillar traces to founder-experience differentiator or
      design-partner proof.
- [ ] At least one pillar shows distinct LinkedIn vs. newsletter format
      variants.
- [ ] Cadence arithmetic is shown against founder-only 4hrs/week capacity.
- [ ] Engagement/reach metrics are explicitly separated from the demo-request
      conversion metric.
