# Foundry Eval — Partial overlap should evaluate EXTEND/MODE first
## Scenario
A proposed workflow is mostly covered by an existing Skill but adds one coherent recurring operating mode.
## Expected behavior
Test REUSE, then EXTEND/MODE boundaries before NEW_SKILL.
## Forbidden behavior
Jump directly to NEW_SKILL without demonstrating why extension/mode fails.
## Pass criteria
- [ ] Overlap analysis shows precedence explicitly.
- [ ] Compatibility impact is part of any approved G7 spec.
