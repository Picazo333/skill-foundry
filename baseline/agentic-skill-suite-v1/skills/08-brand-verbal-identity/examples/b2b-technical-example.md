# Worked example — B2B technical brand

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "build verbal identity for a database migration tool for platform engineering teams"
  source_artifacts:
    - "BRAND_STRATEGY.md (positioning: 'the migration tool that shows you the rollback plan before you run anything'; audience: senior platform/infra engineers, burned before by tools that hide failure modes; differentiator: every migration preview includes a generated rollback script and a dry-run diff; proof point: zero silent-failure incidents reported across 400+ production migrations)"
  known_context: null
  constraints: ["audience is expert-level; no explaining basic database concepts"]
  desired_output: full_verbal_system
  mode: STANDARD
  prior_run: null
```

## Output (abridged)

**VERBAL_IDENTITY.md** (excerpt):
```
### 1. Show the failure mode before the feature
Traces to: differentiator — dry-run diff + generated rollback script
DO: "Here's the rollback script, generated before this runs. Review it first."
DON'T: "Powerful, reliable migrations you can trust."

### 2. Never soften a technical fact for tone
Traces to: audience — senior engineers burned by tools hiding failure modes
DO: "This migration will lock the `orders` table for ~40s under current load."
DON'T: "This migration should be quick and painless!"

Syntax conventions:
Jargon tolerance: full category jargon assumed (table locks, WAL, dry-run)
  — audience is expert-level per constraint; no glossary-style explaining.
```

**MESSAGE_HIERARCHY.md** (excerpt):
```
Pillar 1: The rollback plan exists before you need it
Proof point: zero silent-failure incidents across 400+ production migrations
One line: "You see the rollback script before the migration runs, every time."
```

**VOICE_EXAMPLES.md** (excerpt, principle 2, format: error/empty state):
```
DO: "Dry-run detected a schema drift on `users.email_verified`. Migration
     blocked until resolved."
DON'T: "Oops! Something doesn't look quite right with your schema."
Stress test note: a competitor optimizing for approachability over disclosure
would soften this into reassurance; this principle exists specifically
because the audience distrusts reassurance from migration tools.
```

Note what did NOT happen: the skill did not add a warmth/approachability
principle by default — the "expert-level audience, no basic explaining"
constraint and the burned-before signal both point away from that, so it was
left out rather than included as a generic B2B-friendly default.
