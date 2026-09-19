# VNext Gate Acceptance Matrix

This document is the compact operational checklist for `VNEXT_MASTER_PLAN.md`.

| Gate | Mandatory evidence | Hard fail conditions |
|---|---|---|
| G0 | baseline commit, Foundry validator, unit tests, V1 baseline, Noema conformance | any current baseline regression |
| G1 | authority matrix, contract reuse matrix, compressed non-regression contract | unresolved ownership collision required by vertical slice |
| G2 | research decision matrix with only decision-relevant research | open blocking architecture unknown |
| G3 | architecture 1.0, vertical slice spec, failure model, architecture red-team | any open critical red-team defect |
| G4 | one end-to-end candidate, deterministic + behavioral + independent + adversarial evidence | paper-PASS, baseline mutation, audit bypass |
| G5 | portfolio discovery + Plan Lock + waves + publication semantics demonstrated | source loss, architecture drift, canon collision |
| G6 | synthetic canary + 15–25 real items + metrics | critical false PASS, provenance loss, trust breach, unrecoverable run |
| G7 | release report, acceptance manifest, full source reconciliation | unresolved critical exception or missing terminal disposition |

## Required commands where applicable

```bash
python tools/validate_foundry.py
python -m unittest tests.test_validate_foundry -v
```

Noema conformance must use the protocol version pinned by `noema.project.yaml`.

## Evidence semantics
- `PASS` may not be inferred from artifact presence.
- `NOEMA PASS` means repository conformance only.
- `FOUNDRY PASS` requires Foundry-domain evidence.
- `ECOSYSTEM PASS` additionally requires composition/integration evidence.
- `UNTESTED` is never equivalent to `PASS`.

## Merge semantics
A gate branch can merge only if:
1. all mandatory evidence exists;
2. all deterministic checks pass;
3. independent audit required by the gate passes;
4. no hard-fail condition is open;
5. execution manifest is updated;
6. no material deviation remains hidden.

## Final stop
After G7 release evidence is complete, stop and request final operator review.
