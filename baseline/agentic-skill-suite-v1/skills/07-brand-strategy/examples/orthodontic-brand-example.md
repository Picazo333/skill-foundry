# Worked example — orthodontic brand (local multi-location practice)

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "define initial positioning for a 4-location orthodontic practice group entering a market with 6 established competitors"
  source_artifacts:
    - "BRAND_DISCOVERY_BRIEF.md (audience: parents of tweens/teens + adult self-pay patients; all 6 competitors advertise 'friendly, modern, affordable braces'; this practice's actual differentiator per owner interviews: in-house 3D scanning + same-week same-day appliance fabrication, cutting the typical 2-3 week wait for adjustments/replacements to same-day; competitors all use outsourced labs)"
  known_context: null
  constraints: ["healthcare marketing compliance — no comparative claims naming competitors, no guaranteed-outcome language"]
  desired_output: full_strategy_set
  mode: STANDARD
  prior_run: null
```

## Output (abridged)

**POSITIONING_SYSTEM.md** (excerpt — 3 territories generated):
```
Territory 1 — "Friendly modern affordable care" (matches all 6 competitors' claims)
  Distinctiveness: 1 (identical to every direct competitor's actual claim)
  → discarded: fails distinctiveness before scoring further

Territory 2 — "Same-day orthodontic technology"
  Distinctiveness: 5 (no competitor in the frame offers in-house same-day fabrication)
  Credibility: 5 (directly supported — in-house 3D scanning + same-day fabrication, owner-confirmed)
  Relevance: 4 (parent/self-pay audience evidence shows appointment-frequency and wait-time as a stated pain point)
  Extensibility: 4 (extends to any future appliance type the practice adds)
  Business fit: 5 (reinforces the in-house lab investment already made)
  Total: 23 — RECOMMENDED

Territory 3 — "Affordable family-friendly braces"
  Distinctiveness: 2 (overlaps heavily with competitor claims)
  → discarded: distinctiveness too low, same failure mode as Territory 1

Commoditization swap test on Territory 2: "[Practice] is the orthodontic
practice that eliminates the multi-week adjustment wait, because appliances
are scanned and fabricated in-house same-day." Swapping in a competitor's
name reads as false — none of the 6 use in-house fabrication. PASS.
```

**BRAND_STRATEGY.md** (excerpt):
```
Differentiation statement: In-house 3D scanning and same-day appliance
fabrication remove the 2-3 week wait every other practice in this market
imposes — evidence: owner interview + discovery brief, all 6 competitors
confirmed using outsourced labs.

Strategic pillars:
1. Same-day fabrication — RTB: in-house scanning/fabrication equipment, confirmed in discovery brief.
2. Fewer visits, less disrupted school/work — RTB: derived directly from pillar 1's mechanism, not a separate claim.
```

**STRATEGIC_GUARDRAILS.md** (excerpt):
```
Anti-goal: Never state or imply guaranteed treatment outcomes or timelines
("straight teeth in X months") — why: healthcare marketing constraint from
RUN_REQUEST, and no clinical-outcome evidence was supplied to back a claim
like this.
Anti-goal: Never name or visually reference a specific competitor — why:
compliance constraint.
Operational boundary: Any claim about speed must reference the fabrication
mechanism (in-house/same-day), never a bare speed adjective alone — test:
does the copy name the mechanism, or just say "fast"?
```

Note what did NOT happen: "friendly, modern, affordable" was generated,
scored, and explicitly rejected for failing distinctiveness — not silently
omitted — because it's what every competitor already claims.
