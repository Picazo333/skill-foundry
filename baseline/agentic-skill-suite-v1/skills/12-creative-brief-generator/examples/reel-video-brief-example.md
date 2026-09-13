# Worked example — Reel/video brief

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "Instagram Reel introducing Solene's new refillable jar line"
  source_artifacts:
    - "BRAND_BOOK.md (Solene: DTC skincare; positioning: 'skincare that doesn't cost the planet'; voice: warm, plainspoken, never preachy; visual: matte earth tones, no glossy 'clinical' beauty lighting; claims policy: no unverified environmental-impact numbers without footnote)"
  known_context:
    deliverable_type: "Instagram Reel, 30s"
    channel: "Instagram, organic + boosted"
    audience: "existing customers (repeat-purchase, refill-eligible)"
    offer: "refillable jar program launch"
    cta: "Shop the refill"
  constraints: []
  desired_output: full_brief_set
  mode: STANDARD
  prior_run: null
```

## Output (abridged)

**CREATIVE_BRIEF.md** (excerpt):
```
## Format & Channel Specs
| Variant | Dimensions/Duration | Notes |
|---|---|---|
| Primary | 9:16, 1080x1920, 30s | hook in first 2s per platform convention |

## Single-Minded Message
> Refill it — don't throw it out.

### Support points
1. Same formula, new refillable jar — source: BRAND_BOOK.md § Product.
2. Made for people who already buy from us, not a general sustainability pitch — source: RUN_REQUEST audience.

## Anti-Patterns
- No glossy/clinical beauty lighting — matte, natural light per BRAND_BOOK.md § Visual System.
- No "saves X% plastic" style stat unless a verified, footnoted figure is supplied — none was supplied this run, so no such claim appears.

## Open Flags
- No verified environmental-impact figure was supplied. The brief deliberately omits any numeric claim rather than inventing one — flag for whoever sources a verified stat if one becomes available.
```

**ASSET_REQUIREMENTS.md** (excerpt): refillable jar product footage
(mandatory, owner: product/photography), captions/on-screen text file for
sound-off viewing (mandatory).

**PRODUCTION_HANDOFF.md** (excerpt): execution medium = video editor;
delivery as .mp4, 1080x1920; review against acceptance criteria; next step
→ `brand-quality-auditor`.

Note what did NOT happen: no environmental-impact percentage was invented to
make the pitch punchier — the claims-policy mandatory and the missing source
data are both surfaced explicitly instead.
