# Eval Case — Orthodontic brand entering a commoditized local market

## Scenario
A multi-location orthodontic practice group needs positioning in a market
where all 6 competitors already use nearly identical "friendly, modern,
affordable" claims. Tests that the skill finds and validates a real,
evidence-backed differentiator instead of a healthcare-marketing-compliant
version of the same generic claim everyone else uses — and respects
regulatory constraints while doing it.

## Input
```yaml
RUN_REQUEST:
  objective: "define initial positioning for a 4-location orthodontic practice group entering a market with 6 established competitors"
  source_artifacts:
    - "BRAND_DISCOVERY_BRIEF.md (audience: parents of tweens/teens + adult self-pay patients; all 6 competitors advertise 'friendly, modern, affordable braces'; differentiator per owner interviews: in-house 3D scanning + same-day appliance fabrication vs. competitors' 2-3 week outsourced-lab wait)"
  known_context: null
  constraints: ["healthcare marketing compliance — no comparative claims naming competitors, no guaranteed-outcome language"]
  desired_output: full_strategy_set
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Generate multiple territories including one resembling the market-generic
   "friendly, modern, affordable" claim, then score it low on distinctiveness
   and discard it explicitly rather than silently omitting it.
2. Generate and recommend a territory built on the in-house same-day
   fabrication fact, with all five axes scored and cited to the discovery
   brief.
3. Run the commoditization swap test on the recommendation and record a
   PASS with the reasoning shown.
4. Encode the compliance constraints as operational guardrails (no named
   competitor comparisons, no guaranteed-outcome language) — not just
   restated as a note.

## Expected artifacts
- `POSITIONING_SYSTEM.md` — 3+ territories with full five-axis scoring; the
  generic "friendly/modern/affordable" territory present and marked
  discarded for low distinctiveness; recommended territory scored highest
  and passing the swap test.
- `BRAND_STRATEGY.md` — differentiation statement citing the same-day
  fabrication fact with a source; no comparative or outcome-guarantee
  language anywhere.
- `STRATEGIC_GUARDRAILS.md` — anti-goals covering both compliance
  constraints as testable rules, not restated prose.

## Forbidden behavior
- Must not recommend a territory that fails the commoditization swap test.
- Must not include a comparative claim naming a competitor or an
  outcome-guarantee claim anywhere in any artifact, given the stated
  constraint.
- Must not invent clinical-outcome evidence (e.g. treatment-time claims) not
  present in the discovery brief.

## Pass criteria
- [ ] The generic territory is generated, scored, and explicitly discarded
      — not omitted.
- [ ] The recommended territory's differentiation traces to the same-day
      fabrication fact with a cited source.
- [ ] The commoditization swap test is shown and passes for the
      recommendation.
- [ ] No compliance-violating language (comparative or outcome-guarantee)
      appears anywhere in the output set.
