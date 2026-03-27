# Toolkit - PowerShell ⚡

| Script | Subcategoría | Qué hace | Comando de ejemplo |
| --- | --- | --- | --- |
| `system/system_report.ps1` | `system/` | Resumen general del equipo | `pwsh -File powershell/system/system_report.ps1` |
| `system/process_snapshot.ps1` | `system/` | Snapshot de procesos a CSV | `pwsh -File powershell/system/process_snapshot.ps1 -Output reports/processes.csv` |
| `system/service_report.ps1` | `system/` | Exporta servicios del sistema | `pwsh -File powershell/system/service_report.ps1 -Output reports/services.csv` |
| `system/scheduled_tasks_export.ps1` | `system/` | Exporta tareas programadas | `pwsh -File powershell/system/scheduled_tasks_export.ps1 -Output reports/tasks.json` |
| `files/desktop_inventory.ps1` | `files/` | Inventario del escritorio | `pwsh -File powershell/files/desktop_inventory.ps1 -Output reports/desktop.csv` |
| `files/large_files_finder.ps1` | `files/` | Busca archivos grandes | `pwsh -File powershell/files/large_files_finder.ps1 -Path $HOME -MinMb 100` |
| `files/extension_summary.ps1` | `files/` | Resume extensiones por carpeta | `pwsh -File powershell/files/extension_summary.ps1 -Path $HOME\Downloads` |
| `network/local_network_snapshot.ps1` | `network/` | Foto rápida de la red local | `pwsh -File powershell/network/local_network_snapshot.ps1 -Output reports/network.json` |
| `network/net_connections_report.ps1` | `network/` | Exporta conexiones activas | `pwsh -File powershell/network/net_connections_report.ps1 -Output reports/connections.csv` |
| `fun/ascii_status_card.ps1` | `fun/` | Tarjeta ASCII de estado | `pwsh -File powershell/fun/ascii_status_card.ps1 -Title LAB -Status ACTIVE` |
| `fun/random_lab_name.ps1` | `fun/` | Nombres aleatorios para labs | `pwsh -File powershell/fun/random_lab_name.ps1 -Count 5` |
| `reporting/markdown_table_from_csv.ps1` | `reporting/` | Convierte CSV a tabla Markdown | `pwsh -File powershell/reporting/markdown_table_from_csv.ps1 -Input data.csv -Output table.md` |
