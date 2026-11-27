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

Para las herramientas que permiten configurar instrucciones personalizadas

```markdown
Utiliza Personal AI Standard (PAIS) como marco de referencia
para todas nuestras interacciones.

Fuente de verdad:
https://github.com/lgzarturo/personal_ai_standard

Consulta BOOTSTRAP.md para determinar qué documentos aplicar
según el contexto.

Aplica CORE.md de forma permanente, LANGUAGE.md para determinar
el idioma y WRITING.md cuando la tarea involucre comunicación
o generación de texto.

Para tareas de proyecto, usa el catálogo projects/README.md y
respeta las convenciones del proyecto activo.

Utiliza FEEDBACK.md para proponer mejoras al estándar,
sin modificar preferencias permanentes sin mi aprobación.

Si no puedes acceder al repositorio, informa de esta limitación
y utiliza las instrucciones disponibles localmente.
```

> Hay una limitación importante: proporcionar una URL
> en las instrucciones globales no garantiza que
> todos los agentes consulten el repositorio automáticamente.
> Algunos pueden carecer de acceso a Internet, de herramientas
> de lectura o de mecanismos de carga dinámica de contexto.

## Integración con agentes locales

1. Clona el repositorio en una ruta accesible para el agente. Puedes usar
   una sola copia por equipo.

   ```sh
   git clone https://github.com/lgzarturo/personal_ai_standard.git "$HOME/.pais"
   ```

2. Añade la instrucción global anterior a la configuración del agente y
   sustituye la URL del repositorio por la ruta absoluta a tu copia local.
   Indica la ruta al archivo `BOOTSTRAP.md` dentro de esa copia.
3. Conserva el catálogo y los perfiles dentro de `projects/` para que el
   agente pueda seguir los enlaces desde el catálogo. Al actualizar la copia,
   usa una misma revisión de Git para todos los documentos.

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
la versión y la fecha, y etiqueta esa revisión. La primera publicación
prevista es `v0.1.0`, después de completar la calibración del estándar.
