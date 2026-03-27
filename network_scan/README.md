# Network Scan Lab

Aquí registro mis escaneos de red dentro del laboratorio. Cada vez que levanto una topología (subredes VLAN 10/20, routers virtuales, proxies de control) la documento: rangos usados, reglas de firewall que no quiero romper y la política de throttling que sigo para no saturar nada.

Mi flujo es este:
1. Defino el alcance y los hosts autorizados (los hostnames `lab-gw`, `lab-dmz`, `lab-client01`).
2. Uso `arp-scan` y `nbtscan` para confirmar qué IPs están activas antes de lanzar escaneos más profundos.
3. Lanzo `nmap`+`vulscan` por cada segmento y guardo las salidas en `reports/network/`.

En el README principal de cada carpeta incluyo capturas de pantalla de la topología y cualquier nota de comportamiento extraño (picos de latencia, puertos cambiantes). Los toolkits te dicen qué herramientas usé y cómo reproducir el mismo escaneo con los flags exactos: eso sirve para compartir descubrimientos y evitar que alguien repita un comando que antes saturó la red.

## Comandos utilizados
- `arp-scan -l 10.0.0.0/24` para obtener un inventario rápido antes del escaneo completo.
- `nmap -T3 -sC -sV -oA reports/network/nmap-full 10.0.1.0/24` con salida XML para alimentar reportes y `vulscan`.
- `masscan 10.0.2.0/24 --rate 800 -p0-65535 -oG reports/network/masscan.gnmap` centro para evitar brutos.

## Técnicas aplicadas
- Escaneo escalonado: primero discovery (arp-scan+masscan), luego nmap con NSE y más tarde pentesting manual.
- Reservas de ancho: uso `--rate` controlado y pausas para que los routers de laboratorio no reinicien interfaces.
- Validación cruzada: corro Vulscan y comparo con `Greenbone/OpenVAS` para ver si los CVEs coinciden.

## Recomendaciones personales
- Mantén un directorio `reports/network/yyyy-mm-dd/` con todos los outputs (nmap, masscan, netdiscover, scripts). Así puedes comparar sesiones.
- Si un host responde con TTL irregular, vuelve a escanearlo a diferentes horas; a veces los routers de lab tienen reglas rotativas.
- Guarda cualquier script de preprocesamiento (por ejemplo `scripts/network/normalize-nmap.py`) en `network_scan/scripts/` y pon notas en el README.