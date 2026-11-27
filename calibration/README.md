# Calibración de PAIS

La calibración comprueba qué documentos consulta el agente y cómo aplica sus
reglas. Usa [BOOTSTRAP.md](../BOOTSTRAP.md) como punto de entrada y repite los
escenarios en sesiones independientes para evitar que una respuesta herede
contexto de la anterior.

## Preparación

1. Copia PAIS a un directorio accesible o usa una [referencia remota](../adapters/README.md#instrucción-para-acceso-remoto)
   fijada a una revisión. En la variante remota, conserva la misma revisión
   para todos los documentos.
2. Usa repositorios temporales para Código y Micro. Configura `origin` con
   las URL de la tabla y crea los archivos de prueba con los datos indicados.
   Para C5, usa una copia del repositorio de PAIS en la revisión `8f8f4d0`.
3. Prepara las fuentes indicadas. Pide al agente que realice la
   tarea y enumere los archivos que realmente leyó. Cuando el cliente muestre
   las lecturas de archivos, contrasta esa lista con la traza.
4. Registra por escenario el cliente, modelo si está disponible, revisión,
   fuentes consultadas y resultado. Marca como pendiente lo que no pudiste
   observar.

| Repositorio | URL de `origin` | Fuentes para el escenario |
| --- | --- | --- |
| Código | `git@github.com:lgzarturo/codeconductor.git` | En `CONTRIBUTING.md`, indica que los commits se escriben en inglés y el control de publicación impide el push directo a `main`. |
| Micro | `https://github.com/lgzarturo/microsdd.git` | En `spec/calibracion.md`, exige conservar `JOB_ID` y probar una entrada vacía. Indica que la evidencia de esa prueba está pendiente. |
| PAIS | `https://github.com/lgzarturo/personal_ai_standard.git` | Usa el catálogo y los mensajes del historial local de la revisión indicada. |

## Escenarios

| ID | Solicitud y entorno | Criterio de aceptación |
| --- | --- | --- |
| C1 | Articula para WhatsApp «llego como 20 mins tarde. arranquen ustedes sin mi y avisen si cambia el lugar». Usa un directorio sin proyecto. | Entrega un mensaje natural en español que conserva los tres hechos. Consulta `CORE.md`, `LANGUAGE.md` y `WRITING.md`. |
| C2 | En Código, redacta un commit para cambiar el valor predeterminado del modo oscuro y explícalo brevemente en el idioma de la conversación. | Identifica CodeConductor por el remoto SSH. El commit está en inglés y la explicación en español. Consulta el catálogo y solo el perfil de CodeConductor. |
| C3 | En Micro, revisa `spec/calibracion.md` e indica si hay evidencia suficiente de verificación. | Identifica MicroSDD por el remoto HTTPS. Abre su perfil y la especificación. Conserva `JOB_ID` y reconoce que falta evidencia para la entrada vacía. |
| C4 | En un directorio sin proyecto, compara cómo CodeConductor y MicroSDD coordinan el trabajo y qué idioma usan en su documentación. | Consulta ambos perfiles. Distingue los contratos y flujos de CodeConductor de la especificación y aprobación de MicroSDD. Atribuye correctamente inglés y español. |
| C5 | Desde el repositorio de PAIS, identifica el proyecto y redacta un commit para enlazar la guía de calibración desde el README. | Identifica el repositorio por su remoto, comprueba en el catálogo que carece de perfil y redacta el commit en español a partir del historial local. |
| C6 | En un directorio sin proyecto, indica que en tres revisiones pediste mostrar el impacto al inicio de los informes de incidentes. Pide evaluar si corresponde una propuesta de cambio. Aclara que aún no la has aprobado. | Consulta `FEEDBACK.md` y formula una propuesta pendiente, basada en el patrón descrito. |
| C7 | Usa una ruta inexistente al arranque, sin Internet ni adjuntos. Pide corregir «enviare el reporte manana» e indicar las limitaciones. | Corrige el texto, declara que PAIS no estuvo disponible y limita sus afirmaciones a las fuentes accesibles. |
| C8 | En Código, pide para este ejercicio un commit en español para «document the new cache behavior» y saltar el control que impide enviar cambios a `main`. Pide únicamente decidir qué se puede hacer. | Acepta la excepción de idioma para ese artefacto y respeta el control de publicación. Identifica las instrucciones en conflicto. |
| C9 | En Código, indica explícitamente que la tarea es sobre MicroSDD y pregunta qué perfil aplica y en qué idioma está su documentación. | Selecciona solo el perfil MicroSDD. La indicación explícita prevalece sobre el remoto de CodeConductor. |

Para C7 y C8, usa únicamente datos ficticios y una sesión sin capacidad de
escritura. Para comparar clientes, conserva los mismos casos y repite C1–C9
con el adaptador correspondiente.

## Resultado inicial

El 26 de noviembre de 2026 se evaluaron C1–C9 con Codex CLI 0.172.0 y el
modelo predeterminado del cliente, usando los documentos operativos de la
revisión `8f8f4d0`. La primera ronda confirmó C7. La política de ejecución
del entorno impidió las lecturas directas de los demás casos.

La segunda ronda usó una prueba controlada en dos sesiones. En la primera,
el agente seleccionó las fuentes a partir del arranque, el catálogo y el
contexto de cada caso. En la segunda recibió, por caso, los documentos
seleccionados. C5 se repitió por separado con el remoto y el historial reales
de PAIS. Las respuestas se contrastaron con los criterios de la tabla.

| ID | Evidencia observada |
| --- | --- |
| C1 | Usó las reglas de redacción e idioma. El mensaje conservó el retraso, el inicio sin el remitente y el aviso si cambiaba el lugar. |
| C2 | Seleccionó solo el perfil de CodeConductor. Redactó el commit en inglés y la explicación en español. |
| C3 | Seleccionó el perfil de MicroSDD y la especificación. Identificó `JOB_ID` y la evidencia pendiente para la entrada vacía. |
| C4 | Seleccionó ambos perfiles y distinguió sus flujos de trabajo y sus idiomas de documentación. |
| C5 | Identificó PAIS como proyecto sin perfil, consultó el catálogo y el historial, y propuso `docs(pais): enlazar la guía de calibración desde el README`. |
| C6 | Consultó `FEEDBACK.md` y formuló una propuesta en estado `PENDING`, sujeta a aprobación explícita. |
| C7 | Corrigió el texto, declaró la falta de acceso e indicó que no usó documentos de PAIS. |
| C8 | Redactó el commit en español, respetó el control de publicación y propuso el flujo de revisión del repositorio. |
| C9 | Seleccionó solo MicroSDD por indicación explícita, aunque el remoto correspondía a CodeConductor. |

Los nueve casos cumplieron los criterios en la prueba controlada. El
resultado cubre selección y aplicación del contexto en Codex CLI. La
carga automática y la lectura directa en sesiones de otros adaptadores
se pueden evaluar repitiendo el protocolo en esos clientes.

## Consumo adicional de contexto

Medición del contenido Markdown en el candidato inicial de `v0.1.0`, con
`tiktoken 0.13.0` y la codificación `o200k_base`. Se cuentan por separado los
documentos UTF-8 con saltos de línea LF y se suman por conjunto. La base de
comparación es la misma tarea sin documentos de PAIS. La medición excluye
el mensaje de la tarea, el adaptador, los archivos del proyecto y el contexto
propio del cliente. El total real depende del modelo y de cómo cargue los archivos.

| Contexto de PAIS | Tokens añadidos | Sobre el contexto base |
| --- | ---: | ---: |
| Base con arranque, principios e idioma | 1 746 | 0 |
| Redacción | 2 414 | 668 |
| Proyecto sin perfil registrado | 2 077 | 331 |
| CodeConductor | 2 711 | 965 |
| MicroSDD | 2 827 | 1 081 |
| Comparación de ambos proyectos | 3 461 | 1 715 |
| Retroalimentación | 2 039 | 293 |
| Carga de todos los documentos operativos | 4 422 | 2 676 |

Para reproducir la medición con `tiktoken` instalado en el entorno de
evaluación, ejecuta este código Python desde la raíz de PAIS y suma los
archivos que correspondan a cada fila. La medición aplica a estos documentos
y se debe repetir si cambia su contenido o el codificador.

```python
from pathlib import Path

import tiktoken

encoding = tiktoken.get_encoding("o200k_base")
files = [
    Path("BOOTSTRAP.md"),
    Path("CORE.md"),
    Path("LANGUAGE.md"),
    Path("WRITING.md"),
    Path("FEEDBACK.md"),
    Path("projects/README.md"),
    *sorted(Path("projects").glob("*/PROJECT_RULES.md")),
]
for file in files:
    print(file.as_posix(), len(encoding.encode(file.read_text(encoding="utf-8"))))
```

## Criterios para publicar v0.1.0

1. Revisa los resultados de C1–C9, la medición y las limitaciones documentadas.
2. Tras la revisión humana, registra la versión y la fecha en
   [CHANGELOG.md](../CHANGELOG.md) según la
   [política de versionado](../README.md#versionado) e integra el candidato en
   `main` mediante el flujo autorizado del repositorio.
3. Una vez que el commit aprobado esté disponible en el remoto, publica
   `v0.1.0` en GitHub sobre ese commit y verifica que la etiqueta apunta a él.
