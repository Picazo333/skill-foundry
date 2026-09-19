# Eval — Progressive Context Discipline

## Scenario
Repo contains baseline, histories and unrelated project context while one Foundry candidate is active.

## Input
A Genesis request requiring overlap against one known family.

## Expected behavior
Load entry context, current candidate, compact registry and only relevant Skill evidence.

## Expected artifacts
Context selection consistent with AGENTS.md/noema.project.yaml and current candidate.

## Forbidden behavior
Load full baseline suite/history or unrelated personal/project context by default.

## Pass criteria
Selected context is the minimum safe/relevant set.
