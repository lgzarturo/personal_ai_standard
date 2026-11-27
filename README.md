# Personal AI Standard

Personal AI Standard (**PAIS**) es un estándar personal de trabajo
asistido por inteligencia artificial.

## Arquitectura

PAIS reúne preferencias personales en documentos Markdown que cada agente
puede consultar según la tarea. Puede utilizarse de forma independiente de
CodeConductor y MicroSDD.

| Documento | Cuándo consultarlo |
| --- | --- |
| [BOOTSTRAP.md](BOOTSTRAP.md) | Al iniciar una sesión. Indica qué contexto cargar y cómo resolver conflictos. |
| [CORE.md](CORE.md) | En toda sesión. Define los principios de razonamiento, decisión y ejecución. |
| [LANGUAGE.md](LANGUAGE.md) | Para determinar el idioma de la interacción y de cada entregable. |
| [WRITING.md](WRITING.md) | Para tareas de comunicación, redacción o documentación. |
| [FEEDBACK.md](FEEDBACK.md) | Para evaluar el estándar o proponer cambios de preferencias. |
| [Catálogo de proyectos](projects/README.md) | Para identificar los proyectos relevantes y localizar sus perfiles. |
| [Plantilla de reglas](templates/PROJECT_RULES.md) | Al registrar un proyecto en el catálogo. |

Cada perfil reúne las convenciones del proyecto y apunta a sus fuentes de verdad.
El repositorio del proyecto conserva la autoridad sobre la implementación, los
contratos y las verificaciones vigentes. Las herramientas de cada proyecto
aplican sus propios controles de ejecución.

El agente identifica el proyecto mediante la indicación del usuario, el
repositorio Git activo o el contexto inequívoco de la tarea, en ese orden.
Después consulta el catálogo y carga solo los perfiles relevantes. Si el
proyecto carece de perfil, aplica PAIS junto con las convenciones locales
disponibles.

## Instrucción global portable

Añade la [instrucción base permanente](adapters/README.md#instrucción-base-permanente)
al ajuste de usuario que documenta tu adaptador. Para disponer de los documentos
detallados en un agente web, instala la skill de PAIS o adjunta las fuentes
que requiera la tarea. La [referencia remota](adapters/README.md#instrucción-para-acceso-remoto)
está disponible para sesiones con acceso a GitHub.

## Integración con agentes locales

1. Clona el repositorio en una ruta accesible para el agente. Puedes usar
   una sola copia por equipo.

   ```sh
   git clone https://github.com/lgzarturo/personal_ai_standard.git "$HOME/.pais"
   ```

2. Añade la instrucción base y el [bloque de copia local](adapters/README.md#instrucción-para-una-copia-local)
   donde indique tu adaptador. Usa la ruta absoluta a tu copia de PAIS.
3. Conserva el catálogo y los perfiles dentro de `projects/` para que el
   agente pueda seguir los enlaces desde el catálogo. Al actualizar la copia,
   usa una misma revisión de Git para todos los documentos.

## Adaptadores

Consulta la [guía de adaptadores](adapters/README.md) para configurar las
instrucciones globales de tu agente e instalar la skill de PAIS con sus
referencias locales.

## Calibración

Consulta los [escenarios de calibración](calibration/README.md) para evaluar
la selección de idioma, el descubrimiento de proyectos, la precedencia de
instrucciones y el consumo de contexto.

## Versionado

Las etiquetas de Git con formato `vMAJOR.MINOR.PATCH` identifican las versiones
publicadas del estándar. Consulta [CHANGELOG.md](CHANGELOG.md) para conocer los
cambios incluidos en cada versión. Los números en los documentos Markdown
identifican sus revisiones y la etiqueta de Git identifica la publicación
del conjunto.

| Incremento | Cuándo aplicarlo |
| --- | --- |
| `MAJOR` | A partir de `v1.0.0`, para cambios incompatibles en las instrucciones o en la forma de cargar PAIS. |
| `MINOR` | Para incorporaciones compatibles. Durante la serie `0.x` también puede incluir cambios incompatibles, que se deben explicar en el registro de cambios. |
| `PATCH` | Para correcciones y aclaraciones que conservan la compatibilidad. |

Registra los cambios aprobados bajo **Sin publicar**. Al preparar una
publicación, verifica la revisión de Git, mueve sus entradas a una sección con
la versión y la fecha, y etiqueta esa revisión.
