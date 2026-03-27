# Toolkit - Web 🌐

Registro vivo de proxies, scanners y flujos que uso en auditorías web. Cada herramienta tiene enlace, casos de uso concretos, cómo la lanzo y qué aprendo de los resultados; así puedes replicar pasos sin perderte entre flags.

## Herramientas principales

### OWASP ZAP
- **Enlace:** https://github.com/zaproxy/zaproxy
- **Caso de uso:** línea base de seguridad y pruebas manuales contra aplicaciones en contenedores. Uso `quick-start.context` para delimitar las URLs permitidas y cargo los scripts de autenticación automática.
- **Comando de ejemplo:** `docker run -v $(pwd)/zap:/zap/wrk/:rw -t owasp/zap2docker-stable zap-baseline.py -t http://localhost:3000 -r reports/zap/baseline.html`.
- **Notas útiles:** mantengo `reports/zap/session.session` y lo importo en ZAP GUI para continuar auditorías. Los ficheros de alerta (`alerts.xml`) van a `reports/zap/alerts/` y los enlazo con mi cuaderno de pentesting.
- **Recomendaciones:** guarda la CA en `web/proxies/ca/` y reutilízala entre ZAP y Burp; así evitas repetir la configuración SSL en cada proyecto.
- **Cuándo usarlo:** antes de tocar payloads manuales para comprobar configuraciones de seguridad y para registrar todo el tráfico.
- **Cuándo no:** si necesitas fuzzing de alto volumen porque ZAP consume muchas sesiones cuando hay páginas con 100+ endpoints.

### Burp Suite Community
- **Enlace:** https://portswigger.net/burp
- **Caso de uso:** tests manuales dirigidos (Repeater/Intruder) y rewrites de requests con macros y comparadores de respuestas.
- **Comando de ejemplo:** `burp --project-file=web/web-lab.burp --config-file=web/burp.config` (ver mi `README` para macros de login en `web/proxies/macro-login.json`).
- **Notas útiles:** guardo las macros en `web/proxies/macros/`, los interceptados en `web/proxies/intercept.log` y exporto las secuencias de Intruder para reproducirlas en otros entornos.
- **Recomendaciones:** combina Repeater con un script de Python que valide si la respuesta contiene el error esperado; así puedes detectar falsos positivos.
- **Cuándo usarlo:** cuando necesitas ajustar payloads o estudiar respuestas dinámicas.
- **Cuándo no:** para escaneos masivos de directorios (usa ffuf/Feroxbuster para eso).

### httpx
- **Enlace:** https://github.com/projectdiscovery/httpx
- **Caso de uso:** filtrado rápido de dominios/subdominios vivos antes de desplegar scanners profundos.
- **Comando de ejemplo:** `httpx -l targets/web/active.txt -status-code -title -o reports/web/httpx-live.txt`.
- **Notas útiles:** `httpx` me permite agregar header personalizados y conectar con `nuclei`/`ffuf` mediante pipelines (`httpx -silent -o o --json | nuclei ...`).
- **Recomendaciones:** añade `-H 'User-Agent: CustomTester'` para evitar bloqueos básicos y usa `-timeout 5` si trabajas con hosts lentos.
- **Cuándo usarlo:** siempre antes de lanzar scripts más ruidosos.
- **Cuándo no:** no lo ejecutes cuando solo quieras revisar archivos locales o URL internos sin salir a red pública.

### nuclei
- **Enlace:** https://github.com/projectdiscovery/nuclei
- **Caso de uso:** escaneos basados en plantillas para CVEs conocidos, misconfiguraciones y mecanismos de autenticación.
- **Comando de ejemplo:** `nuclei -l reports/web/httpx-live.txt -t cves/ -t misconfig/ -o reports/web/nuclei-results.txt`.
- **Notas útiles:** versiono mis plantillas locales en `web/nuclei/templates/` y uso `nuclei -update-templates` antes de cada auditoría.
- **Recomendaciones:** guarda las plantillas con tags personalizados para replicar auditorías por clientes.
- **Cuándo usarlo:** tras obtener hosts vivos.
- **Cuándo no:** en entornos offline que no permiten conexiones a atlas de templates (usa `-update-templates false`).

### ffuf
- **Enlace:** https://github.com/ffuf/ffuf
- **Caso de uso:** fuzzing de rutas y parámetros.
- **Comando de ejemplo:** `ffuf -w wordlists/common.txt -u http://localhost:3000/FUZZ -mc 200,403 -o reports/web/ffuf-200.csv`.
- **Notas útiles:** guardo combos en `web/ffuf/combo-<fecha>.txt` y rehuso wordlists propios (combinando `ffuf` con `python scripts/wordlist-combiner.py`).
- **Recomendaciones:** usa `-recursion-depth 2` para descubrir rutas profundas y `-t 40` cuando la aplicación responde rápido.
- **Cuándo usarlo:** para descubrir endpoints no documentados.
- **Cuándo no:** no lo ejecutes contra APIs con límites estrictos sin acordar con el cliente.

### Feroxbuster
- **Enlace:** https://github.com/epi052/feroxbuster
- **Caso de uso:** enumeración resiliente de directorios con lista personalizada.
- **Comando de ejemplo:** `feroxbuster -u http://localhost:3000 -w wordlists/raft-large-directories.txt -o reports/web/feroxbuster.json`.
- **Notas útiles:** guarda `feroxbuster` en `web/apps/feroxbuster/ferox.log` y actívalo con `--threads 25 --timeout 10` en sondeo intensivo.
- **Recomendaciones:** añade `--custom-extensions php,js,aspx` cuando estés auditando stacks mixtos.
- **Cuándo usarlo:** cuando quieres una enumeración profunda sin depender de proxies.
- **Cuándo no:** si el objetivo responde lento y ya tienes un listado de endpoints exhaustivo.

### Dirsearch
- **Enlace:** https://github.com/maurosoria/dirsearch
- **Caso de uso:** confirmación rápida de directorios importantes y archivos de configuración.
- **Comando de ejemplo:** `python3 dirsearch.py -u http://localhost:3000 -e php,html,zip -r -o reports/web/dirsearch.txt`.
- **Notas útiles:** uso `-u` con lista de dominios y guardo `-r` para seguir redirecciones; los hits los agrego a `web/apps/dirsearch/handbook.md`.
- **Recomendaciones:** combina `dirsearch` con `whatweb` para adjudicar tecnologías a cada endpoint descubierto.
- **Cuándo usarlo:** al inicio de una auditoría web.
- **Cuándo no:** cuando ya has mapeado la aplicación y los archivos generados son muy duros de revisar.

### WhatWeb
- **Enlace:** https://github.com/urbanadventurer/WhatWeb
- **Caso de uso:** fingerprinting de stacks y versiones de componentes.
- **Comando de ejemplo:** `whatweb http://localhost:3000 -a 3 -v --log-verbose web/whatweb/http-tech.txt`.
- **Notas útiles:** los resultados me ayudan a decidir qué payloads (CMS, frameworks) intentar y a documentar `reportes/web/tech-stack.md`.
- **Recomendaciones:** usa `-a 3` solo cuando tengas permiso de hacer requests intensivos.
- **Cuándo usarlo:** al principio para guiar el plan de ataque.
- **Cuándo no:** contra targets que ya te han bloqueado por fingerprinting excesivo.

### Nikto
- **Enlace:** https://github.com/sullo/nikto
- **Caso de uso:** chequeo de cabeceras inseguras, versiones de servidores y plugins peligrosos.
- **Comando de ejemplo:** `nikto -h http://localhost:3000 -output reports/web/nikto.txt`.
- **Notas útiles:** exporto los hallazgos a `reports/web/nikto-<fecha>.json` y los enlazo con los hallazgos manuales para comprobar falsos positivos.
- **Recomendaciones:** siempre cruza resultados con Burp; Nikto tira muchos falsos positivos.
- **Cuándo usarlo:** cuando necesitas enumerar configuraciones inseguras rápidas.
- **Cuándo no:** si ya has hecho un escaneo horizontal con `nuclei` y tienes la lista de CVEs.

### sqlmap
- **Enlace:** https://github.com/sqlmapproject/sqlmap
- **Caso de uso:** automatizar inyecciones SQL cuando el punto vulnerable ya está identificado.
- **Comando de ejemplo:** `sqlmap -u "http://localhost:3000/#/search" --data "q=1" --batch --risk=3 --threads=8 -o reports/web/sqlmap-results.csv`.
- **Notas útiles:** guardo `reports/web/sqlmap-req.txt` con los payloads y uso `--os-shell` solo en laboratorios autorizados.
- **Recomendaciones:** si detectas blind SQLi, ejecuta con `--technique=BT` y `--time-sec 5`.
- **Cuándo usarlo:** cuando la inyección está confirmada.
- **Cuándo no:** en endpoints sin parámetros manipulables.

### OWASP Juice Shop (laboratorio)
- **Enlace:** https://github.com/juice-shop/juice-shop
- **Caso de uso:** entorno para practicar workflows de `web` y `recon`.
- **Comando de ejemplo:** `docker-compose -f juice-shop/docker-compose.yml up` y luego lanzo scripts de Burp y ZAP contra `http://localhost:3000`.
- **Notas útiles:** mantengo snapshot con `docker commit` y los retos reseteados con `docker rm -f juice-shop && docker start juice-shop`.
- **Recomendaciones:** usa el score `juice-shop/score.json` para seguir el progreso y probar payloads nuevos.
- **Cuándo usarlo:** como sandbox para validar nuevas técnicas.
- **Cuándo no:** cuando trabajas en entornos productivos de clientes.

## Combinaciones útiles
- `httpx` → `nuclei`: filtro hosts vivos para no desperdiciar plantillas.
- `ffuf` + `Dirsearch`: confirmación de rutas y ejecución de Burp Intruder sobre hits concretos.
- `Burp` + `sqlmap`: copia la request de Repeater y úsala en `sqlmap --request=request.txt` para replicar pruebas.
- `ZAP` en modo spider + `Feroxbuster` para no dejar endpoints ocultos.

## Notas de laboratorio
- Mantén un archivo `reports/web/tech-stack.md` con los frameworks detectados para reutilizar plantillas de `nuclei`.
- Documenta cada CSV/JSON en `lab-notes.md` y enlaza con la fecha y el target.
- Revisa `web/proxies/README.md` antes de empezar para cargar certificados y macros.
