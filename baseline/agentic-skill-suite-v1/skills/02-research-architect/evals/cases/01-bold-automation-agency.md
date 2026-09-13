# Eval Case — BOLD-like automation agency

## Scenario
A founder wants to launch an AI/automation implementation agency for SMBs
(BOLD-like positioning: workflow automation + AI agents as a service).
Tests whether the skill correctly applies key-area weighting (not equal
distribution) to an operationally dense business, and whether the
workflow-first automation/AI lens is genuinely applied per domain rather
than declared once and forgotten — a real risk on a project whose whole
subject *is* automation, where it's tempting to treat "AI angle" as a
single domain instead of a cross-cutting lens.

## Input
```yaml
RUN_REQUEST:
  objective: "Launch a boutique AI/automation implementation agency serving SMBs (10-200 employees) — workflow audits + custom automation/agent builds. Need to know target verticals, pricing model, and how to differentiate from the flood of similar agencies."
  source_artifacts: []
  known_context: "Founder has 6 years freelance dev experience, no agency-ops experience. No existing client base."
  constraints: ["solo founder for first 6 months", "must reach profitability within 9 months"]
  desired_output: full_architecture_package
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Master decision question names the actual decision (vertical + pricing
   + differentiation choice), not a vague "understand the market" framing.
2. Domain discovery produces domain-native lenses specific to agency/services
   businesses (e.g. delivery-capacity-vs-sales-pipeline tension, productized
   vs. bespoke engagement economics, vertical-specific automation ceiling) —
   not only generic market/competitor/financial lenses.
3. Weighting scores differ meaningfully across domains (importance/
   uncertainty/complexity/risk); iteration allocation in
   `MASTER_RESEARCH_PROGRAM.md` visibly tracks those weights — no domain
   gets `150/N` iterations by default.
4. The workflow-first automation/AI lens is applied as a *cross-cutting*
   check inside multiple operational domains (delivery, sales, client
   onboarding), evidenced by distinct iterations in each, not consolidated
   into one "AI domain" that substitutes for the lens elsewhere.
5. At least 150 valid scope-expansion + 50 valid polishing iterations are
   produced, each traceable to a domain node and passing the material-delta
   test.
6. All 10 QA passes run in order and are logged.
7. Run stops after packaging — no vertical is actually chosen, no pricing
   figure is asserted as a finding.

## Expected artifacts
- `DOMAIN_MAP.md` — weights visibly vary; every domain has ≥1 interconnection.
- `MASTER_RESEARCH_PROGRAM.md` — ≥150 expansion + ≥50 polishing rows; several
  distinct workflow-first automation/AI-lens rows across different domains
  (not one).
- `COVERAGE_DEBT.md` — reflects allocation vs. weight, not just a raw count.
- `RUN_RESULT.quality.iteration_counts` — scope_expansion ≥150,
  domain_polishing ≥50, total_valid ≥200.

## Forbidden behavior
- Must not distribute iterations equally across domains regardless of weight.
- Must not treat "AI/automation" as a single domain that exempts other
  domains from the workflow-first lens.
- Must not assert a chosen vertical, price point, or differentiation angle
  as a conclusion — those are execution-stage findings.
- Must not pad iteration counts with reworded duplicates to hit 150/50.

## Pass criteria
- [ ] Domain weights are non-uniform and allocation tracks them.
- [ ] Workflow-first automation/AI lens iterations appear in ≥2 distinct
      operational domains, not consolidated into one.
- [ ] ≥150 expansion + ≥50 polishing valid iterations, each with a
      material-delta justification.
- [ ] No vertical/price/differentiation choice is stated as a finding.
- [ ] All 10 QA passes logged in order.
