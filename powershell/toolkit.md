# Toolkit - PowerShell ⚡

| Script | Subcategoría | Qué hace | Comando de ejemplo |
| --- | --- | --- | --- |
| `system/system_report.ps1` | `system/` | Resumen general del equipo | `pwsh -File powershell/system/system_report.ps1` |
| `system/process_snapshot.ps1` | `system/` | Snapshot de procesos a CSV | `pwsh -File powershell/system/process_snapshot.ps1 -Output reports/processes.csv` |
| `system/service_report.ps1` | `system/` | Exporta servicios del sistema | `pwsh -File powershell/system/service_report.ps1 -Output reports/services.csv` |
| `system/scheduled_tasks_export.ps1` | `system/` | Exporta tareas programadas | `pwsh -File powershell/system/scheduled_tasks_export.ps1 -Output reports/tasks.json` |
| `system/startup_audit.ps1` | `system/` | Revisa elementos de arranque | `pwsh -File powershell/system/startup_audit.ps1 -Output reports/startup.csv` |
| `system/env_snapshot.ps1` | `system/` | Exporta variables de entorno | `pwsh -File powershell/system/env_snapshot.ps1 -Output reports/env.csv` |
| `system/installed_software_report.ps1` | `system/` | Exporta software instalado | `pwsh -File powershell/system/installed_software_report.ps1 -Output reports/software.csv` |
| `system/list_local_users.ps1` | `system/` | Lista usuarios locales | `pwsh -File powershell/system/list_local_users.ps1 -Output reports/users.csv` |
| `files/desktop_inventory.ps1` | `files/` | Inventario del escritorio | `pwsh -File powershell/files/desktop_inventory.ps1 -Output reports/desktop.csv` |
| `files/large_files_finder.ps1` | `files/` | Busca archivos grandes | `pwsh -File powershell/files/large_files_finder.ps1 -Path $HOME -MinMb 100` |
| `files/extension_summary.ps1` | `files/` | Resume extensiones por carpeta | `pwsh -File powershell/files/extension_summary.ps1 -Path $HOME\Downloads` |
| `files/duplicate_name_report.ps1` | `files/` | Encuentra nombres repetidos | `pwsh -File powershell/files/duplicate_name_report.ps1 -Path $HOME` |
| `files/recent_files_report.ps1` | `files/` | Exporta archivos modificados recientemente | `pwsh -File powershell/files/recent_files_report.ps1 -Path $HOME -Days 3 -Output reports/recent.csv` |
| `files/hash_inventory.ps1` | `files/` | Calcula hashes SHA256 de archivos | `pwsh -File powershell/files/hash_inventory.ps1 -Path $HOME\Desktop -Output reports/hashes.csv` |
| `files/folder_size_report.ps1` | `files/` | Resume tamaños por carpeta | `pwsh -File powershell/files/folder_size_report.ps1 -Path $HOME` |
| `network/local_network_snapshot.ps1` | `network/` | Foto rápida de la red local | `pwsh -File powershell/network/local_network_snapshot.ps1 -Output reports/network.json` |
| `network/net_connections_report.ps1` | `network/` | Exporta conexiones activas | `pwsh -File powershell/network/net_connections_report.ps1 -Output reports/connections.csv` |
| `network/ping_sweep.ps1` | `network/` | Barrido simple por ping | `pwsh -File powershell/network/ping_sweep.ps1 -Base 192.168.1 -Start 1 -End 20` |
| `network/dns_cache_report.ps1` | `network/` | Exporta la caché DNS | `pwsh -File powershell/network/dns_cache_report.ps1 -Output reports/dns.csv` |
| `network/port_check_list.ps1` | `network/` | Comprueba hosts y puertos | `pwsh -File powershell/network/port_check_list.ps1 -Hosts 127.0.0.1,192.168.1.1 -Ports 80,443,3389` |
| `network/adapter_report.ps1` | `network/` | Exporta adaptadores de red | `pwsh -File powershell/network/adapter_report.ps1 -Output reports/adapters.csv` |
| `network/route_table_export.ps1` | `network/` | Exporta la tabla de rutas | `pwsh -File powershell/network/route_table_export.ps1 -Output reports/routes.csv` |
| `reporting/markdown_table_from_csv.ps1` | `reporting/` | Convierte CSV a tabla Markdown | `pwsh -File powershell/reporting/markdown_table_from_csv.ps1 -Input data.csv -Output table.md` |
| `reporting/json_to_markdown.ps1` | `reporting/` | Convierte JSON a Markdown simple | `pwsh -File powershell/reporting/json_to_markdown.ps1 -Input data.json -Output data.md` |
| `reporting/lab_session_template.ps1` | `reporting/` | Crea plantilla Markdown de sesión | `pwsh -File powershell/reporting/lab_session_template.ps1 -Output session.md -Title "Lab web"` |
| `reporting/csv_summary_card.ps1` | `reporting/` | Resumen corto de un CSV | `pwsh -File powershell/reporting/csv_summary_card.ps1 -Input reports/software.csv` |
| `reporting/directory_markdown_index.ps1` | `reporting/` | Índice Markdown de un directorio | `pwsh -File powershell/reporting/directory_markdown_index.ps1 -Path . -Output index.md` |
| `fun/ascii_status_card.ps1` | `fun/` | Tarjeta ASCII de estado | `pwsh -File powershell/fun/ascii_status_card.ps1 -Title LAB -Status ACTIVE` |
| `fun/random_lab_name.ps1` | `fun/` | Nombres aleatorios para labs | `pwsh -File powershell/fun/random_lab_name.ps1 -Count 5` |
| `fun/matrix_console.ps1` | `fun/` | Efecto matrix en consola | `pwsh -File powershell/fun/matrix_console.ps1 -Lines 40 -Width 60` |
| `fun/fake_update_screen.ps1` | `fun/` | Simula una pantalla de actualización | `pwsh -File powershell/fun/fake_update_screen.ps1 -Steps 12` |
| `fun/rainbow_table.ps1` | `fun/` | Texto con colores arcoíris | `pwsh -File powershell/fun/rainbow_table.ps1 -Text "LAB ACTIVE"` |
| `fun/lab_countdown.ps1` | `fun/` | Cuenta atrás para arrancar una sesión | `pwsh -File powershell/fun/lab_countdown.ps1 -Seconds 5` |
