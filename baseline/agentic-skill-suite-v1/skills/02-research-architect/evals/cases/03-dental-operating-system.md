# Eval Case — Dental operating-system research

## Scenario
A team wants to build a practice-management/"operating system" platform for
multi-location dental groups (DSOs). Tests the skill on a regulated,
multi-stakeholder market (clinicians, DSO operators, patients, payers,
regulators) where the domain map must genuinely interconnect across
clinical, operational, financial, compliance and technology domains rather
than treating them as silos — and where the 150+/50+ minimums must be met
with real material-delta discipline given how easy it is to generate
superficially different but substantively repeated "integrate with X EHR"
questions.

## Input
```yaml
RUN_REQUEST:
  objective: "Should we build a practice-management operating system targeting multi-location dental service organizations (DSOs), and if so what should the initial wedge feature be (scheduling/RCM, clinical charting, patient engagement, or multi-location analytics)?"
  source_artifacts: []
  known_context: "Team includes one ex-dental-software PM, two engineers with no healthcare experience. Targeting US market initially."
  constraints: ["must address HIPAA compliance", "must interoperate with at least the top 3 incumbent dental EHR/PMS systems"]
  desired_output: full_architecture_package
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Domain map includes clinical workflow, revenue-cycle/insurance billing,
   multi-location operations, compliance/HIPAA, incumbent-EHR interoperability,
   and buyer-vs-user distinction (DSO exec buys, front-desk/clinician uses)
   as distinct, weighted, interconnected domains.
2. Interoperability-related questions across the ≥150 expansion iterations
   are tested against the material-delta rule: multiple "integrate with EHR
   system X" questions must differ in mechanism/angle (e.g. data-sync
   architecture vs. contractual/API-access barriers vs. clinician workflow
   disruption during migration), not just swap the vendor name — near-
   duplicates that only change the vendor name must be discarded.
3. Alternative-thesis pass (QA pass 7) includes at least one iteration per
   key domain testing the *opposite* of a working hypothesis (e.g. "what if
   DSOs are unwilling to switch PMS at all regardless of features" against
   an assumed hypothesis that feature superiority drives switching).
4. Coverage Debt is tracked and, if compliance or interoperability domains
   run behind their weight, flagged and addressed before Phase 3 closes.
5. Run stops before selecting a wedge feature — that decision is left to
   execution/human judgment, not asserted as a finding.

## Expected artifacts
- `DOMAIN_MAP.md` — clinical/financial/ops/compliance/tech domains present,
  each interconnected to at least one other.
- `MASTER_RESEARCH_PROGRAM.md` — interoperability-related rows show distinct
  material-delta justifications, not vendor-name-only variation.
- `COVERAGE_DEBT.md` — compliance/interoperability debt tracked explicitly.
- `RUN_RESULT.artifacts` contains all 7 required files; no wedge-feature
  choice appears in `summary` or `decisions` as a settled conclusion.

## Forbidden behavior
- Must not produce multiple "integrate with EHR X" rows that differ only by
  vendor name with no distinct mechanism — these must be caught by the
  material-delta test and discarded, not counted toward 150.
- Must not treat compliance (HIPAA) as a checkbox domain with a token
  iteration count disproportionate to its weight given the stated constraint.
- Must not select or recommend a specific wedge feature as a conclusion.

## Pass criteria
- [ ] Domain map spans clinical/financial/ops/compliance/tech with real
      interconnections.
- [ ] Interoperability iterations pass material-delta test on mechanism, not
      vendor-name swapping alone.
- [ ] Compliance domain's iteration count is proportional to its weighted
      importance/risk given the HIPAA constraint.
- [ ] No wedge feature is selected as a conclusion.
- [ ] ≥150 expansion + ≥50 polishing valid iterations achieved without
      vendor-name-only padding.
