# Muse Code

1. Añade la [instrucción base y la referencia local](README.md#instrucción-para-una-copia-local)
   a `~/.config/muse/AGENTS.md` o a `$XDG_CONFIG_HOME/muse/AGENTS.md` si
   configuraste esa ruta. Muse Code carga las reglas de usuario en todos
   los proyectos y da precedencia a las reglas del proyecto si hay conflicto.
2. [Exporta y descomprime la skill](README.md#exportar-e-instalar-la-skill) y
   ejecuta `muse skills install RUTA_AL_DIRECTORIO_PAIS --scope user`
   sobre la carpeta extraída.
3. En una sesión nueva, usa `/rules` para comprobar que aparece la regla
   global. Consulta `muse skills list --source user` y usa `/pais` para
   ejecutar la skill.

[Configuración e instrucciones de Muse Code](https://dev.meta.ai/docs/muse-code/configuration) ·
[Skills en Muse Code](https://dev.meta.ai/docs/muse-code/extending)
