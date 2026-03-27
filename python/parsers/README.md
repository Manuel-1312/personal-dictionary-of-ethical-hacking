# Python Parsers

Esta subcarpeta agrupa scripts que transforman salidas técnicas en formatos más manejables. La idea es convertir logs, XML o salidas de scanners en CSV/Markdown para integrarlos mejor con el resto del repo.

## Scripts actuales
- `log_parser.py` → parsea logs tipo Zeek/Suricata a CSV.
- `inventory_builder.py` → combina salidas de `nmap` y `masscan` para generar inventario unificado.

## Recomendaciones
- Mantén estos helpers pequeños y previsibles.
- Si un parser empieza a depender de muchos formatos distintos, conviene separarlo en módulos más específicos.
