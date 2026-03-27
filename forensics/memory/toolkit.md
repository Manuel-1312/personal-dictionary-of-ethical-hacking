# Toolkit - Memoria 🧠

Documenta tus capturas y análisis de RAM; incluye versiones del sistema, scripts usados y hallazgos.

| Herramienta | Enlace | Categoría | Notas |
| --- | --- | --- | --- |
| LiME | https://github.com/504ensicsLabs/LiME | Captura Linux | Guarda offsets, rutas y el método de extracción.
| DumpIt | https://www.moonsols.com/ | Captura Windows | Indica la versión del SO y si fue en caliente o en frío.
| Volatility 3 | https://github.com/volatilityfoundation/volatility3 | Análisis | Lista plugins ejecutados y resultados clave (`pslist`, `malfind`).
| Rekall | https://github.com/google/rekall | Análisis | Usa para doble verificación y registra comparativas.
| Belkasoft RAM Capturer | https://belkasoft.com/ | Captura | Documenta hash y contexto (por ejemplo UEFI/Legacy).
| Magnet RAM Capture | https://www.magnetforensics.com/ | Captura | Guarda el archivo y qué artefactos analizaste.

## Comandos utilizados
- `./lime -f forensics/memory/mem-20260327.raw -d /tmp`.
- `DumpIt.exe mem-20260327.dmp`.
- `volatility3 -f forensics/memory/mem-20260327.raw windows.pslist`.

## Técnicas aplicadas
- Use LiME para capturas en caliente de Linux y DumpIt para Windows.
- Corro Volatility y Rekall en paralelo para validar hallazgos.

## Recomendaciones personales
- Guarda hashes en `reports/forensics/memory-hashes.txt`.
- Documenta qué aviso o alerta motivó cada captura en `forensics/memory/cases/`.