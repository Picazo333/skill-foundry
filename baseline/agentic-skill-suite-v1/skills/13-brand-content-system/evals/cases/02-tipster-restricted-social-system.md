# Eval Case — Tipster / restricted social content system

## Scenario
A sports-betting tipster brand needs a content system under heavy platform
and regulatory restriction (age-gating, no guaranteed-win claims, several
platforms restrict gambling content entirely). Tests that the skill derives
pillars from the brand's actual edge (a documented staking/track-record
methodology) rather than generic "hot tips" content, and that channel-role
assignment correctly excludes/restricts channels the vertical can't safely
use natively.

## Input
```yaml
RUN_REQUEST:
  objective: "build content system across the channels this vertical can actually use"
  source_artifacts:
    - "BRAND_STRATEGY.md (approved): positioning = 'the only tipster who
       publishes the losing bets too'; differentiator = full public
       staking record including losses, published same-day; audience pain
       = distrust of tipsters who only show wins; proof point = 3-year
       public staking log"
    - "VERBAL_IDENTITY.md (approved): direct, no hype language; banned:
       'guaranteed', 'can't lose', 'sure thing', any implied win-rate
       promise not tied to the published log; must include age-gate/
       responsible-gambling notice on every piece"
  known_context:
    channels_in_use: ["X/Twitter", "Telegram", "YouTube"]
    production_capacity: "1 person, ~5hrs/week"
    vertical_constraints: ["18+ age-gating required every post", "no guaranteed-outcome language (ad standards)", "some platforms restrict gambling ad content by policy"]
  constraints: ["must not run into platform gambling-content policy violations"]
  desired_output: full_system
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Pillars trace to the "publishes losses too" differentiator and the
   3-year public staking log — not a generic "daily tips" or "hot picks"
   category.
2. Channel-role map addresses platform gambling-content policy explicitly
   per channel (e.g. Telegram/owned-audience channel may carry more direct
   pick content than a public feed subject to ad policy).
3. Compliance boundaries include the age-gate requirement and banned
   language list applied per pillar/channel, not as a single footer note.
4. Cadence reflects the stated 1 person / 5hrs/week capacity with
   arithmetic shown.

## Expected artifacts
- `CONTENT_PILLARS.md` — pillars traced to the loss-transparency
  differentiator and staking log, explicitly distinct from "hot tips."
- `CONTENT_PIPELINE.md` — compliance table listing age-gating and banned
  language per pillar/channel; cadence arithmetic against 5hrs/week.
- `CONTENT_SYSTEM.md` — channel-role map that reflects the differing
  restriction level per channel, not identical treatment across all three.

## Forbidden behavior
- Must not create a "hot tips"/"today's picks" pillar with no traced source
  distinguishing it from any generic tipster account.
- Must not omit the age-gate/responsible-gambling boundary from any
  pillar/channel row.
- Must not use banned language ("guaranteed", "can't lose") anywhere in
  generated format hooks/CTAs.
- Must not assign identical, unrestricted treatment to all three channels
  when the input states platform policy varies.

## Pass criteria
- [ ] Every pillar traces to the loss-transparency differentiator or staking
      log, not a generic tips category.
- [ ] Age-gate and banned-language boundaries appear per pillar/channel.
- [ ] Channel-role map differentiates channels by restriction level.
- [ ] Cadence arithmetic is shown against the 5hrs/week capacity.
