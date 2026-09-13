# Drift-vs-Canon Comparison Method

How to compare a delivered artifact to canon (`SKILL.md` steps 2-11)
without substituting reviewer taste for canon, and how to track drift
across audits.

## 1. Canon sufficiency check (before any comparison)
For each dimension you intend to grade (strategy / verbal / visual), ask:
- Is there an explicit, approved canon artifact for this dimension?
- Does it define concrete, checkable rules (banned/approved vocabulary,
  named color roles, defined voice attributes, positioning statement) —
  not just an adjective ("modern", "premium") with nothing operational
  behind it?

If either answer is no for a dimension, that dimension cannot be graded.
Either:
- The whole run is `BLOCKED` if the *requested* objective depends on that
  dimension, or
- The dimension is explicitly marked ungraded/out-of-scope and the run
  proceeds on the dimensions that do have sufficient canon.

Never fill the gap with what "good brands generally do."

## 2. Rule-by-rule comparison, not gestalt impression
Work through canon rule by rule (not "does this feel on-brand overall").
For each rule:
1. State the rule as canon defines it.
2. Find the specific evidence in the artifact (a quote, a color hex, a
   layout element) that the rule applies to.
3. Classify: does the evidence comply, violate, comply-but-weakly, or is
   compliance undecidable from canon as written (→ `DEFER`)?

This keeps every finding traceable and prevents a single strong
impression ("this whole page feels off") from silently deciding many
individual rule outcomes.

## 3. Distinguish violation from missing coverage
A canon rule that simply doesn't address something in the artifact is not
a violation of that rule — it's uncovered territory. Don't invent a
violation by analogy to a different rule. If the artifact does something
canon never addresses at all, either:
- it's genuinely out of scope (log as observation), or
- it's material enough to need a canon decision (→ `DEFER`, handoff to
  the owning brand skill).

## 4. Drift vs. regression vs. accepted deviation
When a prior audit exists (`mode: UPDATE`):
- **New drift** — wasn't flagged before (or didn't exist before) and now
  violates canon. Likely indicates canon erosion in day-to-day production.
- **Regression** — was flagged and marked fixed before; the same violation
  is back. Signals the fix wasn't durable (e.g. reverted, or fixed in one
  place but not templated).
- **Accepted deviation** — a known, documented exception (in
  `known_context`/`known exceptions`) that intentionally departs from
  canon. Track it for visibility in `DRIFT_REGISTER.md`, but never
  reclassify it as a fresh `FIX` unless the exception's scope has been
  exceeded.

## 5. Keep the classification honest under time pressure
`FIX` is reserved for actual canon violations, not "the ideal version of
this artifact would also do X." If the audit objective is "check for
regression" and something is a fresh, non-regressed quality issue, it's
still a real finding — classify by canon compliance, not by whether it
fits the stated objective's framing.

## 6. When canon itself conflicts
If two canon sources disagree (e.g. old brand book unrevised section vs.
newer verbal identity doc), do not silently pick one. Classify the
relevant items as `DEFER`, note the canon conflict explicitly in
`unresolved`, and hand off to `brand-book-builder` to reconcile canon —
auditing is not the place to resolve upstream canon contradictions.
