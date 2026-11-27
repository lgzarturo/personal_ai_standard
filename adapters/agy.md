# Google Antigravity

1. Crea `~/.gemini/config/rules/pais.md` con este encabezado. Debajo, añade
   la [instrucción base y la referencia a la copia local](README.md#instrucción-para-una-copia-local).

   ```yaml
   ---
   trigger: always_on
   ---
   ```

2. [Exporta la skill](README.md#exportar-e-instalar-la-skill) y descomprime
   `pais.zip` en `~/.gemini/config/skills/pais/`. Ese directorio personal es
   compartido por Antigravity App y la CLI `agy`. El IDE puede descubrirlo
   también desde su configuración global.
3. En Antigravity App, comprueba **Customizations → Installed → Skills & Rules**.
   En `agy`, usa `/skills` para comprobar la skill y `/pais` para invocarla.

Antigravity también lee la regla global de `~/.gemini/GEMINI.md`. Si ya
configuraste allí el bloque base para Gemini CLI, conserva una sola copia
de la regla que Antigravity vaya a cargar.

[Reglas de Antigravity](https://antigravity.google/docs/rules/) ·
[Descubrimiento de personalizaciones](https://antigravity.google/docs/customization-discovery/) ·
[Agent Skills de Antigravity](https://antigravity.google/docs/skills/)
