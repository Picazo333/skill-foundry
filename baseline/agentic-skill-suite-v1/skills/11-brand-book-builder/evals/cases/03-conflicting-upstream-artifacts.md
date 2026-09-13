# Eval Case — Brand book with conflicting upstream artifacts

## Scenario
Verbal canon describes a calm, reassuring brand for risk-averse first-time
buyers; visual canon's own stated rationale describes an urgent,
high-energy system for an excitement-seeking audience, and application
rules use countdown/urgency ad motifs. This is an explicit, visible
contradiction (not a subtle one — see case 04 for that variant). Tests that
the skill surfaces rather than resolves or hides an outright conflict.

## Input
```yaml
RUN_REQUEST:
  objective: "compile operational brand book"
  source_artifacts:
    - "VERBAL_IDENTITY.md (principle: 'the calm, expert friend'; audience: risk-averse, first-time buyers wanting reassurance)"
    - "MESSAGE_HIERARCHY.md (master message: 'buying your first home without the panic')"
    - "VOICE_EXAMPLES.md (calm, reassuring DO/DON'T pairs throughout)"
    - "IDENTITY_SYSTEM.md (high-saturation red/black system; rationale states: 'urgent, high-energy, for a fast-moving audience that wants excitement, not hand-holding')"
    - "DESIGN_TOKENS.json (matches IDENTITY_SYSTEM.md)"
    - "APPLICATION_RULES.md (countdown/urgency ad motifs, 'act now' CTAs, flashing accent color)"
  known_context: null
  constraints: []
  desired_output: full_book
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Step 1 gate passes — all artifacts present and individually well-formed.
2. Step 6 coherence check compares audience/register across verbal and
   visual canon and finds a direct conflict: two different audiences
   ("risk-averse, wants reassurance" vs. "excitement-seeking, wants no
   hand-holding") and two different emotional registers.
3. The book is still compiled — both sides shown as sourced, neither edited
   to soften or match the other.
4. The conflict is stated explicitly in `BRAND_BOOK.md`'s Governance
   section, in `BRAND_BOOK_ASSET_CHECKLIST.md`'s Coherence gaps table, and
   in `RUN_RESULT.unresolved`.
5. Step 9's usability test is marked failed/at-risk — a reader following
   different sections would produce inconsistent output — and `RUN_RESULT`
   reflects `status: PARTIAL`, not `COMPLETE`.
6. `RUN_RESULT.handoff` recommends `brand-identity-system` and/or
   `brand-verbal-identity` (and `brand-strategy` if referenced) to resolve
   the conflict, not `creative-brief-generator`.

## Expected artifacts
- `BRAND_BOOK.md` — compiled with both sides shown, governance section
  states the conflict explicitly.
- `BRAND_BOOK_ASSET_CHECKLIST.md` — Coherence gaps table has one row citing
  the specific audience/register conflict.
- `RUN_RESULT` — `status: PARTIAL`, `unresolved` names the conflict,
  `quality.usability_test_passed: false`.

## Forbidden behavior
- Must NOT soften "urgent, high-energy" or the audience language in either
  artifact's restated content to make them appear to agree.
- Must NOT pick one side (e.g. defaulting to voice as "more correct") and
  silently drop the other.
- Must NOT report `status: COMPLETE`.

## Pass criteria
- [ ] Both the calm-voice and urgent-visual language appear in `BRAND_BOOK.md`
      unedited from their sources.
- [ ] The conflict is named explicitly in at least the Governance section,
      the asset checklist, and `RUN_RESULT.unresolved`.
- [ ] `RUN_RESULT.status` is `PARTIAL`, not `COMPLETE`.
