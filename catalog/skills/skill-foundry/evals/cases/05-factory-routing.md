# Eval — Factory Route Is Operational

## Scenario
After G5, user asks Foundry to process a multi-item Skill/capability portfolio.

## Input
“Procesa estas 100 propuestas como Factory.”

## Expected behavior
Classify as FACTORY and route to `SF-WF-003_PORTFOLIO_FACTORY.md`, beginning raw preservation/source accounting and architecture discovery before any manufacturing.

## Expected artifacts
Factory portfolio root plus source ledger/normalized-item path as execution begins.

## Forbidden behavior
Return the old G4 `BLOCKED_NOT_IMPLEMENTED`, fabricate immediate 100-Skill output, or skip Portfolio Review / Plan Lock.

## Pass criteria
FACTORY is selected and the canonical Factory workflow is the next action.
