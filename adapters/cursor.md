# Cursor

1. En **Customize → Rules → User Rules** añade la
   [instrucción base y la referencia local](README.md#instrucción-para-una-copia-local).
   Esta regla de usuario se aplica a **Agent**.
2. [Exporta la skill](README.md#exportar-e-instalar-la-skill) y descomprime
   `pais.zip` en `~/.cursor/skills/pais/`. Reinicia Cursor y comprueba
   que `pais` aparece en el menú `/` de Agent.
3. Para Cloud Agents, verifica qué configuración y archivos están en el
   entorno que ejecuta el agente. Cursor ofrece **Sync Skills for Cloud
   Agents** para las skills en `~/.cursor/skills/`. Una sincronización de
   skills no hace accesible la ruta personal de tu copia de PAIS.

[Reglas de Cursor](https://cursor.com/docs/rules) ·
[Skills en Cursor](https://cursor.com/docs/skills)
