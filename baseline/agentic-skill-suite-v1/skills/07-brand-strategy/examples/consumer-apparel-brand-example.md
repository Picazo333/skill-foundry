# Worked example — consumer apparel brand

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "reposition a 6-year-old direct-to-consumer performance-apparel brand ahead of a wholesale retail expansion"
  source_artifacts:
    - "BRAND_DISCOVERY_BRIEF.md (original positioning: 'premium athletic wear for everyone'; VoC evidence from 200 reviews: repeat buyers overwhelmingly cite the brand's size range (XS-5X in every style, not just core styles) as the reason they stayed after trying competitors; business model: manufacturing partner supports full size range at no cost premium, unlike most competitors who upcharge or limit extended sizes to select styles)"
    - "prior BRAND_STRATEGY.md (mode: UPDATE — prior_run)"
  known_context: "retail buyers have said the current 'for everyone' positioning reads as undifferentiated on the shelf next to 8 other performance-wear brands"
  constraints: ["must retain existing brand name and logo — visual/verbal identity work is out of scope for this run"]
  desired_output: full_strategy_set
  mode: UPDATE
  prior_run: "prior_run/BRAND_STRATEGY.md, prior_run/POSITIONING_SYSTEM.md"
```

## Output (abridged)

**POSITIONING_SYSTEM.md** (excerpt — delta against prior strategy, 3 territories generated):
```
Territory 1 (prior, retained for comparison) — "Premium athletic wear for everyone"
  Distinctiveness: 1 (retail buyer feedback confirms this reads as identical to 8 shelf competitors)
  → superseded: this is exactly the commoditization failure retail buyers flagged

Territory 2 — "Every size, every style, no upcharge"
  Distinctiveness: 5 (VoC + business model confirm no direct competitor matches full-range-at-no-premium)
  Credibility: 5 (manufacturing partner fact, business-model evidence)
  Relevance: 5 (200-review VoC data directly names this as the repeat-purchase driver)
  Extensibility: 5 (applies to every current and future style category)
  Business fit: 5 (zero cost-structure change required — already the model)
  Total: 25 — RECOMMENDED

Territory 3 — "Performance tech for real bodies" (tech-forward framing)
  Distinctiveness: 3 (some overlap with 2 competitors' "innovation" claims)
  Credibility: 3 (no specific fabric/tech evidence supplied in discovery brief)
  → discarded: credibility too low without supplied technical evidence; could be revisited if that evidence is gathered

Commoditization swap test on Territory 2: "[Brand] is the performance-apparel
brand that offers every size in every style at no upcharge, because the
manufacturing model was built for full-range production from day one."
Swapping in any of the 8 shelf competitors reads as false per VoC evidence
(reviewers explicitly compared and stayed for this reason). PASS.
```

**BRAND_STRATEGY.md** (excerpt):
```
Strategic decision: reposition from an undifferentiated "for everyone" claim
to the evidence-backed full-size-range differentiator ahead of wholesale
retail expansion, where shelf differentiation is the stated business need.

Unresolved: Territory 3's tech-forward angle was discarded for low
credibility only because supporting fabric/tech evidence wasn't in this
run's inputs — flagged as revisitable, not permanently rejected, if that
evidence is gathered later.
```

**STRATEGIC_GUARDRAILS.md** (excerpt):
```
Anti-goal: Never let "for everyone" language re-enter messaging as a
standalone claim — why: retail buyers and this run's swap test both
identified it as the commoditized failure mode being repositioned away
from.
Operational boundary: Any size-range claim must be checkable against the
actual in-market size range per style — test: does the claim match current
catalog data, not aspirational range?
```

Note what did NOT happen: because `constraints` scoped out identity work,
this run did not touch logo/visual/name — it stayed strictly on strategy,
consistent with the non-trigger boundary in `SKILL.md`.
