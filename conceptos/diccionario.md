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

## Web

| Término | Definición | Ejemplo / Consejo |
| --- | --- | --- |
| **Proxy** | Intermediario que intercepta tráfico HTTP/S para manipular peticiones/respuestas. | Burp/ZAP son proxies; captura request y edita parámetros desde Repeater para iterar. |
| **Fuzzing** | Enviar entradas automáticas variadas para descubrir rutas o parámetros frágiles. | `ffuf` o `Feroxbuster` prueban `FUZZ` en URLs. Usa wordlists propias y revisa respuestas 200/302/401. |
| **Inyección SQL** | Insertar código SQL en parámetros para romper consultas del backend. | Usa `sqlmap` con un request real: `sqlmap -r request.txt`. Documenta parámetro y payload exitoso. |
| **Cabeceras HTTP** | Metadatos (CSP, HSTS, Server) que indican configuración y versiones. | Un `Server: Apache/2.4.54` ayuda a saber si hay exploits sin autenticación. |
| **Autenticación** | Mecanismo que verifica identidad (cookies, tokens). | Anota qué cookies de sesión se renuevan y qué headers se prueban en Burp Intruder para detectar fallos. |
| **CSRF** | Solicitud falsa que se ejecuta con credenciales del usuario. | Usa un HTML simple que envía un POST a `transfer.php` para demostrar la exposición. |

## Reconocimiento y OSINT

| Término | Definición | Aplicación rápida |
| --- | --- | --- |
| **Footprinting** | Recopilar información pública para definir el perímetro digital. | Incluye DNS, certificados, redes sociales y papel del objetivo. |
| **OSINT** | Inteligencia de fuentes abiertas; combina web, redes y APIs. | Documenta cada fuente (Google, LinkedIn, Shodan) con fecha y query. |
| **Subdominios** | Dominios extra bajo el mismo dominio principal (`api.example.com`). | Úsalos para encontrar apps olvidadas con `assetfinder` + `dnsx`. |
| **Shodan** | Motor que indexa banners de servicios expuestos. | `shodan search "org:Example"` devuelve IPs y puertos, ideal para comparar con tus escaneos internos. |
| **Wayback Machine** | Archivo histórico de páginas web. | Extrae URLs antiguas para ver endpoints ya retirados que aún podrían existir en entorno de producción. |
| **Seguridad Humana** | Considerar el factor humano: correos, roles, infraestructura social. | Documenta perfiles y organiza los hallazgos en `reports/osint/people.md`. |

## Defensa

| Término | Definición | Cómo ayuda |
| --- | --- | --- |
| **IDS/IPS** | Detector/Protector de intrusiones (Zeek, Suricata). | Detectan patrones maliciosos en el tráfico; registra falsos positivos y afínalos para el SOC. |
| **Hunting** | Búsqueda proactiva de señales de ataque en logs. | Usa `Velociraptor`/`Grafana` para preguntas como "¿qué procesos nuevos aparecieron?". |
| **Playbook** | Procedimiento documentado para responder a un tipo de incidente. | Mantén plantillas en `defense/playbooks/` con pasos, comandos y contactos críticos. |
| **Correlación** | Relacionar eventos de varios sensores para ver un ataque completo. | Combina registros de Zeek, Suricata y Wazuh para confirmar una campaña. |
| **Dashboards** | Paneles visuales (Grafana, Kibana) que representan alertas y métricas clave. | Versiona dashboards y anota filtros/queries en `defense/dashboards/json/`. |

## Forense

| Término | Definición | Punto clave |
| --- | --- | --- |
| **Adquisición** | Copia bit a bit de discos/memoria (E01, dd) para preservar evidencia. | Siempre registra hashes y evita trabajar sobre la imagen original. |
| **Cadena de custodia** | Registro de cómo y quién manipuló cada evidencia. | Usa `forensics/chain-of-custody.txt` para documentar transferencias y firmas. |
| **Línea temporal** | Ordenar eventos por marca temporal para reconstruir incidentes. | `log2timeline` + `Timesketch` ayudan a visualizar la secuencia. |
| **Memoria volátil** | Datos en RAM que desaparecen al reiniciar; contienen procesos activos. | Extrae dump con `Belkasoft`, `AVML` o `Volatility`. |
| **Análisis de red** | Revisar capturas para validar qué tráfico cruzó. | Usa `Zeek`/`NetworkMiner` para ver archivos transferidos o conexiones sospechosas. |

## WiFi

| Término | Definición | Nota de seguridad |
| --- | --- | --- |
| **Handshake** | Truco inicial entre cliente y AP para verificar la clave. | Guardar el handshake permite probar diccionarios más tarde. |
| **Captura pasiva** | Escuchar sin interactuar para mapear redes/clients. | Ideal para descubrir canales antes de atacar. |
| **Cracking** | Probar diccionarios/reglas para recuperar claves WPA/WPA2. | Usa `hashcat` con `hc22000` para GPUs y `aircrack` para labs ligeros. |
| **MITM inalámbrico** | Interceptación/modificación del tráfico WiFi en tiempo real. | Solo en entornos autorizados; documenta scripts y interfaces. |
| **Visualización** | Mapas de SSID/BSSID/potencia (Airgraph, Kismet). | Útil para detectar clones o APs no autorizados. |

## Tips extra

- Siempre apunta la fuente del conocimiento (libro, blog, CVE, notas del laboratorio) para contextualizar las definiciones.
- Usa este diccionario como referencia rápida antes de escribir un informe o preparar un script.
