# Skill Foundry — Agent Entry Map

Start with **this file + `noema.project.yaml` + the current task**. Do not recursively preload the repository.

## Authority
Skill Foundry owns its taxonomy, ontology, registry, G0–G10 lifecycle, Skill contracts, evals, packages, candidate state and Foundry handoffs. Noema governs repository-level conformance, context routing and interoperability only; it does not redefine Foundry semantics.

## Context routing
Choose the task mode in `noema.project.yaml` (`patch`, `build`, `audit`, `research`, `architect`, or `recover`) and load only that mode's required files. Optional files are loaded only when the task needs them.

After routed context, load only the **current** candidate/spec/build/handoff named by the task. Never load the full baseline suite or full history by default.

## Invariants
- Baseline `baseline/agentic-skill-suite-v1/` is immutable unless an explicit migration is approved.
- Decision precedence: `REUSE → EXTEND → MODE → DEPENDENT_SKILL → NEW_SKILL → NO_SKILL`.
- G6 human decision remains mandatory for architecture/closure.
- `SKILL.md` is the portable canonical Skill core; platform adapters stay thin.
- Unrelated personal/project context must not enter Foundry unless supplied as cycle input.
- `main` is stable canon; never force-push.

## Validation
For Foundry-domain changes run:
`python tools/validate_foundry.py`
`python -m unittest tests.test_validate_foundry -v`

Noema conformance is a separate repository-governance gate and does not replace Foundry evals or quality gates.
