# Eval Case — Dental practice reels system

## Scenario
A dental practice with approved strategy and verbal identity needs an
ongoing short-form video system. Tests that pillars are derived from the
practice's actual differentiator (live chairside camera narration) rather
than generic dental-content categories, that cadence reflects a genuinely
small production team, and that healthcare compliance boundaries are
explicit per pillar rather than one blanket disclaimer.

## Input
```yaml
RUN_REQUEST:
  objective: "build initial content system for Instagram/TikTok reels"
  source_artifacts:
    - "BRAND_STRATEGY.md (approved): positioning = 'the practice that shows
       you what it's doing, not just tells you'; differentiator = intraoral
       camera used on every patient with live chairside narration; audience
       pain = adults with dental anxiety from being kept in the dark;
       proof point = before/after case documentation on every treatment"
    - "VERBAL_IDENTITY.md (approved): plain, calm, never fear-based; banned:
       guaranteed-outcome claims, diagnosis-by-video, unsupported claims"
  known_context:
    channels_in_use: ["Instagram Reels", "TikTok"]
    production_capacity: "1 clinician + 1 part-time editor, ~3hrs/week combined"
    vertical_constraints: ["no diagnosis via video", "no guaranteed-outcome claims"]
  constraints: ["healthcare advertising compliance applies to every asset"]
  desired_output: full_system
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Journey map and pillar derivation trace each pillar to a specific
   strategy line (camera/narration differentiator, documented-case proof
   point, named anxiety pain) — not to a generic "patient education" or
   "testimonials" category.
2. Cadence in `CONTENT_PIPELINE.md` shows the arithmetic against the stated
   ~3hrs/week capacity, not an aspirational daily-posting number.
3. Compliance boundaries (no diagnosis via video, no guaranteed-outcome
   language) appear explicitly against the specific pillar(s) they apply to.
4. `MEASUREMENT_MODEL.md` does not treat reach/views/completion rate as a
   revenue signal; booking-link clicks are marked intent, not closed sale.

## Expected artifacts
- `CONTENT_PILLARS.md` — 3–5 pillars, each with a quoted/near-verbatim
  traced source from `BRAND_STRATEGY.md`.
- `CONTENT_PIPELINE.md` — cadence with explicit arithmetic tied to the
  3hrs/week figure; compliance boundary table naming the two vertical
  constraints against specific pillars.
- `MEASUREMENT_MODEL.md` — a "not a revenue proxy" list including
  reach/views; conversion metric defined separately (e.g. booking
  attribution).

## Forbidden behavior
- Must not include a generic "testimonials" or "dental tips" pillar with no
  traced source.
- Must not propose a cadence (e.g. "daily") with no capacity arithmetic
  behind it given that capacity was explicitly stated.
- Must not fold the two named vertical compliance constraints into one
  generic disclaimer line detached from specific pillars.
- Must not present video completion rate or reach as a conversion/revenue
  metric.

## Pass criteria
- [ ] Every pillar traces to a specific `BRAND_STRATEGY.md` line.
- [ ] Cadence shows arithmetic against the stated 3hrs/week capacity.
- [ ] Both vertical constraints appear as explicit per-pillar boundaries.
- [ ] No reach/view/completion metric is treated as revenue.
