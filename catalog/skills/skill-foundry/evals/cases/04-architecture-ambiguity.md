# Eval — Architecture-changing Ambiguity

## Scenario
User says they want “something reusable” but it is unclear whether they want to execute an existing workflow or engineer a new capability.

## Input
“Hazme algo reusable para research.”

## Expected behavior
Return AMBIGUOUS and ask only the minimum question whose answer changes whether Foundry should engineer a capability.

## Expected artifacts
One concise blocking question; no buildable spec.

## Forbidden behavior
Guess NEW_SKILL or force-route to Factory.

## Pass criteria
Ambiguity is acknowledged and no architecture is fabricated.
