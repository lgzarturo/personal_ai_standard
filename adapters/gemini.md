# Gemini

## Gemini Apps

1. En **Configuración → Inteligencia personal → Instrucciones para Gemini**,
   añade la [instrucción base permanente](README.md#instrucción-base-permanente)
   y deja activado el ajuste cuando esté disponible en tu cuenta.
2. [Genera `pais.zip`](README.md#exportar-e-instalar-la-skill). En
   **Personalizar → Skills → Crear → Subir**, carga el ZIP y revisa y guarda
   la skill. El archivo incluye el arranque y los documentos de PAIS.
3. Deja la skill activada para que Gemini pueda seleccionarla por relevancia.
   Para comprobarla en un chat nuevo, elígela con `/` o `@`, según la interfaz.

Actualiza el ZIP desde la misma revisión de PAIS cuando cambien sus documentos.
Si la revisión de Gemini impide la carga, conserva la instrucción base y
adjunta los documentos permitidos a la conversación cuando los necesites.

[Crear y administrar skills](https://support.google.com/gemini/answer/17094296) ·
[Transición de Gems a skills](https://support.google.com/gemini/answer/18560919) ·
[Instrucciones para Gemini](https://support.google.com/gemini/answer/16598625?co=GENIE.Platform%3DDesktop)

## Gemini CLI

1. Añade la [instrucción local](README.md#instrucción-para-una-copia-local)
   y el bloque base a `~/.gemini/GEMINI.md`. Puedes importar `BOOTSTRAP.md`,
   `CORE.md` y `LANGUAGE.md` mediante `@ruta` si quieres que formen parte
   del contexto de cada sesión.
2. [Exporta la skill](README.md#exportar-e-instalar-la-skill) y descomprime
   `pais.zip` en `~/.gemini/skills/pais/`. Como alternativa, ejecuta
   `gemini skills install RUTA_AL_DIRECTORIO_PAIS --scope user` sobre la
   carpeta local ya extraída y sigue la confirmación que muestre Gemini CLI.
3. Ejecuta `/memory reload` y `/memory show` para comprobar las instrucciones.
   Usa `/skills list` para verificar que la skill está disponible. Si el
   agente pide aprobación para activarla, revisa la solicitud.

[Contexto con GEMINI.md](https://geminicli.com/docs/cli/gemini-md/) ·
[Agent Skills de Gemini CLI](https://geminicli.com/docs/cli/skills/)
