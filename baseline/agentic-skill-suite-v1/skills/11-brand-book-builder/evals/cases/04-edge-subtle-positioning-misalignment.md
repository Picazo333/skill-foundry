# Eval Case (edge/failure) — Subtle positioning misalignment between verbal and visual canon

## Scenario
Verbal identity and visual identity were each built competently, from
strategy work that shifted subtly between the two runs (the strategy itself
was never formally revised, but different engagements pulled from slightly
different framings of the same brand). Neither artifact is internally
inconsistent, and neither uses obviously clashing language like case 03's
"calm" vs. "urgent" — the mismatch is in who each artifact is quietly
building for. This is the case the skill must catch by actually running the
coherence check's audience/positioning cross-reference, not by pattern-
matching for an explicit contradiction.

## Input
```yaml
RUN_REQUEST:
  objective: "compile operational brand book"
  source_artifacts:
    - "VERBAL_IDENTITY.md (principles built around 'the expert who respects your time' — traced to BRAND_STRATEGY.md's differentiator: 'fastest turnaround in the category'; audience implicitly professional/B2B, terse, efficiency-focused DO examples)"
    - "MESSAGE_HIERARCHY.md (pillars: speed, reliability, expertise — all traced to the same 'fastest turnaround' differentiator)"
    - "VOICE_EXAMPLES.md (short, efficient copy across all formats, no warmth/relationship language)"
    - "IDENTITY_SYSTEM.md (rationale traces color/type choices to a DIFFERENT strategy differentiator: 'most personal, relationship-driven service in the category' — soft color palette, hand-drawn accents, warm imagery direction described as 'building a personal relationship, not a transaction')"
    - "DESIGN_TOKENS.json (matches IDENTITY_SYSTEM.md prose — warm palette, organic shapes)"
    - "APPLICATION_RULES.md (imagery guidance: 'always show a real person's face, warm and approachable' — no efficiency/speed motif anywhere)"
    - "BRAND_STRATEGY.md (supplied; contains BOTH differentiators — 'fastest turnaround' AND 'most personal, relationship-driven service' — as separate bullet points from an earlier, broader strategy phase, never reconciled into one primary differentiator)"
  known_context: null
  constraints: []
  desired_output: full_book
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Step 1 gate passes — all 6 canon artifacts plus `BRAND_STRATEGY.md` are
   individually well-formed and traced.
2. Step 6's coherence check, specifically the "traceable-to-different-
   strategy" item (`references/verbal-visual-coherence-checklist.md` #5),
   detects that `VERBAL_IDENTITY.md`/`MESSAGE_HIERARCHY.md` trace to the
   "fastest turnaround" differentiator while `IDENTITY_SYSTEM.md`/
   `APPLICATION_RULES.md` trace to the "most personal, relationship-driven"
   differentiator — two legitimate but different differentiators from the
   same strategy document, never reconciled into one.
3. This is flagged as a coherence gap even though neither individual
   artifact contradicts itself, and even though no artifact uses language
   that directly clashes with the other (unlike case 03's overt "calm" vs.
   "urgent" wording) — the skill must not treat "no explicit contradiction
   found" as "no gap," because the audience/positioning-alignment items
   (#1–#2 in the checklist) also fail here: efficiency-focused, terse voice
   vs. warm, relationship-focused imagery describe two different brand
   experiences.
4. The book is compiled with both sides shown as sourced; the gap is stated
   in Governance, the asset checklist, and `RUN_RESULT.unresolved`, citing
   `BRAND_STRATEGY.md`'s two unreconciled differentiators as the likely root
   cause.
5. `RUN_RESULT.handoff` recommends `brand-strategy` (to reconcile which
   differentiator is primary) as well as whichever of
   `brand-verbal-identity`/`brand-identity-system` built against the
   now-deprioritized one, rather than treating this as a routine handoff to
   `creative-brief-generator`.

## Expected artifacts
- `BRAND_BOOK.md` — Governance section names the specific misalignment
  (efficiency/speed voice vs. warmth/relationship visual system) and traces
  it to two different, unreconciled differentiators in `BRAND_STRATEGY.md`.
- `BRAND_BOOK_ASSET_CHECKLIST.md` — Coherence gaps table has a row for this,
  distinct in kind from a "missing example" entry.
- `RUN_RESULT` — `unresolved` names the gap; `status` is `PARTIAL` (not
  `COMPLETE`) since a designer/writer executing from the book alone would
  reasonably produce mismatched output depending which section they leaned
  on.

## Forbidden behavior
- Must NOT report `status: COMPLETE` with an empty `unresolved` on the
  reasoning that "neither artifact is individually wrong" or "nothing
  explicitly contradicts."
- Must NOT invent a reconciling third differentiator or silently favor one
  differentiator over the other while compiling (e.g. quietly warming up the
  voice section or speeding up the visual section's framing to make them
  match).
- Must NOT skip running checklist item #5 just because `BRAND_STRATEGY.md`
  was supplied and each individual artifact looks locked/complete on its
  own.

## Pass criteria
- [ ] The gap is identified from the checklist's differentiator-tracing
      item, not only from surface-level language matching.
- [ ] Neither `VERBAL_IDENTITY.md`'s nor `IDENTITY_SYSTEM.md`'s content is
      altered in the book to make the two look more aligned than they are.
- [ ] `RUN_RESULT.status` is `PARTIAL`, `unresolved` names the two
      unreconciled differentiators, and `handoff` names `brand-strategy`.
