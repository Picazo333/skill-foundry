# Worked example — executive deck brief

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "Series A pitch deck core narrative for Nimbus Robotics"
  source_artifacts:
    - "BRAND_BOOK.md (Nimbus Robotics: warehouse-automation hardware+software; positioning: 'the retrofit, not the rebuild' — installs on existing warehouse racking rather than requiring a new facility; voice: confident, engineer-credible, avoids hype language like 'revolutionary'/'game-changing'; visual: deck template exists with defined chart style — bar/line only, no 3D chart effects)"
  known_context:
    deliverable_type: "investor pitch deck, core narrative"
    channel: "in-person + emailed PDF"
    audience: "Series A investors, general partners with some but not deep robotics background"
    offer: null
    cta: "request a follow-up technical demo"
  constraints: ["under 15 slides for the core narrative; appendix separate"]
  desired_output: full_brief_set
  mode: STANDARD
  prior_run: null
```

## Output (abridged)

**CREATIVE_BRIEF.md** (excerpt):
```
## Audience & Context
- Who: Series A GPs, some but not deep robotics background — avoid unexplained jargon, but do not oversimplify the technical differentiation (retrofit vs. rebuild) since that IS the investment thesis.
- Job of the asset: get a follow-up technical demo booked.

## Single-Minded Message
> You don't need to rebuild your warehouse to automate it.

## Brand Mandatories
| Mandatory | Rule | Source |
|---|---|---|
| Voice | Confident, engineer-credible; no "revolutionary"/"game-changing"/hype language | BRAND_BOOK.md § Verbal Identity |
| Visual | Bar/line charts only, no 3D effects; use defined deck template | BRAND_BOOK.md § Visual System |

## Format & Channel Specs
| Variant | Spec | Notes |
|---|---|---|
| Core narrative | <=15 slides | per RUN_REQUEST constraint |
| Appendix | separate, no slide cap | technical deep-dive, financials |

## Acceptance Criteria
- [ ] No slide uses "revolutionary," "game-changing," "disruptive" or equivalent hype language.
- [ ] All charts are bar/line, using the defined deck template — no 3D chart effects.
- [ ] Core narrative deck is 15 slides or fewer, not counting appendix.
- [ ] Closing slide contains the "request a technical demo" CTA.
```

**PRODUCTION_HANDOFF.md** (excerpt): execution medium = designer/copywriter
pair using the existing deck template file; delivery as .pptx + exported
PDF; review against acceptance criteria before it goes to the founder for
final sign-off.

Note what did NOT happen: the brief did not soften the technical retrofit-
vs-rebuild differentiation to make it more "accessible" — the audience note
explicitly says not to oversimplify the actual investment thesis, since
that's the single-minded message itself.
