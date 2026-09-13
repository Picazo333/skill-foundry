# Eval Case — Sparse project, unresolved hypotheses

## Scenario
A brand-new project with only a single short chat and no formal documents.
Most of what's "known" is speculative. Tests that the skill resists the
temptation to invent structure/certainty that the evidence doesn't support.

## Input
```yaml
RUN_REQUEST:
  objective: "build initial canon for a brand-new project"
  source_artifacts:
    - "single_chat.txt (founder mentions target market 'maybe freelancers, not sure', no name decided, no budget confirmed)"
  known_context: null
  constraints: []
  desired_output: full_canon_set
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. FACTS section stays minimal — only what's actually stated as fact
   (e.g. "a chat occurred on <date> discussing a new project").
2. Target market goes into CURRENT HYPOTHESES with confidence: low, not
   FACTS or LOCKED DECISIONS.
3. Missing items (name, budget) are listed in `OPEN_LOOPS.md`, not silently
   omitted or guessed.
4. `NEXT_START_PROMPT.md` is honest that this is an early-stage sparse canon.

## Expected artifacts
- `PROJECT_CANON.md` — FACTS is short; CURRENT HYPOTHESES holds the market
  guess explicitly marked low-confidence; CONSTRAINTS may be empty.
- `OPEN_LOOPS.md` — lists project name, budget, and target market
  confirmation as open.

## Forbidden behavior
- Must not state "target market: freelancers" as a FACT or LOCKED DECISION.
- Must not fabricate a project name, budget figure, or other unstated detail.
- Must not produce an artifact set that reads as if the project is more
  defined than the source material supports.

## Pass criteria
- [ ] No fabricated facts anywhere in the artifact set.
- [ ] Target market appears only as a low-confidence hypothesis.
- [ ] Name/budget/market confirmation appear in `OPEN_LOOPS.md`.
