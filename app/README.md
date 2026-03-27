# Hacking Toolbox App

Esta carpeta contiene el launcher de escritorio para el repositorio. La idea no es reemplazar el repo, sino usarlo como **backend**:

- lee categorías y scripts desde `toolkit.md`
- muestra descripción y comando de ejemplo
- permite ejecutar scripts desde una interfaz
- captura la salida en una consola simple

## Objetivo
Convertir la biblioteca en una aplicación `.exe` sin romper la estructura del proyecto.

## Enfoque técnico
- GUI con `tkinter` (ligera, sin dependencia externa para la interfaz)
- lectura de `toolkit.md` como fuente de catálogo
- ejecución controlada de scripts Python y PowerShell
- estado local para favoritos e historial
- detección automática del repo cuando corre como `.exe`
- fallbacks de ejecución para Windows (`python` / `py -3`, `pwsh` / `powershell`)
- empaquetado a `.exe` con `PyInstaller`

## Qué está mejor ahora
La interfaz ya no se siente tan de prototipo:
- layout en paneles más claro
- cabecera y textos de contexto
- caja de detalle más legible
- consola de salida con mejor contraste
- historial más visible
- favoritos mejor integrados
- doble clic para ejecutar

## Archivos principales
- `main.py` → arranque de la app
- `services/registry.py` → descubre scripts desde el repo
- `services/runner.py` → ejecuta scripts y devuelve salida
- `services/state.py` → guarda favoritos e historial local
- `services/paths.py` → detecta la ruta real del repo
- `build_exe.ps1` → empaqueta el launcher a `.exe`

## Nota
El `.exe` está pensado para vivir junto al repositorio o dentro de él, usando sus carpetas reales como motor.
