# Reference: key-area weighting method and 10-pass final QA checklist

Used in `SKILL.md` Phase 1 (weighting) and Phase 4 (final QA).

## Key-area weighting method (not blind equal distribution)

For every domain in `DOMAIN_MAP.md`, score 1-5 on four axes:

1. **Importance** — how central is this domain to the master decision
   question? (5 = the decision cannot be made without it; 1 = nice-to-know.)
2. **Uncertainty** — how unknown is the current state of this domain?
   (5 = no reliable information exists yet; 1 = already well understood.)
3. **Complexity** — how many moving parts/sub-questions does this domain
   actually contain? (5 = many interacting variables; 1 = a single fact.)
4. **Risk/decisions affected** — how much downstream harm or how many other
   decisions hinge on getting this domain right? (5 = wrong answer here
   invalidates multiple other domains' conclusions; 1 = isolated impact.)

**Weight = importance + uncertainty + complexity + risk** (max 20, min 4).

### Allocating iterations from weight
- Sum all domain weights to get a total.
- A domain's target share of the 150 scope-expansion iterations ≈
  `(domain weight / total weight) × 150`, subject to a floor (every domain
  gets at least a handful of iterations so nothing is entirely unexamined)
  and a ceiling (no single domain should consume so much of the budget that
  materially different domains go unexplored — if one domain's proportional
  share would exceed roughly a third of the total, that is itself a sign the
  domain map is too coarse and should be split into sub-domains).
- Re-check actual allocation against target at every Coverage Debt
  recomputation (`COVERAGE_DEBT.md`); a domain running persistently below
  its proportional share accrues debt.

### What "blind equal distribution" looks like (defect, not baseline)
- N domains, 150 iterations, exactly `150/N` iterations each regardless of
  weight — this is the specific failure this method exists to prevent.
- Fix: re-derive weights honestly (don't inflate low-importance domains to
  justify an even split) and re-allocate proportionally.

## 10-pass final QA checklist (Phase 4)

Run in order; log pass/fail + fix for each before advancing. A later pass
may surface a failure in an earlier one — re-run the earlier pass after
fixing, don't just patch forward.

1. **Coverage** — cross-check `DOMAIN_MAP.md` weights against actual
   iteration counts per domain (`MASTER_RESEARCH_PROGRAM.md`); no
   high-weight domain should sit near the floor.
2. **Specificity** — every surviving question names a concrete population,
   metric, mechanism, or boundary. Reject anything that reads like
   "research the market" or "understand the competition."
3. **Commercial** — pricing, unit economics, revenue model, and
   monetization angles are present wherever they bear on the master
   decision.
4. **Operational** — delivery, fulfillment, staffing, and workflow angles
   are present wherever relevant.
5. **Tech/data/automation** — confirm the workflow-first automation/AI lens
   (SKILL.md step 7) was actually applied per applicable domain, not just
   declared; spot-check that at least one iteration per operational domain
   asks the "what could be automated/AI-assisted" question.
6. **Risk/trust** — regulatory, reputational, counterparty, and
   trust-signal risks appear somewhere in the program, not only "growth"
   angles.
7. **Alternative-thesis** — for each key (high-weight) domain, at least one
   iteration actively tests the opposite of the working hypothesis, not
   only confirmatory questions.
8. **Novelty** — re-run the material-delta test across the *entire* final
   set (not just pairwise-adjacent iterations as they were added); remove
   any surviving near-duplicate.
9. **Consolidation** — Phase 3 dedupe/boundary/interconnection work is
   actually reflected in the current `DOMAIN_MAP.md` and
   `MASTER_RESEARCH_PROGRAM.md`, not sitting in a separate unmerged log.
10. **Executability** — a Research Executor could act on every surviving
    question without inventing methodology: each has a domain, a decision
    link, and (where applicable) a primary-evidence tag.
