> **Historical bootstrap document.** Do not treat these one-time installation steps as current project state. Agents start at `AGENTS.md` + `noema.project.yaml`.

# EJECUTA ESTO — DESDE CERO

No uses Bash. No crees ramas manualmente.

1. Crea en GitHub.com un repositorio **privado** llamado `skill-foundry` y marca la opción para inicializarlo con README.
2. GitHub Desktop → **Clone repository** → clónalo en `C:\SkillFoundry\Cursor`.
3. GitHub Desktop → **Clone repository** otra vez → clónalo en `C:\SkillFoundry\Antigravity`.
4. Extrae este ZIP **directamente dentro de `C:\SkillFoundry\Cursor`**. Acepta reemplazar README si Windows lo pregunta.
5. GitHub Desktop, copia Cursor → **Commit to main** con `Install Skill Foundry foundation` → **Push origin**.
6. GitHub Desktop, copia Antigravity → `main` → **Fetch origin** → **Pull origin**.
7. Cursor: `Lee prompts/START_CURSOR.md y ejecútalo completo. No termines hasta cumplir todos sus entregables y validaciones.`
8. Antigravity: `Lee prompts/START_ANTIGRAVITY.md y ejecútalo completo. No termines hasta cumplir todos sus entregables y validaciones.`
9. Al terminar ambos: mergea primero `agent/antigravity → main`.
10. Luego Cursor: `Lee prompts/RECONCILE_CURSOR_AFTER_ANTIGRAVITY.md y ejecútalo completo.` Cuando termine, mergea `agent/cursor → main`.

Después usa `OPERATOR_WORKFLOW.md` para los ciclos reales de creación/evolución de Skills.
