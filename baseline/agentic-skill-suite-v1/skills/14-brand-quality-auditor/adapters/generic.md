# Generic adapter — Brand Quality Auditor

For any chat-based LLM interface with file upload or paste support.

## Invocation
Paste or reference `SKILL.md` as a system/instruction message, then supply
the `RUN_REQUEST` fields as a message: the artifact to audit, the brand
canon artifact(s) to audit against, objective, mode. If no canon is
supplied, the run must return `BLOCKED` — say this explicitly in the
invocation instructions so a chat-only interface doesn't skip the canon
gate.

## File I/O
- **Reading sources:** paste text/HTML directly, upload images/files if
  supported, or paste links/descriptions of the artifact under audit.
  Canon artifacts (verbal/visual/strategy) must be pasted or uploaded
  alongside it — never assumed from memory of an earlier turn.
- **Writing outputs:** the assistant returns the three required artifacts
  (`BRAND_QA_REPORT.md`, `FIX_LIST.md`, `DRIFT_REGISTER.md`) as separate,
  clearly delimited markdown blocks so they can be saved as separate
  files by the user.

## Environment constraints
No filesystem access assumed. The user is responsible for saving the
returned artifacts and re-supplying both the canon and the prior
`DRIFT_REGISTER.md`/`BRAND_QA_REPORT.md` on the next `mode: UPDATE` run —
neither is reconstructable from chat memory alone.

## Fallback
N/A — this is the baseline all other adapters specialize.
