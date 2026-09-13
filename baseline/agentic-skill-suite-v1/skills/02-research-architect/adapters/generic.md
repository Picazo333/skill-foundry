# Generic adapter — Research Architect

For any chat-based LLM interface with file upload or paste support.

## Invocation
Paste or reference `SKILL.md` as a system/instruction message, then supply
the `RUN_REQUEST` fields as a message (objective, mode, constraints, etc.).
For `mode: AUTONOMOUS`, tell the model explicitly it should not pause for
confirmation between iterations or phases — some chat interfaces otherwise
default to turn-by-turn interaction; state that checkpoints substitute for
confirmation, not replace them.

## File I/O
- **Reading sources:** paste text directly, or upload `PROJECT_CANON.md` /
  a prior `MASTER_RESEARCH_PROGRAM.md` / `CHECKPOINT.md` if resuming.
- **Writing outputs:** the assistant returns the 7 required artifacts as
  separate, clearly delimited markdown blocks (one per artifact), including
  `CHECKPOINT.md` at every logical block boundary specified in `SKILL.md` —
  not just once at the end, since a long 200+iteration run may exceed a
  single response and need to continue across turns.

## Environment constraints
No filesystem access assumed and no guaranteed single-response length for a
200+iteration program. If the interface truncates long responses, the
assistant must checkpoint and continue in a follow-up turn rather than
silently truncating `MASTER_RESEARCH_PROGRAM.md`. On any new session, the
user must re-paste the last `CHECKPOINT.md` plus artifacts to resume — no
persistent memory is assumed.

## Fallback
N/A — this is the baseline all other adapters specialize.
