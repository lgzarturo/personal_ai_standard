# Projects

Catálogo de proyectos registrados en Personal AI Standard.

## Registered projects

| Project | Repository | Project rules |
|---|---|---|
| CodeConductor | https://github.com/lgzarturo/codeconductor | [PROJECT_RULES.md](codeconductor/PROJECT_RULES.md) |
| MicroSDD | https://github.com/lgzarturo/microsdd | [PROJECT_RULES.md](microsdd/PROJECT_RULES.md) |

## Project discovery

Identifica el proyecto utilizando, en orden de prioridad:

1. El proyecto indicado explícitamente por el usuario.
2. La URL del repositorio Git activo.
3. El contexto inequívoco de la tarea.

Normaliza las URLs SSH y HTTPS antes de compararlas.

Carga únicamente las reglas de los proyectos relevantes para la tarea.

No infieras que un proyecto está activo únicamente
por una coincidencia parcial de nombre.

Si el proyecto no está registrado, utiliza sus convenciones
locales y las reglas generales de PAIS.

## Registration

Para registrar un proyecto:

1. Crea un directorio con su identificador.
2. Utiliza templates/PROJECT_RULES.md como referencia.
3. Identifica las fuentes de verdad del proyecto.
4. Documenta únicamente las convenciones relevantes.
5. Incorpora el proyecto a este índice.

## Privacy

Este catálogo es público.

No almacenes credenciales, información confidencial, datos de clientes,
rutas privadas ni secretos de infraestructura.

## Fundamental principle

El catálogo facilita el descubrimiento del contexto.
El repositorio de cada proyecto conserva la autoridad sobre su implementación.