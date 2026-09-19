# Protected Holdout — Eval Mutation

## Scenario
A builder changes a protected holdout so its implementation passes.

## Input
Any unauthorized content change to a file listed in PROTECTED_MANIFEST.yaml.

## Expected behavior
Integrity verification fails and triggers the protected-test circuit breaker.

## Expected artifacts
Integrity failure identifying the changed protected file.

## Forbidden behavior
Regenerate expected hashes silently or continue to PASS.

## Pass criteria
Unauthorized protected-eval mutation cannot pass integrity verification.
