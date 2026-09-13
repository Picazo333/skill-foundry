# Worked example — B2B automation agency with unclear offer

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "build discovery brief for a B2B workflow-automation agency, offer is not clearly defined yet"
  source_artifacts:
    - "founder_email_thread.txt (3 founders, disagree on core offer)"
    - "current_site_copy.txt ('We help businesses automate everything')"
    - "past_client_list.txt (7 past clients: 2 e-commerce, 3 logistics, 2 healthcare admin)"
  known_context: null
  constraints: ["no additional stakeholder interviews possible this round"]
  desired_output: full_discovery_set
  mode: STANDARD
  prior_run: null
```
Email thread excerpts — Founder A: "We're really a consulting shop that
happens to build automations." Founder B: "No, we're a productized service
— fixed-scope workflow builds, that's what scales." Founder C: "Half our
revenue is actually just ongoing retainer support, we should lean into
that." No agreement reached in the thread.

## Output (abridged)

**BRAND_DISCOVERY_BRIEF.md**
```
## FACTS
- 7 past clients: 2 e-commerce, 3 logistics, 2 healthcare admin — source:
  past_client_list.txt

## CLAIMS
- "We're really a consulting shop" — asserted by: Founder A, source:
  founder_email_thread.txt
- "We're a productized service — fixed-scope workflow builds" — asserted
  by: Founder B, source: founder_email_thread.txt
- "Half our revenue is ongoing retainer support" — asserted by: Founder C,
  source: founder_email_thread.txt — note: stated as a revenue fact but no
  financial data supplied to verify the "half" figure; kept as CLAIM
  pending a source per fact-vs-opinion-rubric.md's ambiguous-statement rule.

## Contradictions
- **Business model definition: consulting vs. productized fixed-scope vs.
  retainer support** — side A (Founder A): consulting shop; side B (Founder
  B): productized fixed-scope builds; side C (Founder C): retainer/ongoing
  support is the real revenue driver. All three sources: founder_email_thread.txt.
  This is not a stylistic disagreement — it changes what the business
  fundamentally sells, and the thread shows no resolution. Passed to
  brand-strategy unresolved, not picked.

## Discovery axes
### Business objective
- Not stated — HYPOTHESIS (unconfirmed): the offer-definition disagreement
  itself may be the actual trigger for seeking brand discovery (i.e., brand
  work is being used to force an offer decision). Flagged explicitly as
  inference, not extracted from any source, for brand-strategy to confirm
  with the founders before treating as objective.
```

**DISCOVERY_GAPS.md**
```
| Gap | Blocks | Closing question | Owner |
|---|---|---|---|
| No agreed definition of the core offer | positioning axis, competitive frame | "Which of consulting / productized builds / retainer support is the primary offer, or is it genuinely a blend — and if a blend, which is the entry point for new clients?" | all 3 founders jointly |
| Business objective for doing brand work now | business objective | "What prompted brand discovery now — is it meant to force the offer decision, or is the offer decision assumed settled already?" | founders |

Constraint noted: "no additional stakeholder interviews possible this
round" (RUN_REQUEST.constraints) means these gaps cannot be closed within
this run — they are logged as material and blocking, with status: PARTIAL
or BLOCKED as appropriate, rather than guessed at to force a COMPLETE brief.
```

**REFERENCE_MAP.md**
```
No references or anti-references were named in any supplied source
material. Section left empty rather than inferring references from the
client industries (e-commerce/logistics/healthcare admin) — inferring a
visual/verbal reference nobody named would be inventing source material.
```

Note what did NOT happen: the skill did not pick a side among the three
founders' competing definitions of the business, and did not treat
Founder C's "half our revenue" claim as a verified fact just because it was
stated as a number. With no interview round possible, `RUN_RESULT.status`
would be `PARTIAL` (a usable but incomplete brief with clearly flagged
blocking gaps), not `COMPLETE`.
