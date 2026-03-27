


[![Ethical Lab](https://img.shields.io/badge/Ethical-Lab-blueviolet?logo=shield&logoColor=white)](README.md)

**Autor:** Manuel Sánchez Brito · [LinkedIn](https://www.linkedin.com/in/manuel-sanchez-brito)

## 🎯 Propósito
Este repositorio organiza herramientas de código abierto y documentación enfocada en aprendizaje ético: todo lo que encuentres aquí está pensado para usarse **en entornos controlados**, con alcance autorizado. El objetivo es ayudar a estudiantes y profesionales a encontrar colecciones útiles sin tener que buscar en cientos de repositorios dispersos.

🏅 **Portada**: un solo lugar con estructura clara, badges y recursos vetados para prácticas responsables y compartidas.

## 🚀 Quick start
1. Clona el repositorio y crea tu entorno (puede ser WSL, VM o contenedor).
2. Lee `README.md` para orientarte sobre la estructura.
3. Consulta los `toolkit.md` de cada carpeta para ver herramientas recomendadas.
5. Siempre mantén el entorno aislado y sigue el código de conducta.

## 🧭 Sección de recursos
- **Documentación:** https://docs.owasp.org/ (OWASP Guides) y https://www.lvh.io/ (laboratorios vulnerables).
- **Comunidades:** https://www.reddit.com/r/netsecstudents/ y https://www.twitch.tv/directory/game/Cybersecurity.
- **Repositorios de referencia:** https://github.com/OWASP/securing-devops y https://github.com/OWASP/CheatSheetSeries.
- **Boletines y cursos:** https://www.sans.org/cyber-security-courses/ y https://www.cybrary.it/.

## 🗂️ Estructura del repositorio
- `wifi/` – herramientas inalámbricas (puede tener subcarpetas como `captura/`, `auditorias/`).
- `web/` – escaneos web, aplicaciones vulnerables, proxies y fuzzers.
- `network_scan/` – discovery y fingerprinting.
- `recon/` – reconocimiento pasivo y activo (subcarpetas en `passive/` y `active/`).
- `automation/` – scripts, playbooks y reporting (tiene `orchestration/` y `reporting/`).
- `python/` – utilidades propias en Python para parsear logs, normalizar outputs, inventariar servicios web, generar manifiestos de hashes y extraer IOCs; mira los comandos de `python/toolkit.md` para ejemplos claros.
- `defense/` – monitoreo, detección y respuesta (con `monitoring/` e `incident_response/`).
- `exploitation/` – validación de hallazgos en laboratorio, con subcarpetas `frameworks/`, `web_exploitation/`, `active_directory/`, `privilege_escalation/`, `post_exploitation/` y `notes/` para documentar casos y evidencias.
- `evasion/`, `osint/`, `forensics/` – técnicas de evasión controlada, investigación OSINT y análisis forense.
- Cada carpeta incluye un `toolkit.md` con referencias oficiales y consejos de uso responsable.

## 🎯 Foco actual: explotación de laboratorio
La sección `exploitation/` ya forma parte del núcleo del repositorio y está pensada para documentar la **validación controlada de hallazgos** sin perder contexto ni evidencia.

### Subcategorías integradas
- `exploitation/frameworks/` → frameworks, RPC, consolas y validación guiada.
- `exploitation/web_exploitation/` → fallos web reproducidos con requests, endpoints y mitigación.
- `exploitation/active_directory/` → dominios AD de laboratorio, rutas de privilegio y notas de hardening.
- `exploitation/privilege_escalation/` → escalada local en Linux/Windows de laboratorio.
- `exploitation/post_exploitation/` → impacto controlado, artefactos, limpieza y cierre.
- `exploitation/notes/` → plantillas reutilizables para casos, cronología y evidencias.

### Cómo se conecta con el resto del repo
- Se alimenta de hallazgos previos en `web/`, `network_scan/` y `recon/`.
- Genera artefactos y notas que luego encajan en `defense/` y `forensics/`.
- Se apoya en `python/` para hashes, extracción de IOCs y reporting auxiliar.

## 📁 Otros archivos útiles
- `lab-notes.md` (puedes crearlo) para registrar qué herramienta usas y qué aprendiste.
- `toolkit.md` en cada carpeta, explica cómo catalogar nuevas herramientas.
- Añade tu propia subcarpeta si quieres dividir un área en más detalle (por ejemplo `web/proxies/`).

## 📝 Buenas prácticas
1. **Aislado y seguro**: usa snapshots, redes privadas y desconecta del entorno real si es necesario.
2. **Documentación**: registra comandos clave, resultados y hallazgos en `lab-notes.md` o dentro de cada carpeta.
3. **Ética y alcance**: trabaja solo sobre activos autorizados y nunca reutilices exploits fuera del laboratorio.
4. **Compartir es educar**: cuando agregues un recurso, cita la fuente original y menciona el uso educativo.
5. **Lee el CODE_OF_CONDUCT** antes de contribuir; define claramente el compromiso ético y el alcance permitido.

## 🧠 Contribuciones
¿Quieres aportar una herramienta, tutorial o plantilla? Haz un fork, agrega tu contenido siguiendo esta estructura y abre un pull request. Mantén claro que todo aquí es para uso ético y añade referencias oficiales siempre que sea posible. Este proyecto se distribuye bajo licencia MIT (`LICENSE`).

## 🐍 Crecimiento de la librería Python
La carpeta `python/` ya no es solo un rincón de scripts sueltos: ahora está organizada por subcategorías y se está convirtiendo en una caja de utilidades reutilizable para reporting, inventario, extracción de IOCs, hashes y automatización ligera.

Para planificar su crecimiento sin perder coherencia, el repo incluye `python/ROADMAP.md`, una hoja de ruta con ideas priorizadas para nuevos helpers orientados a:
- `network_scan/`
- `web/`
- `recon/`
- `defense/`
- `forensics/`
- `exploitation/`

Además, la fase 2 ya ha ampliado la librería con nuevas subcategorías (`recon/`, `reporting/`, `ad/`) y scripts enfocados a diff de subdominios, reporting de Nmap, bundling de notas y documentación de casos AD.

La fase 3 añade una capa más práctica para forense y evidencia: resumen de PCAPs, indexado de evidencias, enriquecimiento de IOCs y reporting ligero de resultados de fuzzing web.

La fase 4 remata esa línea con más utilidades de conversión y trazabilidad: parser de Masscan a CSV, manifiestos de capturas web, conversión de CSV a Markdown y plantillas de cadena de custodia.

Y para no perder de vista qué necesita cada helper, la carpeta ya incluye `python/DEPENDENCIES.md`, donde se separan dependencias de `pip` y herramientas externas del sistema como `tshark`.

## 📘 Cheat Sheets & Referencias rápidas
- `CHEAT_SHEETS.md`: resumen ágil con comandos y tips esenciales por categoría.
- `CHEAT_SHEETS_EXT.md`: guía extendida con técnicas, comandos, scripts, recursos premium y plantillas adjuntas para cada bloque.
- Usa estos documentos como referencia previa a una sesión o para entrenar a un compañero: están listos para imprimirse o compartir en la sala de SOC.


