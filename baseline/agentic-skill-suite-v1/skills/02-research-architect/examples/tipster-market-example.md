# Worked example (abridged) — sports betting / tipster market

## Input
```yaml
RUN_REQUEST:
  objective: "We want to launch a paid sports-betting tipster subscription service. Should we build it, and if so, what model (pure tips vs. tips+community vs. copy-betting) and what market first?"
  source_artifacts: []
  known_context: "Founders have built two prior subscription products (unrelated niches). No existing betting/gambling operating experience. Budget: bootstrapped, ~$40k runway."
  constraints: ["must remain compliant with gambling-advertising law in target market", "no in-house odds/trading desk planned"]
  desired_output: full_architecture_package
  mode: AUTONOMOUS
  prior_run: null
```

## Output (abridged excerpts)

**PROJECT_RESEARCH_BRIEF.md**
```
Master decision-oriented research question:
> What must be true about tipster-market economics, trust dynamics, and
> regulatory exposure for the founders to decide, within 90 days, whether to
> launch a paid tipster subscription — and if so, in which model and market?

Hypotheses (unverified):
- "Copy-betting" commands higher willingness-to-pay than pure tips — confidence: low
- Existing subscriber churn in this niche is driven mainly by tipster track-record
  volatility, not price — confidence: low
```

**DOMAIN_MAP.md** (excerpt)
```
### Bookmaker relationship & limiting behavior — weight: 17/20
  Importance 5, Uncertainty 5, Complexity 4, Risk 3
  Lens type: domain-native
  Interconnects with: Unit economics (limited accounts cap achievable tipster
    ROI, which caps subscriber-visible track record), Trust signals (public
    track record must survive bookmaker limiting without looking fabricated)
  Scope-expansion iterations allocated: 22 (of 150)

### Regulatory/advertising compliance — weight: 16/20
  Importance 5, Uncertainty 4, Complexity 3, Risk 4
  Interconnects with: Distribution/acquisition channel (ad platforms'
    gambling-adjacent content policies), Market selection (jurisdiction
    determines allowed claims)
  Scope-expansion iterations allocated: 19

### Generic "market size" domain — NOT included as a standalone lens
  Rejected during Phase 1: too generic for this domain-native market; folded
  into "Addressable subscriber pool by tipster niche" instead, which is
  domain-native and interconnects with Distribution.
```

**MASTER_RESEARCH_PROGRAM.md** (excerpt, 3 of 150+50 rows)
```
| # | Domain | Question | Material delta | Decision link | Primary-evidence trigger |
|---|---|---|---|---|---|
| 12 | Bookmaker relationship | At what stake-size and win-rate threshold do major UK bookmakers typically begin limiting an account, and does this vary meaningfully by sport? | New mechanism (limiting threshold), not previously asked | Determines whether a public-track-record model is even sustainable | yes — no reliable secondary data; requires direct interviews with active bettors/tipsters |
| 47 | Trust signals | What third-party verification services (e.g. independent tip-tracking sites) do subscribers actually check before paying, vs. which do they claim to check but don't? | New angle: stated vs. revealed trust behavior | Informs whether to invest in third-party verification integration pre-launch | yes — requires user interviews, not just survey of existing tools |
| 163 (polishing) | Distribution ↔ Regulatory | Red-team: does the planned acquisition channel (paid social ads) survive the regulatory domain's finding that gambling-adjacent ad content is restricted on 2 of 3 candidate platforms? | Consolidation: forces explicit reconciliation between two previously separate domains | Directly changes go/no-go on planned channel | no |
```

**COVERAGE_DEBT.md** (excerpt)
```
| Domain | Weight | Expected | Actual | Debt | Status |
|---|---|---|---|---|---|
| Bookmaker relationship & limiting | 17 | 21 | 22 | -1 | paid down |
| Copy-betting technical/regulatory feasibility | 15 | 19 | 11 | 8 | open — carried forward, flagged in RUN_RESULT.unresolved |
```

**GAP_LEDGER.md** (excerpt)
```
Contradiction ledger:
- #1: Founder known_context assumes copy-betting commands higher WTP, but a
  white-space finding (below) shows no incumbent has proven this in this
  niche — logged, not resolved.

White-space ledger:
- Incumbents largely serve football/horse racing; no evaluated incumbent
  targets combat-sports tipster niche specifically — raised weight of
  "Market/niche selection" domain from 12 to 15.

Primary-evidence triggers: 9 iterations tagged (bookmaker limiting behavior,
subscriber trust-verification behavior, willingness-to-pay by model) —
none answerable from secondary sources alone.
```

**EXECUTOR_START_PROMPT.md** (excerpt) — points a future Research Executor
at iterations #1-#150+#1-#50 in priority order by domain weight, flags the
9 primary-evidence-trigger iterations as needing interviews before any
secondary-source pass, and explicitly states: "This prompt starts
execution; research-architect does not answer any of these questions
itself."

## RUN_RESULT (abridged)
```yaml
RUN_RESULT:
  status: COMPLETE
  summary: "Weighted 11-domain architecture for tipster subscription decision; 158 expansion + 52 polishing iterations validated; 1 domain carries open coverage debt."
  artifacts: [PROJECT_RESEARCH_BRIEF.md, MASTER_RESEARCH_PROGRAM.md, DOMAIN_MAP.md, COVERAGE_DEBT.md, GAP_LEDGER.md, CHECKPOINT.md, EXECUTOR_START_PROMPT.md]
  decisions: ["Copy-betting feasibility split into its own domain rather than folded into 'model selection'"]
  unresolved: ["Copy-betting technical/regulatory feasibility domain carries 8 iterations of coverage debt", "WTP-by-model contradiction (founder hypothesis vs. no incumbent proof) unresolved"]
  handoff: {next_skill: "ai-resource-router", reason: "9 primary-evidence-trigger iterations need routing to interview/survey tooling before execution begins"}
  quality:
    iteration_counts: {scope_expansion: 158, domain_polishing: 52, total_valid: 210, discarded_no_material_delta: 14}
    coverage_debt_open: 1
    key_area_weighting_applied: true
    domain_map_interconnected: true
    ten_pass_qa_complete: true
    stopped_before_execution: true
```

Note what did NOT happen: no bookmaker limiting thresholds, subscriber
willingness-to-pay figures, or trust-verification findings were actually
looked up or answered — those are execution-stage work for whatever
consumes `EXECUTOR_START_PROMPT.md` next.
