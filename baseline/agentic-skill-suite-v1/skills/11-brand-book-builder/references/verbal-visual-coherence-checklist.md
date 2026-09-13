# Reference: verbal/visual coherence checklist

Used in `SKILL.md` step 6 — the core gate that distinguishes this skill from
a mechanical copy-paste compile. Run every item below against the 6 source
artifacts. Any "no" or "unclear" answer is a flagged coherence gap: record
it, do not resolve it by editing either source's meaning.

## 1. Audience alignment
- Does the audience implied by `VERBAL_IDENTITY.md`'s tone (formality,
  vocabulary, humor level) match the audience implied by
  `IDENTITY_SYSTEM.md`'s color/type/imagery choices (e.g. a playful, warm
  voice paired with a stark, corporate visual system is a mismatch worth
  flagging)?
- Does `MESSAGE_HIERARCHY.md`'s stated target audience match any audience
  language in `IDENTITY_SYSTEM.md` or `APPLICATION_RULES.md`?

## 2. Positioning consistency
- Do `MESSAGE_HIERARCHY.md`'s pillars/differentiators show up anywhere in
  `IDENTITY_SYSTEM.md`'s application rules or rationale — or does the visual
  system pull toward a different category/positioning than the verbal
  canon claims (e.g. voice claims "premium, quiet" while the visual system's
  reference points read "budget, loud")?
- Does either artifact make a category or competitive claim
  (explicitly or through category-convention choices) that the other
  contradicts or never acknowledges?

## 3. Register consistency across the same surface
- For any surface `APPLICATION_RULES.md` and `VOICE_EXAMPLES.md` both
  cover (e.g. social, product/UI), do the two artifacts' guidance actually
  read as the same register when applied together? Draft a one-line mental
  application (don't publish it) and check the voice and visual feel like
  one brand, not two overlaid on the same page.

## 4. Constant vs. contextual mismatch
- Does `VERBAL_IDENTITY.md`'s tone modulation matrix (what changes by
  context: sales, support, crisis, etc.) have any counterpart in
  `IDENTITY_SYSTEM.md`/`APPLICATION_RULES.md` (does the visual system also
  modulate by context, or is it static)? A static visual system paired with
  a highly contextual voice isn't automatically wrong, but is worth noting
  in governance so application authors don't assume visual modulation exists
  where it doesn't.

## 5. Traceable-to-different-strategy check
- If `BRAND_STRATEGY.md` is supplied: does each artifact's core claim trace
  to the *same* positioning statement/differentiator in it? If
  `VERBAL_IDENTITY.md` traces its principles to one differentiator and
  `IDENTITY_SYSTEM.md` traces its visual choices to a different one (both
  legitimately present in an earlier, broader strategy), that is exactly the
  "built for subtly different positioning" gap this check exists to catch —
  flag it even though neither artifact is individually wrong.
- If `BRAND_STRATEGY.md` is not supplied: state that this specific check
  could not be run against a shared source, as an explicit limitation, not a
  silent skip.

## Recording a gap
For each gap found, log in `BRAND_BOOK_ASSET_CHECKLIST.md` and
`RUN_RESULT.unresolved`:
- The specific artifacts/lines in tension.
- Why it matters operationally (what a designer/writer would get wrong if
  they didn't know).
- Which upstream skill (`brand-verbal-identity` or `brand-identity-system`,
  or both, or `brand-strategy` if the root cause is upstream of both) should
  resolve it.

Never leave a gap unrecorded because "it's probably fine" — an unrecorded
gap is the exact silent-invention failure mode this skill exists to
prevent, just inverted (silently ignoring instead of silently patching).
