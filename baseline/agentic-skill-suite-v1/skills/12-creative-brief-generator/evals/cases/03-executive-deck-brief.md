# Eval Case — Executive deck brief

## Scenario
A robotics startup needs a Series A pitch deck core narrative, capped at 15
slides, with a strict "no hype language" voice rule. Tests that a hard
numeric format constraint from the request and a voice-boundary canon rule
are both enforced concretely (not just gestured at) in the acceptance
criteria.

## Input
```yaml
RUN_REQUEST:
  objective: "Series A pitch deck core narrative for Nimbus Robotics"
  source_artifacts:
    - "BRAND_BOOK.md (positioning: 'the retrofit, not the rebuild'; voice: confident, engineer-credible, avoids hype language like 'revolutionary'/'game-changing'; visual: bar/line charts only, no 3D effects)"
  known_context:
    deliverable_type: "investor pitch deck, core narrative"
    channel: "in-person + emailed PDF"
    audience: "Series A GPs, some but not deep robotics background"
    cta: "request a follow-up technical demo"
  constraints: ["under 15 slides for the core narrative; appendix separate"]
  desired_output: full_brief_set
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. `CREATIVE_BRIEF.md` states the 15-slide cap as a format spec, with
   appendix explicitly separated from the cap.
2. Acceptance criteria include a checkable, specific hype-language rule
   (naming banned words/phrases, not "keep it professional").
3. Acceptance criteria include a checkable chart-style rule (bar/line only,
   no 3D).
4. The audience note does not oversimplify the retrofit-vs-rebuild
   technical differentiation, since it IS the core investment thesis.

## Expected artifacts
- `CREATIVE_BRIEF.md` — format spec table shows core narrative <=15 slides,
  appendix uncapped; acceptance criteria checklist includes the hype-
  language and chart-style checks named above.
- `PRODUCTION_HANDOFF.md` — references the existing deck template rather
  than describing a new one.

## Forbidden behavior
- Must NOT produce a vague acceptance criterion like "feels investor-ready"
  in place of the checkable hype-language/chart-style rules.
- Must NOT let the slide count exceed 15 for the core narrative in the spec.
- Must NOT flatten the retrofit-vs-rebuild thesis into generic "we automate
  warehouses" framing that loses the actual differentiation.

## Pass criteria
- [ ] Format spec states <=15 slides for core narrative, appendix separate.
- [ ] At least one acceptance criterion names specific banned hype words.
- [ ] At least one acceptance criterion checks chart style (bar/line, no 3D).
