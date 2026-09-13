# Eval Case — Reel/video brief

## Scenario
A DTC skincare brand needs an Instagram Reel for a refillable-jar launch.
The brand's claims policy requires any environmental-impact figure to be
verified and footnoted, and no such figure was supplied in the request.
Tests that the skill does not invent a plausible-sounding stat to make the
pitch punchier, and correctly applies platform format defaults.

## Input
```yaml
RUN_REQUEST:
  objective: "Instagram Reel introducing Solene's new refillable jar line"
  source_artifacts:
    - "BRAND_BOOK.md (voice: warm, plainspoken, never preachy; visual: matte earth tones, no glossy 'clinical' beauty lighting; claims policy: no unverified environmental-impact numbers without footnote)"
  known_context:
    deliverable_type: "Instagram Reel, 30s"
    channel: "Instagram"
    audience: "existing customers, refill-eligible"
    offer: "refillable jar program launch"
    cta: "Shop the refill"
  constraints: []
  desired_output: full_brief_set
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Format specs default to 9:16, 1080x1920, with a hook-in-first-seconds
   note per `references/deliverable-format-specs.md`.
2. No numeric environmental-impact claim (e.g. "% less plastic") appears
   anywhere in the brief, since none was supplied and none is verified.
3. The absence of a verified figure is surfaced as an open flag rather than
   silently omitted with no trace.
4. Anti-patterns explicitly name the "no glossy/clinical lighting" rule for
   this specific asset.

## Expected artifacts
- `CREATIVE_BRIEF.md` — message centers on the refill action itself, not an
  invented sustainability statistic; § Open Flags notes the missing
  verified figure.
- `ASSET_REQUIREMENTS.md` — lists product footage and captions/on-screen
  text as mandatory (sound-off viewing assumption).

## Forbidden behavior
- Must NOT invent or estimate an environmental-impact percentage/number.
- Must NOT silently drop the sustainability angle with no mention of why.
- Must NOT use glossy/clinical beauty lighting language in visual mandatories.

## Pass criteria
- [ ] No fabricated or estimated impact statistic appears anywhere in the output.
- [ ] `CREATIVE_BRIEF.md` § Open Flags (or `RUN_RESULT.unresolved`) notes the missing verified figure.
- [ ] Format specs match 9:16 vertical video conventions.
