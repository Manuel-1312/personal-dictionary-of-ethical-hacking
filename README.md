

# 🛡️ Personal Dictionary of Ethical Hacking

[![Ethical Lab](https://img.shields.io/badge/Ethical-Lab-blueviolet?logo=shield&logoColor=white)](README.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Code of Conduct](https://img.shields.io/badge/Code%20of%20Conduct-Active-green)](CODE_OF_CONDUCT.md)
[![Quality Checks](https://img.shields.io/badge/CI-MarkdownLint%20%2B%20Links-informational)](/.github/workflows/face3-quality.yml)

> **Autor:** Manuel Sánchez Brito · [LinkedIn](https://www.linkedin.com/in/manuel-sanchez-brito)

**Biblioteca curada de herramientas, scripts y documentación para aprender hacking ético de forma responsable.** Todo lo que encuentras aquí está pensado para usarse **exclusivamente en entornos controlados** y con autorización explícita.

---

## ✨ Características principales

| Característica | Descripción |
| --- | --- |
| 📚 **Diccionario de conceptos** | Definiciones claras con ejemplos prácticos para cada área de seguridad. |
| 🐍 **+25 scripts Python** | Parsers, forensics, IOCs, reporting — listos para usar con pocas dependencias. |
| 💻 **+49 scripts PowerShell** | Inventario, red, sistema y reporting para Windows sin dependencias externas. |
| 🖥️ **App de escritorio** | Launcher con GUI (Tkinter) para ejecutar scripts desde una interfaz visual. |
| 📋 **Cheat sheets** | Versión rápida y extendida con comandos organizados por categoría. |
| 🔄 **CI/CD integrado** | MarkdownLint + verificación de enlaces automática en cada push/PR. |

---

## 🚀 Instalación y primeros pasos

```bash
# 1. Clona el repositorio
git clone https://github.com/Manuel-1312/personal-dictionary-of-ethical-hacking.git
cd personal-dictionary-of-ethical-hacking

# 2. (Opcional) Instala dependencias Python si vas a usar los scripts
pip install -r python/requirements.txt

# 3. Explora la estructura
ls -la
```

### Requisitos previos

- **Python 3.9+** para los scripts de `python/` y `fun-scripts/`
- **PowerShell 5.1+** o **pwsh 7+** para los scripts de `powershell/`
- **Entorno aislado** (VM, WSL, contenedor Docker) — nunca ejecutes en producción

### Uso rápido

```bash
# Generar hashes de evidencia
python python/forensics/hash_manifest.py -i ./evidencia/ -o hashes.csv

# Extraer IOCs de un archivo de texto
python python/forensics/ioc_extractor.py -i sospechoso.txt -o iocs.csv

# Parsear logs de Zeek/Suricata a CSV
python python/parsers/log_parser.py -i conn.log -o conexiones.csv

# Comparar subdominios entre dos escaneos
python python/recon/subdomain_diff.py --old antes.txt --new despues.txt -o diff.md

# Inventario rápido del sistema Windows
pwsh -File powershell/system/system_report.ps1

# Barrido de ping en la red local
pwsh -File powershell/network/ping_sweep.ps1 -Base 192.168.1 -Start 1 -End 254
```

---

## 🗂️ Estructura del repositorio

```text
📦 personal-dictionary-of-ethical-hacking/
├── 📂 app/                  → Launcher GUI de escritorio (Tkinter + PyInstaller)
├── 📂 automation/            → Orquestación, snapshots y reporting automatizado
│   ├── orchestration/        → Pipelines con Ansible
│   └── reporting/            → Plantillas y conversores de informes
├── 📂 conceptos/             → Diccionario de términos de seguridad
├── 📂 defense/               → Monitoreo, hunting e incident response
│   ├── monitoring/           → Security Onion, Zeek, Suricata, Wazuh
│   └── incident_response/    → Contención y respuesta a incidentes
├── 📂 evasion/               → Técnicas de evasión controlada + mitigaciones
├── 📂 exploitation/          → Validación controlada de hallazgos en laboratorio
│   ├── frameworks/           → Metasploit, Empire, consolas
│   ├── web_exploitation/     → SQLi, XSS, endpoints vulnerables
│   ├── active_directory/     → Dominios AD de lab, BloodHound
│   ├── privilege_escalation/ → Escalada Linux/Windows
│   ├── post_exploitation/    → Artefactos, limpieza y cierre
│   └── notes/                → Plantillas reutilizables de casos
├── 📂 forensics/             → Análisis forense (disco y memoria)
├── 📂 fun-scripts/           → Scripts creativos: banners, generadores, humor
├── 📂 network_scan/          → Host discovery y vulnerability assessment
├── 📂 osint/                 → Investigación de fuentes abiertas
├── 📂 powershell/            → 49 scripts para Windows
│   ├── system/               → Inventario, procesos, servicios, software
│   ├── files/                → Hashes, duplicados, tamaños
│   ├── network/              → Conexiones, firewall, WiFi, ping sweep
│   ├── reporting/            → Conversores CSV/JSON → Markdown/HTML
│   └── fun/                  → ASCII art, matrix, countdowns
├── 📂 python/                → 25 utilidades organizadas por subcategoría
│   ├── parsers/              → Zeek, masscan, nmap → CSV
│   ├── forensics/            → Hashes, IOCs, PCAPs, cadena de custodia
│   ├── web/                  → Cabeceras HTTP, fuzzing, screenshots
│   ├── recon/                → Diff de subdominios
│   ├── reporting/            → Nmap XML → Markdown, CSV → tablas
│   └── ad/                   → Notas de Active Directory
├── 📂 recon/                 → Reconocimiento pasivo y activo
├── 📂 web/                   → Proxies, escáneres y labs web
├── 📂 wifi/                  → Auditorías inalámbricas
├── 📄 CHEAT_SHEETS.md        → Referencia rápida de comandos
├── 📄 CHEAT_SHEETS_EXT.md    → Guía extendida con contexto y técnicas
├── 📄 CATALOG.md             → Índice viviente de todas las secciones
├── 📄 CHANGELOG.md           → Registro de cambios del proyecto
├── 📄 CONTRIBUTING.md        → Guía para contribuir
├── 📄 CODE_OF_CONDUCT.md     → Compromiso ético
└── 📄 SECURITY.md            → Política de divulgación responsable
```

> 💡 Cada carpeta incluye un `toolkit.md` con herramientas recomendadas y ejemplos de uso responsable.

---

## 🔗 Navegación rápida

| Recurso | Para qué sirve |
| --- | --- |
| [conceptos/diccionario.md](conceptos/diccionario.md) | Diccionario de términos explicados de forma sencilla |
| [CHEAT_SHEETS.md](CHEAT_SHEETS.md) | Comandos esenciales por categoría (formato rápido) |
| [CHEAT_SHEETS_EXT.md](CHEAT_SHEETS_EXT.md) | Guía extendida con técnicas, recursos y plantillas |
| [CATALOG.md](CATALOG.md) | Índice completo del repositorio con estado actual |
| [python/ROADMAP.md](python/ROADMAP.md) | Hoja de ruta para nuevos scripts Python |
| [python/DEPENDENCIES.md](python/DEPENDENCIES.md) | Dependencias detalladas por script |

---

## 🖥️ App de escritorio (Launcher)

El repositorio incluye una app en `app/` que funciona como interfaz visual para lanzar scripts.

**Funcionalidades:**

- Explora scripts por categoría (Python, PowerShell, Fun Scripts)
- Muestra descripción, ruta y ejemplo de cada script
- Ejecuta directamente desde la interfaz con argumentos personalizados
- Guarda favoritos e historial de ejecuciones
- Se puede empaquetar como `.exe` con PyInstaller

```bash
# Ejecutar directamente
cd app && python main.py

# Compilar como ejecutable Windows
pwsh -File app/build_exe.ps1
# El binario queda en dist/HackingToolbox.exe
```

---

## 🧭 Recursos externos recomendados

- **OWASP:** [docs.owasp.org](https://docs.owasp.org/) · [CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)
- **Comunidades:** [r/netsecstudents](https://www.reddit.com/r/netsecstudents/)
- **Formación:** [SANS Courses](https://www.sans.org/cyber-security-courses/) · [Cybrary](https://www.cybrary.it/)

---

## 📝 Buenas prácticas

1. **Aislamiento**: usa snapshots, redes privadas y desconecta del entorno real.
2. **Documentación**: registra comandos, resultados y hallazgos en cada sesión.
3. **Ética**: trabaja solo sobre activos autorizados. Nunca reutilices exploits fuera del laboratorio.
4. **Calidad**: todos los merges pasan por CI (MarkdownLint + link check) antes de llegar a `main`.
5. **Compartir**: cita fuentes originales y menciona el uso educativo al añadir recursos.

---

## 🤝 Contribuir

¿Quieres aportar una herramienta, tutorial o plantilla? Lee la [guía de contribución](CONTRIBUTING.md), respeta el [Código de Conducta](CODE_OF_CONDUCT.md) y usa las plantillas de [issues](.github/ISSUE_TEMPLATE/) y [pull requests](PULL_REQUEST_TEMPLATE.md).

## 🛡️ Seguridad

¿Detectaste un fallo? Consulta [SECURITY.md](SECURITY.md) para reportar vulnerabilidades de forma responsable.

## 📄 Licencia

Este proyecto se distribuye bajo licencia [MIT](LICENSE). Úsalo con responsabilidad.

