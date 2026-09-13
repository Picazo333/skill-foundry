# Worked example — medical compliance tone

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "build verbal identity for a continuous glucose monitor companion app"
  source_artifacts:
    - "BRAND_STRATEGY.md (positioning: 'the CGM app that tells patients what a number means, not just the number'; audience: newly diagnosed Type 2 diabetics, anxious about self-management; differentiator: plain-language explanation of readings validated by an endocrinologist review board; proof point: every explanation string reviewed and signed off by the board before ship)"
  known_context: null
  constraints: ["FDA-adjacent claims restrictions apply — cannot state or imply diagnosis, treatment efficacy, or medical advice"]
  desired_output: full_verbal_system
  mode: STANDARD
  prior_run: null
```

## Output (abridged)

**VERBAL_IDENTITY.md** (excerpt):
```
### 1. Explain the number before reassuring about it
Traces to: differentiator — "tells patients what a number means, not just the number"
DO: "182 mg/dL is above your target range of 80–130. This usually happens after a
     high-carb meal or missed dose — here's what tends to bring it back down."
DON'T: "Don't worry — a lot of people see numbers like this!"

### 2. Never phrase an explanation as medical advice
Traces to: constraint — FDA-adjacent claims restrictions
DO: "Readings like this are often linked to timing of your last meal. Talk to your
     care team about whether an adjustment makes sense for you."
DON'T: "You should take your insulin now."

## Prohibited claims
- Any phrasing that implies the app diagnoses a condition ("this means you have...").
- Any phrasing that implies the app recommends a treatment/dosage change
  without deferring to the user's care team.
- Any reassurance phrased as a guarantee of outcome ("this will bring your
  levels down").
- Mark any claim outside these two categories that a writer is unsure about
  NEEDS LEGAL REVIEW rather than guessing.
```

**MESSAGE_HIERARCHY.md** (excerpt):
```
Pillar 1: Endocrinologist-reviewed, not algorithm-guessed
Proof point: every explanation string signed off by the review board before ship
One line: "Every explanation is reviewed by an endocrinologist before it reaches you."
```

**VOICE_EXAMPLES.md** (excerpt, principle 2, format: error/empty state):
```
DO: "We can't generate an explanation for this reading pattern yet. Your care
     team can help interpret it in the meantime."
DON'T: "Hmm, something's off with this one! Might want to get that checked out."
Stress test note: a competitor without board-reviewed content couldn't safely
make either claim in the DO column — "we can't explain this yet" is only
crediblewhen every explanation the app *does* give is reviewed, per Pillar 1.
```

Note what did NOT happen: the skill did not invent a friendlier, punchier
DON'T-avoidance voice ("innovative diabetes companion!") — every principle
stays anchored to the reviewed-explanation differentiator and the FDA-adjacent
constraint, and the prohibited-claims section is present because the
constraint was explicitly supplied.
