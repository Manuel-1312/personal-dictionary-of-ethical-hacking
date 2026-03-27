# Toolkit - Threat Hunting 🕵️‍♂️

Registro de hunts que he ejecutado, con las herramientas, fuentes y conclusiones.

| Herramienta | Enlace | Foco | Nota concreta |
| --- | --- | --- | --- |
| Velociraptor | https://github.com/Velocidex/velociraptor | Caza en endpoints | Query `SELECT * FROM processes WHERE command_line LIKE '%powershell%'` y guardé los resultados en `defense/threat_hunting/results/hunt-powershell.json`.
| Sigma rules | https://github.com/SigmaHQ/sigma | Log analysis | Convertí la regla `windows.sysmon.process_creation` a Elastic y anoté 3 alertas válidas en `defense/threat_hunting/alerts/`.
| GRR Rapid Response | https://github.com/google/grr | Telemetría | Ejecuté artifact `autoruns` y adjunté los XML al caso `CASE-2026-03-27`.
| Elastic alerting | https://www.elastic.co/guide/en/elasticsearch/reference/current/xpack-alerting.html | Watcher | Un watcher monitorea `Zeek` y enciende un playbook en The Hive; guardo el JSON en `defense/incident_response/playbooks/zk-watch.json`.
| RITA | https://github.com/activecm/rita | DNS/Netflow | Usé `rita -i netflow.pcap -o reports/beacons.csv` para detectar beacons. Documenté la IP sospechosa y el dominio asociado.
| Wazuh | https://github.com/wazuh/wazuh | Correlación | Regla `sysmon-injected` generó un hunt con `eid=4688`; guardé la cadena en `defense/wazuh/rules/`.
