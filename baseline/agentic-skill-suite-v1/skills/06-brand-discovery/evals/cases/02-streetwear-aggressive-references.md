# Eval Case — Streetwear brand with aggressive references

## Scenario
A pre-launch streetwear label gives founder voice notes packed with named
references (Supreme, Vetements) and strong opinions, plus a pricing sheet
that quietly contradicts one of the founders' stated intents. Tests whether
references get mapped by underlying quality rather than surface
similarity, and whether the skill catches a contradiction that spans a
verbal statement and a numeric fact.

## Input
```yaml
RUN_REQUEST:
  objective: "build discovery brief for new streetwear label pre-launch"
  source_artifacts:
    - "founder_voice_notes_transcript.txt (wants Supreme-style drop scarcity, wants 'anyone on a normal budget' to afford it, visual style 'aggressive, ugly-cool like Vetements through a skate shop', explicitly rejects 'quiet luxury streetwear')"
    - "moodboard_notes.txt (references: Supreme drops, Vetements runway)"
    - "pricing_sheet_draft.xlsx (hoodie $180, tee $70)"
  known_context: null
  constraints: []
  desired_output: full_discovery_set
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Supreme is mapped as a reference for the *drop/scarcity mechanic*
   specifically, not for visual style — the transcript names it for hype
   mechanics only.
2. Vetements is mapped as a reference for the *aggressive/deconstructed
   visual quality*, kept distinct from the Supreme entry rather than merged
   just because both are "streetwear-adjacent."
3. "Quiet luxury streetwear" is captured as an anti-reference with its
   stated quality (reads as luxury, contradicts accessibility).
4. The skill identifies the contradiction between "scarcity/hype, exclusive
   feel" and "anyone on a normal budget" as an explicit, unresolved
   Contradictions entry — and separately notes the $180 hoodie FACT sits in
   tension with the "normal budget" framing, without picking a resolution.
5. No visual direction, logo concept, or color/typography suggestion is
   produced from the Vetements/Supreme references — they are documented as
   signals only.

## Expected artifacts
- `REFERENCE_MAP.md` — Supreme and Vetements appear as separate reference
  entries under different underlying qualities (or explicitly cross-linked
  by quality, not merged into one generic "streetwear reference" blob);
  "quiet luxury" anti-reference is present with a stated quality; an
  "opposed-quality pairs" entry connects the hype/exclusive references to
  the accessibility aspiration.
- `BRAND_DISCOVERY_BRIEF.md` — Contradictions section contains the
  exclusive-vs-accessible tension, citing both founder statements and, at
  minimum, notes the $180 price point as relevant supporting FACT.

## Forbidden behavior
- Must NOT resolve the exclusive-vs-accessible contradiction (e.g. by
  concluding "so the price point should be lower" or picking a lane).
- Must NOT merge Supreme and Vetements into one undifferentiated reference
  entry that loses which quality each was invoked for.
- Must NOT produce a color palette, logo direction, or moodboard image
  description as an output.

## Pass criteria
- [ ] Supreme and Vetements are mapped to distinct underlying qualities, not
      merged by industry/surface similarity.
- [ ] The exclusive-vs-accessible contradiction is explicit, unresolved, and
      cites both sides plus the $180 pricing fact.
- [ ] No visual/design output appears anywhere in the artifact set.
