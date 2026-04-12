# Toolkit - Apps Vulnerables 🧪

Documenta cada aplicación vulnerable, su stack y qué retos completaste en el laboratorio.

## Plantilla base
- **Enlace:** referencia oficial.
- **Caso de uso:** propósito de la herramienta.
- **Comando de ejemplo:** comando representativo.
- **Notas útiles:** observaciones clave.
- **Recomendaciones:** consejos de uso.
- **Cuándo usar / cuándo no:** límites y contexto.

## 1. Aplicaciones vulnerables de laboratorio

### OWASP Juice Shop
- **Enlace:** https://github.com/juice-shop/juice-shop
- **Caso de uso:** Aplicación web Node.js/Express con múltiples vulnerabilidades OWASP Top 10.
- **Comando de ejemplo:** `docker run -d --name juice-shop -p 3000:3000 bkimminich/juice-shop`
- **Notas útiles:** Mantén un `score.json` y restauraciones por container; ideal para practicar XSS, SQLi y más.
- **Recomendaciones:** Usa el modo CTF para seguir retos estructurados; documenta vectores y soluciones.
- **Cuándo usarlo:** Práctica de vulnerabilidades web en entorno realista con scoring integrado.
- **Cuándo no:** Para aprender conceptos básicos sin guía; es mejor empezar con DVWA a nivel bajo.

### WebGoat
- **Enlace:** https://github.com/WebGoat/WebGoat
- **Caso de uso:** Plataforma de aprendizaje guiado de vulnerabilidades web en Java/Spring.
- **Comando de ejemplo:** `docker-compose -f web/apps/webgoat-compose.yml up -d`
- **Notas útiles:** Documenta módulos completados y configuraciones de seguridad; tiene lecciones explicativas integradas.
- **Recomendaciones:** Sigue el orden de módulos; anota las soluciones con contexto para revisarlas después.
- **Cuándo usarlo:** Aprendizaje guiado con explicaciones de vulnerabilidades y exploits paso a paso.
- **Cuándo no:** Práctica libre sin guía; Juice Shop o DVWA son mejores para exploración abierta.

### DVWA
- **Enlace:** https://github.com/digininja/DVWA
- **Caso de uso:** Aplicación PHP/MySQL con niveles de dificultad configurables.
- **Comando de ejemplo:** `python3 web/apps/reset-dvwa.py`
- **Notas útiles:** Usa niveles (`low/medium/high`) y guarda scripts de reset para repetir escenarios.
- **Recomendaciones:** Completa cada vulnerabilidad en los tres niveles para entender las defensas aplicadas.
- **Cuándo usarlo:** Práctica controlada de SQLi, XSS, CSRF, LFI con dificultad graduable.
- **Cuándo no:** Entornos expuestos a internet; DVWA no tiene autenticación robusta por defecto.

### Mutillidae II
- **Enlace:** https://github.com/webpwnized/mutillidae
- **Caso de uso:** Aplicación PHP con más de 40 vulnerabilidades y soporte OWASP Top 10.
- **Comando de ejemplo:** `docker run -d -p 80:80 webpwnized/mutillidae:latest`
- **Notas útiles:** Mantén scripts para restaurar DB y documenta módulos explorados; incluye hints por nivel.
- **Recomendaciones:** Usa el menú de hints para guiarte; registra los payloads que funcionan por categoría.
- **Cuándo usarlo:** Cuando quieres variedad de vulnerabilidades más allá de DVWA con pistas integradas.
- **Cuándo no:** Sin reset de DB periódico; el estado acumulado puede confundir los resultados.

### OWASP Broken Web Apps
- **Enlace:** https://github.com/OWASP/OWASPBrokenWebApplications
- **Caso de uso:** Colección de múltiples apps vulnerables en una sola VM.
- **Comando de ejemplo:** `VBoxManage startvm "OWASP BWA" --type headless`
- **Notas útiles:** Anota apps desplegadas y dependencias; incluye WebGoat, DVWA, Mutillidae y más.
- **Recomendaciones:** Usa solo en red aislada; la VM no tiene hardening y expone muchos servicios.
- **Cuándo usarlo:** Cuando quieres acceso a múltiples apps sin desplegar cada una por separado.
- **Cuándo no:** Laboratorios con acceso a red externa; la VM es intencionalmente insegura.

### Juice Shop CTF
- **Enlace:** https://owasp.org/www-project-juice-shop/
- **Caso de uso:** Modo CTF de Juice Shop con scoring y retos estructurados.
- **Comando de ejemplo:** `docker run -d -p 3000:3000 -e CTF_KEY=mysecret bkimminich/juice-shop`
- **Notas útiles:** Documenta retos resueltos y vectores usados; integrable con CTFd para competiciones.
- **Recomendaciones:** Configura `CTF_KEY` y conecta con CTFd para tracking de puntuación grupal.
- **Cuándo usarlo:** Competiciones internas o sesiones de equipo con scoring y retos definidos.
- **Cuándo no:** Práctica libre individual; el modo estándar de Juice Shop es más flexible para aprendizaje.

## Comandos utilizados
- `docker run -d --name juice-shop -p 3000:3000 bkimminich/juice-shop`.
- `docker-compose -f web/apps/webgoat-compose.yml up -d`.
- `python3 web/apps/reset-dvwa.py`.

## Técnicas aplicadas
- Restauración periódica de contenedores para evitar persistencias.
- Anotación de retos y payloads en `web/apps/notes.md`.

## Recomendaciones personales
- Mantén un archivo `web/apps/state.md` con la versión y lecciones pendientes.
- Incluye los comandos de despliegue para cada app en su README correspondiente.
