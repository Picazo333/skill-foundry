# Drift Register

**Artifact:** <name/link/path>
**Canon baseline:** <canon artifact(s), version/date>
**Prior audit (if UPDATE mode):** <path to prior DRIFT_REGISTER.md/BRAND_QA_REPORT.md, or "none — first audit">

## New drift introduced this run
Items that were PASS (or absent) in the prior audit and are now
FIX/POLISH/DEFER.

| # | Canon rule | What changed | Classification | First seen |
|---|---|---|---|---|
| | | | | <date/run> |

## Regressions
Previously FIX and marked resolved, now failing again against the same
canon rule.

| # | Canon rule | Prior resolution | Current state | Classification |
|---|---|---|---|---|

## Already-known / accepted drift
Carried forward from a prior audit, still present, not newly introduced.
Includes documented known exceptions (pre-approved deviations) — flagged
here for visibility, not reclassified as new findings.

| # | Canon rule | Status | Accepted by / when (if exception) |
|---|---|---|---|

## AI-slop / genericity trend
Running count of AI-slop checklist hits over time, each still tied to its
canon citation from `BRAND_QA_REPORT.md`.

| Run/date | Hits | Canon rules most violated | Trend vs. prior |
|---|---|---|---|
