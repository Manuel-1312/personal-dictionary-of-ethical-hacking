# Toolkit - Proxies Web 🛡️

Guarda proxies interceptores, scripts y CA propios que usas en auditorías; documenta certificados y filtros aplicados.

| Herramienta | Enlace | Categoría | Notas |
| --- | --- | --- | --- |
| OWASP ZAP | https://github.com/zaproxy/zaproxy | Proxy + spider | Activa scripts y detalla contextos autenticados.
| Burp Suite CE | https://portswigger.net/burp/releases/community | Proxy manual | Exporta CA y guarda extensiones instaladas.
| mitmproxy | https://mitmproxy.org/ | Interceptor en CLI | Usa `mitmdump` y documenta hooks y flows.
| Fiddler Everywhere | https://www.telerik.com/fiddler | Proxy GUI | Documenta filtros y endpoints interceptados.
| Charles Proxy | https://www.charlesproxy.com/ | Proxy SSL | Usa para móviles y describe bypass de SSL pinning.
| Burp Collaborator | https://portswigger.net/burp/collaborator | Detección OOB | Anota triggers y cómo reproducirlos.

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