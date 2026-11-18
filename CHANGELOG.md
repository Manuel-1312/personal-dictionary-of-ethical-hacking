# Changelog

Todos los cambios notables de este proyecto se documentan en este archivo.

El formato sigue las convenciones de [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).
Las versiones se organizan por *Faces* (fases) del proyecto.

## [Sin versión] - En desarrollo

### Añadido

- **CHANGELOG.md**: registro formal de cambios del proyecto.
- **Tests unitarios** para los scripts Python (`tests/`): parsers, forensics, reporting y recon.
- **CI workflow mejorado**: paso de tests Python integrado en el pipeline de calidad.
- **Diccionario ampliado**: nuevos términos en `conceptos/diccionario.md` (Exfiltración, Pivoting, Lateral Movement, etc.).
- **Diccionario: 65 términos nuevos** repartidos por las 14 secciones: AD (SPN, Delegación Kerberos, ADCS/ESC, NTLM Relay, Shadow Credentials, DPAPI), Cripto (Padding Oracle, Length Extension, HMAC, PFS), Cloud (AssumeRole, OIDC Federation, Entra ID) y Red/Web/Malware/Herramientas, entre otras.

### Cambiado

- **README.md** reescrito: estructura más clara, ejemplos de uso, diagrama del repositorio y navegación rápida.
- **CONTRIBUTING.md** ampliado: flujo de trabajo detallado, estándares por tipo de contribución y checklist de verificación.
- **CI workflow** (`face3-quality.yml`): corregido el import roto de `markdown_it_py` → `markdown_it`, mejorada la extracción de enlaces y añadida deduplicación.
- **log_parser.py**: refactorizado para cumplir PEP 8 (espaciado, docstrings, constantes extraídas).
- **inventory_builder.py**: refactorizado con docstrings, tipado, PEP 8 y lógica de origen mejorada (detecta hosts presentes en ambas herramientas).
- **Comentarios humanizados** en scripts clave: explicaciones del *por qué* además del *qué*.

### Corregido

- Import roto en el CI link-check (`import markdown_it_py` → `from markdown_it import MarkdownIt`).
- Extracción de enlaces en CI: ahora busca en tokens inline/children en vez de solo tokens raíz.
- `inventory_builder.py`: el campo Origin ahora detecta correctamente hosts encontrados por ambas herramientas (`both`).
- **Índice del diccionario**: anclas internas (`#-red` → `#red`, etc.) que quedaron rotas al retirar el emoji de las cabeceras.
- **App (launcher)**: `app/services/registry.py` parseaba los `toolkit.md` como tablas Markdown, pero se habían convertido a formato de fichas (`### script` + bullets), así que el catálogo salía vacío y la app no listaba ningún script. Reescrito el parser al formato actual: ahora carga las 80 entradas (Python, PowerShell, Fun Scripts) y todas resuelven a ficheros reales.
- **Scripts Python**: `inventory_builder.py` (`parse_nmap` capturaba la IP con paréntesis `(10.0.0.5)` cuando nmap muestra DNS inverso; ahora la limpia, con test de regresión) y `DEPENDENCIES.md` (corrige las dependencias falsas: `log_parser.py` y `inventory_builder.py` son solo librería estándar, no `pandas`/`xmltodict`).
- **Scripts PowerShell**: `directory_markdown_index.ps1` (string roto `` "- `$rel`" `` que impedía generar el índice), `ping_sweep.ps1` (`Test-Connection -ComputerName` no existe en PowerShell 7; ahora host posicional, válido en 5.1 y 7+), `port_check_list.ps1` (variable automática `$host` → `$targetHost`), 5 scripts de `reporting/` (parámetro `$Input` colisionaba con la variable automática; renombrado a `$Path` con `[Alias('Input')]`), BOM UTF-8 en los 4 ficheros con acentos (mojibake en PS 5.1) y emoji residual en `fake_update_screen.ps1`. PSScriptAnalyzer: 0 avisos salvo `Write-Host` intencional en salidas de consola.
- **Toolkits**: correcciones técnicas en 10 `toolkit.md` — emoji residual (`⬆`) y `<br>` sueltos, herramienta renombrada (`hcxpcaptool` → `hcxpcapngtool`), flujo WiFi actualizado a `hc22000`/`-m 22000`, flag inválido de airgraph (`-g netxml` → `-g CAPR`), binario Wazuh (`agent-control` → `agent_control`), herramienta inexistente (`velocity`), imagen Docker de ZAP obsoleta (`owasp/zap2docker-stable` → `ghcr.io/zaproxy/zaproxy:stable`) y enlace equivocado de Cyber Triage.

## [Face 4] - Anterior a este changelog

### Añadido

- Scripts de conversión: `masscan_to_csv.py`, `web_screenshot_manifest.py`, `csv_to_markdown_table.py`.
- `chain_of_custody_builder.py` para plantillas de cadena de custodia.
- Launcher de escritorio (`app/`) con GUI Tkinter.
- `CHEAT_SHEETS_EXT.md` como guía extendida.
- `COMMUNITY.md` con estrategia de difusión.
- Scripts fun: ASCII generators, fake breach reports, lab utilities.

### Cambiado

- Organización de `python/` en subcategorías (`parsers/`, `web/`, `forensics/`, `recon/`, `reporting/`, `ad/`).
- PowerShell organizado en `system/`, `files/`, `network/`, `reporting/`, `fun/`.
- `exploitation/` expandido con subcategorías completas y plantillas.

## [Face 3] - Calidad automatizada

### Añadido

- GitHub Actions workflow (`face3-quality.yml`) con MarkdownLint y link check.
- `.markdownlint.json` con reglas de formato.
- `pcap_summary.py`, `evidence_indexer.py`, `ioc_enricher.py`.
- `SECURITY.md` con política de divulgación responsable.

## [Face 2] - Expansión de scripts

### Añadido

- Subcategorías de Python: `recon/`, `reporting/`, `ad/`.
- `subdomain_diff.py`, `nmap_xml_to_markdown.py`, `markdown_case_bundler.py`.
- `ad_notes_builder.py` para documentación de laboratorios AD.
- `python/ROADMAP.md` y `python/DEPENDENCIES.md`.

## [Face 1] - Estructura base

### Añadido

- Estructura inicial del repositorio con todas las carpetas principales.
- `README.md`, `CODE_OF_CONDUCT.md`, `LICENSE` (MIT).
- `conceptos/diccionario.md` con definiciones base.
- `CHEAT_SHEETS.md` con comandos por categoría.
- `CATALOG.md` como índice del proyecto.
- Toolkits (`toolkit.md`) en cada carpeta.

---

> [!TIP]
> Cada vez que hagas un cambio relevante, documéntalo aquí antes de hacer merge.
> Un changelog bien mantenido es la memoria del proyecto.
