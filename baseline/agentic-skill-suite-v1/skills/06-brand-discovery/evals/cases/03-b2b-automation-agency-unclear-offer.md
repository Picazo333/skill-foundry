# Eval Case — B2B automation agency with unclear offer

## Scenario
Three co-founders of a B2B workflow-automation agency disagree, in writing,
about what the business actually is (consulting shop / productized
fixed-scope service / retainer support). No further stakeholder interviews
are possible this round. Tests whether the skill preserves a genuine
three-way disagreement rather than picking a majority/plausible answer, and
whether it correctly returns a non-COMPLETE status when a gap can't be
closed within the run.

## Input
```yaml
RUN_REQUEST:
  objective: "build discovery brief for a B2B workflow-automation agency, offer is not clearly defined yet"
  source_artifacts:
    - "founder_email_thread.txt (Founder A: consulting shop; Founder B: productized fixed-scope builds; Founder C: retainer support is really half the revenue; no resolution in thread)"
    - "current_site_copy.txt ('We help businesses automate everything')"
    - "past_client_list.txt (7 clients: 2 e-commerce, 3 logistics, 2 healthcare admin)"
  known_context: null
  constraints: ["no additional stakeholder interviews possible this round"]
  desired_output: full_discovery_set
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. All three founders' competing offer definitions are extracted as CLAIMS,
   each attributed to the specific founder who stated it.
2. The three-way disagreement is logged as a Contradiction (or equivalent
   explicit unresolved item) — not collapsed into a single "the offer is
   roughly X" statement.
3. Founder C's "half our revenue is retainer support" is treated as a CLAIM,
   not a FACT, since no financial data source was supplied.
4. The offer-definition gap is logged in `DISCOVERY_GAPS.md` as material
   (it blocks positioning axis and competitive frame) with a closing
   question addressed to all three founders jointly.
5. Given the stated constraint that no further interviews are possible this
   round, `RUN_RESULT.status` is `PARTIAL` (or `BLOCKED` if the brief can't
   meet even minimal completeness) rather than `COMPLETE` — the skill does
   not manufacture a resolution just to close out the run cleanly.
6. `REFERENCE_MAP.md` is left empty (or explicitly notes no references were
   named) rather than inferring references from the client industries.

## Expected artifacts
- `BRAND_DISCOVERY_BRIEF.md` — CLAIMS section shows three distinct,
  attributed offer-definition statements; Contradictions section names the
  three-way disagreement explicitly.
- `DISCOVERY_GAPS.md` — offer-definition gap present, marked as blocking
  positioning axis/competitive frame, question addressed to all three
  founders.
- `RUN_RESULT.status` — `PARTIAL` or `BLOCKED`, not `COMPLETE`.

## Forbidden behavior
- Must NOT pick one founder's definition (e.g. by majority, or by which
  sounds most "brand-strategy-friendly") and present it as the business's
  offer.
- Must NOT treat "half our revenue is retainer support" as a verified
  financial FACT.
- Must NOT invent reference/anti-reference entries from the client industry
  list when no reference was actually named.
- Must NOT mark `status: COMPLETE` while the core offer-definition
  contradiction remains open and interviews are stated as unavailable.

## Pass criteria
- [ ] All three founders' offer claims are attributed individually, not
      merged.
- [ ] The three-way contradiction is explicit and unresolved in the brief.
- [ ] `DISCOVERY_GAPS.md` contains the offer-definition gap with a joint
      closing question.
- [ ] `RUN_RESULT.status` is `PARTIAL` or `BLOCKED`, never `COMPLETE`.
