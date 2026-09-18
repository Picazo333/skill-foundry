> **Historical bootstrap document.** The repository already exists and has completed its V5 foundation reconciliation. Agents must start at `AGENTS.md` + `noema.project.yaml`, not here. Retained for provenance/reinstallation only.

# SKILL FOUNDRY — START FROM ZERO

This is the complete, repository-ready Skill Foundry package.

## One rule
Do not create Git repositories from this ZIP itself. First create one remote GitHub repository, clone it twice with GitHub Desktop, then extract this ZIP into the Cursor clone and push it to `main`.

## Exact setup
1. On GitHub.com create a new **private** repository named `skill-foundry` and initialize it with a README.
2. In GitHub Desktop clone it to `C:\SkillFoundry\Cursor`.
3. In GitHub Desktop clone the same repository a second time to `C:\SkillFoundry\Antigravity`.
4. Extract **this ZIP directly into `C:\SkillFoundry\Cursor`**. Its files are stored at ZIP root, so no extra wrapper folder should appear. If Windows asks to replace the README, accept.
5. In GitHub Desktop, with the Cursor clone selected, commit all changes to `main` with `Install Skill Foundry foundation`, then **Push origin**.
6. Select the Antigravity clone in GitHub Desktop, keep it on `main`, click **Fetch origin**, then **Pull origin**.
7. Open `C:\SkillFoundry\Cursor` in Cursor and send: `Lee prompts/START_CURSOR.md y ejecútalo completo. No termines hasta cumplir todos sus entregables y validaciones.`
8. Open `C:\SkillFoundry\Antigravity` in Antigravity and send: `Lee prompts/START_ANTIGRAVITY.md y ejecútalo completo. No termines hasta cumplir todos sus entregables y validaciones.`

The agents create/use their own branches. You do not create branches manually and you do not use Bash.

## Initial integration after both finish
1. Review/merge `agent/antigravity` into `main` first.
2. Tell Cursor: `Lee prompts/RECONCILE_CURSOR_AFTER_ANTIGRAVITY.md y ejecútalo completo.`
3. When Cursor returns `READY_FOR_REVIEW`, review/merge `agent/cursor` into `main`.
4. Skill Foundry is ready for its first real workflow. See `OPERATOR_WORKFLOW.md`.
