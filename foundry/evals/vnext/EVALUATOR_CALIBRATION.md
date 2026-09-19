# Evaluator Calibration Protocol

Model-based evaluators are not trusted merely because they are independent.

Before relying on an evaluator for a critical gate or after material evaluator changes:
1. run at least one known-good fixture;
2. run at least one known-bad fixture;
3. verify expected PASS/FAIL;
4. record model/tool/version where available;
5. record calibration artifact;
6. if calibration fails, mark evaluator unavailable for that gate and route to rework.

Deterministic evaluators are covered by unit/regression tests rather than model calibration.

Calibration evidence belongs with the gate/run evidence and must not be inferred from narrative claims.
