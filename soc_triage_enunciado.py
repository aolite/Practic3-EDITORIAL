"""
Ejercicio 2 — Código base
Lee el enunciado en soc_triage_enunciado.md
"""

import asyncio
from pathlib import Path

import anthropic

client = anthropic.AsyncAnthropic()
AGENT_MODEL = "claude-sonnet-4-6"


# ══════════════════════════════════════════════════════════
# DATO: LA ALERTA
# ══════════════════════════════════════════════════════════

ALERT_TEXT = """
ALERT ID: ALERT-2026-05-27-0342
Timestamp: 2026-05-27T03:42:17Z
Source: SIEM-Elastic
Rule triggered: Anomalous outbound data transfer > 500MB
Severity: HIGH

Source host: prod-db-replica-03.internal
Source IP: 10.0.4.17
Destination IP: 185.234.72.19
Destination port: 443
Bytes out: 2,147,483,648 (2 GB)
Protocol: HTTPS
User: svc-backup-agent
Time window: 03:00 - 03:42 UTC

DNS queries observed:
  - storage-cdn-eu.cloudprovider.com
  - api.transfer-service.io
  - exfil-drop.darksite.onion.ws

Processes running on source host:
  - pg_dump (PID 8821, started 03:01:02)
  - curl (PID 8834, started 03:01:15)
  - gpg (PID 8840, started 03:01:20)
  - split (PID 8845, started 03:01:25)

File changes on source host:
  - /tmp/.cache/dump_20260527.sql.gpg.001
  - /tmp/.cache/dump_20260527.sql.gpg.002
  - /tmp/.cache/dump_20260527.sql.gpg.003

Authentication events (last hour):
  - [02:55:00] login_success user=svc-backup-agent method=ssh_key
  - [02:56:12] sudo_escalation user=svc-backup-agent cmd=pg_dump
  - [02:58:30] login_failed user=admin source=185.234.72.19
  - [02:58:45] login_failed user=admin source=185.234.72.19
  - [02:59:01] login_failed user=root source=185.234.72.19
"""


# ══════════════════════════════════════════════════════════
# CÓDIGO BASE
# ══════════════════════════════════════════════════════════

async def launch_agent(name: str, brief: str, output_path: Path) -> str:
    """Launch a specialist agent and persist its report to disk."""
    print(f"  → [{name}] starting analysis...")
    response = await client.messages.create(
        model=AGENT_MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": brief}],
    )
    result = response.content[0].text
    output_path.write_text(result, encoding="utf-8")
    print(f"  ✓ [{name}] done → {output_path.name}")
    return result


# ══════════════════════════════════════════════════════════
# TAREA 2: Briefs de 2 agentes especialistas
# ══════════════════════════════════════════════════════════

def build_my_agent_1_brief(alert: str) -> str:
    # TODO: Brief del primer agente de tu dimensión
    return f"""
    ...
    """


def build_my_agent_2_brief(alert: str) -> str:
    # TODO: Brief del segundo agente de tu dimensión
    return f"""
    ...
    """


# ══════════════════════════════════════════════════════════
# TAREA 3: Brief del sub-orquestador
# ══════════════════════════════════════════════════════════

def build_my_sub_orchestrator_consolidation(
    report_1: str, report_2: str
) -> str:
    # NOTA: En la solución de referencia, el brief de consolidación se construye
    # como un f-string directamente dentro de cada función de sub-orquestador
    # (network_sub, endpoint_sub, identity_sub), no como función separada.
    # Ambas aproximaciones son válidas:
    #   - Este stub (modular): más fácil de probar de forma aislada.
    #   - La de la solución (incrustada): menos indirecciones, más compacta.
    # TODO: Brief del sub-orquestador
    return f"""
    ...
    """


# ══════════════════════════════════════════════════════════
# TAREA 4: Sub-orquestador completo
# ══════════════════════════════════════════════════════════

async def my_sub_orchestrator(alert: str, output_dir: Path) -> str:
    # output_dir es un objeto pathlib.Path que ya existe.
    # Los ficheros de salida se escriben pasando la ruta a launch_agent():
    #   output_dir / "nombre.md"
    #
    # Nombres de fichero que debe crear según la dimensión elegida:
    #   - Dimensión Red:       output_dir / "net_dns.md"
    #                          output_dir / "net_destination.md"
    #   - Dimensión Endpoint:  output_dir / "ep_processes.md"
    #                          output_dir / "ep_files.md"
    #   - Dimensión Identidad: output_dir / "id_auth.md"
    #                          output_dir / "id_escalation.md"
    #
    # TODO: 1. Lanzar 2 agentes en paralelo
    #       2. Consolidar con el sub-orquestador
    #       3. Devolver resultado
    return ""  # TODO: implementar


# ══════════════════════════════════════════════════════════
# TAREA 5: Orquestador principal
# ══════════════════════════════════════════════════════════

async def main():
    output_dir = Path("soc_triage_output")
    output_dir.mkdir(exist_ok=True)

    # TODO: 1. Lanzar 3 sub-orquestadores en paralelo
    #       2. Generar veredicto final con MITRE ATT&CK

    pass


if __name__ == "__main__":
    asyncio.run(main())
