# Práctica 3 — EDITORIAL: lanzamiento multi-agente de FinanzApp

Sistema multi-agente con la API de Claude que prepara la campaña de lanzamiento de **FinanzApp**, una app de finanzas personales para millennials (25-35 años). Un Director de Marketing reparte el trabajo entre cuatro agentes especialistas, que trabajan en paralelo, y después consolida sus resultados en un plan de lanzamiento coherente.

El enunciado completo está en [`Enunciado/Ejercicio-3.pdf`](Enunciado/Ejercicio-3.pdf) y las respuestas razonadas en [`Practica3.md`](Practica3.md).

## Arquitectura

Se usa un **patrón de orquestación paralelo**: las cuatro piezas son independientes entre sí y solo comparten los datos del producto.

```
              DIRECTOR DE MARKETING  (Fase 1: reparto de briefs)
                         │
     ┌───────────────┬───┴───────────┬───────────────┐
     ▼               ▼               ▼               ▼
 Copywriter    Email Marketer   Social Media     PR Manager    (Fase 2: en paralelo)
     └───────────────┴───┬───────────┴───────────────┘
                         ▼
              DIRECTOR DE MARKETING  (Fase 3: consolidación)
```

| Agente | Entregable | Fichero de salida |
|---|---|---|
| Copywriter | Texto de la landing page | `01-LandingPage.md` |
| Email Marketer | 3 emails de lanzamiento | `02-EmailMarketer.md` |
| Social Media | 5 posts (X, Instagram, LinkedIn) | `03-SocialMedia.md` |
| PR Manager | Nota de prensa | `04-PRManager.md` |
| Director de Marketing | Plan de lanzamiento consolidado con calendario (desde el 1/12/2026) | `05-PlanLanzamiento.md` |

Cada brief sigue la misma estructura: **objetivo**, **contexto**, **entregable** y **qué no hacer**.

## Estructura del repositorio

```
.
├── Enunciado/Ejercicio-3.pdf   # Enunciado de la práctica
├── Practica3.md                # Respuestas a las tareas
├── marketing_multi-agent.py    # Orquestador y briefs de los agentes
└── marketing_output/           # Resultados generados (ignorado por git)
```

## Requisitos

- Python 3.10+
- Una API key de Anthropic

## Uso

```bash
python -m venv venv
source venv/bin/activate
pip install anthropic

export ANTHROPIC_API_KEY="tu-api-key"
python marketing_multi-agent.py
```

Los resultados se guardan en `marketing_output/`.
