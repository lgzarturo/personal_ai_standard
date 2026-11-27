# MicroSDD — Project Rules

## Identity

- Project: MicroSDD
- Repository: https://github.com/lgzarturo/microsdd
- Package: microsdd

## Context

MicroSDD es un arnés ligero de ingeniería asistida por
inteligencia artificial que prioriza código mínimo,
correcto, verificable y trazable.

Utiliza especificaciones aprobadas, roles diferenciados,
restricciones de ejecución y mecanismos de validación
para controlar el alcance de los cambios.

Claude Code proporciona la orquestación nativa.

## Language

- Interacción con el usuario: español neutro.
- Documentación: español.
- Código fuente: respetar las convenciones existentes.
- Commits: respetar las convenciones del repositorio.
- Issues y pull requests: español como propuesta predeterminada.

Conservar identificadores, comandos y terminología técnica
cuando traducirlos reduzca precisión.

## Sources of truth

Base URL: https://github.com/lgzarturo/microsdd

- README.md: propósito, instalación y uso.
- CLAUDE.md: instrucciones operativas.
- docs/AGENT.md: contexto de ingeniería.
- docs/arquitectura.md: arquitectura.
- docs/convenciones.md: convenciones verificables.
- docs/especificaciones.md: especificaciones.
- spec/: contratos de tareas.
- .microharness/: arnés y configuración.
- .claude/hooks/: controles de ejecución.
- CHANGELOG.md: historial de versiones.

Consultar la configuración y las especificaciones vigentes
antes de ejecutar cambios.

## Engineering

- Priorizar KISS y YAGNI.
- Utilizar DRY y SOLID cuando resuelvan problemas concretos.
- Preservar el carácter ligero del arnés.
- Preferir la biblioteca estándar de Python.
- Mantener compatibilidad multiplataforma.
- Evitar servicios, dependencias e infraestructura innecesarios.
- Preferir controles ejecutables sobre instrucciones declarativas.
- Mantener cambios pequeños y trazables.

## Workflow

Respetar el flujo establecido:

1. Líder.
2. Autor de especificación.
3. Aprobación humana.
4. Implementador.
5. Revisor independiente.
6. Aprobación de cierre.

Un solo agente modifica el código de implementación.

El alcance aprobado y las pruebas selladas constituyen
restricciones del trabajo, no sugerencias.

## Verification

- Verificar el estado del arnés.
- Respetar los recibos RDD.
- Ejecutar las pruebas requeridas.
- Preservar la integridad de las especificaciones.
- Respetar los límites de archivos y líneas establecidos.
- No inventar aprobaciones, resultados ni evidencia.

Los valores de configuración deben consultarse en el repositorio activo.

## Restrictions

- No deshabilitar hooks para completar una tarea.
- No ampliar el alcance sin aprobación.
- No alterar pruebas selladas sin autorización.
- No confundir reglas Markdown con controles de seguridad.
- No afirmar que una aprobación tiene garantía criptográfica cuando no existe.
- No introducir dependencias de shell incompatibles con Windows.

## Version control

Respetar el proceso de versionado definido por el proyecto.

Separar los cambios funcionales de los cambios de versión
cuando así lo requieran sus controles.

## Definition of done

Una tarea está completa cuando satisface la especificación aprobada,
supera las verificaciones aplicables, conserva la evidencia correspondiente
y obtiene las aprobaciones requeridas.

## Scope

Estas reglas complementan PAIS.

MicroSDD conserva la autoridad sobre sus especificaciones,
máquina de estados, controles y mecanismos de verificación.