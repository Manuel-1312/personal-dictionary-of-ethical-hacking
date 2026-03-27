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
- empaquetado a `.exe` con `PyInstaller`

## Archivos principales
- `main.py` → arranque de la app
- `services/registry.py` → descubre scripts desde el repo
- `services/runner.py` → ejecuta scripts y devuelve salida
- `services/state.py` → guarda favoritos e historial local
- `build_exe.ps1` → empaqueta el launcher a `.exe`

## Mejoras de esta fase
La app ya tiene una base más utilizable de verdad:
- buscador por categoría y texto
- panel de detalle del script
- caja para argumentos extra
- botón para usar el comando de ejemplo como base
- botón para copiar comando
- favoritos
- historial local de ejecuciones
- consola con stdout/stderr y código de salida

## Nota
El `.exe` está pensado para vivir junto al repositorio o dentro de él, usando sus carpetas reales como motor.
