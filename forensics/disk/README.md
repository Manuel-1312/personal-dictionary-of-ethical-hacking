# Forense de Disco

Cada vez que capturo un disco con `dd`, `dc3dd` o `FTK Imager` dejo constancia:
- Máquina objetivo (ej. `lab-win10`, `lab-server`), versión de OS y hora.
- Comando exacto (`dd if=/dev/sdb of=images/drive.img bs=4M conv=sync,noerror`).
- Hashes (`sha256sum images/drive.img > reports/forensics/disk-hashes.txt`).

También describo cómo monto la imagen (`mount -o ro,loop=0 images/drive.img /mnt/drive`) y qué hallazgos saqué (logs, artefactos). Si hago carving con `bulk_extractor` o `Plaso`, guardo los output y linkeo el informe en `forensics/cases/`.

## Comandos utilizados
- `dd if=/dev/sdb of=forensics/disk/images/server-20260327.img bs=4M conv=sync,noerror`.
- `hashdeep -rl forensics/disk/images/server-20260327.img > reports/forensics/disk-hashes.txt`.
- `bulk_extractor -o forensics/disk/bulk/server-20260327 forensics/disk/images/server-20260327.img`.

## Técnicas aplicadas
- Captura en caliente vs en frío según el SO; documenta en la nota si es una VM o un host físico.
- Carving con Autopsy/Bulk Extractor y timeline con Plaso.

## Recomendaciones personales
- Guarda las imágenes en `forensics/disk/images/` y los hashes en `reports/forensics/`.
- Si la imagen corresponde a un incidente, enlaza el caso (`CASE-YYYY-MM-DD.md`).