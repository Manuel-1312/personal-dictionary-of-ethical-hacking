# 🖥️ Hacking Toolbox App

🚀 Esta carpeta contiene el launcher de escritorio para el repositorio. La idea no es
reemplazar el repo, sino usarlo como **backend**:

- 📖 Lee categorías y scripts desde `toolkit.md`
- 📝 Muestra descripción y comando de ejemplo
- ▶️ Permite ejecutar scripts desde una interfaz
- 🖥️ Captura la salida en una consola simple

> [!NOTE]
> El `.exe` está pensado para vivir junto al repositorio o dentro de él, usando sus
> carpetas reales como motor.

---

## 🎯 Objetivo

Convertir la biblioteca en una aplicación `.exe` sin romper la estructura del proyecto.

---

## 🔧 Enfoque técnico

- GUI con `tkinter` (ligera, sin dependencia externa para la interfaz)
- Lectura de `toolkit.md` como fuente de catálogo
- Ejecución controlada de scripts Python y PowerShell
- Estado local para favoritos e historial
- Detección automática del repo cuando corre como `.exe`
- Fallbacks de ejecución para Windows (`python` / `py -3`, `pwsh` / `powershell`)
- Empaquetado a `.exe` con `PyInstaller`

---

## ✨ Qué está mejor ahora

La interfaz ya no se siente tan de prototipo:

- 📐 Layout en paneles más claro
- 📋 Cabecera y textos de contexto
- 🔍 Caja de detalle más legible
- 🎨 Consola de salida con mejor contraste
- 📜 Historial más visible
- ⭐ Favoritos mejor integrados
- 🖱️ Doble clic para ejecutar

---

## 📂 Archivos principales

- `main.py` → arranque de la app
- `services/registry.py` → descubre scripts desde el repo
- `services/runner.py` → ejecuta scripts y devuelve salida
- `services/state.py` → guarda favoritos e historial local
- `services/paths.py` → detecta la ruta real del repo
- `build_exe.ps1` → empaqueta el launcher a `.exe`

> [!TIP]
> Para generar el ejecutable, usa `build_exe.ps1` desde PowerShell. Asegúrate de tener
> PyInstaller instalado y de ejecutar el script desde la raíz del repositorio.

---

*📂 Volver al [índice principal](../README.md)*
