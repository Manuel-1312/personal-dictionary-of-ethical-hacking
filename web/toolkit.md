# Toolkit - Web 🌐

Registro vivo de proxies, scanners y pruebas que ejecuto en auditorías web. Cada fila incluye qué módulo activé, los comandos exactos y dónde guardé los resultados.

| Herramienta | Enlace | Categoría | Mis notas de campo |
| --- | --- | --- | --- |
| OWASP ZAP | https://github.com/zaproxy/zaproxy | Proxy + spider | Uso la versión dockerizada, cargo `quick-start.context` y lanzo `zap-baseline.py`. Logro capturar los retos de Juice Shop en `zap/reports/`. |
| Burp Suite CE | https://portswigger.net/burp/releases/community | Proxy manual | Proyecto `burp/web-lab.burp`. Hice auth con macros, guardé el CA en `~/.burp/ca` y usé Repeater para repetir un POST con carga útil de SQLi. |
| OWASP Juice Shop | https://github.com/juice-shop/juice-shop | App vulnerable | Mantengo un `score.json` y restauro con `docker rm`+`docker run` al final de cada sesión. Anoté el comando `npm run start -- --production=false`. |
| WebGoat | https://github.com/WebGoat/WebGoat | Laboratorio | Desplegado en `docker-compose webgoat`. Guardo la lección que resuelvo y el payload `sql` usado. |
| Nikto | https://github.com/sullo/nikto | Escaneo de cabeceras | `nikto -h http://localhost:3000` → exporto `/reports/nikto/nikto-3000.html` para referencias. |
| sqlmap | https://github.com/sqlmapproject/sqlmap | SQLi automatizado | `sqlmap -u http://localhost:3000/#/search --batch --risk=3` y guardo el `.csv` con parámetros inyectados. |
| ffuf | https://github.com/ffuf/ffuf | Fuzzing | `ffuf -w wordlists/common.txt -u http://localhost:3000/FUZZ` y registro la respuesta 200 en `ffuf/logs`. |
| Dirsearch | https://github.com/maurosoria/dirsearch | Enumeración | `python3 dirsearch.py -u http://localhost:3000 -e php,html` y anoto rutas descubiertas en `web/apps/dirsearch.txt`. |

## Comandos utilizados recientemente
- `zap-baseline.py -t http://localhost:3000 -r reports/zap/baseline.html` para tener una línea base antes de atacar.
- `burpsuite -project-file web-lab.burp` con macros de login para repetir sesiones.
- `sqlmap -u http://localhost:3000/#/search --batch --risk=3 --dump` y guardo `logs/sqlmap-results.csv` para la próxima revisión.

## Técnicas aplicadas
- Escaneo combinado (Nikto + sqlmap) para contrastar cabeceras inseguras vs. inyecciones reales.
- Pruebas manuales con Burp Repeater + Intruder usando payloads como `' OR '1'='1` para calibrar la respuesta.
- Restauración periódica de contenedores (`docker rm -f juice-shop && docker run ...`) para mantener los retos en estado limpio.

## Recomendaciones personales
- Guarda la CA de Burp/ZAP en `web/proxies/ca/` para no tener que regenerarla cada vez.
- Si ffuf devuelve muchos 302, añade `-mc 200,403` y registra los hits en `web/apps/ffuf/`.
- Documenta las rutas descubiertas con Dirsearch en `reports/web/dirsearch-<fecha>.txt` para compararlas con la próxima auditoría.
