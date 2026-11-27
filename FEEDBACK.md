# Feedback and Continuous Learning

Version: 0.1.0

## Objective

Identificar preferencias recurrentes y mejorar
progresivamente el estándar personal.

## Feedback classification

Clasifica cada observación como:

- Writing preference.
- Reasoning preference.
- Language preference.
- Project convention.
- Factual correction.
- Context-specific instruction.
- Explicit personal preference.

## Learning rules

- No generalices una corrección aislada.
- Diferencia preferencias permanentes y situacionales.
- Identifica patrones recurrentes.
- Conserva ejemplos representativos.
- No atribuyas al usuario preferencias inferidas
  como si hubieran sido explícitamente confirmadas.
- Detecta contradicciones con reglas existentes.

## Change proposals

Toda modificación propuesta debe incluir:

- Observación.
- Evidencia.
- Patrón identificado.
- Regla actual.
- Regla propuesta.
- Justificación.
- Documento afectado.
- Impacto esperado.

## Approval

Estados permitidos:

- PENDING
- ACCEPTED
- REJECTED
- SUPERSEDED

Una preferencia propuesta no se convierte en una
regla permanente sin aprobación explícita.

Los agentes no pueden modificar autónomamente
los documentos centrales.

## Versioning

Registra cambios aprobados mediante Git y CHANGELOG.md.

Cada modificación debe ser trazable y reversible.

## Fundamental principle

Aprender significa identificar y validar preferencias,
no acumular instrucciones indiscriminadamente.
