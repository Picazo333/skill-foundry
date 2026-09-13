# Codex adapter — Brand Quality Auditor

## Invocation
Reference this skill from the repo's agent-instructions file (e.g.
`AGENTS.md`) as: "For brand QA on creative/content artifacts, read
`skills/14-brand-quality-auditor/SKILL.md` and follow it exactly,
including the canon gate — do not audit without locating explicit,
approved canon in the repo first." The coding agent loads `SKILL.md` on
demand rather than keeping it permanently in context.

## File I/O
Reads the artifact under audit and canon (brand book, verbal/visual
identity docs) from the repo working tree — typically under a
`brand/` or `canon/` directory, or wherever `brand-book-builder`'s output
lives in this repo. If no such canon directory/files exist or are found
empty, this is treated exactly as canon-not-supplied: return `BLOCKED`
rather than falling back to generic web/copy conventions. Writes the
three required artifacts as real files in the repo (default: alongside
the artifact under audit, or an `audits/` directory per repo convention).

## Environment constraints
Prefer canon files under version control (higher authority) over any
inline comments or commit messages describing "what the brand should feel
like" — the latter is not approved canon and must not substitute for it.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
