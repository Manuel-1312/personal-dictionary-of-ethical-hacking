# Toolkit - Python Tools 🐍

Documenta cada script, comando o helper que programas para esta biblioteca y anota qué dependencias necesita.

| Script | Descripción | Comando de ejemplo | Notas |
| --- | --- | --- | --- |
| `log_parser.py` | Extrae IPs, puertos y alertas de Zeek/Suricata para CSV/Markdown | `python python/log_parser.py --input defense/monitoring/logs/bro.log --output automation/reporting/results/zeek-summary.csv` | Usa pandas y argparse; genera un CSV con columnas `timestamp`, `src`, `dst`, `protocol`, `port`. |
| `inventory_builder.py` | Combina `nmap` y `masscan` para generar inventario unificado | `python python/inventory_builder.py --nmap reports/network/nmap-full.xml --masscan reports/network/masscan.gnmap --out reports/network/inventory.md` | Requiere `xmltodict`; el Markdown resultante alimenta `reports/network/index.md`. |

## Comandos utilizados recientemente
- `python python/log_parser.py --input defense/monitoring/logs/zeek.log --output automation/reporting/results/defense/zeek-summary.csv`.
- `python python/inventory_builder.py --nmap reports/network/nmap-full.xml --masscan reports/network/masscan.gnmap --out reports/network/inventory.md`.

## Técnicas de desarrollo
1. Mantengo `python/requirements.txt` con las dependencias (`pandas`, `xmltodict`) y uso un entorno virtual para aislar.
2. Cada script imprime pasos clave (`start`, `processing`, `done`) para poder rastrear errores desde la línea de comandos.

## Recomendaciones personales
- Documenta qué entornos (WSL, virtualenv) probaste y qué versiones de Python (3.11) usas.
- Añade tests simples (input mock + expected output) para que cualquiera pueda validar el script.
