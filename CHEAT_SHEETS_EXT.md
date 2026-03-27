# Cheat Sheets Extensas — Biblioteca Ética

Esta guía extendida es la libreta que me llevo a cada sesión. Respirala como un bloc con pestañas: cada bloque tiene comandos probados, técnicas con contexto, recomendaciones personales y enlaces que consulto a menudo.

---
## 🛰️ WiFi (Notas del campo)
### Comandos esenciales
- `sudo airmon-ng check kill && sudo airmon-ng start wlan0` → limpio NetworkManager y pongo la tarjeta en monitor mode.
- `airodump-ng --write captures/session-YYYYMMDD --output-format csv,pcap wlan0mon` → guardo CSV y PCAP para reconstruir sesiones con Airgraph y Wireshark.
- `hcxdumptool -i wlan0mon --enable_status=1 --pmkid=1 -o captures/pmkid-YYYYMMDD.pcapng` → capturo PMKID/handshakes modernos.
- `hashcat --show` sobre la captura para confirmar si la clave ya estaba en rockyou o si usé una máscara.

### Técnicas y aprendizajes
1. Siempre comienzo con 5 minutos de captura pasiva para medir el ruido y documentar qué dispositivos están despiertos.
2. Uso antenas distintas (Alpha para 5 GHz, TP-Link para 2.4 GHz) y dejo nota en el README de la sesión con driver + potencia.
3. Si el handshake no aparece, cambio de canal y vuelvo a capturar antes de atacar; lo anoto porque me ha salvado de sesiones desperdiciadas.

### Recomendaciones personales
- Guarda los `.cap` en carpetas fechadas (`captures/2026-02-27/`) y escribe en cada nota de sesión qué adaptador y driver usaste.
- Si `wifite` se cuelga, injerto un script `scripts/wifi/change-channel.sh` para probar otro canal automáticamente.
- Añade una sección de “objetivo” en `lab-notes.md` (ej., auditoría WPA3 vs. evaluación de WPS) para contextualizar la sesión.

### Recursos rápidos
- Documentación: https://www.aircrack-ng.org/docs/ y https://github.com/ZerBea/hcxdumptool.
- Utilidades: https://github.com/threat9/routersploit para entender los routers que simulo.

---
## 🌐 Web (estilo diario)
### Comandos probados
- `docker run -d --name juice-shop -p 3000:3000 bkimminich/juice-shop` → arranco el lab y guardo `score.json` antes/después.
- `zap-baseline.py -t http://localhost:3000 -r reports/zap/base.html -d` → primer barrido automático.
- `ffuf -w /usr/share/wordlists/raft-large-directories.txt -u http://localhost:3000/FUZZ -mc 200,403 -o web/apps/ffuf/ffuf-20260327.json`.
- `sqlmap -u "http://localhost:3000/#/search" --batch --risk=3 --dump` y guardo `/logs/sqlmap-results.csv`.

### Técnicas destacadas
1. Completo Nikto + sqlmap: primero detecto cabeceras/servicios, luego intento exploitation automática y manual.
2. Uso Burp Repeater/Intruder con payloads tipo `' OR '1'='1` para afinar la lógica.
3. Restauro contenedores al final (scripts `reset-juice-shop.sh`) y documente el paso en `web/apps/notes.md`.

### Consejos prácticos
- Mantén los certificados y proxy flows en `web/proxies/ca/` con notas de la fecha.
- Si ffuf devuelve códigos 302, añade `-s -mc 200,403` y guarda los hits para revisarlos en Burp.
- Anota nuevas rutas de Dirsearch en `reports/web/dirsearch/` para compararlas con la sesión previa.

### Recursos adicionales
- Burp docs: https://portswigger.net/burp/documentation. OWASP Top Ten: https://owasp.org/www-project-top-ten/.
- Lista de extensiones de Burp: `web/proxies/extensions.md` (Autorize, JSON Beautifier, Active Scan++). También guardo payloads en `web/apps/payloads.md`.

---
## 🛡️ Defensa & Monitorización
### Comandos clave
- `so-import-pcap -f security-onion.pcap` para inyectar tráfico sintético.
- `wazuh-control -a` luego de añadir logs nuevos.
- `velociraptor config apply --config defense/hunting/vql/global.yaml` para ejecutar hunts programados.
- `so-import-rules` con la rule_id (ej. 2100455) que quiero validar.

### Trabajo diario
1. Correlaciono alertas de Zeek, Suricata y Wazuh antes de abrir un incidente; pongo en la nota cuál dio primero.
2. Velociraptor busca `powershell` con cadenas sospechosas; los resultados van a `defense/threat_hunting/results/`.
3. The Hive dispara workflows Cortex; guardo los JSON en `defense/incident_response/playbooks/`.

### Recomendaciones cortas
- Lista falsos positivos en `defense/monitoring/alerts/falsos.csv` con el motivo de descartarlos.
- Documenta las consultas de Elastic (`event.module:suricata`, `event.dataset:zeek.http`) usadas en cada dashboard.
- Tras contener un incidente ejecuto `scripts/restore-network.sh` y anoto los pasos.

### Recursos para refrescar
- Security Onion docs: https://docs.securityonion.net/.
- Wazuh docs: https://docs.wazuh.com/4.0/.

---
## 📡 Network Scan & Vulnerability Assessment
### Comandos frecuentes
- `arp-scan -l 10.0.0.0/24` para discovery.
- `nmap -T3 -sC -sV -oA reports/network/nmap-full 10.0.0.0/24` con XML para análisis posterior.
- `ma --config /etc/openvas/policies/light.xml --output reports/network/openvas/scan-20260327.xml`.
- `nikto -h http://10.0.0.5 -outpusscan 10.0.2.0/24 --rate 800 -p0-65535 -oG reports/network/masscan.gnmap` antes de nmap.
- `openvas-cli --target 10.0.2.5t reports/network/nikto/nikto-10.0.0.5.html`.
- `gobuster dir -u http://10.0.0.5 -w /usr/share/wordlists/raft-large.txt -o reports/network/gobuster-lab.txt`.

### Técnicas aplicadas
1. Discovery (arp-scan, fping) primero, luego nmap con scripts y finalmente OpenVAS.
2. Comparo nmap + Vulscan vs. Greenbone y verifico con `curl` antes de reportar CVEs.
3. Uso VulnWhisperer para consolidar outputs en dashboards semanales.

### Recomendaciones personales
- Actualiza `reports/network/index.md` con un resumen simple de cada sesión.
- Si repites un CVE, verifica el banner y la versión real del servicio.
- Llevo scripts como `scripts/network/compare-cves.py` para ver diferencias en el tiempo.

### Recursos clave
- Nmap docs: https://nmap.org/docs.html.
- Greenbone CE: https://www.greenbone.net/en/community-edition/.

---
## 🧭 Reconocimiento & OSINT
### Comandos por tipo
- Pasivo: `amass enum -d example.lab -config recon/amass.conf -o outputs/recon/amass.json`, `theHarvester -d example.lab -b google -l 200`.
- Activo: `nmap -sS -Pn -oA recon/active/nmap-active 10.0.1.5`, `rustscan -a 10.0.1.5 -- -A -sV`.
- OSINT: `shodan host 10.0.1.5 --fields ip_str,port,hostnames`, `sublist3r -d example.lab -o outputs/recon/sublist3r.txt`.

### Técnicas preferidas
1. Mantengo hipótesis en `recon/log.md` y actualizo cuando aparecen subdominios nuevos.
2. Contrasto datos pasivos con escaneos activos antes de crear tickets.
3. Registro todo en `lab-notes.md` para no perder el contexto.

### Consejos
- Guarda outputs fechados para comparar evolución.
- Documenta la fuente y la fecha de cada hallazgo operativo.
- Respeta los límites de APIs (Shodan, Censys, SecurityTrails).

---
## 🐍 Python Tools y scripts propios
- `python python/log_parser.py --input defense/monitoring/logs/zeek.log --output automation/reporting/results/zeek-summary.csv` → parsea logs Zeek/Suricata y genera CSV/markdown con IPs/puertos.
- `python python/inventory_builder.py --nmap reports/network/nmap-full.xml --masscan reports/network/masscan.gnmap --out reports/network/inventory.md` → normaliza escaneos y crea un inventario comprimido.
- Configura un virtualenv y corre `pip install -r python/requirements.txt` para no mezclar dependencias del sistema.

### Técnicas de desarrollo
1. Cada script imprime pasos concretos (`start`, `processing`, `done`) para que el historial muestre qué sucedió.
2. Uso `argparse` + `Path` para validar rutas y mantener outputs organizados.
3. Guardar logs de cada ejecución (`python/logs/2026-03-27.log`) ayuda a replicar fallos.

### Recomendaciones personales
- Documenta en `python/README.md` qué versión de Python usas (3.11) y qué entornos virtuales creaste.
- Añade tests simples con entradas mock y una carpeta `python/tests/` para poder validar los scripts.
- Expande `python/toolkit.md` con nuevos scripts y anota qué problema resuelven (parsear JSON, generar reports, etc.).

---
## 🤖 Automatización & Reportes
### Comandos útiles
- `ansible-playbook -i automation/orchestration/inventory lab.yml --tags web`.
- `python automation/reporting/scripts/render.py --template automation/reporting/templates/standard.md --output automation/reporting/results/report-20260327.pdf`.
- `pandoc automation/reporting/templates/standard.md -o automation/reporting/results/report-2026.pdf`.
- `docker compose -f automation/orchestration/docker-compose.yml up --build`.

### Técnicas
1. Antes de cada playbook tomo snapshot y guardo el log (`orchestration/logs/run-YYYYMMDD.log`).
2. Combino pruebas automáticas (Playwright+Allure) con reportes manuales (Markdown+Pandoc).
3. Versiono templates y anoto variables obligatorias en `automation/reporting/templates/notes.md`.

### Recomendaciones
- Aclara qué partes del pipeline son manuales y cuáles automáticas.
- Mantén las plantillas en Git y documenta cada variable y su propósito.
- Guarda salidas en `automation/reporting/results/` con el nombre del caso y la fecha.

---
## 🧨 Exploitation de laboratorio
### Comandos base
- `msfconsole -q` para abrir un workspace limpio y separar sesiones por objetivo.
- `searchsploit --nmap reports/network/nmap-full.xml` para mapear hallazgos con PoCs públicas.
- `sudo -l`, `find / -perm -4000 -type f 2>/dev/null` y `pspy64` para revisar rutas de escalada en Linux de laboratorio.
- `whoami /priv`, `whoami /groups` y `winPEAS.exe` para enumerar privilegios y configuraciones débiles en Windows de prueba.
- `tar czf evidence-YYYYMMDD.tgz notes/ outputs/` para empaquetar evidencias de una sesión.

### Técnicas y aprendizajes
1. Nunca empiezo esta fase sin un hallazgo previo ya registrado en `network_scan/`, `web/` o `recon/`.
2. Prefiero validación mínima primero (manual o con herramienta ligera) y luego framework, para saber exactamente qué cambió.
3. Cierro cada sesión documentando impacto, limpieza, snapshot restaurado y mitigación recomendada.

### Recomendaciones personales
- Mantén una nota por caso con objetivo, prerequisitos, resultado y pasos de reversión.
- Enlaza cualquier IOC generado con `defense/` para que el repositorio conecte ataque y detección.
- Si pruebas privilege escalation, guarda tanto la salida en bruto como un resumen humano corto.

---
## 🔎 OSINT & Forense
### Comandos básicos
- `shodan search org:"Example Inc" --fields ip_str,org,port > outputs/osint/infra/shodan-org.json`.
- `curl "https://crt.sh/?q=%25example.com" --output outputs/osint/infra/crtsh-example.pdf`.
- `amass enum -d example.lab -config osint/amass.yml -o outputs/osint/amass.json`.
- `dd if=/dev/sdb of=forensics/disk/images/server-YYYYMMDD.img bs=4M conv=sync,noerror`.
- `./lime -f forensics/memory/mem-YYYYMMDD.raw -d /tmp`.
- `volatility3 -f forensics/memory/mem-YYYYMMDD.raw windows.pslist`.

### Técnicas y prácticas
1. Hashing inmediato y cadena de custodia en `reports/forensics/chain-of-custody.md`.
2. Volatility + Belkasoft para comparar artefactos.
3. Cada fichero lleva un `.md` con motivo y herramienta.

### Recomendaciones humanas
- Guarda artefactos en `outputs/osint/` y enlázalos desde `lab-notes.md`.
- Anota la política de privacidad y quién autorizó la captura.
- Documenta cada hash, el responsable y la ubicación en `forensics/chain-of-custody.md`.

---
## Recursos premium y plantillas
- WiFi: `wifi/notas/` (tabla antena/driver/observaciones) y script `scripts/wifi/start-monitor.sh`.
- Web: macros en `web/proxies/macros.md` y el `web/apps/scoreboard.md` con retos completados.
- Defensa: un `case-notes.md` por incidente en The Hive y dashboards versionados en `defense/monitoring/dashboards/`.
- Network: `network_scan/scripts/report-host.py` y `network_scan/rate-limits.md`.
- Recon & OSINT: `recon/osint/quick-queries.md`, `recon/bibliography.md` y repositorios referenciados.
- Automatización: `automation/reporting/templates/usage.md` y log `automation/orchestration/logs/ci-checks.csv`.
- Forense: `forensics/chain-of-custody.md` por caso y `forensics/notes.md` con versiones de herramientas.
