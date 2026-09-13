# Adapter contract

Adapters are thin environment wrappers around one canonical `SKILL.md`. They
translate invocation, file loading, artifact paths, tool conventions and
environment constraints for a specific platform. They must never fork the
canonical methodology, procedure, outputs, quality gates or stop conditions
(`PORTABILITY.md`).

Generate adapters only after the canonical skill's `SKILL.md` + schemas +
evals exist and are stable.

Each adapter file (`adapters/<platform>.md`) should be short and answer only:
1. **Invocation** — how a user/agent triggers this skill on this platform
   (slash command, custom GPT instructions, system prompt section, Cursor
   rule file, etc.).
2. **File I/O** — how the platform reads `source_artifacts` and writes
   required output artifacts (native filesystem, uploaded files, chat-pasted
   content, repo working tree, etc.).
3. **Environment constraints** — anything platform-specific that changes
   *how* the canonical procedure is carried out without changing *what* it
   does (e.g. no persistent filesystem → ask the user to paste/re-upload
   `prior_run` artifacts each session).
4. **Fallback** — if the platform has no formal "skill"/custom-instruction
   primitive, the adapter is a portable instruction wrapper: a copy-pasteable
   system-prompt block that reproduces the canonical `RUN_REQUEST` →
   procedure → `RUN_RESULT` contract in plain instructions.

## Per-platform notes

- **generic.md** — the baseline: any LLM chat interface with file
  upload/paste. This is what every other adapter specializes.
- **claude.md** — Claude/Claude Code: this skill's home platform; runs as a
  Skill directory (`SKILL.md` + supporting files) invoked by name; has
  native filesystem access when run as an agent (Claude Code) or file
  upload when run in claude.ai.
- **chatgpt.md** — Custom GPT instructions / Projects: no native multi-file
  skill primitive, so the adapter is the portable instruction wrapper
  (system-prompt block) plus guidance to attach source artifacts as
  Project/Custom-GPT knowledge files.
- **codex.md** — Codex / coding-agent context: skill lives as a repo file
  (e.g. `AGENTS.md` section or a referenced doc) the agent is told to read
  before acting; file I/O is the repo working tree.
- **gemini.md** — Gemini (Gems / API system instructions): same portable
  instruction wrapper pattern as ChatGPT; note Gemini-specific context
  window / file-upload conventions where they differ.
- **cursor.md** — Cursor: skill lives as a `.cursor/rules` entry or
  project doc the agent is pointed at; file I/O is the repo working tree,
  same as Codex, but invocation differs (rule auto-attach vs. explicit
  mention).

## What an adapter must NOT do
- Must not add, remove, or reorder required output artifacts.
- Must not weaken a quality gate or stop condition "because the platform is
  faster/slower".
- Must not silently assume context the canonical skill marks as
  `DO_NOT_LOAD_BY_DEFAULT`.
- Must not duplicate the full procedure — reference `SKILL.md`, don't restate it.
