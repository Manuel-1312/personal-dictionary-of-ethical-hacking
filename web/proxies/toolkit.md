# Toolkit - Proxies Web 🛡️

Guarda proxies interceptores, scripts y CA propios que usas en auditorías; documenta certificados y filtros aplicados.

## Plantilla base
- **Enlace:** referencia oficial.
- **Caso de uso:** propósito de la herramienta.
- **Comando de ejemplo:** comando representativo.
- **Notas útiles:** observaciones clave.
- **Recomendaciones:** consejos de uso.
- **Cuándo usar / cuándo no:** límites y contexto.

## 1. Proxies interceptores

### OWASP ZAP
- **Enlace:** https://github.com/zaproxy/zaproxy
- **Caso de uso:** Proxy + spider con scripts de automatización y contextos autenticados.
- **Comando de ejemplo:** `zap-baseline.py -t http://lab.local -r reports/proxies/zap-baseline.html`
- **Notas útiles:** Activa scripts y detalla contextos autenticados; útil para escaneo pasivo y activo.
- **Recomendaciones:** Guarda contextos ZAP por proyecto; usa el modo daemon para integración en CI.
- **Cuándo usarlo:** Auditorías web automatizadas o semiautomáticas con contexto de autenticación.
- **Cuándo no:** Análisis manual puntual donde Burp Suite CE ofrece mejor ergonomía.

### Burp Suite CE
- **Enlace:** https://portswigger.net/burp/releases/community
- **Caso de uso:** Proxy manual de referencia para análisis y manipulación de tráfico web.
- **Comando de ejemplo:** `burpsuite -project-file web/proxies/web-lab.burp`
- **Notas útiles:** Exporta CA y guarda extensiones instaladas; usa Repeater e Intruder para validación manual.
- **Recomendaciones:** Guarda el proyecto Burp por sesión; documenta qué extensiones activas usaste.
- **Cuándo usarlo:** Análisis manual detallado de peticiones, manipulación de parámetros y validación de hallazgos.
- **Cuándo no:** Escaneo automatizado a escala; la versión CE tiene límites en Intruder y Scanner.

### mitmproxy
- **Enlace:** https://mitmproxy.org/
- **Caso de uso:** Proxy interceptor en CLI con soporte de scripts Python para automatización.
- **Comando de ejemplo:** `mitmdump -s web/proxies/mitm-scripts/log.py`
- **Notas útiles:** Usa `mitmdump` y documenta hooks y flows; ideal para transformaciones automáticas.
- **Recomendaciones:** Guarda scripts de hook en `web/proxies/mitm-scripts/`; versiona flows útiles.
- **Cuándo usarlo:** Automatización de modificaciones de tráfico o integración con scripts Python.
- **Cuándo no:** Análisis visual interactivo donde una GUI es más eficiente.

### Fiddler Everywhere
- **Enlace:** https://www.telerik.com/fiddler
- **Caso de uso:** Proxy GUI multiplataforma con filtros y breakpoints visuales.
- **Comando de ejemplo:** interfaz gráfica con filtros por endpoint
- **Notas útiles:** Documenta filtros y endpoints interceptados; útil para tráfico mixto HTTP/HTTPS.
- **Recomendaciones:** Configura filtros por dominio para reducir ruido; exporta sesiones en HAR.
- **Cuándo usarlo:** Análisis rápido de tráfico de apps desktop o web con interfaz intuitiva.
- **Cuándo no:** Análisis profundo de seguridad; Burp Suite ofrece más herramientas especializadas.

### Charles Proxy
- **Enlace:** https://www.charlesproxy.com/
- **Caso de uso:** Proxy SSL/TLS con soporte para bypass de SSL pinning en móviles.
- **Comando de ejemplo:** instalación de CA en dispositivo móvil + proxy configurado
- **Notas útiles:** Usa para móviles y describe el proceso de bypass de SSL pinning por app.
- **Recomendaciones:** Documenta el proceso de instalación de CA por dispositivo; guarda sesiones por app auditada.
- **Cuándo usarlo:** Análisis de tráfico de apps móviles donde el SSL pinning es un obstáculo.
- **Cuándo no:** Auditorías web puras donde mitmproxy o Burp son más eficientes.

### Burp Collaborator
- **Enlace:** https://portswigger.net/burp/collaborator
- **Caso de uso:** Detección de vulnerabilidades out-of-band (OOB) como SSRF, XXE y blind injection.
- **Comando de ejemplo:** payload generado desde Burp Suite Professional
- **Notas útiles:** Anota triggers y cómo reproducirlos; cada interacción OOB debe documentarse con timestamp.
- **Recomendaciones:** Usa el servidor Collaborator solo durante la sesión activa; registra cada interacción detectada.
- **Cuándo usarlo:** Validación de vulnerabilidades OOB donde el payload no produce respuesta directa visible.
- **Cuándo no:** Laboratorios sin acceso a internet externo; las interacciones OOB no llegarán al servidor Collaborator.

## Comandos utilizados
- `zap-baseline.py -t http://lab.local -r reports/proxies/zap-baseline.html`.
- `burpsuite -project-file web/proxies/web-lab.burp`.
- `mitmdump -s web/proxies/mitm-scripts/log.py`.

## Técnicas aplicadas
- Captura de cabeceras y autenticaciones con macros.
- Inyección de payload en Burp Intruder para validar flujos.

## Recomendaciones personales
- Documenta qué certificados instalaste en el sistema.
- Guarda los flows en `web/proxies/flows/` con fecha y nota.
