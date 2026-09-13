# Cursor adapter — Brand Discovery

## Invocation
Add as a `.cursor/rules` entry (or project doc referenced from one) that
points at `skills/06-brand-discovery/SKILL.md`: "When asked to run or update
brand discovery, follow this file's procedure exactly." Unlike Codex's
explicit-mention pattern, a Cursor rule can auto-attach based on file-path
glob (e.g. a `discovery/` or `brand/` directory) or manual `@`-mention, per
the project's rule configuration.

## File I/O
Reads `source_artifacts` from the repo working tree (same as `codex.md`).
Writes the three required artifacts as real files in the repo.

## Environment constraints
Same as `codex.md`: prefer version-controlled source material (prior brief,
committed interview notes) over untracked scratch as higher-authority
sources; apply the FACTS/CLAIMS boundary regardless of file provenance.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
