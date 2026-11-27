# OpenCode

Añade la [instrucción local](README.md#instrucción-para-una-copia-local)
a `~/.config/opencode/AGENTS.md` si quieres que el agente lea el arranque
a partir de una referencia. También puedes cargar directamente el arranque
mediante la propiedad `instructions` del archivo `opencode.json` o
`opencode.jsonc` global o del proyecto. Para esa modalidad, añade a
`instructions` una ruta local como `~/.pais/BOOTSTRAP.md` o la URL remota.

```json
{
  "instructions": [
    "https://raw.githubusercontent.com/lgzarturo/personal_ai_standard/main/BOOTSTRAP.md"
  ]
}
```

Conserva las demás entradas de configuración. En el primer mensaje, indica
al agente el directorio local o la URL base de la misma revisión para
resolver los documentos relativos que menciona `BOOTSTRAP.md`.
Si la URL no está disponible, usa la configuración con la copia local.

[Instrucciones de OpenCode](https://opencode.ai/docs/instructions)
