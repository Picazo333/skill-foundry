# SKILL FOUNDRY — WORKFLOW DEL OPERADOR

Después del bootstrap inicial, ésta es la secuencia normal.

1. **Nuevo workflow:** en Antigravity envía `Lee prompts/NEW_WORKFLOW_ANTIGRAVITY.md y ejecútalo sobre lo siguiente:` seguido de tu explicación real del proceso.
2. **Antigravity trabaja G0–G5:** reconstruye el workflow, mina capacidades, compara las 15 Skills, investiga sólo si aporta, y presenta la arquitectura mínima.
3. **Tú decides en G6:** corriges/apruebas/rechazas/pides más investigación. Éste es el checkpoint humano principal.
4. **Después de tu decisión:** dile a Antigravity `Lee prompts/AFTER_HUMAN_DECISION_ANTIGRAVITY.md y aplícalo a la decisión que acabo de dar.`
5. **Si hay algo que construir:** mergea la spec aprobada a `main`; luego Cursor ejecuta `prompts/BUILD_APPROVED_CURSOR.md`.
6. **Auditoría:** Antigravity ejecuta `prompts/AUDIT_CURSOR_BUILD_ANTIGRAVITY.md` contra el build de Cursor.
7. **Si sale REWORK:** Cursor ejecuta `prompts/REWORK_CURSOR.md` y vuelve a auditoría.
8. **Si sale PASS:** mergea el build de Cursor a `main`; luego Antigravity ejecuta `prompts/PUBLISH_AFTER_PASS_ANTIGRAVITY.md`; mergea ese pequeño cierre canónico.
9. **Terminado:** registry, taxonomía/ontología (sólo si aplica), routing/handoffs, provenance y checkpoint quedan actualizados.

Una ejecución también puede terminar correctamente en `REUSE` o `NO_SKILL`; no existe obligación de fabricar una Skill.
