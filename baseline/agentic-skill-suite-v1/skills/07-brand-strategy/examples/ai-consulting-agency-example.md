# Worked example — AI consulting agency

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "define positioning for a 12-person AI implementation consultancy competing against large SI firms (Accenture-scale) and solo/boutique AI consultants"
  source_artifacts:
    - "BRAND_DISCOVERY_BRIEF.md (audience: mid-market ops/IT leaders burned by a failed pilot with a big SI or a stalled internal build; evidence: 5 client interviews all cite 'we got a slide deck, not a working system' as the reason they left their prior vendor; this agency's model: every engagement ships a working production system within the first engagement, no pure-strategy-only engagements offered; team is 12 engineers, no offshore subcontracting)"
    - "competitor_map.md (large SIs: broad scope, slow, strategy-heavy; boutique consultants: fast but single-person bus-factor risk, client interviews flagged this as a real fear)"
  known_context: null
  constraints: ["cannot claim to be faster/cheaper than named competitors without data — no benchmark data was supplied"]
  desired_output: full_strategy_set
  mode: STANDARD
  prior_run: null
```

## Output (abridged)

**POSITIONING_SYSTEM.md** (excerpt — 4 territories generated):
```
Territory A — "AI experts you can trust" (generic authority claim)
  Credibility: 2 (no specific evidence beyond team's own claim of expertise)
  Distinctiveness: 1 (every AI consultancy in the frame claims trust/expertise)
  → discarded: fails both distinctiveness and credibility

Territory B — "We ship production systems, not slide decks"
  Distinctiveness: 5 (directly opposes the stated large-SI pattern client interviews named)
  Credibility: 5 (business model fact: no pure-strategy engagements offered, evidence-backed)
  Relevance: 5 (5/5 client interviews cite this exact pain point independently)
  Extensibility: 3 (ties specifically to implementation work; may strain if agency later adds pure-advisory offerings)
  Business fit: 5 (matches actual engagement model, no change required)
  Total: 23 — RECOMMENDED

Territory C — "Full team, no bus-factor risk"
  Distinctiveness: 4 (addresses the boutique-consultant fear named in competitor_map.md)
  Credibility: 4 (12 in-house engineers, no offshore subcontracting — evidence-backed)
  Relevance: 3 (fear was noted in competitive context, not directly in the 5 client interviews)
  Extensibility: 4
  Business fit: 5
  Total: 20 — discarded in favor of B (lower relevance score; kept as a supporting RTB, not the lead territory)

Commoditization swap test on Territory B: "[Agency] is the AI consultancy
that ships a working production system in the first engagement, because no
engagement type is strategy-only by design." Swapping in a large SI's name
reads as false (interview evidence says they deliver decks); swapping in a
boutique consultant's name is ambiguous on delivery but fails on the
bus-factor risk named separately. PASS as the lead territory.
```

**BRAND_STRATEGY.md** (excerpt):
```
Differentiation statement: Every engagement ships a working production
system in the first phase — no pure-strategy-only offering exists — directly
countering the "slide deck, not a system" complaint 5/5 interviewed clients
raised about prior vendors.

Reasons-to-believe:
1. No strategy-only engagement type offered — RTB source: business model, discovery brief.
2. 12 in-house engineers, no offshore subcontracting — RTB source: discovery brief; supports Territory C as a secondary proof point, not restated as the lead claim.
```

**STRATEGIC_GUARDRAILS.md** (excerpt):
```
Anti-goal: Never claim to be faster or cheaper than a named competitor —
why: constraint from RUN_REQUEST, no benchmark data supplied to back it.
Operational boundary: Any claim of "production system" must be checkable
against a real, named deliverable in case studies — test: does the proof
point name an actual shipped artifact, not just "results"?
```
