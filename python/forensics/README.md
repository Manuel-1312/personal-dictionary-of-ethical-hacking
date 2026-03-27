# Python Forensics Helpers

Esta subcarpeta reúne utilidades relacionadas con artefactos, evidencias e IOCs. Son scripts pensados para ayudar en triage rápido, cadena de custodia ligera y análisis preliminar.

## Scripts actuales
- `hash_manifest.py` → genera manifiestos de hashes.
- `ioc_extractor.py` → extrae IOCs básicos desde texto plano.

## Recomendaciones
- Si añades nuevos helpers aquí, intenta que generen salidas reutilizables (CSV/Markdown/JSON) y fáciles de enlazar desde `forensics/` o `exploitation/notes/`.
