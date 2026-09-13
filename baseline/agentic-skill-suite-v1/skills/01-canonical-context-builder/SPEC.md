# SPEC — Canonical Context Builder

## Identity
**ID:** `canonical-context-builder`  
**Category:** knowledge

## Purpose
Reconstruct and maintain the current canonical truth of a project from fragmented conversations, files, renames, decisions and prior outputs.

## Trigger when
- A project accumulated many chats/files/versions.
- Need a clean handoff to a new agent/conversation.
- Need to separate current decisions from deprecated proposals.
- Need to update canon after a completed phase.

## Do not use for
- Generic summarization with no canonical-state requirement.
- Researching facts outside supplied sources.
- Replacing uncertain data with guesses.

## Minimum inputs
- project materials or current canonical artifact
- objective of the context build/update

## Optional inputs
- prior PROJECT_CANON.md
- decision logs
- changelogs
- checkpoints
- repo state

## Required outputs
- `PROJECT_CANON.md`
- `DECISION_REGISTER.md`
- `OPEN_LOOPS.md`
- `DEPRECATED_REGISTER.md`
- `NEXT_START_PROMPT.md`

## Procedure
1. Inventory sources and rank likely authority/recency.
2. Extract entities, renames, decisions, constraints, completed work, open loops and discarded directions.
3. Resolve only evidence-resolvable conflicts; preserve unresolved conflicts explicitly.
4. Build canonical sections: FACTS, LOCKED DECISIONS, CURRENT HYPOTHESES, CONSTRAINTS, DEPRECATED, OPEN LOOPS.
5. When prior canon exists, create a delta and avoid rewriting stable sections.
6. Create a concise handoff so another agent can continue without rereading history.
7. Run contradiction and staleness passes.
8. Stop when the next agent can continue accurately from canon + referenced artifacts.

## Quality gates
- No deprecated decision appears as current.
- No unsupported fact is invented.
- Every unresolved contradiction remains visible.
- Handoff references canonical artifacts, not conversational memory.

## Handoffs
- `research-architect`
- `product-auditor`
- `brand-discovery`
- `brand-skill-orchestrator`
- `rapid-capture-triage`

## Required eval scenarios
- Regula-like project with multiple renamed versions.
- Brand project with rejected visual directions.
- Sparse project with unresolved hypotheses.

## Sonnet implementation requirements
- Turn this into an executable `SKILL.md`, not a descriptive essay.
- Define `REQUIRED_CONTEXT`, `OPTIONAL_CONTEXT`, `DO_NOT_LOAD_BY_DEFAULT`.
- Add compact input/output schemas.
- Add failure modes and stop conditions.
- Add at least 3 evals plus 1 edge/failure case.
- Reference `/shared` for common rules; do not duplicate suite boilerplate.
- Generate thin adapters for generic, ChatGPT, Codex, Claude, Gemini and Cursor.
- Ensure clean resume from artifacts/checkpoints without prior chat memory.
