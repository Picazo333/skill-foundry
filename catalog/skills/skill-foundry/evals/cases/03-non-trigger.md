# Eval — Ordinary Domain Task Non-trigger

## Scenario
User asks for an ordinary task unrelated to capability engineering.

## Input
“Resume este texto en cinco puntos.”

## Expected behavior
Do not invoke Skill Foundry merely because an LLM can perform the task.

## Expected artifacts
No Foundry candidate or architecture artifact.

## Forbidden behavior
Route to GENESIS, create a Skill candidate, or ask Foundry architecture questions.

## Pass criteria
The request is classified as non-trigger for Skill Foundry.
