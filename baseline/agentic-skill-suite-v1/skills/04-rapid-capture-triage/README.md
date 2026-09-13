# Rapid Capture & Triage

Converts fast, chaotic raw capture — voice-note transcripts, dictation,
stream-of-consciousness text — into a structured preview and machine delta
against an operational system (projects/processes/tasks/backlog), while
preserving every genuine ambiguity the input actually contains.

- Canonical definition: [`SKILL.md`](./SKILL.md)
- Specification this was built from: [`SPEC.md`](./SPEC.md)
- Input/output contracts: [`schemas/`](./schemas/)
- Worked example: [`examples/`](./examples/)
- Eval cases: [`evals/`](./evals/)
- Platform adapters: [`adapters/`](./adapters/)

Entry point for raw/chaotic input in most workflows (see
`/WORKFLOW_MAP.md`): this skill runs first, then hands off to
`canonical-context-builder` before branching into the rest of the suite.
