# Generic adapter — Brand Identity System

Baseline adapter for any LLM chat interface with file upload/paste. Every
other adapter in this folder specializes this one.

## Invocation
Paste or reference `SKILL.md` at the start of the session:
> "Follow the procedure in `SKILL.md` exactly for Brand Identity System.
> On each run, expect a RUN_REQUEST (objective, source artifacts — minimum
> `BRAND_STRATEGY.md` and `APPROVED_VISUAL_DIRECTION.md` — constraints,
> mode). Produce all three required artifacts (`IDENTITY_SYSTEM.md`,
> `DESIGN_TOKENS.json`, `APPLICATION_RULES.md`) as separate, clearly
> labeled sections. Compute every color-contrast ratio using the method in
> `references/contrast-verification-method.md` — never assert 'accessible'
> without the number. Never invent a hex value, type-scale ratio, or logo
> dimension with no trace to `APPROVED_VISUAL_DIRECTION.md` or a
> `references/` derivation method."

## File I/O
`BRAND_STRATEGY.md` and `APPROVED_VISUAL_DIRECTION.md` (plus any optional
context: `VISUAL_ANTI_PATTERNS.md`, `GENERATION_LANGUAGE.md`, mark
geometry, licensing constraints) are pasted or uploaded at session start.
The three required artifacts are returned as separate, clearly delimited
markdown/JSON sections in the response, ready for the user to save as
files for handoff to `brand-book-builder`.

## Environment constraints
No persistent filesystem: on a follow-up or `mode: UPDATE` run, the user
must re-paste/re-upload `BRAND_STRATEGY.md`, `APPROVED_VISUAL_DIRECTION.md`,
and the prior `IDENTITY_SYSTEM.md`/`DESIGN_TOKENS.json` — do not assume
they persist between sessions.

## Fallback
This entire file is the fallback pattern every platform-specific adapter
in this folder specializes.
