# Toolkit - Reconocimiento 🧭

Lista herramientas de recon pasivo/activo con notas de las sesiones donde las usaste. Incluye qué archivo generaste y en qué paso de la hipótesis contribuyeron.

| Herramienta | Enlace | Paso | Nota real |
| --- | --- | --- | --- |
| Amass | https://github.com/OWASP/Amass | Footprint DNS | Corrí `amass enum -d example.lab -config recon/amass.conf -o outputs/recon/amass.json` y descubrí `vpn.example.lab`. |
| Recon-ng | https://github.com/lanmaster53/recon-ng | Framework | Module `recon/domains-contacts` → output `outputs/recon/recon-ng-contacts.csv`. |
| SpiderFoot | https://github.com/smicallef/spiderfoot | Correlación | `sf.py -s passive --config sf.json` y exporté `outputs/recon/spiderfoot.json`. |
| Shodan CLI | https://help.shodan.io/the-shodan-command-line-client | Búsqueda de servicios | `shodan host 10.0.1.5` → guardo `outputs/recon/shodan-host10.0.1.5.json`. |
| Sublist3r | https://github.com/aboul3la/Sublist3r | Enumeración | `sublist3r -d example.lab -o outputs/recon/sublist3r.txt` y comparo con Amass. |
| DNSDumpster / SecurityTrails | https://dnsdumpster.com/ | Mapas de infraestructura | Descargué mapa PDF y lo guardé en `outputs/recon/dnsmap.pdf`. |
| PassiveTotal (RiskIQ) | https://www.riskiq.com/ | Historial | Registré IPs antiguas en `reports/recon/passive.csv`. |

## Comandos utilizados
- `amass enum -d example.lab -config recon/amass.conf -o outputs/recon/amass.json`.
- `shodan host 10.0.1.5 --fields ip_str,port,hostnames`.
- `sublist3r -d example.lab -o outputs/recon/sublist3r.txt`.

## Técnicas aplicadas
- Combinación de fuentes pasivas y activas para verificar hosts.
- Comparación de datos con CSV previos (`recon/history.csv`).

## Recomendaciones personales
- Guarda los outputs en carpetas fechadas y enlázalos desde `lab-notes.md`.
- Documenta la fuente final (Shodan, Amass, etc.) para mantener la trazabilidad.
- Respeta los límites indicados por cada servicio y no automates queries ilegales.