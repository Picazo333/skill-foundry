# Cursor adapter — Brand Quality Auditor

## Invocation
Add as a `.cursor/rules` entry (or project doc referenced from one) that
points at `skills/14-brand-quality-auditor/SKILL.md`: "When asked to QA a
brand/creative/content artifact, follow this file's procedure exactly,
including the canon gate — do not audit without locating explicit,
approved canon first." Unlike Codex's explicit-mention pattern, a Cursor
rule can auto-attach based on file-path glob (e.g. files under
`marketing/`, `brand/`, `content/`) or manual `@`-mention, per the
project's rule configuration.

## File I/O
Reads the artifact under audit and canon from the repo working tree (same
as `codex.md`). Writes the three required artifacts as real files in the
repo. If canon files aren't present at the expected repo location, return
`BLOCKED` rather than auditing against generic conventions.

## Environment constraints
Same as `codex.md`: version-controlled canon files are the source of
truth; inline suggestions or PR comments about "brand feel" are not
approved canon and must not substitute for it.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
