# Eval Case — AI consulting agency vs. large SIs and boutiques

## Scenario
A 12-person AI implementation consultancy needs positioning against both
large systems integrators and solo/boutique consultants, using direct
client-interview evidence about why prior vendors failed. Tests that the
skill weighs relevance (evidence strength) correctly against distinctiveness
when choosing among multiple credible, evidence-backed territories, and
respects a no-benchmark-claims constraint.

## Input
```yaml
RUN_REQUEST:
  objective: "define positioning for a 12-person AI implementation consultancy competing against large SI firms and solo/boutique AI consultants"
  source_artifacts:
    - "BRAND_DISCOVERY_BRIEF.md (5/5 client interviews cite 'we got a slide deck, not a working system' as the reason they left prior vendors; agency ships a working production system in every engagement, no strategy-only offering exists; team is 12 in-house engineers, no offshore subcontracting)"
    - "competitor_map.md (large SIs: broad/slow/strategy-heavy; boutiques: fast but single-person bus-factor risk flagged by clients as a fear)"
  known_context: null
  constraints: ["cannot claim to be faster/cheaper than named competitors without benchmark data — none supplied"]
  desired_output: full_strategy_set
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Generate at least two credible, evidence-backed territories (the
   "ships production systems, not decks" claim and the "no bus-factor risk"
   claim) plus at least one weak/generic territory (e.g. bare "AI experts
   you can trust") that gets scored low and discarded.
2. Score both credible territories on all five axes; recommend the one with
   the stronger relevance evidence (5/5 direct client interviews) over the
   one with only competitive-context evidence, and say so explicitly.
3. Fold the non-recommended credible territory in as a supporting RTB rather
   than discarding its evidence entirely.
4. Do not introduce any faster/cheaper comparative claim, honoring the
   stated constraint.

## Expected artifacts
- `POSITIONING_SYSTEM.md` — territories scored; recommendation rationale
  explicitly names the relevance-evidence gap between the top two
  candidates as the deciding factor.
- `BRAND_STRATEGY.md` — RTBs include both the production-system fact and the
  in-house-team fact, each with its own citation.
- `STRATEGIC_GUARDRAILS.md` — an anti-goal against unsupported
  faster/cheaper claims.

## Forbidden behavior
- Must not recommend the generic "AI experts you can trust" territory.
- Must not merge the two credible territories into one claim that loses the
  traceability of which evidence backs which part.
- Must not state or imply a speed/cost comparison to named or unnamed
  competitors without benchmark data.

## Pass criteria
- [ ] At least 3 territories generated, one clearly generic and discarded
      with a stated reason.
- [ ] Recommendation explains the relevance-based tiebreak between the two
      strong candidates.
- [ ] Every RTB in `BRAND_STRATEGY.md` cites a specific discovery-brief or
      competitor-map fact.
- [ ] No faster/cheaper comparative claim appears anywhere in the output.
