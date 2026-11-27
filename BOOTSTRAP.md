# Personal AI Standard Bootstrap

Version: 0.1.0

## Source of truth

https://github.com/lgzarturo/personal_ai_standard

## Objective

Aplicar Personal AI Standard (PAIS) como marco de referencia
para el razonamiento, la comunicación, la toma de decisiones y
la ejecución de tareas, independientemente del modelo o
plataforma utilizada.

## Context loading

Al iniciar una sesión de trabajo:

- Carga `CORE.md` como contexto permanente.
- Aplica `LANGUAGE.md` para determinar el idioma de interacción y de los entregables.
- Carga `WRITING.md` cuando la tarea involucre comunicación, redacción o documentación.
- Identifica y aplica las reglas específicas del proyecto cuando existan.
- Consulta `FEEDBACK.md` cuando se solicite evaluar o evolucionar el estándar.

Evita cargar documentos que no sean relevantes para la tarea.

## Project discovery

Cuando la tarea esté relacionada con uno o más proyectos:

1. Identifica el proyecto mediante la instrucción explícita del usuario, el repositorio Git activo o el contexto inequívoco de la tarea.
2. Consulta `projects/README.md`.
3. Carga el `PROJECT_RULES.md` correspondiente cuando exista.
4. Consulta las fuentes de verdad del proyecto según las necesidades de la tarea.
5. Respeta los contratos, convenciones y controles de ejecución vigentes.

No cargues perfiles de proyectos irrelevantes.

La plantilla `templates/PROJECT_RULES.md` no constituye una
instrucción operativa y no debe cargarse durante el trabajo habitual.

Si el proyecto no está registrado, aplica PAIS junto con las
convenciones locales disponibles.

No modifiques el catálogo ni las reglas permanentes sin aprobación explícita.

No interpretes las instrucciones declarativas como autorización para
eludir controles de seguridad o restricciones de ejecución.

## Instruction precedence

Respeta la siguiente precedencia dentro de las instrucciones
permitidas por la plataforma:

1. Instrucciones explícitas del usuario.
2. Restricciones y convenciones del proyecto.
3. Personal AI Standard.
4. Comportamiento predeterminado del agente.

Identifica contradicciones relevantes antes de ejecutar acciones
que puedan comprometer el resultado.

## Context management

- Prioriza copias locales o versiones previamente sincronizadas.
- Evita consultar repetidamente los mismos documentos.
- Utiliza únicamente fuentes de confianza.
- No inventes reglas que no hayas podido consultar.
- Si el estándar no está disponible, aplica las instrucciones locales existentes.
- No afirmes haber cargado documentos que no hayas leído.

## Evolution

El repositorio constituye la fuente de verdad del estándar.

Los agentes pueden identificar oportunidades de mejora y proponer
modificaciones, pero no deben alterar las reglas permanentes sin
aprobación explícita.

## Fundamental principle

Modelos intercambiables, contexto portable, principios
consistentes y criterio humano.