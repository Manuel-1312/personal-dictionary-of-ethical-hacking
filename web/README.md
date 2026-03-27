# Web Security Lab

Este directorio es mi biblioteca de proxies, escáneres y aplicaciones vulnerables. Cuando preparo una auditoría en mi máquina (Kali en WSL + Docker con Juice Shop) sigo este flujo:

1. Inicia la app vulnerable: `docker run -p 3000:3000 bkimminich/juice-shop` y guardo un `score.json` para controlar qué retos están resueltos.
2. Preparo el proxy (Burp o ZAP) y anoto la sesión (`proxy-2026-03-27.burp`). Siempre exporto los certificados para no romper HTTPS.
3. Hago escaneo de cabeceras con `Nikto` y fuzzing con `ffuf` antes de pasar a las pruebas manuales con Repeater/Intruder.

Dentro de `web/` tienes:

- **Scanners** (`web/toolkit.md`, `web/apps/toolkit.md`): cada tabla incluye qué pruebas hice (injection, auth, uploads) y cómo guardé los resultados.
- **Proxies** (`web/proxies/`): explico qué scripts activé y qué extensiones usé.
- **Apps vulnerables** (`web/apps/`): dejo notas de versiones, cómo restauro los contenedores y qué nuevos retos completé.

Cuando algo da error (por ejemplo, Burp no intercepta HTTPS porque falta mi CA), lo anoto también para no repetirlo. El objetivo es que cualquier persona pueda replicar la auditoría copiando fechas, comandos y archivos de salida.

## Comandos utilizados
- `docker run -d --name juice-shop -p 3000:3000 bkimminich/juice-shop` para garantizar un entorno limpio y documentar el `score.json` antes/después.
- `zap-baseline.py -t http://localhost:3000 -r reports/zap/baseline.html` para tener una línea base antes de las pruebas manuales.
- `ffuf -w /usr/share/wordlists/dirb/common.txt -u http://localhost:3000/FUZZ` para detectar rutas ocultas y registrar las respuestas 200/403.

## Técnicas aplicadas
- Escaneo combinado (Nikto + sqlmap): primero detecto cabeceras inseguras y después uso SQLMap para confirmar inyecciones.
- Probar proxies con scripts de autenticación (Burp macros) para validar flujos login y evitar bloqueos por rate-limits.
- Revertir contenedores (`docker rm -f` + `docker run`) tras cada sesión para no arrastrar cookies/CSRF tokens.

## Recomendaciones personales
- Siempre documenta qué endpoints exactos probaste y qué payload devolvió error 500; facilita reproducir fallos en equipos de desarrollo.
- Guarda la CA de Burp/ZAP en `web/proxies/ca/` junto al README para no olvidarla en futuras instalaciones.
- Si ffuf falla porque la app responde con 302, agrega `-s -mc 200,403` y guarda los logs en `web/apps/ffuf/`.