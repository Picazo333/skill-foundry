# Evals — AI Resource Router

4 cases in `cases/`: 3 core scenarios (from `SPEC.md`'s required eval
scenarios) + 1 edge/failure case. Each follows
`/shared/templates/EVAL_TEMPLATE.md`.

| Case | Type | Tests |
|---|---|---|
| `01-mixed-quota-day.md` | core | multi-tool batch, capability fit vs. opportunity pressure, concurrency cap |
| `02-single-capable-model-despite-expiring-quota.md` | core | capability fit beats quota-burning even under expiry pressure |
| `03-two-accounts-same-provider-different-resets.md` | core | two accounts of one provider treated as separate resources with independent reset clocks |
| `04-edge-no-tool-satisfies-constraints.md` | edge/failure | must NOT force-route a task no available tool can actually do |
