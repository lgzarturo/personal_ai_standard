# Adaptadores de PAIS

Cada adaptador indica dónde colocar la referencia a [BOOTSTRAP.md](../BOOTSTRAP.md).
El resto del contexto se selecciona desde ese documento según la tarea.

| Plataforma | Configuración |
| --- | --- |
| [ChatGPT](chatgpt.md) | Instrucciones personalizadas o de proyecto. |
| [Claude](claude.md) | Instrucciones y conocimiento de un proyecto de Claude. |
| [Claude Code](claude-code.md) | `CLAUDE.md` del usuario. |
| [Codex](codex.md) | `AGENTS.md` del usuario. |
| [Gemini](gemini.md) | Instrucciones de un Gem o `GEMINI.md` para Gemini CLI. |
| [Cursor](cursor.md) | User Rules de Cursor Agent. |
| [Muse Code](muse.md) | `AGENTS.md` del proyecto. |
| [OpenCode](opencode.md) | `AGENTS.md` del usuario o `instructions` en la configuración. |

## Instrucción para una copia local

[Prepara una copia local](../README.md#integración-con-agentes-locales) y sustituye
`RUTA_ABSOLUTA_A_PAIS` por su ruta en el equipo donde corre el agente. Añade el
bloque al archivo o ajuste que indique tu adaptador y conserva las instrucciones
que ya existan.

```text
Aplica Personal AI Standard (PAIS). Lee RUTA_ABSOLUTA_A_PAIS/BOOTSTRAP.md
al iniciar la sesión. Resuelve los demás documentos de PAIS desde el directorio
que contiene BOOTSTRAP.md y carga únicamente los que indique para la tarea.
Si la ruta no es accesible, informa de la limitación y usa las instrucciones
disponibles en el proyecto.
```

Para comprobar la instalación, abre una sesión en un repositorio distinto de
PAIS. Pide al agente que indique la ruta de `BOOTSTRAP.md` que pudo leer y la
ruta del documento que define el idioma. Debe localizar `LANGUAGE.md` bajo la
misma copia de PAIS.

## Instrucción para acceso remoto

```text
Aplica Personal AI Standard (PAIS). Lee este documento al iniciar la sesión:
https://raw.githubusercontent.com/lgzarturo/personal_ai_standard/main/BOOTSTRAP.md
Resuelve los demás archivos desde el directorio de esa misma revisión y carga
únicamente los que indique BOOTSTRAP.md para la tarea. Si un archivo remoto
no es accesible, usa su copia adjunta de la misma revisión. Si ambas faltan,
indica la limitación y continúa con las instrucciones de la tarea.
```

Para fijar una revisión, sustituye `main` por el identificador de un commit
o una etiqueta publicada de PAIS en la URL.

Si la plataforma requiere adjuntos, usa archivos de una sola revisión. Empieza
por `BOOTSTRAP.md`, `CORE.md` y `LANGUAGE.md`. Incorpora `WRITING.md` para tareas
de redacción, `FEEDBACK.md` para revisar el estándar y el catálogo y los perfiles
pertinentes para tareas de proyecto. Si la plataforma presenta todos los
archivos en una lista plana, indica en las instrucciones la ruta original del
catálogo y de cada perfil adjunto.

En una sesión nueva, pide al agente que indique la URL o el adjunto de
`BOOTSTRAP.md` que leyó y qué archivo consultó para determinar el idioma.
Repite la prueba con el enlace inaccesible y los archivos adjuntos. El agente
debe identificar de dónde obtuvo el contexto o señalar la limitación si ambas
fuentes faltan.
