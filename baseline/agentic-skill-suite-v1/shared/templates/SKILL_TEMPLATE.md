# [SKILL NAME]

> Canonical skill definition. Adapters in `adapters/` are thin wrappers over
> this file — they may not change purpose, procedure, outputs, quality gates
> or stop conditions. See `PORTABILITY.md` and `shared/adapters/README.md`.

## Identity
- **ID:** `<skill-id>`
- **Category:** `<category>`
- **Version:** `1.0.0`
- **Purpose:** one sentence — what canonical truth or artifact this skill produces.

## Trigger
Use this skill when:
- ...

## Non-trigger
Do not use this skill for:
- ...
(If another skill is the correct one, name it.)

## Context policy
- **REQUIRED_CONTEXT:** the minimum artifacts/facts that must be loaded before running.
- **OPTIONAL_CONTEXT:** artifacts that improve quality but are not blocking.
- **DO_NOT_LOAD_BY_DEFAULT:** context that is expensive, irrelevant by default,
  or would bias the run (e.g. full conversation history, unrelated skills' canon).

Prefer canonical artifacts over conversational memory (`ARCHITECTURE.md`).

## Inputs

### Minimum inputs
- ...

### Optional inputs
- ...

### RUN_REQUEST envelope
```yaml
RUN_REQUEST:
  objective:
  source_artifacts:
  known_context:
  constraints:
  desired_output:
  mode:        # QUICK | STANDARD | DEEP | AUDIT | UPDATE | AUTONOMOUS (only modes this skill supports)
  prior_run:   # checkpoint/artifact reference, if resuming
```

## Procedure
Numbered, executable steps — not a description of "AI best practices". Each
step should be concrete enough that two independent runs against the same
inputs converge on materially the same artifact.

1. ...
2. ...
3. ...

### Checkpoints
When and what to checkpoint mid-run (for long/autonomous procedures). State
what "resume from checkpoint" means concretely for this skill.

## Outputs

### Required output artifacts
- `ARTIFACT_NAME.md` — one line on what it contains.

### RUN_RESULT envelope
```yaml
RUN_RESULT:
  status:      # COMPLETE | PARTIAL | BLOCKED
  summary:
  artifacts:
  decisions:
  unresolved:
  handoff:
  quality:
```

### Output schema
See `schemas/output.schema.json` for the machine-checkable shape of the
artifact set / RUN_RESULT.

## Handoffs
Which skills this one hands off to, and what exactly it passes (canonical
artifacts + decisions + unresolved items + constraints + a recommended next
skill — never "read the whole conversation").

- → `<skill-id>` — why / what's passed.

## Failure modes
Concrete ways this skill can go wrong, and what to do instead:
- **<failure mode>** — <detection> → <corrective behavior>.

## Quality gates
Skill must satisfy `QUALITY_GATES.md` skill-level gates 1–10, plus any
skill-specific gates below:
- ...

## Stop conditions
- Normal completion: ...
- Blocked (insufficient input): ...
- Never continue past: ...

## Examples
See `examples/` for at least one worked input → output pair.

## Evals
See `evals/` — minimum 3 scenarios + 1 edge/failure case, using
`shared/templates/EVAL_TEMPLATE.md`.
