# Diccionario de conceptos

Explicaciones sencillas como si fuera un diccionario. Cada término lleva su definición concreta, alguna intuición práctica y un ejemplo breve cuando aplica.

## Red

| Término | Definición | Nota práctica |
| --- | --- | --- |
| **TCP** | Protocolo orientado a conexión: garantiza entrega ordenada de bytes entre dos extremos. | Ideal para servicios que no toleran pérdida (HTTP, SSH, bases de datos). Si ves una conexión establecida, casi siempre hay una sesión TCP previa. |
| **UDP** | Protocolo sin conexión: paquetes ligeros sin confirmación. | Muy usado para DNS, video y algunos escáneres porque es rápido, pero no garantiza entrega ni orden. Si ves grandes volúmenes UDP, no esperes handshake. |
| **IP** | Protocolo de Internet encargado de enrutar paquetes entre redes. | Todo paquete IP lleva dirección origen y destino; de ahí derivan IPv4 e IPv6. |
| **Servicios** | Procesos o demonios escuchando en puertos (HTTP, SMTP, etc.). | Cuando un escáner encuentra un puerto abierto, el servicio indica el vector de ataque. Guarda el banner (como `curl http://host:port`) para identificar la versión. |
| **Versiones** | Números que indican la edición del software (ej. Apache 2.4.54). | Las versiones permiten cruzar contra CVEs. Si `nmap` muestra `OpenSSH 8.2p1`, busca exploits conocidos para esa versión. |
| **Vulnerabilidades** | Debilidades en software/configuración que permiten abuso. | Se clasifican por severidad (CVSS). Documenta si es remota/local y qué condiciones la activan. |
| **Exploit** | Código o secuencia que provoca la vulnerabilidad para lograr ejecución, fuga o escalada. | Siempre corre en un entorno controlado; anota comandos y payloads para reproducirlo. |
| **Payload** | Carga útil entregada por un exploit (shell, reverse shell, meterpreter). | Describe qué hace: `payload=cmd/unix/reverse` o `meterpreter`. Sirve para explicar resultados en el reporte. |
| **Consola/Terminal** | Interfaz de texto para ejecutar comandos (PowerShell, bash, cmd). | Usa alias (`CTRL+R`, `history`) y mantén un bloc de notas con comandos útiles por sesión. |
| **Framework** | Conjunto de herramientas que agrupan exploits, módulos y scripts (Metasploit, Empire). | Un framework permite repetir pasos (configuración de exploits, payloads, post-explotación). Mantén un `workspace` por objetivo. |
| **DNS** | Sistema de nombres de dominio que traduce nombres legibles (google.com) a direcciones IP. | Esencial en recon: consultar registros A, MX, TXT y NS revela infraestructura. Herramientas: `dig`, `nslookup`, `dnsx`. |
| **DHCP** | Protocolo que asigna IPs automáticamente a dispositivos en la red. | En labs, controlar DHCP ayuda a predecir rangos de IP y detectar equipos no autorizados (rogue DHCP). |
| **NAT** | Traducción de direcciones de red: permite que muchos dispositivos compartan una IP pública. | Al escanear desde fuera, la IP visible puede ocultar múltiples hosts internos. Documenta siempre si estás detrás de NAT. |
| **VLAN** | Red virtual que segmenta tráfico dentro de un mismo switch físico. | Entender VLANs es clave para evaluar la segmentación: un VLAN hopping puede exponer tráfico que debería estar aislado. |
| **Firewall** | Dispositivo o software que filtra tráfico basándose en reglas (IP, puerto, protocolo). | Durante un pentest, identifica qué puertos están filtrados vs cerrados. Un puerto filtrado puede indicar un firewall bloqueando. |

## Web

| Término | Definición | Ejemplo / Consejo |
| --- | --- | --- |
| **Proxy** | Intermediario que intercepta tráfico HTTP/S para manipular peticiones/respuestas. | Burp/ZAP son proxies; captura request y edita parámetros desde Repeater para iterar. |
| **Fuzzing** | Enviar entradas automáticas variadas para descubrir rutas o parámetros frágiles. | `ffuf` o `Feroxbuster` prueban `FUZZ` en URLs. Usa wordlists propias y revisa respuestas 200/302/401. |
| **Inyección SQL** | Insertar código SQL en parámetros para romper consultas del backend. | Usa `sqlmap` con un request real: `sqlmap -r request.txt`. Documenta parámetro y payload exitoso. |
| **Cabeceras HTTP** | Metadatos (CSP, HSTS, Server) que indican configuración y versiones. | Un `Server: Apache/2.4.54` ayuda a saber si hay exploits sin autenticación. |
| **Autenticación** | Mecanismo que verifica identidad (cookies, tokens). | Anota qué cookies de sesión se renuevan y qué headers se prueban en Burp Intruder para detectar fallos. |
| **CSRF** | Solicitud falsa que se ejecuta con credenciales del usuario. | Usa un HTML simple que envía un POST a `transfer.php` para demostrar la exposición. |
| **XSS** | Inyección de scripts en el navegador de la víctima a través de una aplicación web. | Hay tres tipos: reflejado, almacenado y DOM-based. Busca campos de entrada que devuelvan tu input sin sanitizar. |
| **SSRF** | Forzar al servidor a hacer peticiones a recursos internos o externos. | Prueba con `http://127.0.0.1` o `http://169.254.169.254` (metadata de cloud) en parámetros de URL. |
| **IDOR** | Acceso directo a objetos internos cambiando un identificador (ej. `?id=1` → `?id=2`). | Cambia IDs en la URL o en el body y compara respuestas. Si accedes a datos de otro usuario, es un IDOR. |
| **Directory Traversal** | Navegar fuera del directorio esperado usando secuencias como `../`. | Prueba `../../etc/passwd` en parámetros de archivo. Documenta la ruta exacta que funcionó. |

## Reconocimiento y OSINT

| Término | Definición | Aplicación rápida |
| --- | --- | --- |
| **Footprinting** | Recopilar información pública para definir el perímetro digital. | Incluye DNS, certificados, redes sociales y papel del objetivo. |
| **OSINT** | Inteligencia de fuentes abiertas; combina web, redes y APIs. | Documenta cada fuente (Google, LinkedIn, Shodan) con fecha y query. |
| **Subdominios** | Dominios extra bajo el mismo dominio principal (`api.example.com`). | Úsalos para encontrar apps olvidadas con `assetfinder` + `dnsx`. |
| **Shodan** | Motor que indexa banners de servicios expuestos. | `shodan search "org:Example"` devuelve IPs y puertos, ideal para comparar con tus escaneos internos. |
| **Wayback Machine** | Archivo histórico de páginas web. | Extrae URLs antiguas para ver endpoints ya retirados que aún podrían existir en entorno de producción. |
| **Seguridad Humana** | Considerar el factor humano: correos, roles, infraestructura social. | Documenta perfiles y organiza los hallazgos en `reports/osint/people.md`. |
| **Google Dorking** | Uso de operadores avanzados de Google para encontrar información expuesta. | `site:target.com filetype:pdf`, `inurl:admin`, `intitle:"index of"`. Documenta cada dork que dé resultados. |
| **Certificate Transparency** | Logs públicos de certificados SSL/TLS emitidos. | `crt.sh` permite descubrir subdominios por certificados emitidos. Complementa `amass` y `subfinder`. |

## Defensa

| Término | Definición | Cómo ayuda |
| --- | --- | --- |
| **IDS/IPS** | Detector/Protector de intrusiones (Zeek, Suricata). | Detectan patrones maliciosos en el tráfico; registra falsos positivos y afínalos para el SOC. |
| **Hunting** | Búsqueda proactiva de señales de ataque en logs. | Usa `Velociraptor`/`Grafana` para preguntas como "¿qué procesos nuevos aparecieron?". |
| **Playbook** | Procedimiento documentado para responder a un tipo de incidente. | Mantén plantillas en `defense/playbooks/` con pasos, comandos y contactos críticos. |
| **Correlación** | Relacionar eventos de varios sensores para ver un ataque completo. | Combina registros de Zeek, Suricata y Wazuh para confirmar una campaña. |
| **Dashboards** | Paneles visuales (Grafana, Kibana) que representan alertas y métricas clave. | Versiona dashboards y anota filtros/queries en `defense/dashboards/json/`. |
| **SIEM** | Plataforma que centraliza, normaliza y correlaciona logs de seguridad. | Herramientas: Splunk, Elastic SIEM, Wazuh. Configura alertas para los IOCs más relevantes. |
| **EDR** | Detección y respuesta en endpoints: monitorea procesos, archivos y conexiones en cada host. | Complementa al SIEM dando visibilidad a nivel de host. Velociraptor y osquery son opciones open source. |
| **Zero Trust** | Modelo que no confía en nada por defecto, ni siquiera dentro de la red interna. | Implica verificar identidad y autorización en cada acceso, no solo en el perímetro. |

## Explotación y post-explotación

| Término | Definición | Contexto de laboratorio |
| --- | --- | --- |
| **Pivoting** | Usar una máquina comprometida como trampolín para acceder a otras redes internas. | Configura túneles SSH o usa `chisel`/`ligolo` para alcanzar segmentos no accesibles directamente. |
| **Lateral Movement** | Moverse entre hosts dentro de la misma red usando credenciales o vulnerabilidades. | Técnicas comunes: Pass-the-Hash, PsExec, WMI. Documenta cada salto en tus notas de caso. |
| **Exfiltración** | Sacar datos del entorno comprometido hacia el exterior. | En labs, simula con archivos de prueba. Herramientas: `curl`, DNS tunneling, ICMP exfil. |
| **Persistence** | Técnicas para mantener el acceso tras un reinicio o cierre de sesión. | Registros de inicio, tareas programadas, servicios creados. Documenta y limpia siempre al terminar el lab. |
| **Privilege Escalation** | Pasar de un usuario con pocos privilegios a administrador/root. | Linux: `sudo -l`, SUID, capabilities. Windows: `whoami /priv`, servicios mal configurados, tokens. |
| **C2 (Command & Control)** | Servidor central que controla implantes o shells remotas en un lab. | Herramientas educativas: Sliver, Mythic, Covenant. Siempre en redes aisladas y documentado. |

## Forense

| Término | Definición | Punto clave |
| --- | --- | --- |
| **Adquisición** | Copia bit a bit de discos/memoria (E01, dd) para preservar evidencia. | Siempre registra hashes y evita trabajar sobre la imagen original. |
| **Cadena de custodia** | Registro de cómo y quién manipuló cada evidencia. | Usa `forensics/chain-of-custody.txt` para documentar transferencias y firmas. |
| **Línea temporal** | Ordenar eventos por marca temporal para reconstruir incidentes. | `log2timeline` + `Timesketch` ayudan a visualizar la secuencia. |
| **Memoria volátil** | Datos en RAM que desaparecen al reiniciar; contienen procesos activos. | Extrae dump con `Belkasoft`, `AVML` o `Volatility`. |
| **Análisis de red** | Revisar capturas para validar qué tráfico cruzó. | Usa `Zeek`/`NetworkMiner` para ver archivos transferidos o conexiones sospechosas. |
| **Artefactos** | Rastros que deja la actividad en un sistema: logs, registros, prefetch, shellbags. | Cada SO tiene sus propios artefactos. En Windows: Event Logs, Prefetch, Amcache. En Linux: auth.log, bash_history. |
| **Triage** | Recogida rápida de artefactos clave sin hacer imagen completa del disco. | Útil cuando el tiempo apremia. Herramientas: KAPE, Velociraptor, CyLR. |

## WiFi

| Término | Definición | Nota de seguridad |
| --- | --- | --- |
| **Handshake** | Truco inicial entre cliente y AP para verificar la clave. | Guardar el handshake permite probar diccionarios más tarde. |
| **Captura pasiva** | Escuchar sin interactuar para mapear redes/clients. | Ideal para descubrir canales antes de atacar. |
| **Cracking** | Probar diccionarios/reglas para recuperar claves WPA/WPA2. | Usa `hashcat` con `hc22000` para GPUs y `aircrack` para labs ligeros. |
| **MITM inalámbrico** | Interceptación/modificación del tráfico WiFi en tiempo real. | Solo en entornos autorizados; documenta scripts y interfaces. |
| **Visualización** | Mapas de SSID/BSSID/potencia (Airgraph, Kismet). | Útil para detectar clones o APs no autorizados. |
| **Evil Twin** | Crear un AP falso que imita uno legítimo para interceptar tráfico. | Solo para demos en lab aislado. Herramientas: `hostapd-wpe`, `wifipumpkin3`. |
| **WPA3** | Evolución de WPA2 con handshake SAE resistente a ataques de diccionario. | Requiere herramientas actualizadas; `hcxdumptool` soporta captura, pero el cracking es mucho más costoso. |

## Tips extra

- Siempre apunta la fuente del conocimiento (libro, blog, CVE, notas del laboratorio) para contextualizar las definiciones.
- Usa este diccionario como referencia rápida antes de escribir un informe o preparar un script.
- Si un término no aparece aquí, añádelo siguiendo el formato de la tabla correspondiente y abre un PR.
