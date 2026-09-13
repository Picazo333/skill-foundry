# Eval Case — Consumer apparel repositioning ahead of retail expansion

## Scenario
A 6-year-old DTC apparel brand's original "premium for everyone" positioning
now reads as commoditized on a retail shelf; a repositioning run (`mode:
UPDATE`) must use VoC and business-model evidence to find a real
differentiator, while a constraint keeps visual/verbal identity explicitly
out of scope. Tests `mode: UPDATE` behavior (diffing against prior strategy)
and correct non-trigger boundary respect.

## Input
```yaml
RUN_REQUEST:
  objective: "reposition a 6-year-old DTC performance-apparel brand ahead of a wholesale retail expansion"
  source_artifacts:
    - "BRAND_DISCOVERY_BRIEF.md (VoC from 200 reviews: repeat buyers cite full XS-5X size range in every style as the reason they stayed; manufacturing partner supports full range at no cost premium, unlike competitors who upcharge/limit extended sizes)"
    - "prior BRAND_STRATEGY.md, prior POSITIONING_SYSTEM.md"
  known_context: "retail buyers say current 'for everyone' positioning reads as undifferentiated next to 8 shelf competitors"
  constraints: ["must retain existing brand name and logo — visual/verbal identity work is out of scope for this run"]
  desired_output: full_strategy_set
  mode: UPDATE
  prior_run: "prior_run/BRAND_STRATEGY.md, prior_run/POSITIONING_SYSTEM.md"
```

## Expected behavior
1. Load the prior strategy as baseline; explicitly identify the prior
   "for everyone" positioning as the territory being superseded, with the
   retail-buyer feedback as the reason.
2. Generate and recommend the full-size-range-at-no-upcharge territory,
   scored against VoC + business-model evidence.
3. Run the commoditization swap test against the 8 shelf competitors named
   in context and record the result.
4. Produce all three strategy artifacts, but do not produce or reference
   any logo, name, color, or verbal-tone content — the constraint scopes
   that out.

## Expected artifacts
- `POSITIONING_SYSTEM.md` — prior territory shown as superseded with reason;
  new recommended territory scored and passing the swap test.
- `BRAND_STRATEGY.md` — differentiation statement traces to the VoC size-range
  evidence, not a restated "for everyone" claim.
- `STRATEGIC_GUARDRAILS.md` — an anti-goal specifically against "for
  everyone"-style language re-entering messaging.

## Forbidden behavior
- Must not silently drop the prior strategy without noting it was
  superseded and why.
- Must not touch logo, name, visual system, or actual tone-of-voice copy —
  that's out of scope per the stated constraint and per this skill's
  non-trigger boundary.
- Must not invent fabric/technology claims beyond what discovery evidence
  supports (a tech-forward territory should be discarded/flagged if
  evidence for it is missing, not embellished to make it viable).

## Pass criteria
- [ ] Prior "for everyone" territory is explicitly marked superseded with a
      stated reason, not just absent.
- [ ] Recommended territory's differentiation traces to the 200-review VoC
      evidence and the manufacturing-model fact.
- [ ] No visual, verbal-tone, name, or logo content appears in any output
      artifact.
- [ ] Any technology/fabric-based territory without supporting evidence is
      discarded or flagged, not fabricated into credibility.
