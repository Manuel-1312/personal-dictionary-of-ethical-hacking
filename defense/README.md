# Defensa y Monitorización

Esta carpeta es mi cuaderno de operaciones defensivas: sensores desplegados, dashboards que reviso y playbooks que pruebo cuando el laboratorio genera alertas. En mi última ronda levanté un stack con Security Onion (Zeek + Suricata) sobre un host dedicado y uso Wazuh para correlacionar eventos de los endpoints.

Dentro hay dos líneas claras:

- `monitoring/`: sensores, dashboards y hunting.
- `incident_response/`: playbooks, contención y seguimiento tras una detección.

Cada README en subcarpetas detalla qué consultas, reglas o scripts activé. Guarda los CSV/JSON que generas y menciona qué alertas eran falsas positivas para que el equipo no las repita. Si corres un hunt en Velociraptor o un playbook en The Hive, enlázalo aquí para que cualquiera recree la investigación.

## Comandos utilizados
- `so-import-pcap -f security-onion.pcap` para inyectar tráfico sintético y validar reglas.
- `wazuh-control -a` para sincronizar los agentes luego de instalar nuevos logs.
- `velociraptor config apply --config defense/hunting/vql/global.yaml` para ejecutar hunts programados.

## Técnicas aplicadas
- Detección múltiple (Zeek + Suricata + Wazuh) para capas coincidentes de alerta; anoto cuál disparó primero.
- Hunting proactivo con Velociraptor revisando `powershell` en endpoints; guardo los resultados en `defense/threat_hunting/results/`.
- Playbooks de incident response generados en The Hive y ejecutados via Cortex para automatizar recolección.

## Recomendaciones personales
- Mantén un `dashboard` que combine alertas de varios sensores para comparar tiempos de detección.
- Documenta alertas falsas en `defense/monitoring/alerts/falsos.csv` para que el equipo no vuelva a investigar lo mismo.
- Guarda los playbooks de contención en `defense/incident_response/playbooks/` y anota en ellos qué cambios de red deben revertirse tras el caso.