# Adaptadores de PAIS

Configura la instrucción global para que las preferencias básicas estén presentes
desde una sesión nueva. La skill `pais` aporta los documentos completos cuando el
agente la selecciona o el usuario la invoca. La disponibilidad global de una skill
depende de la cuenta o del equipo. El cliente decide cuándo cargar sus referencias.

| Plataforma | Instrucciones de inicio | Skill disponible para el usuario |
| --- | --- | --- |
| [ChatGPT](chatgpt.md) | Instrucciones personalizadas. | Menú Skills en cuentas habilitadas. |
| [Claude](claude.md) | Instrucciones del perfil. | Menú Skills en cuentas habilitadas. |
| [Claude Code](claude-code.md) | `~/.claude/CLAUDE.md`. | `~/.claude/skills/pais/`. |
| [Codex](codex.md) | `AGENTS.md` en el directorio personal de Codex. | `~/.agents/skills/pais/`. |
| [Gemini](gemini.md) | Instrucciones para Gemini Apps o `~/.gemini/GEMINI.md` en CLI. | Menú Skills en Gemini Apps o `~/.gemini/skills/pais/` en CLI. |
| [Antigravity](agy.md) | `~/.gemini/config/rules/pais.md` con activación permanente. | `~/.gemini/config/skills/pais/`. |
| [Cursor](cursor.md) | User Rules. | `~/.cursor/skills/pais/`. |
| [Muse Code](muse.md) | Reglas de usuario de Muse Code. | Instalación con alcance `user`. |
| [OpenCode](opencode.md) | `~/.config/opencode/AGENTS.md`. | `~/.config/opencode/skills/pais/`. |

## Instrucción base permanente

Añade este bloque en el ajuste global o archivo que indique el adaptador. Conserva
el contenido que ya exista.

```text
Aplica Personal AI Standard (PAIS). Usa español neutro para la conversación.
Para cada entregable, sigue mi indicación explícita y las convenciones
aplicables del proyecto. Distingue hechos de supuestos, apoya tus conclusiones
en evidencia y prioriza corrección, simplicidad y seguridad. Al redactar,
conserva mi intención y mi voz. Respeta los controles del entorno y pide
aprobación antes de convertir una preferencia en una regla permanente.
Si está disponible la skill pais, úsala para consultar las reglas detalladas
de idioma, redacción, retroalimentación o del proyecto.
```

## Instrucción para una copia local

[Prepara una copia local](../README.md#integración-con-agentes-locales), conserva
el bloque base y añade la referencia siguiente. Sustituye
`RUTA_ABSOLUTA_A_PAIS` por la ruta que el agente pueda leer.

```text
Al iniciar la sesión, lee RUTA_ABSOLUTA_A_PAIS/BOOTSTRAP.md. Resuelve los demás
documentos desde ese mismo directorio. Si la ruta resulta inaccesible, informa
de la limitación y aplica las instrucciones disponibles en la sesión.
```

## Exportar e instalar la skill

Ejecuta desde la raíz de una copia de PAIS la orden del formato que corresponda.
Solo se requiere Python 3.9 o superior para preparar los archivos.

```sh
python adapters/package-skill.py pais.zip
python adapters/package-skill.py pais-claude.zip --claude
```

- `pais.zip` contiene `SKILL.md` en la raíz. Úsalo para Gemini Apps y, si la
  función está disponible, para ChatGPT. Para clientes locales, descomprímelo
  dentro del directorio `pais/` que indique el adaptador.
- `pais-claude.zip` contiene la carpeta `pais/` que requiere la carga de Claude.

Los ZIP incluyen copias en texto de los documentos vigentes. Las identidades
de repositorio se conservan como texto para que el paquete funcione sin URLs
ni scripts. Reexporta el ZIP y actualiza la instalación si cambian las fuentes.
Si el cliente ya descubre la skill desde otro directorio compatible,
conserva una sola instalación.

## Instrucción para acceso remoto

Usa esta opción en un chat que permita consultar fuentes externas. Las skills
exportadas llevan sus propias referencias.

```text
Aplica Personal AI Standard (PAIS). Lee este documento al iniciar la sesión:
https://raw.githubusercontent.com/lgzarturo/personal_ai_standard/main/BOOTSTRAP.md
Resuelve los demás archivos desde el directorio de esa misma revisión y carga
únicamente los que indique BOOTSTRAP.md para la tarea. Si un archivo remoto
no es accesible, usa su copia adjunta de la misma revisión. Si ambas faltan,
indica la limitación y continúa con las instrucciones de la tarea.
```

Fija una revisión sustituyendo `main` por el identificador del commit o por
una etiqueta de PAIS. Si recurres a adjuntos, empieza con `BOOTSTRAP.md`,
`CORE.md` y `LANGUAGE.md`, y añade los documentos que requiera la tarea.

## Comprobar la configuración

1. Abre una sesión nueva fuera del repositorio de PAIS. Sin mencionar la skill,
   pide una respuesta breve y comprueba que sigue la regla global de idioma.
   Si el cliente muestra las instrucciones cargadas, comprueba allí la fuente.
2. Pide usar `pais` para redactar un commit de CodeConductor. Comprueba que el
   commit está en inglés, que la conversación sigue en español y que el perfil
   consultado corresponde al proyecto. Si el cliente ofrece un selector de
   skills, repite la prueba seleccionándola explícitamente.
3. Registra la versión del cliente, el alcance (usuario, proyecto o cuenta) y
   cuáles de los archivos se cargaron. Usa los [escenarios de calibración](../calibration/README.md)
   para ampliar la comprobación.
