# IMPLEMENTATION PLAN — <product name>
_Mode: <AUDIT (new plan) | QA (follow-up plan)> · Run date: <date> · Built by: product-auditor v1.0.0_
_Source: PRODUCT_AUDIT.md, findings <C#/S# refs>_

> This plan is the acceptance contract for an execution agent. An executor
> should not need to reinterpret product intent. Do not implement from this
> document in AUDIT/QA mode — hand off via `ai-resource-router`.

## Implement-now
Ordered for data safety and to avoid rework (migrations before dependent
UI/behavior; shared-dependency items before items that build on them).

### Item <N> — <short title>
- **Problem:** <what's wrong, referencing PRODUCT_AUDIT.md finding ID>
- **Target behavior:** <what correct looks like>
- **Affected components/data/routes:** <explicit list>
- **Dependencies:** <other item #s that must land first, or "none">
- **Migration required:** <yes/no — if yes: migration step + rollback note>
- **Risks:** <what could break>
- **Do NOT touch:** <explicitly protected existing behavior/components>
- **Tests:** <what proves this — unit/integration/manual walkthrough>
- **Acceptance criteria:** <checklist an executor and QA both verify against>

<repeat per item>

## Backlog
Approved but not implement-now this pass, with reason for deferral.
- <item> — deferred: <reason> — severity/complexity: <ref>

## Discarded
Reported but not approved for any plan, with reason (mirrors
`PRODUCT_AUDIT.md` discarded section; kept here for executor visibility).
- <item> — discarded: <reason>

## Sequencing summary
1. <item #> — <why first: e.g. migration>
2. <item #> — <why next: e.g. depends on 1>
...
