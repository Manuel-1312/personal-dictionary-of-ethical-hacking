# Toolkit - Evaluación de Vulnerabilidades ⚠️

Catálogo de herramientas para validar hallazgos de vulnerabilidades en laboratorios y entornos autorizados. Aquí lo importante no es solo detectar, sino poder justificar por qué confías —o no— en cada resultado.

## Plantilla base
- **Enlace:** referencia oficial.
- **Caso de uso:** propósito de la herramienta.
- **Comando de ejemplo:** comando representativo.
- **Notas útiles:** observaciones clave.
- **Recomendaciones:** consejos de uso.
- **Cuándo usar / cuándo no:** límites y contexto.

## 1. Herramientas de evaluación de vulnerabilidades

### Nmap + Vulscan
- **Enlace:** https://github.com/scipag/vulscan
- **Caso de uso:** Correlación de CVE y banners con bases de datos de vulnerabilidades.
- **Comando de ejemplo:** `nmap --script vulscan --script-args vulscandb=scipag -oX reports/network/vulscan.xml 10.0.0.0/24`
- **Notas útiles:** Muy útil para triage rápido, pero siempre pide validación manual después.
- **Recomendaciones:** Combina con `-sV` para banners más precisos; filtra resultados por severidad antes de escalar.
- **Cuándo usarlo:** Primera pasada para relacionar versiones detectadas con CVEs conocidos.
- **Cuándo no:** Para cerrar un informe sin validación manual posterior; los falsos positivos son frecuentes.

### Greenbone / OpenVAS
- **Enlace:** https://www.greenbone.net/
- **Caso de uso:** Escaneo profundo de vulnerabilidades con políticas configurables.
- **Comando de ejemplo:** `omp --create-target ...` + política ligera
- **Notas útiles:** Bueno para una pasada más pesada; conviene controlar mucho el ruido y los falsos positivos.
- **Recomendaciones:** Usa políticas ligeras en laboratorio; documenta qué política y versión de feeds usaste.
- **Cuándo usarlo:** Auditorías programadas donde tienes tiempo para analizar un reporte extenso.
- **Cuándo no:** Discovery rápido o entornos con recursos limitados; el despliegue es pesado.

### Nessus Essentials
- **Enlace:** https://www.tenable.com/products/nessus/nessus-essentials
- **Caso de uso:** Vulnerability scanner con reporting visual integrado.
- **Comando de ejemplo:** `nessuscli managed link --key ...`
- **Notas útiles:** Muy cómodo para host scanning y reporting visual si lo tienes montado en lab.
- **Recomendaciones:** Actualiza los plugins regularmente; exporta reportes en PDF/HTML para comparar sesiones.
- **Cuándo usarlo:** Auditorías de host individuales con necesidad de reporte visual rápido.
- **Cuándo no:** Más de 16 IPs (límite de Essentials); usa OpenVAS para rangos mayores.

### Nikto
- **Enlace:** https://github.com/sullo/nikto
- **Caso de uso:** Análisis básico de cabeceras y configuraciones web.
- **Comando de ejemplo:** `nikto -h http://10.0.0.5 -output reports/network/nikto-10.0.0.5.html`
- **Notas útiles:** Ligero, rápido y útil para sacar una idea general del frente web.
- **Recomendaciones:** Úsalo como primer vistazo; complementa con Burp/ZAP para validar hallazgos.
- **Cuándo usarlo:** Revisión rápida de cabeceras, versiones y rutas conocidas en servidor web.
- **Cuándo no:** Como única fuente de verdad; genera muchos falsos positivos en apps modernas.

### Gobuster
- **Enlace:** https://github.com/OJ/gobuster
- **Caso de uso:** Enumeración de directorios y rutas en aplicaciones web.
- **Comando de ejemplo:** `gobuster dir -u http://10.0.0.5 -w wordlists/common.txt`
- **Notas útiles:** Sirve para complementar la parte de paths antes de afirmar que una superficie es pequeña.
- **Recomendaciones:** Ajusta `-t` (threads) y añade extensiones con `-x` según el stack detectado.
- **Cuándo usarlo:** Después de identificar el servidor web y antes de analizar rutas manualmente.
- **Cuándo no:** En apps con WAF agresivo sin throttling; puede bloquearse rápidamente.

### Lynis
- **Enlace:** https://github.com/CISOfy/lynis
- **Caso de uso:** Auditoría de hardening y configuración de sistemas Linux/macOS.
- **Comando de ejemplo:** `lynis audit system`
- **Notas útiles:** Muy útil para Linux hardening y para tener checklists comparables entre sesiones.
- **Recomendaciones:** Guarda el `lynis-report.dat` de cada sesión para comparar evolución del hardening.
- **Cuándo usarlo:** Auditorías de configuración de host Linux en laboratorio o staging.
- **Cuándo no:** Entornos Windows; para eso usa herramientas específicas como CIS-CAT o MBSA.

### Metasploit auxiliary
- **Enlace:** https://github.com/rapid7/metasploit-framework
- **Caso de uso:** Verificación controlada de vulnerabilidades con módulos scanner.
- **Comando de ejemplo:** `msfconsole -q` + módulos `scanner/`
- **Notas útiles:** Mejor como verificación controlada que como detector principal.
- **Recomendaciones:** Usa workspaces separados; documenta módulo, opciones y resultado por cada verificación.
- **Cuándo usarlo:** Confirmar si un CVE es explotable antes de escalar a exploitation/
- **Cuándo no:** Como escáner masivo; los módulos auxiliares son lentos comparados con herramientas dedicadas.

### nuclei
- **Enlace:** https://github.com/projectdiscovery/nuclei
- **Caso de uso:** Escaneo basado en plantillas para vulnerabilidades comunes y configuraciones.
- **Comando de ejemplo:** `nuclei -l hosts.txt -severity low,medium,high`
- **Notas útiles:** Bueno para priorizar, no para cerrar un informe sin validar.
- **Recomendaciones:** Actualiza las plantillas con `nuclei -update-templates`; filtra por severidad para reducir ruido.
- **Cuándo usarlo:** Triage rápido sobre múltiples hosts con plantillas actualizadas.
- **Cuándo no:** Sin validación manual posterior; las plantillas pueden generar falsos positivos.

### testssl.sh
- **Enlace:** https://github.com/drwetter/testssl.sh
- **Caso de uso:** Análisis completo de configuración TLS/SSL, cifrados y suites.
- **Comando de ejemplo:** `testssl.sh https://target.lab`
- **Notas útiles:** Muy práctico para revisar cifrados, suites y configuración HTTPS.
- **Recomendaciones:** Guarda el output en fichero; usa `--jsonfile` para integrarlo en reportes.
- **Cuándo usarlo:** Cualquier servicio HTTPS del que quieras revisar la configuración TLS en detalle.
- **Cuándo no:** Análisis rápido donde solo necesitas conocer el protocolo; usa sslscan para eso.

### sslscan
- **Enlace:** https://github.com/rbsec/sslscan
- **Caso de uso:** Revisión ligera y rápida de TLS/SSL.
- **Comando de ejemplo:** `sslscan target.lab:443`
- **Notas útiles:** Complemento ligero cuando no necesitas todo el detalle de testssl.sh.
- **Recomendaciones:** Útil como primera verificación; si detectas algo interesante, profundiza con testssl.sh.
- **Cuándo usarlo:** Revisión rápida de protocolo, certificado y cifrados soportados.
- **Cuándo no:** Análisis exhaustivo de configuración TLS; prefiere testssl.sh para ese caso.

### enum4linux-ng
- **Enlace:** https://github.com/cddmp/enum4linux-ng
- **Caso de uso:** Enumeración SMB, usuarios y postura Windows/Samba.
- **Comando de ejemplo:** `enum4linux-ng -A 10.0.0.20`
- **Notas útiles:** Muy bueno para triage de shares, usuarios y SMB posture.
- **Recomendaciones:** Guarda output en `-oY` (YAML) para procesar con scripts posteriores.
- **Cuándo usarlo:** Triage inicial de hosts Windows o Samba antes de profundizar con herramientas AD.
- **Cuándo no:** Entornos con SMB firmado estrictamente o donde el ruido sea un problema.

### smbclient
- **Enlace:** https://www.samba.org/samba/docs/current/man-html/smbclient.1.html
- **Caso de uso:** Acceso manual a shares SMB para validación y exploración.
- **Comando de ejemplo:** `smbclient -L //10.0.0.20/ -N`
- **Notas útiles:** Ideal para contrastar lo que otros scanners dicen sobre shares y acceso.
- **Recomendaciones:** Combina `-L` para listar con acceso directo para confirmar permisos reales.
- **Cuándo usarlo:** Validación manual de shares detectados por enum4linux-ng o nmap.
- **Cuándo no:** Como único método de descubrimiento; complementa siempre con herramientas automatizadas.

## Comandos utilizados
- `nmap --script vulscan --script-args vulscandb=scipag -oX reports/network/vulscan.xml 10.0.0.0/24`.
- `nikto -h http://10.0.0.5 -output reports/network/nikto-10.0.0.5.html`.
- `lynis audit system` y comparación posterior del `lynis-report.dat`.
- `testssl.sh https://10.0.0.5` para una revisión específica de TLS.

## Técnicas aplicadas
- Contrasto al menos dos fuentes antes de elevar un hallazgo importante a "vulnerabilidad real".
- Si el hallazgo viene por banner o firma, intento reproducir con una petición manual, `curl`, `smbclient` o una prueba ligera.
- Mantengo una lista de falsos positivos y la razón del descarte para no repetir el mismo trabajo en futuras sesiones.

## Recomendaciones personales
- Si una herramienta escupe demasiadas alertas, no intentes arreglarlo con fe: recorta scope, cambia política o valida por capas.
- Cuando un hallazgo merezca seguirse, enlázalo con `exploitation/` o con una nota de mitigación para no dejarlo huérfano.
- Genera reportes exportables (XML, CSV, HTML) siempre que puedas; ayudan mucho más que una captura suelta o una nota improvisada.
