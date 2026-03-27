# Proxies Web

Utiliza esta carpeta para instrucciones de configuración de proxies interceptores, extensiones o scripts auxiliares. Incluye notas sobre certificados propios (CA), autop-run scripts y cómo capturas requests/responses.

## Comandos utilizados
- `burpsuite -project-file proxies/web-lab.burp` para cargar sesiones guardadas.
- `zap.sh -daemon -config api.key=changeme` y luego `zap-cli session new`.

## Técnicas aplicadas
- Automatización de login con macros (Burp) y scripts `zaproxy_scripts/auto-login.js`.
- Uso de mitmproxy con `mitmdump -s scripts/capture.py` para manipular headers.

## Recomendaciones personales
- Guarda tu CA en `web/proxies/ca/` y documenta la caducidad para evitar warnings.
- Exporta los flows (Burp `.burp`, ZAP `.session`) al final de cada auditoría.
