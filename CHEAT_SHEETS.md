# Cheat Sheets - Biblioteca Ética

Este archivo recoge los comandos y técnicas clave que ya documentaste en cada sección, pero ahora en formato rápido para consultarlos sin abrir cada carpeta. Actualízalo cuando agregues nuevas herramientas o flujos.

## WiFi
- `airmon-ng check kill && airmon-ng start wlan0` → preparar el adaptador en modo monitor.
- `airodump-ng --write captures/session-YYYYMMDD --output-format csv,pcap wlan0mon` → captura por canal y export para análisis.
- `hcxdumptool --enable_status=1 --pmkid=1 --output captures/pmkid-... wlan0mon` → PMKID/handshakes modernos.
- Técnica: captura pasiva inicial antes de atacar; revisa ruido y señales en Wireshark.
- Recomendación: guarda los `.cap` por fecha y documenta la antena/driver usada.

## Web
- `docker run -d --name juice-shop -p 3000:3000 bkimminich/juice-shop` → entorno de pruebas limpio.
- `zap-baseline.py -t http://localhost:3000 -r reports/zap/base.html` → escaneo base.
- `ffuf -w wordlists/common.txt -u http://localhost:3000/FUZZ -mc 200,403` → fuzzing directorios.
- Técnica: combina scanners automáticos (Nikto, sqlmap) con pruebas manuales (Burp Repeater).
- Recomendación: guarda certificados y flows del proxy en `web/proxies/` para reusarlos.

## Defensa & Monitoring
- `so-import-pcap -f security-onion.pcap` → inyectar tráfico sintético en Security Onion.
- `wazuh-control -a` → sincronizar agentes después de añadir logs.
- `velociraptor config apply --config defense/hunting/vql/global.yaml` → ejecutar hunts programados.
- Técnica: correlaciona alertas Zeek+Suricata+Wazuh antes de declarar un incidente.
- Recomendación: documenta falsos positivos en `defense/monitoring/alerts/falsos.csv`.

## Network Scan & Vulnerability Assessment
- `arp-scan -l 10.0.0.0/24` → discovery antes del escaneo de puertos.
- `nmap -T3 -sC -sV -oA reports/network/nmap-full 10.0.0.0/24` → escaneo completo con scripts.
- `masscan 10.0.2.0/24 --rate 800 -p0-65535 -oG reports/network/masscan.gnmap` → detección rápida.
- `openvas-cli --target 10.0.2.5 --config /etc/openvas/policies/light.xml` → Escaneo profundo controlado.
- Técnica: discovery primero, luego escaneo y finalmente validación con OpenVAS.
- Recomendación: centraliza resultados en `reports/network/index.md` y guarda comparativas.

## Reconocimiento
- `amass enum -d example.lab -config recon/amass.conf -o outputs/recon/amass.json` → subdominios.
- `nmap -sS -Pn -oA recon/active/nmap-active 10.0.1.5` → escaneo activo autorizado.
- `shodan host 10.0.1.5 --fields ip_str,port,hostnames` → búsquedas de servicios.
- Técnica: combina OSINT pasivo (Amass, PassiveTotal) con escaneos activos (nmap, RustScan).
- Recomendación: guarda outputs en carpetas fechadas y documenta la fuente para cada dato.

## Automatización & Reporting
- `ansible-playbook -i automation/orchestration/inventory lab.yml --tags web` → despliegues.
- `python automation/reporting/scripts/render.py --template automation/reporting/templates/standard.md` → generación de PDF.
- `pandoc automation/reporting/templates/standard.md -o automation/reporting/results/report-2026.pdf` → conversión rápida.
- Técnica: usa snapshots antes de los playbooks y vuelve al estado base para repetir flujos.
- Recomendación: mantén los scripts versionados y documenta qué variables actuales se reemplazan en cada ejecución.

## Exploitation (Lab)
- `msfconsole -q` → abrir workspace limpio para validar hallazgos en un entorno controlado.
- `searchsploit --nmap reports/network/nmap-full.xml` → relacionar banners/versiones con referencias públicas.
- `sqlmap -r requests/login.txt --batch` → validar SQLi web a partir de requests guardadas.
- `bloodhound-python -u analyst -p 'Password123!' -d lab.local -ns 10.0.0.10 -c All` → mapear privilegios en AD de laboratorio.
- `sudo -l && find / -perm -4000 -type f 2>/dev/null` → enumeración local Linux previa a privilege escalation.
- `whoami /priv` → revisión rápida de privilegios en Windows de laboratorio.
- `tar czf evidence-YYYYMMDD.tgz notes/ outputs/` → compactar evidencias del caso y enlazarlas con la nota.
- Técnica: parte siempre de un hallazgo previo y documenta evidencia + limpieza al terminar.
- Recomendación: enlaza la explotación con mitigaciones en `defense/` o `network_scan/` y abre una nota en `exploitation/notes/`.

## OSINT & Forense
- `shodan search org:"Example Inc" --fields ip_str,org,port` → inventario de hosts públicos.
- `curl "https://crt.sh/?q=%25example.com"` + guarda el PDF para detectar rotaciones TLS.
- `dd if=/dev/sdb of=forensics/disk/images/server-YYYYMMDD.img bs=4M conv=sync,noerror` → captura forense.
- `./lime -f forensics/memory/mem-YYYYMMDD.raw -d /tmp` → captura RAM en caliente.
- Técnica: siempre registra la cadena de custodia (hashes en `reports/forensics/`) y documenta el motivo del caso.
- Recomendación: guarda los artefactos (`outputs/osint/`, `reports/forensics/`) y enlázalos desde los casos.
