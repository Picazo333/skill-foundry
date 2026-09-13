# ARCHITECTURE — UNIVERSAL SKILL CONTRACT

## Principle
One canonical skill, multiple thin adapters.

A skill is a bounded capability with:
- explicit trigger and non-trigger;
- input contract;
- executable procedure;
- bounded autonomy;
- artifact outputs;
- stop condition;
- QA/evals;
- downstream handoff.

It is not a personality prompt.

## Required final folder contract
```text
skills/<skill>/
├── SKILL.md
├── README.md
├── manifest.json
├── schemas/
│   ├── input.schema.json
│   └── output.schema.json
├── templates/
├── references/
├── examples/
├── evals/
│   ├── cases/
│   └── README.md
└── adapters/
    ├── generic.md
    ├── chatgpt.md
    ├── codex.md
    ├── claude.md
    ├── gemini.md
    └── cursor.md
```

## Standard run envelope
Input:
```yaml
RUN_REQUEST:
  objective:
  source_artifacts:
  known_context:
  constraints:
  desired_output:
  mode:
  prior_run:
```

Output:
```yaml
RUN_RESULT:
  status:
  summary:
  artifacts:
  decisions:
  unresolved:
  handoff:
  quality:
```

## Supported modes
Where relevant: `QUICK`, `STANDARD`, `DEEP`, `AUDIT`, `UPDATE`, `AUTONOMOUS`.

## Handoff rule
Pass canonical artifacts + decisions + unresolved items + constraints + next-skill recommendation. Do not use the whole conversation as the primary handoff.

## Context policy
Every final skill must declare:
- `REQUIRED_CONTEXT`
- `OPTIONAL_CONTEXT`
- `DO_NOT_LOAD_BY_DEFAULT`

Prefer canonical artifacts to historical chat context.
