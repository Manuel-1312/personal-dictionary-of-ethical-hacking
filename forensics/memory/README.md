# Forense de Memoria

Aquí describo cada captura en caliente o en frío: qué herramienta usé (LiME, DumpIt, FTK Imager), qué sistema estaba corriendo y cuánto tardé.

Guardo:
- Comando exacto (`./lime -f /mnt/mem.raw` o `DumpIt.exe mem.dmp`).
- Metadatos (`hostname`, `kernel`, `fecha`) e identificadores (PID, SNAPSHOT).
- Hash (`sha256sum mem.dmp`).

Anexo los análisis (`volatility3 -f mem.dmp malfind`) en `forensics/memory/analysis/` y describo qué artefactos rescato (procesos sospechosos, conexiones TCP). Cada captura lleva un `README` corto que explica qué incidentes motivaron la recolección.

## Comandos utilizados
- `./lime -f /mnt/mem-20260327.raw -d /tmp`.
- `DumpIt.exe mem-20260327.dmp`.
- `volatility3 -f forensics/memory/mem-20260327.raw windows.pslist`.

## Técnicas aplicadas
- Captura en caliente (LiME) para analizar procesos en ejecución.
- Uso de Volatility/Belkasoft para rastrear conexiones y amenazas persistentes.

## Recomendaciones personales
- Guarda los hash en `reports/forensics/memory-hashes.txt`.
- Documenta cuál fue el incidente o alerta que motivó la captura en `forensics/memory/cases/`.