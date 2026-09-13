# Gemini adapter — Research Architect

No native multi-file skill primitive in Gems/consumer Gemini, so this ships
as a portable instruction wrapper, same pattern as `adapters/chatgpt.md`.

## Invocation
Gem system instructions / API system prompt:
> "You are the Research Architect. Follow the attached `SKILL.md` exactly:
> ≥150 valid scope-expansion + ≥50 valid domain-polishing iterations (each
> passing the material-delta/novelty test), key-area weighting instead of
> equal distribution, Coverage Debt, contradiction/white-space/
> primary-evidence ledgers, the workflow-first automation/AI lens, and all
> 10 final QA passes. Produce the 7 required artifacts as labeled sections.
> In `mode: AUTONOMOUS`, proceed through architecture rounds without asking
> to continue, checkpointing after each logical block. Stop before deep
> research in every mode — never answer the research questions."

Attach `SKILL.md` content in the Gem's knowledge/context files, or inline in
the system instruction if no file-attachment step exists.

## File I/O
Source artifacts are pasted or uploaded per host surface. Outputs are
returned as labeled markdown sections; re-supply the prior `CHECKPOINT.md`
and program artifacts on any new session to resume — no persistent memory
assumed.

## Environment constraints
With a large context-window API deployment, prefer passing the full prior
program + checkpoint + new context in one call for a resumed run, rather
than incremental multi-turn reconstruction, to avoid drift in iteration
counts or weighting decisions across turns. A 200+iteration program is
large enough that truncation risk is real — checkpoint before any response
likely to hit a length limit.

## Fallback
This entire adapter is the fallback, same reasoning as the ChatGPT adapter.
