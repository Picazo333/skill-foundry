# Eval Case — App/product brand (habit-tracking mobile app)

## Scenario
A consumer habit-tracking app's approved direction calls for a "quiet
momentum" grammar: soft/approachable materiality, an accent color reserved
for celebration states, and an explicit expressive-motion exception for
milestone completion against an otherwise restrained system. Tests that
the skill handles a wordmark-only (no symbol yet) architecture correctly,
keeps a celebratory accent color usable despite a failing contrast result,
and represents an explicit exception to a general motion-restraint rule
without contradicting itself.

## Input
```yaml
RUN_REQUEST:
  objective: "systematize approved direction into identity rules + tokens"
  source_artifacts:
    - "BRAND_STRATEGY.md (positioning: 'progress you can feel, without the noise')"
    - "APPROVED_VISUAL_DIRECTION.md (materiality: soft/approachable, rounded; color logic: accent reserved for streak/celebration states only; motion: restrained by default, expressive exception on milestone completion)"
  known_context: "no symbol mark yet — wordmark-led lockup only. Cap-height of wordmark = 28px at 200px-wide reference lockup. Channels in scope: iOS/Android product UI, marketing site, Instagram/TikTok, app store listing, email."
  constraints: []
  desired_output: full_system
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Step 1 derives clear space/minimum size from wordmark cap-height (the
   only available mark-relative unit, since no symbol exists) — does not
   invent symbol-based clear-space values for a mark that doesn't exist.
2. Step 2 computes the accent's contrast on every surface proposed and
   finds it fails 3:1 even against the primary brand color — narrows the
   accent to decorative/non-text use rather than dropping the color
   entirely (it's load-bearing for the "celebration" emotional beat) or
   falsely approving it for text/UI.
3. Step 4 sets the radius/iconography choices to the soft/approachable
   pole and states that pole explicitly as the reason, not as an unstated
   default.
4. Step 5 represents both the default restrained motion rule *and* the
   milestone-completion exception, rather than picking one duration/rule
   and dropping the other.
5. Step 9's audit confirms the accent's restricted-use statement is
   identical in the color-role table, the imagery/exceptions notes, and
   `DESIGN_TOKENS.json`'s description field (or equivalent), not
   contradicted anywhere.

## Expected artifacts
- `IDENTITY_SYSTEM.md` — architecture section derived from wordmark
  cap-height only; accent restricted to non-text/decorative use with the
  computed failing ratio shown; motion section states both the default and
  exception cases.
- `DESIGN_TOKENS.json` — no symbol-specific tokens invented for a
  non-existent mark; accent token still present (not deleted) with its
  restricted-use description.
- `APPLICATION_RULES.md` — social surfaces state the accent is illustration/
  celebration-state only, never on-image text color.

## Forbidden behavior
- Must not invent clear-space/minimum-size values for a symbol mark that
  was never supplied.
- Must not delete the accent color from the system because it fails
  contrast — it must be kept and correctly scoped.
- Must not present a single blanket motion duration that ignores either
  the restrained default or the milestone exception.
- Must not silently omit the materiality-axis reasoning behind the
  radius/iconography choice.

## Pass criteria
- [ ] Clear space/minimum size are derived only from the wordmark, with no
      invented symbol-mark geometry.
- [ ] The accent color remains in the system, explicitly scoped to
      decorative/celebration use, with its computed failing ratio stated.
- [ ] Both the default and milestone-exception motion rules are present
      and distinguishable.
- [ ] `DESIGN_TOKENS.json` values match `IDENTITY_SYSTEM.md` exactly,
      including the accent's usage description.
- [ ] `status: COMPLETE`.
