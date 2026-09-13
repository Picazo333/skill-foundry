# Eval Case — Two accounts of the same provider with different resets

## Scenario
A user has two accounts with the same provider (e.g. a personal and a work
account) with independent reset clocks and different unused capacity. The
router must treat them as two separate resources, not collapse them into
one "provider" bucket, and must not assume account relationships (e.g. quota
sharing) that weren't stated.

## Input
```yaml
RUN_REQUEST:
  objective: "route 2 code-review tasks"
  constraints: []
  desired_output: full_routing_set
  mode: STANDARD
  prior_run: null
  tasks:
    - id: T1
      type: [audit]
      definition_of_done: "review PR #142 diff against style guide"
      hard_requirements: ["repo diff read access"]
      urgency: "today"
    - id: T2
      type: [audit]
      definition_of_done: "review PR #143 diff against style guide"
      hard_requirements: ["repo diff read access"]
      urgency: "today"
  tools:
    - id: providerZ_personal
      provider: providerZ
      strengths: ["code review"]
      known_capacity: "10% unused"
      reset_at: "2026-09-14T00:00:00Z"
      renewal_status: renewing
    - id: providerZ_work
      provider: providerZ
      strengths: ["code review"]
      known_capacity: "80% unused"
      reset_at: "2026-09-11T00:00:00Z"
      renewal_status: renewing
```

## Expected behavior
1. `providerZ_personal` and `providerZ_work` are normalized and reasoned
   about as two independent resources (step 2), each with its own capacity,
   reset date and opportunity-pressure calculation — never merged into one
   "providerZ" line item with summed or averaged capacity.
2. Both tools clear axis 1 for both tasks (same capability). Opportunity
   pressure (axis 2) then differentiates: `providerZ_work`'s closer reset
   (2026-09-11) and higher unused capacity (80%) gives it higher pressure
   than `providerZ_personal` (10% unused, reset further out).
3. With two same-fit tasks and two same-capability tools, the router may
   split them across both accounts (spreading load) or route by pressure —
   either is acceptable, but the reasoning must reference each account
   individually, not the provider as a whole.
4. No assumption is made that the two accounts share or pool quota — that
   was not stated in the input.

## Expected artifacts
- `ROUTING_PLAN.md` — T1 and T2 each show a rationale referencing the
  specific account (`providerZ_personal` or `providerZ_work`) individually.
- `CAPACITY_RISK.md` — lists `providerZ_personal` and `providerZ_work` as
  two separate entries with their own known/unknown fields.

## Forbidden behavior
- Must NOT merge the two accounts into a single "providerZ" capacity figure.
- Must NOT assume quota pooling/sharing between the two accounts.
- Must NOT route both tasks to `providerZ_personal` (10% unused) while
  ignoring `providerZ_work`'s much larger unused capacity and closer reset
  without a stated reason.

## Pass criteria
- [ ] `providerZ_personal` and `providerZ_work` appear as distinct entries
      throughout all artifacts, never summed/merged.
- [ ] Routing rationale for each task names the specific account.
- [ ] No quota-sharing assumption appears anywhere in the output.
- [ ] `providerZ_work`'s higher pressure (capacity × reset proximity) is
      reflected in at least one routing decision, or a stated reason is
      given for not using it.
