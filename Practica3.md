# Practica 3- EDITORIAL

## Tarea 1. Elige el patrón de orquestación

**1. ¿El copywriter de la landing page necesita esperar a que el email marketer termine para empezar a trabajar?**

No, el copywriter de la landing page no necesita esperar a ninguno de los otros actores para realizar su trabajo. Ambos trabajan en paralelo sobre el mismo producto, FinanzApp, y parten de los mismos datos de producto, no del resultado del otro.

**2. ¿El PR manager necesita leer los posts de redes sociales para escribir la nota de prensa?**

Tampoco. Son trabajos totalmente independientes sobre el marketing de un mismo producto: la nota de prensa no usa nada de los posts, porque todo lo que necesita está en los datos del producto. Además, redes y prensa tienen focos diferentes en cuanto a audiencia y estilo de escritura.

**3. Con tus respuestas (1) y (2): ¿Qué patrón de orquestación usarías? ¿Paralelo, secuencial o Jerárquico?**

Basándome en las preguntas anteriores, usaría un patrón paralelo: las 4 piezas (landing page, campaña de email, contenido para redes y nota de prensa) son independientes y ninguna necesita el resultado de otra. El Director de Marketing actúa como orquestador: reparte los briefs, los 4 especialistas trabajan a la vez y, cuando terminan, consolida todo para que la campaña sea coherente de forma integral. 

**4. Dibuja el diagrama del sistema (papel o aquí abajo)**

```
                              ┌────────────────────────────┐
                              │   DIRECTOR DE MARKETING    │  Fase 1: REPARTO
                              │     Reparte los briefs     │
                              └──────────────┬─────────────┘
                                             │
           ┌──────────────────────┬──────────┴───────────┬──────────────────────┐
           ▼                      ▼                      ▼                      ▼
┌────────────────────┐ ┌────────────────────┐ ┌────────────────────┐ ┌────────────────────┐
│     COPYWRITER     │ │   EMAIL MARKETER   │ │    SOCIAL MEDIA    │ │     PR MANAGER     │  Fase 2:
│   → Landing page   │ │     → 3 emails     │ │  → Posts de redes  │ │  → Nota de prensa  │  PARALELO
└──────────┬─────────┘ └──────────┬─────────┘ └──────────┬─────────┘ └──────────┬─────────┘
           └──────────────────────┴──────────┬───────────┴──────────────────────┘
                                             ▼
                              ┌────────────────────────────┐
                              │   DIRECTOR DE MARKETING    │  Fase 3: CONSOLIDACIÓN
                              │     Consolida y revisa     │
                              │   → Plan de lanzamiento    │
                              └────────────────────────────┘
```


