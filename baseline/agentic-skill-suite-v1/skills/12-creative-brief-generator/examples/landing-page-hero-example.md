# Worked example — landing page hero brief

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "landing page hero for Ledgerly's Q3 pricing-tier launch"
  source_artifacts:
    - "BRAND_BOOK.md (Ledgerly: bookkeeping+compliance SaaS for solo/small-firm accountants; positioning: 'the compliance layer you don't have to think about'; voice: direct, no jargon, second person; visual: navy/white, one accent teal reserved for CTAs only)"
  known_context:
    deliverable_type: "landing page hero section"
    channel: "web, desktop + mobile"
    audience: "existing free-tier users being shown the new paid tier"
    offer: "new 'Pro' tier: automated compliance filing"
    cta: "Upgrade to Pro"
  constraints: ["no discount language — pricing is not currently on promotion"]
  desired_output: full_brief_set
  mode: STANDARD
  prior_run: null
```

## Output (abridged)

**CREATIVE_BRIEF.md** (excerpt):
```
## Objective & Success Signal
- Objective: convert free-tier users to Pro by making automated filing the obvious upgrade reason.
- Success signal: hero CTA click-through rate from existing free-tier logged-in sessions.

## Single-Minded Message
> Stop filing compliance paperwork by hand.

### Support points
1. Automated filing catches deadlines before they're missed — source: BRAND_BOOK.md § Product (Pro tier).
2. Built for solo/small-firm accountants, not enterprise bloat — source: BRAND_BOOK.md § Positioning.

### Call to action
- "Upgrade to Pro" (per requested CTA)

## Brand Mandatories
| Mandatory | Rule | Source |
|---|---|---|
| Voice | Second person, no jargon, no exclamation points | BRAND_BOOK.md § Verbal Identity |
| Visual | Teal accent reserved for CTA button only, not headline | BRAND_BOOK.md § Visual System |
| Claims | No discount/promotional language | RUN_REQUEST constraint |

## Open Flags
- none
```

**ASSET_REQUIREMENTS.md** (excerpt): approved Pro-tier feature screenshot
(mandatory, owner: product team), navy/white/teal logo lockup (mandatory,
already in brand asset library).

**PRODUCTION_HANDOFF.md** (excerpt): execution medium = designer working in
Figma; review against acceptance criteria before dev handoff; next step →
`brand-quality-auditor` once a draft exists.

Note what did NOT happen: the brief did not add a discount/urgency line even
though "Upgrade to Pro" style CTAs often pair with one elsewhere in the
industry — the stated constraint ruled it out explicitly, so it's absent
rather than snuck back in as a "best practice."
