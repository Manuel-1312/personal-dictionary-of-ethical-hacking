# Host Discovery

Esta subcarpeta explica cómo detecto qué dispositivos están vivos antes de empezar un escaneo de puertos. Anoto la topología (por ejemplo, VLAN 10 para equipos de escritorio, VLAN 20 para servidores), qué rangos exploré y cómo reduzco el ruido (ping 1 vez, pausa de 5 segundos entre hosts).

Los pasos que repito son:
1. `arp-scan` en el segmento para obtener MAC/IP y ver qué switches están respondones.
2. `nbtscan` en máquinas Windows para sacar nombres. Añado cada par `nombre→IP` a `hosts/hosts-lab.csv`.
3. `fping`/`masscan --ping` para confirmar disponibilidad.

Si un dispositivo no responde, lo marco como “pendiente” y vuelvo el siguiente día para descartar apagados. Guarda aquí cualquier script `hosts/refresh.sh` que automatice los pings para tus colegas.

## Comandos utilizados
- `arp-scan -I eth0 -l 10.0.0.0/24` (modo batch) para listar MAC y cultivar una tabla de switches.
- `nbtscan -v 10.0.0.0/24` para relacionar nombres NetBIOS; guardo el resultado en `host-discovery/nbtscan.csv`.
- `fping -a -g 10.0.0.0/24` con pausa de 200 ms entre paquetes para no congestionar.

## Técnicas aplicadas
- Repetición diaria: corro `arp-scan` dos veces al día para detectar nuevos hosts antes de un escaneo mayor.
- Validación de VLAN: si un host aparece con VLAN distinta, lanzo `masscan` solo sobre ese rango para confirmarlo.
- Uso de scripts de `nmap --script broadcast` para detectar dispositivos sin IP (printer discovery).

## Recomendaciones personales
- Mantén `hosts/hosts-lab.csv` actualizado; agrega la fecha en la columna “última vista”.
- Crea un script `hosts/cleanup.sh` que elimine IPs offline para evitar false positives durante el escaneo.
- Si un host está en `pendiente`, deja un comentario en el archivo para que el siguiente operador lo revalide.