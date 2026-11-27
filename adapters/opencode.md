# OpenCode

1. Añade la [instrucción base y la referencia local](README.md#instrucción-para-una-copia-local)
   a `~/.config/opencode/AGENTS.md`.
2. [Exporta la skill](README.md#exportar-e-instalar-la-skill) y descomprime
   `pais.zip` en `~/.config/opencode/skills/pais/`. El agente puede cargarla
   mediante su herramienta `skill` cuando esté disponible y permitida.
3. Para incluir directamente los documentos base en el contexto inicial,
   puedes añadir las rutas locales a `instructions` en tu
   `opencode.json` o `opencode.jsonc` global. Sustituye las rutas si tu
   copia de PAIS está en otro directorio.

```json
{
  "instructions": [
    "~/.pais/BOOTSTRAP.md",
    "~/.pais/CORE.md",
    "~/.pais/LANGUAGE.md"
  ]
}
```

Conserva la configuración y las instrucciones que ya tengas. Para comprobar
la configuración resuelta, usa `opencode debug config`. En una sesión nueva
pide al agente que cargue `pais` y comprueba las fuentes que pudo consultar.

[Archivos de instrucciones](https://opencode.ai/docs/instructions) ·
[Skills en OpenCode](https://opencode.ai/docs/skills/)
