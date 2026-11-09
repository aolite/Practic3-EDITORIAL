"""
Ejercicio 3 — Lanzamiento de un producto (FinanzApp)
Lee el enunciado en Enunciado/Ejercicio-3.pdf
"""

import asyncio
from pathlib import Path

import anthropic

client = anthropic.AsyncAnthropic()
AGENT_MODEL = "claude-sonnet-4-6"

# ══════════════════════════════════════════════════════════
# CÓDIGO BASE
# ══════════════════════════════════════════════════════════

async def launch_agent(name: str, brief: str, output_path: Path, max_tokens: int = 1024) -> str:
    """Launch a specialist agent and persist its report to disk."""
    print(f"  → [{name}] starting analysis...")
    response = await client.messages.create(
        model=AGENT_MODEL,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": brief}],
    )
    result = response.content[0].text
    output_path.write_text(result, encoding="utf-8")
    print(f"  ✓ [{name}] done → {output_path.name}")
    return result


# ══════════════════════════════════════════════════════════
# TAREA 2: Briefs de 4 agentes especialistas
# ══════════════════════════════════════════════════════════

def copywriter_brief() -> str:
    # Objetivo claro — qué tiene que producir exactamente
    # Contexto relevante — datos del producto, audiencia, tono
    # Entregable específico — formato, extensión, estructura
    # Qué NO hacer — lo que más se olvida incluir
    return f"""
    PARA: Eres un experto copywriter de landing pages para campañas de marketing.
    OBJETIVO:
    Generar el texto de la página web de FinanzApp, una app de finanzas personales para millennials (25-35 años).
    CONTEXTO:
    - Datos del producto: (a) Precio: 4,99€/mes o 39,99€/año; (b) Propuesta de valor: conecta TODOS tus bancos en una vista y categoriza los gastos con IA.
    - Audiencia: personas de 25-35 años.
    - Tono: informal, cercano.
    ENTREGABLE:
    - Fichero Markdown con el texto de la landing page incluyendo: (a) Mensajes de atracción de clientes; (b) Texto de planes de precios y beneficios; (c) Pasos para darte de alta.
    QUÉ NO HACER:
    - Diseño de la página web ni de la landing page.
    - Campañas de emails.
    - Notas de prensa.
    - Contenido para redes sociales.
    """

def email_marketer_brief() -> str:
    return f"""
    PARA: Eres un experto en campañas de email marketing.
    OBJETIVO:
    Generar 3 emails para la campaña de lanzamiento de FinanzApp, dirigida a un público de 25-35 años.
    CONTEXTO:
    - Datos del producto: (a) Precio: 4,99€/mes o 39,99€/año; (b) Propuesta de valor: conecta TODOS tus bancos en una vista y categoriza los gastos con IA.
    - Lista de email: 8.000 suscriptores del blog de finanzas.
    - Ya conocen la marca pero NO conocen la app.
    - Oferta de lanzamiento: 50% de descuento el primer año (solo válida la primera semana).
    - Tono: informal y cercano.
    - Vocabulario: usa vocabulario de personas de 25-35 años.
    ENTREGABLE:
    - 3 emails para la campaña de marketing.
    - Emails de 30 palabras.
    - Emails en castellano.
    QUÉ NO HACER:
    - Emails genéricos y sin contexto.
    - Usar vocabulario de IA: "descubre", "revoluciona", "al siguiente nivel", "brutal", "espectacular", "transforma", "domina", emojis, abuso de los dos puntos (:)
    """

def social_media_brief() -> str:
    return f"""
    PARA: Eres un experto en campañas de social media para empresas del sector finanzas.
    OBJETIVO:
    Generar 5 posts para Twitter/X, Instagram y LinkedIn para captar clientes de entre 25 y 35 años.
    CONTEXTO:
    - Datos del producto: (a) Precio: 4,99€/mes o 39,99€/año; (b) Propuesta de valor: conecta TODOS tus bancos en una vista y categoriza los gastos con IA.
    - Tono: informal y cercano.
    - Vocabulario: usa vocabulario de personas de 25-35 años.
    - Centra los posts en las funcionalidades diferenciales de la app.
    ENTREGABLE:
    - 5 posts para Twitter/X, Instagram y LinkedIn, indicando en qué red va cada uno.
    - Posts de 30 palabras.
    - Posts en castellano.
    QUÉ NO HACER:
    - Posts genéricos y sin contexto.
    - Usar vocabulario de IA: "descubre", "revoluciona", "al siguiente nivel", "brutal", "espectacular", "transforma", "domina", emojis, abuso de los dos puntos (:)
    """

def pr_manager_brief() -> str:
    return f"""
    PARA: Eres un experto en redactar notas de prensa para medios especializados.
    OBJETIVO:
    Generar 1 nota de prensa sobre el lanzamiento de FinanzApp para medios especializados en finanzas y tecnología.
    CONTEXTO:
    - Datos del producto: (a) Precio: 4,99€/mes o 39,99€/año; (b) Propuesta de valor: conecta TODOS tus bancos en una vista y categoriza los gastos con IA.
    - Tracción: 2.000 usuarios beta con un NPS de 72.
    - Fundadora: María López, ex-directora de producto en N26.
    - Inversión: ronda seed de 1,2M€.
    - Público objetivo de la app: millennials de 25-35 años.
    - Audiencia de la nota: periodistas de medios especializados.
    - Tono: profesional e informativo.
    ENTREGABLE:
    - 1 nota de prensa con titular, entradilla, cuerpo y datos de contacto.
    - Entre 300 y 400 palabras.
    - Escrita en castellano.
    QUÉ NO HACER:
    - Artículo genérico sobre finanzas o sobre la herramienta FinanzApp.
    - Usar vocabulario de IA: "descubre", "revoluciona", "al siguiente nivel", "brutal", "espectacular", "transforma", "domina", emojis, abuso de los dos puntos (:)
    """

def consolidator_brief(
        landing_page_document: str,
        email_document: str,
        social_media_document: str,
        press_release_document: str
                       ) -> str:
    return f"""
    Eres un senior en marketing que CONSOLIDA la estrategia de marketing del producto FinanzApp.

    TEXTO LANDING PAGE:
    {landing_page_document}

    EMAILS DE MARKETING:
    {email_document}

    SOCIAL MEDIA POSTS:
    {social_media_document}

    NOTA DE PRENSA:
    {press_release_document}

    Tu trabajo:
    1. Revisa que los datos coinciden en todas las piezas (precio, oferta, propuesta de valor) y que el tono es coherente entre canales.
    2. Resuelve los conflictos entre las propuestas para que todo esté armonizado (prioridad: landing page > email > nota de prensa > social media).
    3. Establece la estrategia de publicación de cada uno de los elementos dentro de una línea temporal.

    FORMATO DE SALIDA

    Un documento con este formato EXACTO:

    1. Texto de la landing page
    2. Emails para publicar
    3. Posts para social media
    4. Nota de prensa
    5. Estrategia de publicación dentro de una línea temporal con fecha de inicio del 1 de diciembre de 2026.
    """

# ══════════════════════════════════════════════════════════
# TAREA 5: Orquestador principal
# ══════════════════════════════════════════════════════════

async def main():
    output_dir = Path("marketing_output")
    output_dir.mkdir(exist_ok=True)

    print("▸ FASE 1: Reparto de los briefs")
    briefs = {
        "copywriter": copywriter_brief(),
        "email": email_marketer_brief(),
        "social": social_media_brief(),
        "pr": pr_manager_brief(),
    }

    print("▸ FASE 2: Lanzar los especialistas en paralelo")
    landing, email, social_media, press_release = await asyncio.gather(
        launch_agent("Copywriter", briefs["copywriter"], output_dir / "01-LandingPage.md"),
        launch_agent("EmailMarketer", briefs["email"], output_dir / "02-EmailMarketer.md"),
        launch_agent("SocialMedia", briefs["social"], output_dir / "03-SocialMedia.md"),
        launch_agent("PRManager", briefs["pr"], output_dir / "04-PRManager.md"),
    )

    print("▸ FASE 3: Consolidación (secuencial)")
    await launch_agent(
        "DirectorMarketing",
        consolidator_brief(landing, email, social_media, press_release),
        output_dir / "05-PlanLanzamiento.md",
        max_tokens=8192,
    )

if __name__ == "__main__":
    asyncio.run(main())
