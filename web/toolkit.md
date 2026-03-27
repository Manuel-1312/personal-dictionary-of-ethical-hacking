# Toolkit - Web 🌐

Registro vivo de proxies, laboratorios y herramientas web que encajan bien en auditorías de aplicaciones. La idea no es solo listar nombres: cada entrada recuerda para qué sirve, cómo la usarías en un lab y qué merece la pena guardar como evidencia.

| Herramienta | Enlace | Categoría | Comando / uso típico | Notas de campo |
| --- | --- | --- | --- | --- |
| OWASP ZAP | https://github.com/zaproxy/zaproxy | Proxy + baseline | `zap-baseline.py -t http://localhost:3000 -r reports/zap/baseline.html` | Buena línea base antes de tocar nada; si el target es grande, guarda contexto y exclusiones. |
| Burp Suite CE | https://portswigger.net/burp/releases/community | Proxy manual | `burpsuite -project-file web-lab.burp` | Ideal para repetir requests, macros de login y pruebas finas en Repeater. |
| OWASP Juice Shop | https://github.com/juice-shop/juice-shop | App vulnerable | `docker run --rm -p 3000:3000 bkimminich/juice-shop` | Muy útil para practicar auth, lógica, uploads y client-side issues sin improvisar demasiado. |
| WebGoat | https://github.com/WebGoat/WebGoat | Laboratorio | `docker compose up webgoat` | Sirve para recorrer vulnerabilidades por lecciones y documentar payloads mínimos. |
| Nikto | https://github.com/sullo/nikto | Enumeración web | `nikto -h http://localhost:3000 -output reports/web/nikto-3000.html` | Mejor como detector rápido de cabeceras raras, ficheros típicos y banners inseguros. |
| ffuf | https://github.com/ffuf/ffuf | Fuzzing | `ffuf -w wordlists/common.txt -u http://localhost:3000/FUZZ -mc 200,403` | Muy cómodo para descubrir rutas, parámetros y paneles sin montar demasiado contexto. |
| Dirsearch | https://github.com/maurosoria/dirsearch | Enumeración | `python dirsearch.py -u http://localhost:3000 -e php,html,js` | Bueno para sacar rutas legibles y compararlas luego con ffuf. |
| sqlmap | https://github.com/sqlmapproject/sqlmap | SQLi automatizada | `sqlmap -r requests/login.txt --batch --risk=2` | Mejor usarlo a partir de una request guardada; evita dispararlo a ciegas. |
| httpx | https://github.com/projectdiscovery/httpx | Fingerprinting HTTP | `httpx -l hosts.txt -title -tech-detect -status-code` | Muy útil para inventario rápido de varios objetivos web antes de profundizar. |
| nuclei | https://github.com/projectdiscovery/nuclei | Plantillas / checks | `nuclei -l hosts.txt -severity low,medium,high -o reports/web/nuclei.txt` | Úsalo como triage, no como verdad absoluta; siempre conviene validar lo importante. |
| WhatWeb | https://github.com/urbanadventurer/WhatWeb | Fingerprinting | `whatweb http://localhost:3000` | Ligero y rápido para pistas iniciales sobre CMS, frameworks y cabeceras. |
| Feroxbuster | https://github.com/epi052/feroxbuster | Enumeración recursiva | `feroxbuster -u http://localhost:3000 -w wordlists/common.txt` | Cómodo cuando quieres profundidad y buen rendimiento en rutas web. |

## Comandos utilizados recientemente
- `zap-baseline.py -t http://localhost:3000 -r reports/zap/baseline.html` para tener una línea base antes de tocar la app.
- `burpsuite -project-file web-lab.burp` con macros de login y trabajo manual en Repeater.
- `ffuf -w wordlists/common.txt -u http://localhost:3000/FUZZ -mc 200,403 -of md -o reports/web/ffuf.md`.
- `sqlmap -r requests/login.txt --batch --risk=2 --level=3` para confirmar inyecciones a partir de una request real.
- `httpx -l targets/web.txt -title -tech-detect -status-code -o reports/web/httpx.txt` para inventario inicial.

## Técnicas aplicadas
- Empiezo por fingerprinting ligero (`httpx`, `WhatWeb`, `Nikto`) y solo luego paso a enumeración más agresiva.
- Si aparece un hallazgo interesante, guardo request/response y lo enlazo con `exploitation/web_exploitation/` para no perder el hilo.
- Combino descubrimiento (`ffuf`, `dirsearch`, `feroxbuster`) con validación manual en Burp o ZAP para separar ruido de hallazgos reales.

## Recomendaciones personales
- Guarda siempre requests importantes en `web/requests/` o en una nota del caso; luego sqlmap y Burp se aprovechan muchísimo mejor.
- Si una app usa autenticación, anota cómo mantuviste la sesión viva (cookie, token, macro, rol) porque eso luego explica muchos falsos negativos.
- Si el target devuelve demasiados 302/403, registra una baseline primero para saber qué es comportamiento normal y qué es realmente interesante.
