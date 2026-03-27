# Toolkit - Forense Digital 🔍

Registro práctico de herramientas de adquisición, análisis y documentación forense. Cada bloque sigue la plantilla estándar (enlace, caso de uso, comando, notas, recomendaciones, cuándo usar/no usar) y cierra con flujos y referencias para mantener la cadena de custodia.

## Plantilla guía
- **Enlace:** referencia oficial.
- **Caso de uso:** aporte al análisis forense.
- **Comando de ejemplo:** ejecución reproducible.
- **Notas útiles:** paths, outputs, comparativas.
- **Recomendaciones:** buenas prácticas del laboratorio.
- **Cuándo usar / cuándo no:** límites de la herramienta.

## 1. Adquisición y análisis de disco

### FTK Imager
- **Enlace:** https://accessdata.com/product-download/ftk-imager-version-4.3.0
- **Caso de uso:** imagen forense inicial de discos y pendrives controlados.
- **Comando de ejemplo:** `ftkimager.exe --evidencefile=case01.E01 --log=artifacts/ftk/case01.log --hash=SHA256 --format=E01 --source=\\.\PhysicalDrive2`
- **Notas útiles:** uso modo lectura y registro de hash en `forensics/chain-of-custody.txt`. Copio E01 y logs al servidor de evidencias y sello con comprobantes digitales.
- **Recomendaciones:** documenta número de serie y hardware antes de iniciar. Captura primero la imagen y trabaja sobre la copia.
- **Cuándo usarlo:** cuando se necesitan pruebas admisibles en tribunales.
- **Cuándo no:** si sólo analizas una VM (usa `dd` virtual o monta el VMDK).

### Autopsy + Sleuth Kit
- **Enlace:** https://www.sleuthkit.org/autopsy/
- **Caso de uso:** análisis guiado de FS, extracción de timelines y visualización de artefactos.
- **Comando de ejemplo:** `autopsy --in-place --case gallery --data /mnt/images/case01.E01`
- **Notas útiles:** exporto reportes a `autopsy/reports/<caso>/report.html` y timelines a `autopsy/timelines/<caso>.csv`. Uso Sleuth Kit (`fls`, `icat`, `mactime`) para reconstruir rutas.
- **Recomendaciones:** combina árboles con `tsk_recover` y añade hashes a `autopsy/hashes/<herramienta>.txt`.
- **Cuándo usarlo:** búsqueda de artefactos para presentar a clientes.
- **Cuándo no:** en sistemas sin snapshot, ya que puede alterar timestamps.

### dd / dc3dd
- **Enlace:** https://www.gnu.org/software/coreutils/dd/ / https://github.com/ClaireWarner/dc3dd
- **Caso de uso:** capturas manuales rápidas de discos en laboratorios sin herramientas propietarias.
- **Comando de ejemplo:** `dc3dd if=/dev/sdb of=forensics/images/case02.dd hash=sha256 log=forensics/logs/dc3dd-case02.log`
- **Notas útiles:** usa `count` para limitar sectores y `conv=noerror,sync` para seguir con errores; comprueba hash y guárdalo.
- **Recomendaciones:** prefiere `dc3dd` para más control; `dd` basta si el entorno está limpio.
- **Cuándo usarlo:** cuando no hay alternativa a la captura bit a bit.
- **Cuándo no:** si estás copiando un disco en uso (usa FTK o Guymager con bloqueo).

## 2. Memoria y artefactos volátiles

### Volatility 3
- **Enlace:** https://github.com/volatilityfoundation/volatility3
- **Caso de uso:** extracción de procesos, conexiones y módulos sospechosos.
- **Comando de ejemplo:** `vol.py -f memory/case01.mem windows.pslist.PsList --output-file=volatility/pslist-case01.json`
- **Notas útiles:** guardo plugins clave (`malfind`, `pslist`, `netscan`) en `forensics/memory/plugins.txt` y comparo con Rekall.
- **Recomendaciones:** mantén perfiles en `profiles/Windows10x64.json` y automatiza con `scripts/volatility-runner.py`.
- **Cuándo usarlo:** respuesta inmediata a incidentes.
- **Cuándo no:** desde entornos comprometidos; usa máquinas air-gapped.

### Rekall
- **Enlace:** https://github.com/google/rekall
- **Caso de uso:** cross-check de volcados de memoria, especialmente `psscan` y `dlllist`.
- **Comando de ejemplo:** `rekall -f memory/case01.mem -r pslist > forensics/memory/rekall-pslist.txt`
- **Notas útiles:** convierto a JSON con `jq` y comparo con Volatility.
- **Recomendaciones:** documenta la versión en `forensics/memory/rekall-version.txt`.
- **Cuándo usarlo:** verificación adicional.
- **Cuándo no:** si sólo tienes imágenes Linux (prefiere LiME o avml).

### Redline
- **Enlace:** https://www.fireeye.com/services/freeware/redline.html
- **Caso de uso:** consolidación rápida de hashes, conexiones y módulos en Windows.
- **Comando de ejemplo:** guiado (exporta `RedlineSession.xml`).
- **Notas útiles:** uso Redline para detectar malware sin memorizar plugins; exporto sesiones a `forensics/redirect/redline-<fecha>.zip`.
- **Recomendaciones:** genera IOC y expórtalos a `The Hive`.
- **Cuándo usarlo:** equipos Windows donde necesitas una referencia rápida.
- **Cuándo no:** si buscas análisis profundo (usa Volatility/Rekall).

## 3. Línea temporal y correlación

### Plaso / log2timeline
- **Enlace:** https://github.com/log2timeline/plaso
- **Caso de uso:** generar línea temporal maestra combinando disco/memoria.
- **Comando de ejemplo:** `log2timeline.py --parsers "winlog,chrome" --status_view none plaso/win-case01.plaso forensics/images/case01.E01`
- **Notas útiles:** con `psteal.py`/`psort` exporto fragmentos (`milestone`, `user`, `webhistory`) y guardo en `plaso/outputs/case01.csv`.
- **Recomendaciones:** aplica `--timezone Europe/Madrid`.
- **Cuándo usarlo:** al correlacionar múltiples artefactos.
- **Cuándo no:** si sólo necesitas un artefacto puntual (usa `mdls` o `stat`).

### Timesketch
- **Enlace:** https://github.com/google/timesketch
- **Caso de uso:** visualización colaborativa y búsqueda conjunta.
- **Comando de ejemplo:** `timesketch_importer --sketch=LabCase --story=InitialTimeline plaso/win-case01.plaso`
- **Notas útiles:** exporto `stories` a `reports/forensics/timesketch-case01.json`.
- **Recomendaciones:** conserva esquema de permisos y versiona los `stories`.
- **Cuándo usarlo:** investigaciones largas con varios analistas.
- **Cuándo no:** análisis de emergencia sin tiempo para levantar la plataforma.

## 4. Forense de red y reconstrucción

### NetworkMiner
- **Enlace:** https://www.netresec.com/?page=NetworkMiner
- **Caso de uso:** reconstrucción de sesiones HTTP/FTP/SMB y extracción de archivos.
- **Comando de ejemplo:** `NetworkMiner.exe -r captures/case01.pcap --json -o forensics/network/networkminer`.
- **Notas útiles:** guardo `NetworkMiner_Export.json` y credenciales en `reports/forensics/network/creds.csv`.
- **Recomendaciones:** combínalo con Zeek para relacionar alertas.
- **Cuándo usarlo:** cuando necesitas saber qué archivos se movieron.
- **Cuándo no:** si sólo buscas metadatos, usa Zeek/Arkime.

### Tshark + Xplico
- **Enlace:** https://www.wireshark.org/docs/man-pages/tshark.html / https://www.xplico.org/
- **Caso de uso:** extracción de protocolos y reconstrucción multimedia.
- **Comando de ejemplo:** `tshark -r captures/case01.pcap -Y "http" -T fields -e http.host -e http.uri > forensics/network/http-uris.txt`
- **Notas útiles:** Xplico convierte PCAP a archivos descargados y los subo a `forensics/network/xplico-case01/`.
- **Recomendaciones:** usa filtros `-Y` para reducir output y versiona en `network/filters/tshark.grep`.
- **Cuándo usarlo:** cuando necesitas reconstruir documentos o multimedia.
- **Cuándo no:** si la captura es gigante y sólo buscas metadatos (usa Zeek/Arkime).

## 5. Flujos y documentación
- Documenta la cadena de custodia en `forensics/chain-of-custody.txt` y enlaza cada hash con el log de ejecución (FTK, dd, Volatility).
- Guarda salidas por tipo (`images`, `memory`, `network`) y enlázalas desde `reports/forensics/index.md`.
- Usa `scripts/forensics/validate-hashes.sh` para verificar integridad al mover archivos.
- Genera un dossier final en `reports/forensics/<caso>/` con `summary.md` + la línea temporal exportada de Timesketch.
