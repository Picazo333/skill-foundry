# PRODUCT AUDIT — <product name>
_Mode: <AUDIT | QA> · Run date: <date> · Built by: product-auditor v1.0.0_
_Objective: <audit objective from RUN_REQUEST>_

## Scope inspected
Routes/states/data actually walked this run (not the whole app if scope was
narrower).
- <route/state> — <what was checked>

## Confirmed findings
Reproduced or directly evidenced. Never blended with suspected findings.

| # | Finding | Category | Evidence | Severity |
|---|---|---|---|---|
| C1 | <finding> | regression \| missing-feature \| redundant-UI \| data-risk \| mobile-parity \| simplification | <repro steps / code ref / data ref> | P0–P3 |

## Suspected findings
Plausible but not independently verified this run. Never enters
`IMPLEMENTATION_PLAN.md` as implement-now without a reproduction step.

| # | Finding | Category | Why suspected | Reproduction needed |
|---|---|---|---|---|
| S1 | <finding> | <category> | <reasoning> | <what would confirm it> |

## Canon/prior-audit contradictions
Findings that contradict `PROJECT_CANON.md` locked decisions or a prior
`PRODUCT_AUDIT.md`/`IMPLEMENTATION_PLAN.md`.
- <contradiction> — canon says X, current state shows Y — source: <canon ref>

## Discarded items
Reported items intentionally not carried forward, with reason. Never a
silent drop.
- <item> — discarded: <reason>

---
## QA-mode section (only populated when `mode: QA`)
Verdict per `IMPLEMENTATION_PLAN.md` item being audited, with cited evidence.
No verdict without evidence — mark `unable to verify` rather than guessing.

| Plan item | Verdict | Evidence | Notes |
|---|---|---|---|
| <plan item ref> | done \| partial \| not done \| unable to verify | <route walked / test run / code inspected> | <what's missing, if partial/not done> |

New findings surfaced during QA (not in the original plan) flow into a
follow-up `IMPLEMENTATION_PLAN.md`, classified per the tables above — never
folded silently into "done".
