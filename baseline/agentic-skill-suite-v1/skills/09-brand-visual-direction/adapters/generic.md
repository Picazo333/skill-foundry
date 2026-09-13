# Generic adapter — Brand Visual Direction

Baseline adapter for any LLM chat interface with file upload/paste. Every
other adapter in this folder specializes this one.

## Invocation
Paste or reference `SKILL.md` at the start of the session:
> "Follow the procedure in `SKILL.md` exactly for Brand Visual Direction.
> On each run, expect a RUN_REQUEST (objective, source artifacts —
> minimum `BRAND_STRATEGY.md` — constraints, mode). Produce all four
> required artifacts (`VISUAL_TERRITORIES.md`, `APPROVED_VISUAL_DIRECTION.md`,
> `VISUAL_ANTI_PATTERNS.md`, `GENERATION_LANGUAGE.md`) as separate, clearly
> labeled sections. Run the 8-axis territory definition and the divergence
> audit for real — never present color-swapped territories as materially
> distinct options."

## File I/O
`BRAND_STRATEGY.md` (and any optional context: `POSITIONING_SYSTEM.md`,
references, anti-references) is pasted or uploaded at session start. The
four required artifacts are returned as separate, clearly delimited
markdown sections in the response, ready for the user to save as files for
handoff to `brand-identity-system`.

## Environment constraints
No persistent filesystem: on a follow-up or `mode: UPDATE` run, the user
must re-paste/re-upload `BRAND_STRATEGY.md` and the prior
`VISUAL_TERRITORIES.md`/`APPROVED_VISUAL_DIRECTION.md` — do not assume
they persist between sessions.

## Fallback
This entire file is the fallback pattern every platform-specific adapter
in this folder specializes.
