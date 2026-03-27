# Python Forensics Helpers

Esta subcarpeta reúne utilidades relacionadas con artefactos, evidencias e IOCs. Son scripts pensados para ayudar en triage rápido, cadena de custodia ligera y análisis preliminar.

## Scripts actuales
- `hash_manifest.py` → genera manifiestos de hashes.
- `ioc_extractor.py` → extrae IOCs básicos desde texto plano.
- `ioc_enricher.py` → añade clasificación y contexto simple a un CSV de IOCs.
- `pcap_summary.py` → resume un PCAP usando `tshark` y genera salida Markdown o JSON.
- `evidence_indexer.py` → crea un índice CSV de evidencias con hash y tamaño.

## Recomendaciones
- Si añades nuevos helpers aquí, intenta que generen salidas reutilizables (CSV/Markdown/JSON) y fáciles de enlazar desde `forensics/` o `exploitation/notes/`.
- Cuando un script dependa de herramientas externas (como `tshark`), déjalo claro en la documentación y en el ejemplo de uso.
