# Toolkit - Disco 🧱

Lista herramientas que usas para capturar y analizar imágenes de disco; documenta cada comando y los hashes generados.

## Plantilla base
- **Enlace:** referencia oficial.
- **Caso de uso:** propósito de la herramienta.
- **Comando de ejemplo:** comando representativo.
- **Notas útiles:** observaciones clave.
- **Recomendaciones:** consejos de uso.
- **Cuándo usar / cuándo no:** límites y contexto.

## 1. Herramientas de captura y análisis de disco

### ddrescue
- **Enlace:** https://www.gnu.org/software/ddrescue/
- **Caso de uso:** Captura raw de disco con recuperación de sectores defectuosos.
- **Comando de ejemplo:** `ddrescue -d -f /dev/sdb images/drive.img images/drive.log`
- **Notas útiles:** Usa `status=progress` y guarda logs detallados; reintenta sectores fallidos automáticamente.
- **Recomendaciones:** Guarda siempre el fichero de log de ddrescue; permite reanudar la captura si se interrumpe.
- **Cuándo usarlo:** Captura forense de discos con sectores defectuosos o cuando la integridad es crítica.
- **Cuándo no:** Discos en buen estado donde dd o FTK Imager son más rápidos y simples.

### FTK Imager
- **Enlace:** https://accessdata.com/product-download/ftk-imager-version-4.3.0
- **Caso de uso:** Creación de imágenes forenses con verificación de integridad integrada.
- **Comando de ejemplo:** `ftkimager /dev/sdb images/drive.E01 --e01`
- **Notas útiles:** Registra MD5/SHA1 automáticamente y conserva la cadena de custodia; soporta formatos E01 y raw.
- **Recomendaciones:** Verifica siempre el hash post-captura; exporta el informe de hash junto a la imagen.
- **Cuándo usarlo:** Creación de imágenes forenses certificadas con trazabilidad de cadena de custodia.
- **Cuándo no:** Sistemas Linux donde ddrescue o Guymager son más nativos y eficientes.

### Autopsy / Sleuth Kit
- **Enlace:** https://www.sleuthkit.org/autopsy/
- **Caso de uso:** Análisis forense de imágenes de disco con GUI y exportación de timelines.
- **Comando de ejemplo:** `autopsy` (GUI) o `fls -r image.E01` (Sleuth Kit CLI)
- **Notas útiles:** Exporta timelines y resalta artefactos críticos; integra múltiples módulos de análisis.
- **Recomendaciones:** Crea un caso por incidente; añade todos los artefactos al mismo caso para correlación.
- **Cuándo usarlo:** Análisis profundo de artefactos de disco, recuperación de ficheros y construcción de timelines.
- **Cuándo no:** Análisis rápido de hash o verificación de integridad; usa Hashdeep para eso.

### Guymager
- **Enlace:** https://guymager.sourceforge.io/
- **Caso de uso:** Adquisición forense de disco con GUI en Linux y soporte de múltiples formatos.
- **Comando de ejemplo:** interfaz gráfica con selección de dispositivo y formato de salida
- **Notas útiles:** Documenta qué dispositivos y etiquetas se usaron; soporta formatos EWF, AFF y raw.
- **Recomendaciones:** Usa en distribuciones forenses como CAINE o Tails; documenta dispositivo fuente y destino.
- **Cuándo usarlo:** Adquisición forense en Linux cuando se prefiere una interfaz gráfica a ddrescue.
- **Cuándo no:** Entornos sin GUI o cuando se necesita captura scriptable desde CLI.

### Hashdeep
- **Enlace:** https://github.com/jessek/hashdeep
- **Caso de uso:** Cálculo y verificación de hashes en cascada (MD5, SHA1, SHA256) para directorios.
- **Comando de ejemplo:** `hashdeep -rl images/drive.img > reports/forensics/disk-hashes.txt`
- **Notas útiles:** Calcula sumas en cascada y compara con inventario previo para detectar cambios.
- **Recomendaciones:** Guarda el manifiesto de hashes en repositorio; úsalo para verificar integridad entre entornos.
- **Cuándo usarlo:** Verificación de integridad de imágenes y evidencias antes y después del análisis.
- **Cuándo no:** Cálculo de hash de un solo fichero; `sha256sum` es más rápido para ese caso.

### EWF tools
- **Enlace:** https://www.encase.com/
- **Caso de uso:** Conversión y manipulación de imágenes en formato EWF/E01 (EnCase).
- **Comando de ejemplo:** `ewfacquire /dev/sdb -t images/drive`
- **Notas útiles:** Describe la conversión raw → E01 y captura logs; útil para interoperabilidad con herramientas forenses.
- **Recomendaciones:** Documenta la versión de EWF tools y el formato de compresión usado; verifica hash post-conversión.
- **Cuándo usarlo:** Conversión entre formatos forenses o cuando el receptor del informe requiere formato E01.
- **Cuándo no:** Análisis directo de imágenes raw donde no se necesita conversión de formato.

## Comandos utilizados
- `ddrescue -d -f images/drive.img images/drive.log`.
- `ftkimager /input /dev/sdb /output images/drive.E01`.
- `hashdeep -rl images/drive.img > reports/forensics/disk-hashes.txt`.

## Técnicas aplicadas
- Captura con `ddrescue` seguida por validación con `hashdeep`.
- Remix de artefactos con Autopsy y exportación de timelines para enlaces.

## Recomendaciones personales
- Mantén logs en `forensics/disk/logs/` para poder revisar la opción de recuperación.
- Documenta qué host originó cada imagen y qué incidentes se investigan.
