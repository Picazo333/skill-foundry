# Worked example — dental practice short-form video system

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "build initial content system for Instagram/TikTok reels"
  source_artifacts:
    - "BRAND_STRATEGY.md (approved): positioning = 'the practice that shows
       you what it's doing, not just tells you'; differentiator = intraoral
       camera used on every patient with live chairside narration; audience
       pain = adults with dental anxiety from being kept in the dark during
       procedures; proof point = before/after case documentation on every
       treatment)"
    - "VERBAL_IDENTITY.md (approved): voice = plain, calm, never fear-based;
       banned: before/after claims presented as guaranteed outcomes,
       diagnosis-by-video, any claim not tied to a documented case"
  known_context:
    offer_funnel: "reels -> profile -> booking link"
    channels_in_use: ["Instagram Reels", "TikTok"]
    production_capacity: "1 clinician + 1 part-time editor, ~3hrs/week combined"
    vertical_constraints: ["no diagnosis via video", "no guaranteed-outcome claims (ad healthcare policy)"]
  constraints: ["healthcare advertising compliance applies to every asset"]
  desired_output: full_system
  mode: STANDARD
  prior_run: null
```

## Output (abridged)

**CONTENT_PILLARS.md** (excerpt — 3 pillars, each traced):
```
## Pillar: "What We're Actually Doing" (live chairside narration)
- Journey stage(s): Attention, Trust
- Traced strategy source: "the practice that shows you what it's doing, not
  just tells you" + "intraoral camera used on every patient with live
  chairside narration" — BRAND_STRATEGY.md
- Why specific to this brand: competitors describe procedures verbally
  after the fact; this practice narrates live, on camera, as the
  differentiator itself — not transferable to a practice without that
  camera workflow.
- What this is NOT: not a diagnosis of the viewer's own symptoms (banned
  per VERBAL_IDENTITY.md) — narration stays scoped to the patient on camera.

## Pillar: "Documented, Not Promised" (case-based proof)
- Journey stage(s): Trust, Intent
- Traced strategy source: "before/after case documentation on every
  treatment" — BRAND_STRATEGY.md proof point.
- Why specific to this brand: every case shown is a real documented file,
  not a stock/generic before-after — matches the "shows, doesn't just
  tell" positioning and the banned-claims boundary (no guaranteed outcome
  language, only what the specific case shows).

## Pillar: "In the Dark No Longer" (anxiety-specific reassurance)
- Journey stage(s): Attention, Conversion
- Traced strategy source: audience pain = "adults with dental anxiety from
  being kept in the dark during procedures" — BRAND_STRATEGY.md.
- Why specific to this brand: directly answers the named pain with the
  named differentiator (camera + narration = the opposite of "kept in the
  dark"), not a generic "we care about your comfort" claim.
```

**CONTENT_PIPELINE.md** (excerpt):
```
Cadence: stated capacity = 1 clinician + 1 editor, ~3hrs/week combined.
Arithmetic: ~3hrs ÷ ~50min per reel (chairside capture + edit) ≈ 3
reels/week sustainably, split ~2 "What We're Actually Doing" (highest
production ease — captured during real procedures) : 1 "Documented, Not
Promised" (needs case pairing + compliance check, more editor time).
"In the Dark No Longer" runs as a recurring hook variant inside the other
two rather than its own weekly slot, given capacity.

Compliance boundaries:
| Pillar | Boundary | Source |
|---|---|---|
| Documented, Not Promised | no outcome language beyond what the specific
  shown case documents; no "guaranteed" / "permanent" language | VERBAL_IDENTITY.md
  + healthcare ad policy (known_context) |
| What We're Actually Doing | narration must not diagnose or give medical
  advice about the viewer's own symptoms in comments/captions | vertical_constraints |
```

**MEASUREMENT_MODEL.md** (excerpt):
```
"What We're Actually Doing" (Attention/Trust) -> completion rate, saves.
NOT read as revenue.
"Documented, Not Promised" (Trust/Intent) -> profile visits, link clicks
from bio. NOT read as revenue on its own — booking link clicks are an
intent signal, not a closed sale.
Conversion metric (bookings attributed to reels traffic) tracked
separately via booking-link UTM, reviewed monthly.
```

Note what did NOT happen: the skill did not add a generic "patient
testimonials" pillar even though it's common in dental content, because
nothing in `BRAND_STRATEGY.md` names testimonials as the differentiator —
testimonials appear only as supporting proof inside "Documented, Not
Promised," not as their own pillar.
