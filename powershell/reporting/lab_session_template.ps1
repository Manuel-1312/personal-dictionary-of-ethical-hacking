param([string]$Output = 'lab-session.md', [string]$Title = 'Nueva sesión de lab')
$content = @"
# $Title

- Fecha:
- Objetivo:
- Alcance:
- Entorno:

## Preparación
- Snapshot:
- Herramientas:

## Ejecución
- Pasos:
- Hallazgos:

## Evidencias
- Archivos:
- Capturas:
- Logs:

## Cierre
- Limpieza:
- Mitigación:
- Notas:
"@
Set-Content -Encoding UTF8 -Path $Output -Value $content
Write-Host "Plantilla creada en $Output"
