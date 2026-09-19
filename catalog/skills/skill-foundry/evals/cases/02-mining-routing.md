# Eval — Capability Mining Routing

## Scenario
User supplies a corpus/workflow and asks what durable capabilities can be mined.

## Input
“Analiza estas conversaciones y detecta capabilities o Skills recurrentes.”

## Expected behavior
Classify as MINING; reconstruct/mine capabilities while preserving Capability ≠ Skill and feed only justified candidates toward overlap/Genesis.

## Expected artifacts
Mining route plus structured capability observations/candidate path when execution begins.

## Forbidden behavior
Turn every extracted item into a Skill or skip catalog overlap.

## Pass criteria
MINING is selected and no automatic Skill creation is asserted.
