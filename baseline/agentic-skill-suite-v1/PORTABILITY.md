# PORTABILITY

## Objective
The same capability must remain usable across ChatGPT, Codex, Claude, Gemini and Cursor without divergent logic.

## Source-of-truth hierarchy
1. `SKILL.md`
2. `manifest.json`
3. schemas
4. shared policies
5. adapters

Adapters may define invocation, file loading, artifact paths, tool conventions and environment constraints. They may not change methodology, quality gates, outputs or stop conditions.

If a platform lacks a formal skill primitive, generate a portable instruction wrapper rather than inventing unsupported platform behavior.

## Standalone exports
Generate compiled exports under `exports/<platform>/` when useful. Compiled files are build artifacts, not sources of truth.

## Cross-platform continuity test
A platform switch must be possible using only:
- canonical input artifact;
- current checkpoint;
- adapter;
- canonical skill.

No prior conversational memory may be required for correctness.
