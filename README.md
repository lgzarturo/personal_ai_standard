# Personal AI Standard

Personal AI Standard (**PAIS**) es un estándar personal de trabajo
asistido por inteligencia artificial.

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

Respeta las convenciones específicas de cada proyecto.

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

Usar una copia central de PAIS por equipo.

```
~/.pais/
├── CORE.md
├── WRITING.md
├── LANGUAGE.md
├── BOOTSTRAP.md
├── FEEDBACK.md
└── templates/
    └── PROJECT_RULES.md
```
