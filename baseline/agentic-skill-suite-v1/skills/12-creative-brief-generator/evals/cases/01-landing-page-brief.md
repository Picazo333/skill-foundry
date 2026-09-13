# Eval Case — Landing page hero brief

## Scenario
A B2B SaaS brand needs a landing page hero for a new paid tier launch,
targeted at existing free-tier users. Tests that the brief pulls only the
canon relevant to a web deliverable, resolves to one message/CTA, and
respects an explicit non-canon constraint (no discount language) supplied in
the request rather than defaulting to industry-standard promo copy.

## Input
```yaml
RUN_REQUEST:
  objective: "landing page hero for Ledgerly's Q3 pricing-tier launch"
  source_artifacts:
    - "BRAND_BOOK.md (positioning: 'the compliance layer you don't have to think about'; voice: direct, no jargon, second person; visual: navy/white, teal accent reserved for CTAs only)"
  known_context:
    deliverable_type: "landing page hero section"
    channel: "web"
    audience: "existing free-tier users"
    offer: "new 'Pro' tier: automated compliance filing"
    cta: "Upgrade to Pro"
  constraints: ["no discount language — pricing is not currently on promotion"]
  desired_output: full_brief_set
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Canon extraction pulls positioning, voice and the CTA-only teal rule —
   not the brand's full visual/voice guide.
2. Exactly one single-minded message and one CTA are produced.
3. No discount/promotional language appears anywhere in the brief, honoring
   the stated constraint even though such copy is common for tier-upgrade
   pages.
4. Every brand mandatory in `CREATIVE_BRIEF.md` cites a canon section.

## Expected artifacts
- `CREATIVE_BRIEF.md` — single message tied to automated filing (not
  generic "upgrade now" framing), mandatories table citing BRAND_BOOK.md
  sections, no discount language, checkable acceptance criteria.
- `ASSET_REQUIREMENTS.md` — lists the Pro-tier feature screenshot/asset
  needed, with an owner.
- `PRODUCTION_HANDOFF.md` — names designer/Figma as execution medium and
  points to `brand-quality-auditor` as next step.

## Forbidden behavior
- Must not include discount/promotional/urgency language.
- Must not paste the entire brand book's voice/visual sections verbatim.
- Must not produce two competing headline candidates instead of one message.

## Pass criteria
- [ ] All three required artifacts exist.
- [ ] Exactly one key message and one CTA.
- [ ] No discount/promo language anywhere in `CREATIVE_BRIEF.md`.
- [ ] Every mandatory cites a specific canon source.
