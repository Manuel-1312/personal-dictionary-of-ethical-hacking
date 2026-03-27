# Forense Digital

Esta carpeta guarda cada imagen y script que uso cuando analizo discos, memorias o tráfico. Para cada artefacto anoto:

1. El comando de captura (`dd`, `dc3dd`, `DumpIt`, `LiME`).
2. El hash calculado y dónde lo guardé (`reports/forensics/hash.txt`).
3. El contexto (por qué capturé esa VM, qué incidente estaba investigando).

Los subdirectorios `disk/` y `memory/` explican el flujo preciso y los kit tools listan comandos y notas sobre cada ejecución. Siempre preservo la cadena de custodia en `forensics/chain-of-custody.md` y enlazo el documento desde los casos relevantes.

## Comandos utilizados
- `dd if=/dev/sdb of=forensics/disk/images/server.img bs=4M conv=sync,noerror`.
- `./LiME -f forensics/memory/mem-20260327.raw -d /tmp`.
- `volatility3 -f forensics/memory/mem-20260327.raw windows.pslist`.

## Técnicas aplicadas
- Hashing inmediato después de cada captura y comparación con `hashdeep`.
- Análisis gradual: primero disco con Autopsy, luego memoria con Volatility.

## Recomendaciones personales
- Guarda las copias de hash en `reports/forensics/` y documenta qué herramienta produjo cada valor.
- Si usas VMs, conserva un snapshot previo y anota qué cambios introduciste antes de capturar.