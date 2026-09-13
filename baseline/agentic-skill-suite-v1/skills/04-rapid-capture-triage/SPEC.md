# SPEC — Rapid Capture & Triage

## Identity
**ID:** `rapid-capture-triage`  
**Category:** operations

## Purpose
Convert fast, chaotic voice-note/text capture into structured project/process/task/idea/backlog/supervision/doubt updates while preserving ambiguity and minimizing formatting work.

## Trigger when
- User dictates many updates quickly.
- Need reconcile task priorities/projects from natural language.
- Need preview before JSON/PM update.
- Need Notes-speed capture into structured system.

## Do not use for
- Long-term canonical synthesis across historical files.
- Executing tasks.
- Inventing missing priority/project assignments.

## Minimum inputs
- raw capture

## Optional inputs
- current task/project snapshot
- category taxonomy
- existing JSON
- canonical context

## Required outputs
- `CAPTURE_PREVIEW.md`
- `STRUCTURED_DELTA.json`
- `AMBIGUITIES.md`
- `APPLY_INSTRUCTIONS.md`

## Procedure
1. Segment input into atomic changes without losing wording.
2. Classify: project, process, task, recurrent, supervision, doubt, idea, backlog, remove, rename, move, preserve.
3. Detect explicit priorities/time signals and preserve relative order.
4. Match existing items to detect duplicates, renames and collisions.
5. Apply only explicit changes; preserve unmentioned data.
6. Surface true ambiguities compactly instead of blocking all capture.
7. Produce human preview grouped exactly as target system expects.
8. Produce machine delta/patch only when preview is internally consistent.

## Quality gates
- No silent deletion of unmentioned items.
- Recurrent vs supervision not conflated.
- Duplicate detection performed.
- Machine delta matches preview.
- Original ambiguity preserved.

## Handoffs
- `canonical-context-builder`
- `ai-resource-router`
- `product-auditor`

## Required eval scenarios
- Long chaotic mobile dictation.
- Task reprioritization with renames.
- Partial JSON update.

## Sonnet implementation requirements
- Turn this into an executable `SKILL.md`, not a descriptive essay.
- Define `REQUIRED_CONTEXT`, `OPTIONAL_CONTEXT`, `DO_NOT_LOAD_BY_DEFAULT`.
- Add compact input/output schemas.
- Add failure modes and stop conditions.
- Add at least 3 evals plus 1 edge/failure case.
- Reference `/shared` for common rules; do not duplicate suite boilerplate.
- Generate thin adapters for generic, ChatGPT, Codex, Claude, Gemini and Cursor.
- Ensure clean resume from artifacts/checkpoints without prior chat memory.
