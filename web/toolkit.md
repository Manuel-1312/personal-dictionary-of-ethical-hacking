# Toolkit - Web 🌐

Registro vivo de proxies, scanners y flujos para auditorías web. Este archivo sigue una plantilla fija por herramienta (enlace, caso de uso, comando de ejemplo, notas prácticas, recomendaciones y cuándo usar/no usar) y añade flujos comunes y documentación relacionada para replicar escenarios reales.

## Plantilla de cada herramienta
- **Enlace:** referencia oficial o repositorio.
- **Caso de uso:** qué problema resuelve en la auditoría.
- **Comando de ejemplo:** muestra cómo lo lanzo.
- **Notas útiles:** apuntes prácticos, directorios, outputs relevantes.
- **Recomendaciones:** consejos para evitar errores.
- **Cuándo usarlo / cuándo no usarlo:** límites de aplicación.

## Herramientas principales

### OWASP ZAP
- **Enlace:** https://github.com/zaproxy/zaproxy
- **Caso de uso:** línea base de seguridad y pruebas manuales sobre apps en contenedores.
- **Comando de ejemplo:** `docker run -v $(pwd)/zap:/zap/wrk/:rw -t owasp/zap2docker-stable zap-baseline.py -t http://localhost:3000 -r reports/zap/baseline.html`.
- **Notas útiles:** guardo `reports/zap/session.session` y lo reimporto para continuar. Los `alerts.xml` van a `reports/zap/alerts/` y los enlazo con el cuaderno de pentesting.
- **Recomendaciones:** guarda la CA de ZAP en `web/proxies/ca/` y compártela con Burp para no volver a generar certificados.
- **Cuándo usarlo:** antes de tocar payloads manuales para capturar tráfico completo.
- **Cuándo no:** si buscas fuzzing intenso con cientos de endpoints; hay que usar herramientas más ligeras.

### Burp Suite Community
- **Enlace:** https://portswigger.net/burp
- **Caso de uso:** pruebas manuales dirigidas con Repeater/Intruder y macros autenticadas.
- **Comando de ejemplo:** `burp --project-file=web/web-lab.burp --config-file=web/burp.config` (las macros están en `web/proxies/macro-login.json`).
- **Notas útiles:** guardo macros en `web/proxies/macros/`, interceptados en `web/proxies/intercept.log` y exporto secuencias para otros entornos.
- **Recomendaciones:** combina Repeater con scripts Python que validen errores esperados para filtrar falsos positivos.
- **Cuándo usarlo:** para ajustar payloads y analizar respuestas dinámicas.
- **Cuándo no:** en escaneos masivos de directorios (usa ffuf o Feroxbuster).

### httpx
- **Enlace:** https://github.com/projectdiscovery/httpx
- **Caso de uso:** filtro rápido de dominios/subdominios vivos antes de scanners profundos.
- **Comando de ejemplo:** `httpx -l targets/web/active.txt -status-code -title -o reports/web/httpx-live.txt`.
- **Notas útiles:** agrega headers personalizados y conéctalo a `nuclei`/`ffuf` (`httpx -silent -o o --json | nuclei ...`).
- **Recomendaciones:** añade `-H 'User-Agent: CustomTester'` y `-timeout 5` para hosts lentos.
- **Cuándo usarlo:** siempre antes de scripts ruidosos.
- **Cuándo no:** cuando solo revisas archivos locales sin salir a red pública.

### nuclei
- **Enlace:** https://github.com/projectdiscovery/nuclei
- **Caso de uso:** escaneos con plantillas para CVEs, misconfiguraciones y auth.
- **Comando de ejemplo:** `nuclei -l reports/web/httpx-live.txt -t cves/ -t misconfig/ -o reports/web/nuclei-results.txt`.
- **Notas útiles:** versiono plantillas en `web/nuclei/templates/` y ejecuto `nuclei -update-templates` antes de cada auditoría.
- **Recomendaciones:** etiqueta las plantillas para replicar auditorías por cliente.
- **Cuándo usarlo:** tras obtener hosts vivos.
- **Cuándo no:** entornos offline sin conexión para actualizar plantillas (`nuclei -update-templates false`).

### ffuf
- **Enlace:** https://github.com/ffuf/ffuf
- **Caso de uso:** fuzzing de rutas y parámetros.
- **Comando de ejemplo:** `ffuf -w wordlists/common.txt -u http://localhost:3000/FUZZ -mc 200,403 -o reports/web/ffuf-200.csv`.
- **Notas útiles:** guardo combos en `web/ffuf/combo-<fecha>.txt` y combino wordlists con `python scripts/wordlist-combiner.py`.
- **Recomendaciones:** activa `-recursion-depth 2` y `-t 40` si la app responde rápido.
- **Cuándo usarlo:** para descubrir endpoints ocultos.
- **Cuándo no:** APIs con límites estrictos o rate limits sin autorización.

### Feroxbuster
- **Enlace:** https://github.com/epi052/feroxbuster
- **Caso de uso:** enumeración resiliente de directorios con listas pesadas.
- **Comando de ejemplo:** `feroxbuster -u http://localhost:3000 -w wordlists/raft-large-directories.txt -o reports/web/feroxbuster.json`.
- **Notas útiles:** guarda logs en `web/apps/feroxbuster/ferox.log` y activa `--threads 25 --timeout 10` para exploraciones intensivas.
- **Recomendaciones:** añade `--custom-extensions php,js,aspx` con stacks mixtos.
- **Cuándo usarlo:** cuando necesitas enumeración profunda sin proxies.
- **Cuándo no:** objetivos lentos con muchos 503.

### Dirsearch
- **Enlace:** https://github.com/maurosoria/dirsearch
- **Caso de uso:** confirmación rápida de directorios y archivos.
- **Comando de ejemplo:** `python3 dirsearch.py -u http://localhost:3000 -e php,html,zip -r -o reports/web/dirsearch.txt`.
- **Notas útiles:** usa `-r` para seguir redirecciones y registra hits en `web/apps/dirsearch/handbook.md`.
- **Recomendaciones:** combínalo con WhatWeb para asociar tecnologías.
- **Cuándo usarlo:** al principio de la auditoría.
- **Cuándo no:** después de tener un mapa completo; los resultados pueden ser abrumadores.

### WhatWeb
- **Enlace:** https://github.com/urbanadventurer/WhatWeb
- **Caso de uso:** fingerprinting de stacks y versiones.
- **Comando de ejemplo:** `whatweb http://localhost:3000 -a 3 -v --log-verbose web/whatweb/http-tech.txt`.
- **Notas útiles:** sus resultados alimentan `reportes/web/tech-stack.md` para decidir payloads.
- **Recomendaciones:** usa `-a 3` sólo con permiso para evitar bloqueos.
- **Cuándo usarlo:** al principio para orientar la estrategia.
- **Cuándo no:** tras haber sido bloqueado por fingerprinting excesivo.

### Nikto
- **Enlace:** https://github.com/sullo/nikto
- **Caso de uso:** chequeo de cabeceras, servidores y plugins peligrosos.
- **Comando de ejemplo:** `nikto -h http://localhost:3000 -output reports/web/nikto.txt`.
- **Notas útiles:** exporto hallazgos a `reports/web/nikto-<fecha>.json` y los cruzo con hallazgos manuales.
- **Recomendaciones:** siempre contrastar con Burp por falsos positivos.
- **Cuándo usarlo:** para configuraciones inseguras rápidas.
- **Cuándo no:** si ya tienes la lista de CVEs con `nuclei`.

### sqlmap
- **Enlace:** https://github.com/sqlmapproject/sqlmap
- **Caso de uso:** automatizar inyecciones SQL confirmadas.
- **Comando de ejemplo:** `sqlmap -u "http://localhost:3000/#/search" --data "q=1" --batch --risk=3 --threads=8 -o reports/web/sqlmap-results.csv`.
- **Notas útiles:** guardo `reports/web/sqlmap-req.txt` y uso `--os-shell` sólo en entornos autorizados.
- **Recomendaciones:** en blind SQLi prueba `--technique=BT --time-sec=5`.
- **Cuándo usarlo:** cuando la inyección está confirmada.
- **Cuándo no:** endpoints sin parámetros manipulables.

### OWASP Juice Shop (laboratorio)
- **Enlace:** https://github.com/juice-shop/juice-shop
- **Caso de uso:** sandbox para probar workflows y validar scripts.
- **Comando de ejemplo:** `docker-compose -f juice-shop/docker-compose.yml up` y lanza scripts de Burp/ZAP.
- **Notas útiles:** mantengo snapshots (`docker commit`) y limpio con `docker rm -f juice-shop`.
- **Recomendaciones:** usa `juice-shop/score.json` para medir progreso.
- **Cuándo usarlo:** para validar nuevas técnicas.
- **Cuándo no:** en auditorías en vivo.

## Flujos y documentación relacionada

### Flujos comunes
- `httpx` → `nuclei`: filtra hosts y dispara plantillas específicas.
- `ffuf` + `Dirsearch`: confirma rutas y lanza Burp Intruder sobre los hits.
- `Burp` + `sqlmap`: reutiliza la request de Repeater en `sqlmap --request=request.txt`.
- `ZAP` spider + `Feroxbuster`: aseguran que no quede endpoint oculto.

### Documentación relacionada
- `web/proxies/README.md`: incluye instrucciones para cargar certificados y macros.
- `reports/web/tech-stack.md`: muestra frameworks detectados para reutilizar templates de `nuclei`.
- `reports/web/dirsearch-<fecha>.txt` y `zaproxy/baseline` para comparar sesiones previas.
