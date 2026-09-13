# Reference: concrete format specs by deliverable type

Used in `SKILL.md` step 8 (Specify format/channel constraints and
variants). Treat these as starting defaults — a channel's current
platform spec or the brand's own prior production standard always wins
over this list when they differ; note the override in the brief rather
than silently using a stale number.

## Web
- **Landing page hero:** primary image/video at minimum 1920×1080 (desktop)
  and a distinct crop for mobile (min 1080×1350 or platform default);
  headline typically under ~10 words for above-the-fold legibility; one
  primary CTA button, not competing CTAs.

## Social
- **Instagram/TikTok Reel:** 9:16 vertical, 1080×1920, 15–60s typical for a
  single-message ad/organic post (confirm against the specific campaign
  goal — a longer educational format may run 60–90s); hook must land in the
  first 1–3s; captions/on-screen text required (assume sound-off viewing).
- **Instagram/LinkedIn static post:** 1:1 (1080×1080) or 4:5 (1080×1350);
  4:5 generally gets more feed real estate on mobile.
- **Campaign (multi-asset):** define the variant matrix explicitly
  (aspect ratios × durations × languages) in `ASSET_REQUIREMENTS.md` rather
  than describing one "hero" version and leaving variants implicit.

## Executive / investor deck
- Slide count: a pitch/update deck is typically 10–15 slides for the core
  narrative (appendix separate); a board deck may run longer but should
  still separate "read" slides from "present" slides.
- One idea per slide; a slide needing more than ~2 supporting data points
  is usually two slides.
- Chart/data-viz style should match the brand's defined system if one
  exists; if none exists, flag it as a missing canon input rather than
  inventing a chart style.

## Packaging
- Requires physical production specs beyond the brand's digital identity
  system: dieline/template, bleed and safe-zone margins, print process
  (offset/digital/flexo — affects achievable color fidelity), substrate.
  These are almost never in a digital brand book — treat their absence as
  an `ASSET_REQUIREMENTS.md` item to source from the packaging vendor, not
  a blocker on the creative brief itself unless the brand's color/claims
  rules can't be verified without them.

## Generated media (AI image/video)
- Specify resolution/duration/aspect ratio as above for the target channel.
- Add explicit negative constraints (what the generation must avoid) drawn
  from the visual system's existing anti-pattern language — generic stock-
  photo composition, illegible/garbled on-screen text, inconsistent brand
  color reproduction across frames.
