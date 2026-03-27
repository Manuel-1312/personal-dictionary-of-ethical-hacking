


[![Ethical Lab](https://img.shields.io/badge/Ethical-Lab-blueviolet?logo=shield&logoColor=white)](README.md)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Code of Conduct](https://img.shields.io/badge/Code%20of%20Conduct-Active-green)](CODE_OF_CONDUCT.md)

**Autor:** Manuel Sánchez Brito · [LinkedIn](https://www.linkedin.com/in/manuel-sanchez-brito)

## 🎯 Propósito
Este repositorio organiza herramientas de código abierto y documentación enfocada en aprendizaje ético: todo lo que encuentres aquí está pensado para usarse **en entornos controlados**, con alcance autorizado. El objetivo es ayudar a estudiantes y profesionales a encontrar colecciones útiles sin tener que buscar en cientos de repositorios dispersos.

🏅 **Portada**: un solo lugar con estructura clara, badges y recursos vetados para prácticas responsables y compartidas.

## 🚀 Quick start
1. Clona el repositorio y crea tu entorno (puede ser WSL, VM o contenedor).
2. Lee `README.md` para orientarte sobre la estructura.
3. Consulta los `toolkit.md` de cada carpeta para ver herramientas recomendadas.
4. Siempre mantén el entorno aislado y sigue el código de conducta.

## 🔗 Enlaces rápidos
| Recurso | Descripción |
| --- | --- |
| [README.md](README.md) | Esta guía vive aquí; incluye acceso directo a todas las carpetas principales. |
| [conceptos/diccionario.md](conceptos/diccionario.md) | Diccionario de términos tecnológicos explicado de forma sencilla. |
| [wifi/toolkit.md](wifi/toolkit.md) | Colección en profundidad para auditorías inalámbricas. |
| [web/toolkit.md](web/toolkit.md) | Referencias a proxies, fuzzers y laboratorios web. |
| [defense/toolkit.md](defense/toolkit.md) | Sensores, hunting y dashboards; ideal si trabajas en detección. |
| [automation/reporting/toolkit.md](automation/reporting/toolkit.md) | Plantillas y scripts para automatizar informes. |

## 🧭 Sección de recursos
- **Documentación:** https://docs.owasp.org/ (OWASP Guides) y https://www.lvh.io/ (laboratorios vulnerables).
- **Comunidades:** https://www.reddit.com/r/netsecstudents/ y https://www.twitch.tv/directory/game/Cybersecurity.
- **Repositorios de referencia:** https://github.com/OWASP/securing-devops y https://github.com/OWASP/CheatSheetSeries.
- **Boletines y cursos:** https://www.sans.org/cyber-security-courses/ y https://www.cybrary.it/.

## 🗂️ Estructura del repositorio
- [wifi/](./wifi/) – herramientas inalámbricas.
  - [wifi/auditorias/](./wifi/auditorias/) – carpetas con ensayos de auditoría y registros de pruebas.
  - [wifi/captura/](./wifi/captura/) – capturas de paquetes, handshakes y scripts de análisis.
- [web/](./web/) – escaneos y laboratorios web (incluye `apps/`, `proxies/`).
- [network_scan/](./network_scan/) – discovery y fingerprinting.
  - [network_scan/host_discovery/](./network_scan/host_discovery/) – listas, scripts y resultados de descubrimiento de hosts.
  - [network_scan/vuln_assessment/](./network_scan/vuln_assessment/) – herramientas para correlación de CVE y hallazgos de vulnerabilidades.
- [recon/](./recon/) – reconocimiento pasivo y activo.
  - [recon/passive/](./recon/passive/) – técnicas y toolkits pasivos.
  - [recon/active/](./recon/active/) – técnicas de escaneo activo.
- [automation/](./automation/) – scripts, playbooks y reporting.
  - [automation/orchestration/](./automation/orchestration/) – orquestación de pipelines.
  - [automation/reporting/](./automation/reporting/) – plantillas y templates de informes.
- [python/](./python/) – utilidades Python (reporting, hash, parsing, IOCs).
- [powershell/](./powershell/) – automatización Windows.
  - [powershell/system/](./powershell/system/)
  - [powershell/files/](./powershell/files/)
  - [powershell/network/](./powershell/network/)
  - [powershell/reporting/](./powershell/reporting/)
  - [powershell/fun/](./powershell/fun/)
- [defense/](./defense/) – monitoreo, detección y respuesta.
  - [defense/monitoring/](./defense/monitoring/)
  - [defense/incident_response/](./defense/incident_response/)
  - [defense/thehive/](./defense/thehive/) – casos y automatización.
- [exploitation/](./exploitation/) – validación controlada de hallazgos.
  - [exploitation/frameworks/](./exploitation/frameworks/)
  - [exploitation/web_exploitation/](./exploitation/web_exploitation/)
  - [exploitation/active_directory/](./exploitation/active_directory/)
  - [exploitation/privilege_escalation/](./exploitation/privilege_escalation/)
  - [exploitation/post_exploitation/](./exploitation/post_exploitation/)
  - [exploitation/notes/](./exploitation/notes/)
- [fun-scripts/](./fun-scripts/) – scripts creativos y utilitarios.
- [app/](./app/) – launcher/GUI del repositorio.
- [evasion/](./evasion/) – técnicas de evasión controlada.
- [osint/](./osint/) – investigación de fuentes abiertas.
- [forensics/](./forensics/) – análisis forense integral.
- [conceptos/](./conceptos/) – diccionario de conceptos y recursos explicativos.
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

## 🤝 Cómo contribuir
¿Quieres aportar una herramienta, tutorial o plantilla? Sigue los pasos de [CONTRIBUTING.md](CONTRIBUTING.md), registra cambios en los issues con los templates (`.github/ISSUE_TEMPLATE/`) y rellena [PULL_REQUEST_TEMPLATE.md](PULL_REQUEST_TEMPLATE.md) cuando envíes tu PR. Mantén claro que todo aquí es para uso ético, respeta el [Code of Conduct](CODE_OF_CONDUCT.md) y enlaza referencias oficiales cuando añadas contenido. Este proyecto se distribuye bajo licencia MIT (`LICENSE`).

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

## 🖥️ Launcher / app `.exe`
El repositorio ya incluye una app de escritorio en `app/` pensada para usar la propia biblioteca como backend.

### Qué hace
- lee categorías y scripts desde los `toolkit.md`
- muestra descripción, ruta y comando de ejemplo
- permite ejecutar scripts Python, PowerShell y `fun-scripts` desde una interfaz
- guarda favoritos e historial local
- puede empaquetarse como `.exe`

### Ruta del ejecutable
Tras compilarla, el binario queda en:
- `dist/HackingToolbox.exe`

### Cómo usarla
1. Abre `HackingToolbox.exe` desde la carpeta `dist/`.
2. Elige una categoría (`Python`, `PowerShell`, `Fun Scripts`).
3. Selecciona un script en la lista.
4. Revisa la descripción y el ejemplo de uso.
5. Si hace falta, añade argumentos extra.
6. Pulsa **Ejecutar** o haz doble clic sobre el script.

### Qué ventaja tiene
No sustituye al repo: lo convierte en una toolbox ejecutable, más cómoda para lanzar scripts y revisar resultados sin ir comando por comando en terminal.

## 📘 Cheat Sheets & Referencias rápidas
- `CHEAT_SHEETS.md`: resumen ágil con comandos y tips esenciales por categoría.
- `CHEAT_SHEETS_EXT.md`: guía extendida con técnicas, comandos, scripts, recursos premium y plantillas adjuntas para cada bloque.
- Usa estos documentos como referencia previa a una sesión o para entrenar a un compañero: están listos para imprimirse o compartir en la sala de SOC.


