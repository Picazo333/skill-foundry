# Eval — Obvious Catalog Overlap

## Scenario
A user proposes a new Skill whose responsibility is already clearly covered by a registry Skill.

## Input
“Crea otra Skill para construir contexto canónico desde información fragmentada.”

## Expected behavior
Run catalog preflight and identify Canonical Context Builder before considering NEW_SKILL.

## Expected artifacts
Overlap result using mandatory decision precedence.

## Forbidden behavior
Default to NEW_SKILL because the proposed name differs.

## Pass criteria
Existing coverage is surfaced and NEW_SKILL is not the default outcome.
