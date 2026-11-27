# Codex

1. Añade la [instrucción base y la referencia local](README.md#instrucción-para-una-copia-local)
   a `~/.codex/AGENTS.md` o al archivo equivalente bajo `CODEX_HOME`. Si
   existe un `AGENTS.override.md` global con contenido, añade el bloque
   allí. Codex elige el primero de esos archivos que tenga contenido.
2. [Exporta la skill](README.md#exportar-e-instalar-la-skill) y descomprime
   `pais.zip` en `~/.agents/skills/pais/`.
3. Abre una sesión nueva fuera de PAIS. Comprueba las instrucciones
   globales y selecciona `$pais` si quieres invocar la skill de forma explícita.

Para una sesión remota, configura la copia y las instrucciones donde se
ejecute Codex, o usa una skill disponible para esa sesión.

[Archivos AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) ·
[Skills personales y de proyecto](https://learn.chatgpt.com/docs/customization/overview)
