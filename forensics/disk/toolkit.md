# Toolkit - Disco 🧱

Lista herramientas que usas para capturar y analizar imágenes de disco; documenta cada comando y los hashes generados.

| Herramienta | Enlace | Categoría | Notas |
| --- | --- | --- | --- |
| ddrescue | https://www.gnu.org/software/ddrescue/ | Captura raw | Usa `status=progress` y guarda logs detallados.
| FTK Imager | https://accessdata.com/product-download/ftk-imager-version-4.3.0 | Imagen forense | Registra MD5/SHA1 y conserva la cadena de custodia.
| Autopsy / Sleuth Kit | https://www.sleuthkit.org/autopsy/ | Análisis | Exporta timelines y resalta artefactos críticos.
| Guymager | https://guymager.sourceforge.io/ | GUI para imaging | Documenta qué dispositivos y etiquetas se usaron.
| Hashdeep | https://github.com/jessek/hashdeep | Verificación | Calcula sumas en cascada y compara con inventario.
| EWF tools | https://www.encase.com/ | Conversión | Describe la conversión raw → E01 y captura logs.

## Comandos utilizados
- `ddrescue -d -f images/drive.img`.
- `ftkimager /input /dev/sdb /output images/drive.E01`.
- `hashdeep -rl images/drive.img > reports/forensics/disk-hashes.txt`.

## Técnicas aplicadas
- Captura con `ddrescue` seguida por validación con `hashdeep`.
- Remix de artefactos con Autopsy y exportación de timelines para enlaces.

## Recomendaciones personales
- Mantén logs en `forensics/disk/logs/` para poder revisar la opción de recuperación.
- Documenta qué host originó cada imagen y qué incidentes se investigan.