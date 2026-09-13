# Worked example — streetwear brand with aggressive references

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "build discovery brief for new streetwear label pre-launch"
  source_artifacts:
    - "founder_voice_notes_transcript.txt (2 co-founders, ex-skate scene)"
    - "moodboard_notes.txt (references: Supreme drops, Vetements runway, 'anti-fashion fashion')"
    - "pricing_sheet_draft.xlsx (hoodie $180, tee $70)"
  known_context: null
  constraints: []
  desired_output: full_discovery_set
  mode: STANDARD
  prior_run: null
```
Founder excerpts: "We want the scarcity and hype of Supreme drops." "But
also we want anyone on a normal budget to actually be able to cop a piece —
we're not trying to be exclusive rich-kid stuff." "Visually we want it
aggressive, almost ugly-cool, like Vetements sent it through a skate shop."
"We are NOT trying to be luxury streetwear, we hate that whole
quiet-luxury-but-make-it-hoodie thing."

## Output (abridged)

**BRAND_DISCOVERY_BRIEF.md**
```
## FACTS
- Hoodie priced at $180, tee at $70 — source: pricing_sheet_draft.xlsx

## ASPIRATIONS
- Wants drop-based scarcity/hype model like Supreme — source: founder_voice_notes_transcript.txt
- Wants visual identity described as "aggressive, ugly-cool" — source: founder_voice_notes_transcript.txt

## Contradictions
- **Exclusive hype-scarcity vs. accessible pricing** — side A: "we want the
  scarcity and hype of Supreme drops" (founder_voice_notes_transcript.txt);
  side B: "anyone on a normal budget to actually be able to cop a piece...
  not trying to be exclusive rich-kid stuff" (same source). Note: $180
  hoodie price point (FACT, pricing_sheet_draft.xlsx) is in tension with the
  "normal budget" claim in side B — flagged for brand-strategy alongside
  the scarcity/accessibility contradiction, not resolved here.
```

**REFERENCE_MAP.md**
```
## Aggressive, deconstructed hype
### References
- **Supreme (drop model)** — invoked for: scarcity/hype mechanics, not
  visual style — in the words of: "the scarcity and hype of Supreme drops"
  — source: founders, founder_voice_notes_transcript.txt
- **Vetements (runway)** — invoked for: aggressive, deconstructed,
  "ugly-cool" visual quality — in the words of: "like Vetements sent it
  through a skate shop" — source: founders, founder_voice_notes_transcript.txt

### Anti-references
- **"Quiet-luxury-but-make-it-hoodie" (unnamed category, described not
  named)** — avoid because: reads as luxury streetwear, which contradicts
  the accessible-pricing aspiration — in the words of: "we hate that whole
  quiet-luxury-but-make-it-hoodie thing" — source: founders,
  founder_voice_notes_transcript.txt

## Opposed-quality pairs
- Want **aggressive/ugly-cool, hype-scarcity** (ref: Supreme, Vetements) vs.
  avoid **quiet luxury** (anti-ref, unnamed) — source: founder_voice_notes_transcript.txt.
  This pairs directly with the exclusive-vs-accessible contradiction in
  BRAND_DISCOVERY_BRIEF.md — the visual references point exclusive/hype
  while the stated audience intent points accessible.
```

**DISCOVERY_GAPS.md**
```
| Gap | Blocks | Closing question | Owner |
|---|---|---|---|
| No target customer description beyond "ex-skate scene" self-reference | target audience/segment | "Who specifically is meant to be able to 'cop a piece on a normal budget' — same skate scene as founders, or broader?" | founders |
| Drop cadence/volume not specified | competitive frame (hype model only works at certain scale/frequency) | "How often and how many units per drop?" | founders |
```

Note what did NOT happen: the skill did not decide whether to keep the $180
price point or resolve exclusive-vs-accessible — that tension is handed to
`brand-strategy` intact, with both the verbal contradiction and its
visual-reference echo cross-referenced rather than picked apart separately.
