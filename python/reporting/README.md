# Python Reporting Helpers

Aquí van las utilidades orientadas a transformar resultados técnicos en salidas legibles, compartibles y fáciles de reutilizar en el resto del repositorio.

## Scripts actuales
- `nmap_xml_to_markdown.py` → convierte XML de Nmap en un informe Markdown claro.
- `markdown_case_bundler.py` → une varias notas Markdown en un único informe final.

## Recomendaciones
- Prioriza salidas simples (`Markdown`, `CSV`, `JSON`) sobre formatos difíciles de mantener.
- Si el script sirve para cerrar sesiones, enlázalo desde `automation/reporting/` y `exploitation/notes/`.
