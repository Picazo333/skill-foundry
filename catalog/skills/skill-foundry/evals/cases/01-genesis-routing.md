# Eval — Explicit Genesis Routing

## Scenario
User explicitly asks to create a reusable Skill from a recurrent workflow.

## Input
“Usa Skill Foundry para convertir este proceso recurrente en una Skill.”

## Expected behavior
Classify as GENESIS, resolve canon if available, perform catalog preflight before any NEW_SKILL proposal, and route into canonical G0–G10.

## Expected artifacts
Intent/next-action response and ordinary candidate artifacts once Genesis starts.

## Forbidden behavior
Claim downstream completion, skip G6, or embed a substitute lifecycle.

## Pass criteria
GENESIS is selected and the next canonical Foundry action is identified without architecture fabrication.
