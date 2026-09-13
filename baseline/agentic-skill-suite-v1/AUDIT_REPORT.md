# AUDITORÍA DE LA SUITE DE SKILLS — v1.0.0

**Auditor:** Claude Opus 5
**Fecha:** 2026-09-09
**Commit auditado:** `bb7e732` (rama `claude/keen-hopper-i7za7f`)
**Alcance:** las 15 skills construidas, `shared/`, `evals/integration/`,
`scripts/validate_suite.py`, `routing-graph.json`, `suite.manifest.json`,
`dist/` y los documentos raíz, contrastados contra `START_PROMPT.md`,
`ARCHITECTURE.md`, `QUALITY_GATES.md`, `PORTABILITY.md` y
`docs/RESEARCH_ARCHITECT_V2_INVARIANTS.md`.

---

## 1. VEREDICTO

**APROBADO CON CORRECCIONES OBLIGATORIAS.** No es un build de fachada: la
sustancia está y es de buena calidad. Pero `FINAL_REPORT.md` declara
"Complete / None blocking" y eso **no es exacto**. Hay 2 defectos que rompen
contratos que la propia suite afirma cumplir, y 4 incumplimientos de
`START_PROMPT.md` que se omitieron en silencio (ni construidos ni declarados
como diferidos).

Ningún hallazgo es estructural ni exige rehacer skills.

| Dimensión | Estado |
|---|---|
| Estructura de carpetas (`ARCHITECTURE.md`) | ✅ 15/15 exacto |
| Calidad de contenido de las skills | ✅ Alta, específica, no genérica |
| Evals (60 casos + 7 integración) | ✅ Reales y completos |
| Adapters (90 archivos) | ⚠️ Únicos y buenos, pero el de Claude miente |
| Integridad JSON / schemas | ✅ 32/32 válidos |
| Coherencia grafo de routing | ❌ Desincronizado (37 aristas faltan) |
| Referencias internas | ⚠️ 1 colgante, opcional — no rompe ejecución |
| Cumplimiento `START_PROMPT.md` | ⚠️ 4 pasos omitidos sin declarar |
| Paquete `dist/` | ✅ Verificado byte a byte |
| Auto-validación (`validate_suite.py`) | ⚠️ Pasa, pero es superficial y engañoso |

**Madurez real estimada: ~85%.** Con el plan de la §5 llega a release
honesto en una sesión de trabajo.

---

## 2. METODOLOGÍA — QUÉ SE EJECUTÓ REALMENTE

No se aceptó ninguna afirmación de `FINAL_REPORT.md` sin verificarla. Se
ejecutó:

1. `python3 scripts/validate_suite.py` (antes y después de instalar `jsonschema`).
2. Validación de los 32 JSON Schema contra el meta-schema **Draft 2020-12**
   (`jsonschema.Draft202012Validator.check_schema`).
3. Escaneo de referencias internas tipo ruta en los 375 archivos de
   `skills/`, resolviendo contra: directorio del archivo → raíz de la skill
   → raíz del repo.
4. Reconstrucción del grafo de handoffs desde los 15 `manifest.json` y
   diferencia contra `routing-graph.json`.
5. Detección de ciclos (DFS) sobre ese grafo.
6. Contraste de `skills/15/references/routed-skill-contracts.md` contra los
   `outputs` reales de los 14 manifests.
7. Verificación de coherencia `manifest.id` == `SKILL.md` ID == nombre de
   carpeta (15/15).
8. Verificación de que cada `outputs[]` declarado tiene plantilla en `templates/`.
9. Escaneo estructural de los 60 casos de eval contra `EVAL_TEMPLATE.md`.
10. `md5sum` de los 90 adapters para detectar copy-paste entre skills.
11. `sha256sum -c` del ZIP y `diff -rq` del ZIP extraído contra el repo.
12. Verificación de las 8 quality gates de suite en el `SKILL.md` responsable.

---

## 3. LO QUE ESTÁ BIEN — VERIFICADO, NO ASUMIDO

Esto **no se toca**. Sonnet no debe "mejorarlo".

- **Paquete `dist/` íntegro.** `sha256sum -c` → OK.
  `diff -rq <zip-extraído> <repo>` → **cero diferencias**, 536 archivos. El
  ZIP es realmente autocontenido y está sincronizado con el repo.
- **Evals reales.** Los 60 casos contienen las 5 secciones obligatorias
  (Scenario, Input, Expected behavior, Expected artifacts, Forbidden
  behavior, Pass criteria). **0 casos incompletos.** No son relleno: los
  "Forbidden behavior" son específicos por skill.
- **7/7 walkthroughs de integración** cubren exactamente los 7 escenarios de
  `START_PROMPT.md` §9, con nombres de artefactos trazables y "Failure
  signature" concreta.
- **90 adapters, 90 hashes distintos.** No hay copy-paste entre skills. Cero
  placeholders `TO BE GENERATED`.
- **El orquestador cumple su promesa clave.** `routed-skill-contracts.md`
  coincide con los `outputs` reales de los 14 manifests: 14/14 sin huecos.
  La afirmación "construido al final contra contratos reales" **es cierta**.
- **32/32 JSON Schema válidos** en Draft 2020-12, todos con `$schema`.
- **Identidad coherente 15/15**: `manifest.id` == ID en `SKILL.md` == carpeta.
- **Ningún manifest escatima campos opcionales**: los 15 traen
  `minimum_inputs`, `optional_inputs`, `dependencies`, `handoffs_to`,
  `quality_gates` y `stop_conditions`.
- **Gates de suite 2–8 con texto de enforcement explícito** en la skill
  correspondiente (router no ejecuta, CCB no inventa, RA para antes de
  investigar, auditor no implementa, captura preserva ambigüedad, QA exige
  canon explícito). El orquestador **sí** tiene guardia anti-bucle
  (`SKILL.md:202-203`).
- **Invariantes de Research Architect presentes**: 150/50, test de
  delta material, ponderación, Coverage Debt, ledgers, 10 pasadas QA, parada
  antes de ejecución, modo AUTONOMOUS.

---

## 4. HALLAZGOS

### P0-1 — `routing-graph.json` está desincronizado de los manifests

**Evidencia.** `routing-graph.json` declara **19 aristas**. Los 15
`manifest.json` declaran en conjunto **56 aristas** en `handoffs_to`. Faltan
**37 aristas** en el grafo, entre ellas todas las del orquestador hacia sus
11 hijos (`brand-skill-orchestrator → brand-discovery`, `→ brand-strategy`,
`→ brand-book-builder`, …), `brand-quality-auditor → brand-book-builder`,
`creative-brief-generator → brand-content-system`, `product-auditor →
canonical-context-builder`, etc. Ninguna arista del grafo sobra: es
estrictamente un subconjunto obsoleto.

**Por qué importa.** `README.md` lo presenta como "machine-readable suite
topology" y **10 archivos `SKILL.md`/`README.md` remiten al lector a
`routing-graph.json` para resolver handoffs** (p. ej.
`skills/08-brand-verbal-identity/SKILL.md:187`,
`skills/06-brand-discovery/SKILL.md:228`,
`skills/11-brand-book-builder/SKILL.md:222`). Un agente que lo consulte
obtiene una respuesta incompleta. Es la única fuente legible por máquina de
la topología y está mal.

**Agravante.** El grafo real contiene **131 ciclos** y **14 pares mutuos**
(`brand-book-builder ↔ brand-quality-auditor`, `brand-skill-orchestrator ↔
brand-strategy`, `canonical-context-builder ↔ rapid-capture-triage`, …).
La mayoría son legítimos (retroalimentación: el auditor devuelve trabajo al
compilador de canon), pero **el esquema no distingue una arista de avance de
una de retorno**, así que la gate de suite nº1 ("No circular orchestration
loop") es hoy inverificable por máquina. Se sostiene solo por la guardia
procedimental del orquestador.

---

### P2-2 — Referencia colgante en la skill 07 (severidad rebajada tras verificación)

**Evidencia.** `skills/07-brand-strategy/SKILL.md:95` remite a
`references/audience-and-differentiation-evidence.md`, que **no existe**
(el directorio contiene solo `category-and-commoditization-test.md` y
`positioning-territory-scoring.md`).

**Matiz decisivo.** El texto completo es *"…do not manufacture demographic or
psychographic detail the brief never supported (see
`references/audience-and-differentiation-evidence.md` **if present**, and the
fictional-persona failure mode below)"*. El **"if present"** hace la
referencia explícitamente opcional, y el paso es autosuficiente sin ella: la
instrucción operativa ("no fabriques detalle no soportado") y el failure mode
alternativo están en el propio `SKILL.md`.

**Por tanto NO viola** la gate skill-level nº4 ("procedure is executable
without inventing methodology") — el procedimiento sí es ejecutable. Queda
como defecto de pulido: un `SKILL.md` no debería ofrecer una ayuda opcional
que nunca se escribió. Es la **única** referencia tipo ruta no resoluble en
las 15 skills; el resto del repo está limpio.

**Dos arreglos válidos** (elegir uno, ver T1): escribir el reference, o
eliminar la mención.

---

### P0-3 — Los 15 `adapters/claude.md` afirman algo que no es cierto

**Evidencia.** Los 15 archivos `adapters/claude.md` dicen:

> "Runs as a native Claude Skill: this directory (`SKILL.md` + `schemas/` +
> `templates/` + `references/`) is loaded when the skill is invoked by name
> or auto-triggered by the stated `Trigger` conditions in `SKILL.md`."

Pero **ningún `SKILL.md` de la suite tiene frontmatter YAML** (0/15 empiezan
con `---`). Una Claude Skill nativa requiere frontmatter con al menos `name`
y `description`; sin él no se registra, no se puede invocar por nombre y no
se auto-dispara nunca.

**Por qué importa.** Es la mayor distancia entre lo prometido y lo entregado.
`PORTABILITY.md` exige que un cambio de plataforma sea posible "using only
canonical artifact + checkpoint + adapter". En Claude —la plataforma
nativa— eso hoy no funciona. Además el adapter cierra con
"**Fallback:** N/A — native skill primitive is used directly", cerrando la
única salida.

---

### P1-4 — `exports/` nunca se generó y nadie lo declaró

`START_PROMPT.md` §10 paso 4 ordena "generate exports". `PORTABILITY.md`
define la ubicación: `exports/<platform>/`. **El directorio no existe.**
`FINAL_REPORT.md` no lo menciona ni en "Unresolved issues" ni como diferido
en `docs/FUTURE_EXTENSIONS.md`. Es una omisión silenciosa de un paso
numerado, que es peor que la omisión misma.

### P1-5 — `CHECKPOINT.md` incumple su propio contrato

`START_PROMPT.md` §4 fija la plantilla obligatoria con 10 campos.
`CHECKPOINT.md` omite **`tests_failed:`**. Además, `shared/contracts/checkpoint.schema.json`
existe pero **nada valida `CHECKPOINT.md` contra él** — el validador ni lo mira.

### P1-6 — El validador degrada en silencio y por eso `FINAL_REPORT.md` afirma algo no verificado

`scripts/validate_suite.py:118-120` captura `ImportError` de `jsonschema` y
lo convierte en **warning**, no en fallo — y aun así imprime *"All skills
pass structural validation"* y sale con **código 0**.

En el entorno de build `jsonschema` **no estaba instalado** (tuve que
instalarlo). Por tanto la validación real contra
`skill-manifest.schema.json` **nunca se ejecutó**, pese a que
`FINAL_REPORT.md` afirma: *"every `manifest.json` validates against
`shared/contracts/skill-manifest.schema.json`"*.

**Matiz honesto:** tras instalar `jsonschema`, los 15 manifests **sí pasan**.
La afirmación resultó verdadera — pero fue escrita sin evidencia. El defecto
es del validador y del proceso, no de los manifests.

### P1-7 — Research Architect: falta la gate explícita de ≥200 iteraciones totales

`docs/RESEARCH_ARCHITECT_V2_INVARIANTS.md` lista como bullet propio "minimum
200 valid research-architecture iterations", separado de los ≥150 y ≥50.
`skills/02-research-architect/SKILL.md` solo impone ≥150 y ≥50 (líneas
313-314, 333-334). El envelope emite `total_valid: 0` (línea 257)
**sin umbral asociado**. Aritméticamente 150+50=200, pero no hay gate
explícita y las iteraciones de Fase 1 no se contabilizan.

### P2-8 — Puntos ciegos del validador

No comprueba: validez meta-schema de `schemas/*.json`; enlaces internos
rotos; coherencia `routing-graph.json` ↔ manifests; `CHECKPOINT.md` contra su
schema; que cada `outputs[]` tenga plantilla; ciclos; frontmatter. Es un
comprobador de *presencia de archivos*, no de *integridad*. Cada P0 de esta
auditoría es invisible para él.

### P2-9 — Referencia cruzada mal formada

`skills/10-brand-identity-system/examples/01-web-first-service-cross-section.md`
cita `examples/01-radiotomography-finance.md` como si fuera local; vive en
`skills/09-brand-visual-direction/examples/`.

### P2-10 — Ruido para link-checkers

`skills/05-ai-resource-router/evals/cases/{01,04}-*.md` citan `PROMPTS/T1.md`,
`PROMPTS/T2.md`, `PROMPTS/T3.md`. Son **artefactos de salida** (correcto),
pero indistinguibles de rutas del repo. Conviene marcarlos.

### P2-11 — `docs/BLUEPRINT_VALIDATION.md` es un sello sin evidencia

5 líneas que declaran "**PASS**" sin decir qué se comprobó ni cómo.

---

## 5. PLAN DE CORRECCIÓN PARA SONNET

Ejecutar **en este orden**. Cada tarea trae criterio de aceptación
verificable. No abrir tareas fuera de esta lista.

> Rama: `claude/keen-hopper-i7za7f`. Commit por tarea o por bloque (T1-T3,
> T4-T7, T8-T11, T12-T13). Al final, **repaquetar** — el ZIP quedará
> desincronizado en cuanto se toque el primer archivo.

---

### T1 — Resolver la referencia colgante de la skill 07 (cierra P2-2)

Dos opciones válidas. **Recomendada: escribirlo** (el hueco es real y el
documento aporta), pero si se prefiere cerrar rápido, basta con borrar el
inciso `(see references/audience-and-differentiation-evidence.md if present,
and …)` de `skills/07-brand-strategy/SKILL.md:95` conservando la referencia
al failure mode. **No dejar la mención sin el archivo.**

Si se escribe: crear
`skills/07-brand-strategy/references/audience-and-differentiation-evidence.md`.

Debe ser un documento de método real, al nivel de los otros dos references de
esa skill (léelos primero para calibrar tono, longitud y densidad; rondan las
40-70 líneas y son operativos, no genéricos). Contenido mínimo:

- Qué cuenta como **evidencia** para una afirmación de audiencia (fuente
  primaria, dato observado, testimonio, proxy de mercado) y qué **no**
  (intuición del fundador, analogía con un competidor, deseo).
- El test de **diferenciación**: cómo comprobar que un eje de diferenciación
  es (a) cierto, (b) relevante para esa audiencia, (c) no reclamable
  idénticamente por ≥2 competidores nombrados.
- Qué hacer cuando la evidencia falta: degradar la afirmación a hipótesis,
  registrarla, y **no** dejarla entrar en `BRAND_STRATEGY.md` como hecho.
- Enganche explícito con la gate "no unsupported claims" de esa skill.

Verificar el contexto exacto en `skills/07-brand-strategy/SKILL.md:90-100`
para que el documento responda justo a lo que ese paso invoca.

**Aceptación:** el escaneo de referencias rotas devuelve 0 en `skills/`.

---

### T2 — Regenerar `routing-graph.json` con tipado de aristas (cierra P0-1)

Reconstruir el grafo **desde los manifests**, que son la fuente de verdad
(`PORTABILITY.md` §"Source-of-truth hierarchy" pone `manifest.json` por
encima del grafo).

Nuevo formato:

```json
{
  "generated_from": "skills/*/manifest.json",
  "edge_types": {
    "forward": "avance normal del pipeline",
    "feedback": "retorno de remediación; permitido formar ciclo",
    "conditional": "invocación lateral opcional (router/orquestador)"
  },
  "edges": [
    { "from": "brand-discovery", "to": "brand-strategy",
      "type": "forward", "purpose": "discovery brief" },
    { "from": "brand-quality-auditor", "to": "brand-book-builder",
      "type": "feedback", "purpose": "canon fix loop" }
  ]
}
```

Reglas de clasificación:
- `forward` — sigue el orden de `WORKFLOW_MAP.md`.
- `feedback` — va hacia atrás en ese orden (auditor→compilador,
  hijo→orquestador, cualquier `→ canonical-context-builder` de actualización
  de canon).
- `conditional` — aristas desde/hacia `ai-resource-router` y las del
  orquestador hacia sus hijos.

Las 56 aristas deben aparecer. Conservar los `purpose` actuales de las 19
existentes.

**Aceptación:** el conjunto de aristas de `routing-graph.json` es **idéntico**
al conjunto derivado de los 15 `handoffs_to`; todo ciclo detectado por DFS
atraviesa al menos una arista `feedback` o `conditional`.

---

### T3 — Añadir frontmatter YAML a los 15 `SKILL.md` (cierra P0-3)

Insertar al principio de cada `SKILL.md`, **antes** del `# Título`:

```yaml
---
name: canonical-context-builder
description: Reconstruye y mantiene la verdad canónica de un proyecto — hechos, decisiones cerradas, hipótesis vivas y restricciones — a partir de fuentes fragmentadas. Úsala cuando el contexto esté disperso entre notas, chats y archivos, o antes de research/auditoría/trabajo de marca que dependan de contexto fiable. No inventa hechos ausentes.
---
```

Reglas:
- `name` = el `id` del `manifest.json` (**sin** el prefijo numérico de
  carpeta), 15/15 ya alineados.
- `description` en tercera persona, **una sola línea**, ≤1024 caracteres,
  y debe contener *qué hace* + *cuándo dispararla* + *el no-trigger clave*.
  Derivarla de `purpose` + `triggers` + `non_triggers` del manifest — no
  reinventarla.
- **No** modificar nada más del cuerpo del `SKILL.md`.

Después, corregir el bloque **Fallback** de los 15 `adapters/claude.md`, que
hoy dice "N/A". Sustituirlo por algo veraz, p. ej.:

> **Fallback:** en superficies sin primitiva de Skill (claude.ai sin
> filesystem), cargar `SKILL.md` como instrucción y seguir
> `adapters/generic.md` para la E/S de artefactos.

Y ajustar la línea de *Invocation* para que diga que el registro nativo
depende del frontmatter, ya presente.

**Aceptación:** los 15 `SKILL.md` empiezan por `---`, el frontmatter parsea
como YAML, `name` == `manifest.id` en 15/15, y ningún `adapters/claude.md`
declara un fallback "N/A".

---

### T4 — Endurecer `scripts/validate_suite.py` (cierra P1-6 y P2-8)

Este es el cambio de mayor apalancamiento: cada P0 de arriba existió porque el
validador no podía verlo.

1. **`jsonschema` ausente → error, no warning.** Salir con código 1 y el
   mensaje `FAIL: jsonschema no instalado; la validación de manifests no se
   ejecutó`. Nunca imprimir "All skills pass" si una comprobación no corrió.
2. **Meta-schema:** validar cada `schemas/*.json` con
   `Draft202012Validator.check_schema` y exigir `$schema` presente.
3. **Enlaces internos:** extraer referencias entre backticks que contengan
   `/` y terminen en `.md`/`.json`; resolver contra (directorio del archivo,
   raíz de la skill, raíz del repo); fallar si ninguna existe. Excluir vía
   allowlist las rutas de *artefacto de salida* (ver T9).
4. **Grafo:** derivar las aristas de los manifests y fallar si difieren de
   `routing-graph.json`.
5. **Ciclos:** DFS sobre el grafo; fallar solo si existe un ciclo compuesto
   **íntegramente** de aristas `forward` (eso sí violaría la gate 1).
6. **Checkpoint:** validar `CHECKPOINT.md` (parsear el bloque YAML) contra
   `shared/contracts/checkpoint.schema.json` y exigir los 10 campos de
   `START_PROMPT.md` §4.
7. **Frontmatter:** exigir que cada `SKILL.md` abra con frontmatter YAML
   válido y que `name` == `manifest.id`.
8. **Cobertura de plantillas:** cada entrada de `outputs[]` que **no** acabe
   en `/` debe tener archivo homónimo en `templates/`. *(Ojo: `PROMPTS/` y
   `HANDOFF_PACKAGES/` son salidas-directorio legítimas con plantilla
   asociada — `PROMPT_TEMPLATE.md` y `HANDOFF_PACKAGE_README.md`. No marcarlas.)*
9. **Estructura de evals:** cada caso debe traer las 5 secciones de
   `EVAL_TEMPLATE.md`. *(Hoy 60/60 cumplen — esto blinda la regresión.)*

**Aceptación:** `python3 scripts/validate_suite.py` sale 0 **solo** con todas
las comprobaciones ejecutadas; desinstalar `jsonschema` lo hace salir 1;
introducir a mano un enlace roto lo hace salir 1.

---

### T5 — Gate explícita de ≥200 en Research Architect (cierra P1-7)

En `skills/02-research-architect/SKILL.md`:
- En **Quality gates** (≈línea 313), añadir como bullet propio:
  `≥200 iteraciones válidas totales (post-test de delta material), de las
  cuales ≥150 de expansión de alcance y ≥50 de pulido/consolidación.`
- En el envelope `RUN_RESULT` (≈línea 257), anotar el umbral igual que los
  otros dos: `total_valid: 0  # must be >= 200 for status COMPLETE`.
- En **Stop conditions** (≈línea 333), incluir el total en la condición de
  cierre normal.
- Reflejar el umbral en `schemas/output.schema.json` si `iteration_counts`
  está modelado ahí (`minimum: 200`).

**Aceptación:** `grep -c "200" skills/02-research-architect/SKILL.md` ≥ 3 y el
número aparece en gates, envelope y stop conditions.

---

### T6 — Completar `CHECKPOINT.md` (cierra P1-5)

Añadir `tests_failed: []` en su posición de `START_PROMPT.md` §4 (entre
`tests_passed` y `known_issues`). Actualizar `phase` y `completed` para
reflejar esta ronda de auditoría y corrección — no dejarlo diciendo
"SUITE_COMPLETE / next_exact_action: none" con trabajo abierto.

**Aceptación:** los 10 campos presentes; valida contra `checkpoint.schema.json`
vía T4.6.

---

### T7 — Resolver `exports/` (cierra P1-4)

Decidir **explícitamente**, no omitir. Recomendación: **construirlo**, porque
`PORTABILITY.md` ya lo especifica y es barato.

Generar `exports/<platform>/<skill-id>.md` para las 6 plataformas: un único
archivo autocontenido por skill y plataforma = `SKILL.md` concatenado con su
`adapters/<platform>.md`, con cabecera que declare
`Build artifact — no editar; fuente: skills/<n>/SKILL.md`. Automatizarlo en
`scripts/build_exports.py`, nunca a mano.

Si en su lugar se decide **no** construirlo, entonces hay que registrarlo en
`docs/FUTURE_EXTENSIONS.md` **y** en "Unresolved issues" de
`FINAL_REPORT.md`. Lo inaceptable es el estado actual: omitido y no dicho.

**Aceptación:** o existe `exports/` con 90 archivos generados por script, o
la omisión está declarada en los dos documentos.

---

### T8 — Arreglar la referencia cruzada de la skill 10 (cierra P2-9)

En `skills/10-brand-identity-system/examples/01-web-first-service-cross-section.md`,
cambiar `examples/01-radiotomography-finance.md` por la ruta desde raíz:
`/skills/09-brand-visual-direction/examples/01-radiotomography-finance.md`.

### T9 — Desambiguar los artefactos de salida del router (cierra P2-10)

En `skills/05-ai-resource-router/evals/cases/{01,04}-*.md`, reescribir
`` `PROMPTS/T1.md` `` como `` `<output>PROMPTS/T1.md` `` (o la convención que
adopte T4.3) para que el comprobador de enlaces no los trate como rutas del
repo. Mantener la coherencia con el `outputs[]` del manifest.

### T10 — Dar contenido a `docs/BLUEPRINT_VALIDATION.md` (cierra P2-11)

Sustituir el sello "PASS" por: qué se comprobó, con qué comando, con qué
resultado y en qué fecha. Si no aporta valor sobre `validate_suite.py`,
borrarlo y remitir al validador.

### T11 — Corregir `FINAL_REPORT.md` (cierra la causa raíz)

Es el documento que convirtió huecos en "None blocking". Actualizar:
- "Unresolved issues" debe listar lo que quede realmente abierto tras T1-T10.
- Retirar o matizar la afirmación sobre validación de manifests hasta que T4
  la ejecute de verdad.
- Añadir una línea sobre `exports/` según lo decidido en T7.
- Añadir sección "Auditoría independiente" remitiendo a este `AUDIT_REPORT.md`.

---

### T12 — Revalidar

```bash
python3 scripts/validate_suite.py    # debe salir 0 con TODAS las comprobaciones corriendo
```

### T13 — Repaquetar (obligatorio; el ZIP ya no cuadra)

Rehacer `dist/AGENTIC_SKILL_SUITE_V1.zip` con el mismo contenido de antes
**más** `exports/` y `AUDIT_REPORT.md`, regenerar
`dist/AGENTIC_SKILL_SUITE_V1_SHA256.txt`, y **verificar**:

```bash
sha256sum -c dist/AGENTIC_SKILL_SUITE_V1_SHA256.txt
unzip -q -o dist/AGENTIC_SKILL_SUITE_V1.zip -d /tmp/zipx && diff -rq /tmp/zipx . -x '.git' -x 'dist'
```

Ambos deben salir limpios, como salen hoy. Considerar subir la versión a
`1.0.1` en `suite.manifest.json` y en los 15 manifests si se acepta el
cambio de contrato del frontmatter (T3).

---

## 6. NO TOCAR

Riesgo de regresión sin beneficio:

- Los 60 casos de eval y los 7 walkthroughs de integración. Están completos y
  son específicos.
- Los 90 adapters, más allá del bloque *Fallback*/*Invocation* de
  `claude.md` que exige T3.
- El cuerpo de los 15 `SKILL.md` fuera de lo que piden T3 y T5.
- `MASTER_PLAN.md`, `ARCHITECTURE.md`, `WORKFLOW_MAP.md`,
  `QUALITY_GATES.md`, `START_PROMPT.md` — son la especificación, no el
  entregable.
- Los `SPEC.md` de cada skill.

---

## 7. NOTA SOBRE ORDEN DE OLAS (no es defecto)

`START_PROMPT.md` §3 lista la Wave 1 como CCB → Rapid Capture → Research
Architect → Product Auditor → AI Resource Router. La numeración del repo
(02 Research Architect, 04 Rapid Capture) sigue el catálogo de
`MASTER_PLAN.md`, que difiere. `START_PROMPT.md` autoriza explícitamente
desviarse ("unless a dependency analysis proves a superior one") y
`EXECUTION_PLAN.md` documenta ese análisis. **La numeración de skill no es el
orden de build.** No corregir.

---

## 8. RESUMEN EJECUTIVO

Se construyó una suite sustancial y bien pensada: 15 skills con estructura
idéntica y correcta, 60 evals reales, 7 pruebas de integración, 90 adapters
diferenciados, schemas válidos y un paquete verificable byte a byte. El
trabajo de fondo es sólido.

Falló la **capa de verificación**. El validador comprueba que los archivos
existen, no que digan la verdad — y al degradar en silencio permitió que
`FINAL_REPORT.md` declarara verificado lo que nunca se ejecutó. A la sombra
de eso pasaron: un grafo de routing desincronizado al que 10 documentos
remiten, 15 adapters que prometen una integración nativa imposible sin
frontmatter, una referencia colgante, y cuatro pasos de `START_PROMPT.md`
omitidos sin declararse.

Los dos hallazgos serios son **P0-1 (grafo)** y **P0-3 (frontmatter)**.
Ninguno es estructural. **T2, T3 y T4 resuelven el grueso del riesgo**, y T4
—el validador— es lo que impide que esto vuelva a pasar: hoy los dos P0 son
literalmente invisibles para él.

---

*Auditoría generada por Claude Code.*
