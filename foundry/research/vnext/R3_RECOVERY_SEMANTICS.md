# R3 — Recoverable execution semantics

Status: **DECIDED**
Gate: G2
Date: 2026-09-19

## Decision question

What recovery guarantee can VNext honestly provide using Git-persisted Foundry artifacts plus Noema WorkOrder/Handoff contracts, without adopting a persistent workflow runtime?

## Existing project evidence

Noema RC0 requires durable coordination to live in artifacts rather than conversations. Its WorkOrder contract captures objective, scope, context mode, writes/effects, expected artifacts and capability requirements. Its Handoff contract captures status, artifacts/evidence, remaining work and next action.

Foundry V5 already has candidate/checkpoint state. The gap is semantic precision: a checkpoint file must not be mislabeled as seamless replay.

## External evidence

1. LangGraph documentation, **Thinking in LangGraph**
   - https://docs.langchain.com/oss/javascript/langgraph/thinking-in-langgraph
   - Checkpointers persist state and permit later resume.
   - Resume occurs at node boundaries; work before an interrupt can re-run, so idempotency/replay-safe side effects matter.

2. LangGraph documentation, **Time travel / checkpoints**
   - https://docs.langchain.com/oss/javascript/langchain/frontend/time-travel
   - Persisted checkpoint state can be inspected and execution resumed from a selected point; this is a real runtime feature with persisted graph state.

3. Temporal documentation
   - https://docs.temporal.io/
   - Temporal offers durable execution designed to resume workflows after crashes/outages over long periods.

These systems demonstrate that genuine durable replay requires a workflow runtime/checkpointer/event-history mechanism beyond a Markdown checkpoint.

## Alternatives considered

### A. Claim seamless/durable resume from Git artifacts
Rejected. The repository does not persist live call stack/runtime execution semantics.

### B. Add LangGraph or Temporal now
Rejected. No current measured requirement justifies framework/runtime complexity before the vertical slice/canaries.

### C. Explicit reconstructive recovery
**Chosen.**

## Decision

VNext 1.0 recovery class is:

`RECONSTRUCT_FROM_REPO`

A recoverable work unit must persist enough information for a new executor to resume without reconstructing chat history:

- canonical base commit / relevant branch;
- Noema WorkOrder reference;
- Foundry candidate/portfolio/Skill/spec references;
- completed set or last completed gate/stage;
- persisted artifacts/evidence;
- Handoff status;
- remaining work;
- exact next action;
- known blockers/defects;
- effect/write boundaries;
- replay/idempotency note for any side-effectful step.

No claim of seamless replay is allowed.

## Retry rule

If a step may re-run after interruption, it must be:
- idempotent; or
- protected by explicit detection of already-completed effects; or
- routed to human/blocked state before repeating an irreversible effect.

## Noema/Foundry boundary

Use Noema:
- WorkOrder for generic work envelope;
- Handoff for complete/partial/blocked/failed transfer and remaining/next action;
- StorageRef/Artifact/EvalResult for material evidence.

Use Foundry:
- G0–G10 candidate state;
- Skill/portfolio lifecycle;
- defect/rework state;
- architecture exceptions;
- gate/CompletionCertificate semantics.

No standalone generic `Run` entity is required for the vertical slice.

## Deferred infrastructure

LangGraph/Temporal/persistent runtime remains deferred until canary or production evidence shows that reconstructive recovery causes material failure/cost.

## Confidence

High.

## Revisit trigger

Reopen if:
- interrupted G4/G5/G6 work cannot be resumed reliably from repo artifacts;
- repeated side-effect duplication occurs;
- long-running jobs require durable waits/timers/external event replay;
- manual reconstruction exceeds the complexity threshold defined by Noema's “complexity must pay rent” invariant.
