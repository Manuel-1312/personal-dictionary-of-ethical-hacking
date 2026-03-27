# Toolkit - Forense Digital 🔍

Registro práctico de herramientas de adquisición, análisis y documentación forense. Cada entrada muestra cómo la lanzo, qué comando uso, dónde guardo los artefactos clave y cuándo conviene usarla o descartarla para no contaminar la evidencia.

## 1. Adquisición y análisis de disco

### FTK Imager
- **Enlace:** https://accessdata.com/product-download/ftk-imager-version-4.3.0
- **Caso de uso:** imagen forense inicial de discos y pendrives en entorno controlado.
- **Comando de ejemplo:** `ftkimager.exe --evidencefile=case01.E01 --log=artifacts/ftk/case01.log --hash=SHA256 --format=E01 --source=\\.\PhysicalDrive2`
- **Notas útiles:** siempre ejecutado con la unidad en modo solo lectura y registro de hash original en `forensics/chain-of-custody.txt`. Copio los directorios `e01` y el log al servidor de evidencias y cierro el caso con sellos digitales.
- **Recomendaciones:** documenta el número de serie del disco y el software/hardware usado. Si el objetivo permite clonación bit a bit, toma primero una imagen y luego trabaja sobre esa copia.
- **Cuándo usarlo:** cuando necesitas pruebas admisibles en tribunales o quieres preservar el bitstream exacto.
- **Cuándo no:** si solo estás analizando una VM y no necesitas un E01 (en ese caso, usa `dd` virtual o monta el VMDK directamente).

### Autopsy + Sleuth Kit
- **Enlace:** https://www.sleuthkit.org/autopsy/
- **Caso de uso:** análisis guiado de FS, extracción de timelines y visualización de artefactos.
- **Comando de ejemplo:** `autopsy --in-place --case gallery --data /mnt/images/case01.E01`
- **Notas útiles:** exporto reportes `autopsy/reports/<caso>/report.html` y guardo timelines `autopsy/timelines/<caso>.csv`. Uso Sleuth Kit (`fls`, `icat`, `mactime`) para reconstruir rutas que no aparecen en la GUI.
- **Recomendaciones:** combina el árbol de archivos con `tsk_recover` para recuperar versiones borradas y añade los hashes a `autopsy/hashes/<herramienta>.txt`.
- **Cuándo usarlo:** cuando necesitas buscar artefactos discretos (logs, correos) y presentar evidencias al cliente.
- **Cuándo no:** no lo uses en sistemas sin snapshot, porque Autopsy puede alterar timestamps (prefiere trabajar con una imagen montada).

### dd / dc3dd
- **Enlace:** https://www.gnu.org/software/coreutils/dd/ / https://github.com/ClaireWarner/dc3dd
- **Caso de uso:** capturas manuales rápidas de discos, especialmente en laboratorios de red donde no quieres herramientas propietarias.
- **Comando de ejemplo:** `dc3dd if=/dev/sdb of=forensics/images/case02.dd hash=sha256 log=forensics/logs/dc3dd-case02.log`
- **Notas útiles:** include `count` para limitar sectores y `conv=noerror,sync` para seguir leyendo aun con errores. Comprueba el hash y guárdalo en el registro de cadena de custodia.
- **Recomendaciones:** usa `dc3dd` cuando quieras más control sobre logs; `dd` es suficiente si trabajas en un entorno Linux limpio.
- **Cuándo usarlo:** para replicar exactos bits cuando no hay mejor alternativa.
- **Cuándo no:** no lo uses sin verificar que no estás capturando un disco en uso (prefiere `FTK` o `Guymager` con bloqueo).

## 2. Memoria y artefactos volátiles

### Volatility 3
- **Enlace:** https://github.com/volatilityfoundation/volatility3
- **Caso de uso:** extracción de procesos en memoria, conexiones de red, handles y módulos sospechosos.
- **Comando de ejemplo:** `vol.py -f memory/case01.mem windows.pslist.PsList --output-file=volatility/pslist-case01.json`
- **Notas útiles:** guardo plugins clave (`malfind`, `pslist`, `netscan`) en `forensics/memory/plugins.txt` y comparo con la salida de `rekall` para validar hallazgos. Siempre registro los tiempos `VolatilityTimestamp` y los exporto a `reports/forensics/memory-timeline.csv`.
- **Recomendaciones:** mantén una copia de los perfiles y usa `volatility3 -p profiles/Windows10x64.json` para evitar errores; automatiza con `python scripts/volatility-runner.py`.
- **Cuándo usarlo:** en respuesta inmediata a incidentes que requieren evidencia volátil.
- **Cuándo no:** no lo corras desde un entorno comprometido (trabaja desde una imagen limpia o una máquina air-gapped).

### Rekall
- **Enlace:** https://github.com/google/rekall
- **Caso de uso:** cross-check de volcado de memoria (especialmente `psscan`, `dlllist`).
- **Comando de ejemplo:** `rekall -f memory/case01.mem -r pslist > forensics/memory/rekall-pslist.txt`
- **Notas útiles:** su salida es más fácilmente legible cuando se usa `-o json`, así que la convierto con `jq` y la comparo con `Volatility`.
- **Recomendaciones:** guarda la versión de Rekall para cada caso en `forensics/memory/rekall-version.txt`.
- **Cuándo usarlo:** como verificación adicional después de Volatility.
- **Cuándo no:** si tu imagen solo dispone de Linux y prefieres herramientas como LiME o `avml`.

### Redline
- **Enlace:** https://www.fireeye.com/services/freeware/redline.html
- **Caso de uso:** consolidación rápida de hash indicators, conexiones de red y módulos de memoria en Windows.
- **Comando de ejemplo:** guiado (exporta `RedlineSession.xml` y los AR para `malwareworkflow`).
- **Notas útiles:** uso Redline para detectar malware sin tener que memorizar plugins; exporto la sesión a `forensics/redirect/redline-<fecha>.zip`.
- **Recomendaciones:** puedes usar la API para generar IOC (hash+dominio) y exportarlos a `TheHive`.
- **Cuándo usarlo:** en equipos Windows de clientes donde quieras una referencia rápida sin scripting.
- **Cuándo no:** si buscas análisis profundo (usa Volatility/Rekall en su lugar).

## 3. Línea temporal y correlación

### Plaso / log2timeline
- **Enlace:** https://github.com/log2timeline/plaso
- **Caso de uso:** generar la línea temporal maestro de actividades en disco y memoria.
- **Comando de ejemplo:** `log2timeline.py --parsers "winlog,chrome" --status_view none plaso/win-case01.plaso forensics/images/case01.E01`
- **Notas útiles:** luego uso `psteal.py`/`psort` para extraer fragmentos (milestone, user, webhistory). Exporto la línea a `plaso/outputs/case01.csv` y la guardo en `reports/forensics/timeline-<caso>.csv`.
- **Recomendaciones:** aplica `--timezone Europe/Madrid` para evitar errores de guardia.
- **Cuándo usarlo:** cuando necesitas correlacionar múltiples artefactos (registro web + logs de Windows).
- **Cuándo no:** si solo necesitas un artefacto puntual (usa `mdls` o `stat`).

### Timesketch
- **Enlace:** https://github.com/google/timesketch
- **Caso de uso:** visualización colaborativa de la línea temporal y búsqueda conjunta.
- **Comando de ejemplo:** `timesketch_importer --sketch=LabCase --story=InitialTimeline plaso/win-case01.plaso`
- **Notas útiles:** me sirve para que un equipo consensúe hallazgos y para exportar `stories` a `reports/forensics/timesketch-case01.json`.
- **Recomendaciones:** mantén el esquema de permisos (admin, analista) y versiona los STORIES en Git.
- **Cuándo usarlo:** en investigaciones largas que involucran varios analistas.
- **Cuándo no:** en análisis de emergencia donde no puedes arrancar la plataforma Timesketch.

## 4. Forense de red y reconstrucción

### NetworkMiner
- **Enlace:** https://www.netresec.com/?page=NetworkMiner
- **Caso de uso:** reconstrucción de sesiones HTTP/FTP/SMB y extracción de archivos.
- **Comando de ejemplo:** `NetworkMiner.exe -r captures/case01.pcap --json -o forensics/network/networkminer`.
- **Notas útiles:** guardo `NetworkMiner_Export.json` y las credenciales en `reports/forensics/network/creds.csv`.
- **Recomendaciones:** combina con Zeek para correlacionar las alertas.
- **Cuándo usarlo:** cuando necesitas saber qué archivos se descargaron o qué credenciales se transmitieron.
- **Cuándo no:** si solo quieres metadatos de red (usa Zeek y Arkime en su lugar).

### Tshark + Xplico
- **Enlace:** https://www.wireshark.org/docs/man-pages/tshark.html / https://www.xplico.org/
- **Caso de uso:** extracción de protocolos específicos y reconstrucción de sesiones multimedia.
- **Comando de ejemplo:** `tshark -r captures/case01.pcap -Y "http" -T fields -e http.host -e http.uri > forensics/network/http-uris.txt`
- **Notas útiles:** Xplico convierte PCAP a archivos descargados; exporto el ZIP y lo subo a `forensics/network/xplico-case01/`.
- **Recomendaciones:** usa filtros `-Y` para reducir output y versiona los filtros en `network/filters/tshark.grep`.
- **Cuándo usarlo:** cuando necesitas reconstruir documentos, correo o multimedia.
- **Cuándo no:** si la captura es demasiado grande y solo necesitas metadatos; en ese caso, usa `Zeek` y `Arkime`.

## 5. Procedimientos y documentación
- Documenta la cadena de custodia en `forensics/chain-of-custody.txt` y enlaza cada hash con el log del comando (FTK, dd, Volatility).
- Guarda las salidas en carpetas por tipo: `forensics/images/`, `forensics/memory/`, `forensics/network/` y linkéalas desde `reports/forensics/index.md`.
- Usa `scripts/forensics/validate-hashes.sh` para verificar que los hash no cambian al mover archivos entre análisis.
- Al cierre del caso, genera un dossier en `reports/forensics/<caso>/`, con `summary.md` + el timeline exportado de Timesketch.
