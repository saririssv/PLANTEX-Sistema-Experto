# PLANTEX - Sistema Experto para Diagnóstico de Plantas

## Descripción

PLANTEX es un sistema experto desarrollado en Python que permite identificar posibles problemas en plantas mediante una base de conocimiento compuesta por hechos y reglas.

El usuario responde una serie de preguntas relacionadas con el estado de la planta. Las respuestas son almacenadas como hechos y posteriormente procesadas por un motor de inferencia para obtener un diagnóstico y una recomendación.

## Tecnologías utilizadas

- Python
- Tkinter
- Pillow

## Funcionamiento

El sistema funciona mediante las siguientes etapas:

1. El usuario responde las preguntas sobre el estado de la planta.
2. Las respuestas se almacenan como hechos.
3. Los hechos son comparados con las reglas de la base de conocimiento.
4. El motor de inferencia realiza tres fases:
   - Equiparación.
   - Resolución de conflictos.
   - Ejecución.
5. El sistema muestra el diagnóstico y una recomendación.

## Base de conocimiento

El sistema contiene diferentes hechos relacionados con características de las plantas, como:

- Hojas amarillas.
- Tierra húmeda.
- Tierra seca.
- Poca luz.
- Hojas caídas.
- Manchas en las hojas.
- Presencia de plagas.
- Crecimiento lento.
- Bordes secos.
- Tallo débil.

Además, cuenta con reglas que permiten relacionar estas condiciones con diferentes diagnósticos.

## Motor de inferencia

### Equiparación

Compara los hechos ingresados por el usuario con las condiciones establecidas en las reglas.

### Resolución de conflictos

Cuando existen varias reglas compatibles, selecciona la regla que será utilizada según la estrategia implementada en el sistema.

### Ejecución

Ejecuta la regla seleccionada y obtiene el diagnóstico correspondiente.

## Requisitos

- Python 3.x
- Pillow

## Ejecución

Para ejecutar el sistema, descargar el repositorio y ejecute
