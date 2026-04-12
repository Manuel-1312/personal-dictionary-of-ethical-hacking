# Toolkit - PowerShell ⚡

Colección de scripts PowerShell para inventario, análisis, reporting y utilidades de laboratorio.

## Plantilla de scripts
- **Subcategoría:** carpeta a la que pertenece.
- **Descripción:** qué hace el script.
- **Comando de ejemplo:** cómo lanzarlo.
- **Notas:** dependencias o advertencias clave.

## 1. system/

### `system_report.ps1`
- **Subcategoría:** `system/`
- **Descripción:** Resumen general del equipo: SO, hardware, uptime y configuración básica.
- **Comando de ejemplo:** `pwsh -File powershell/system/system_report.ps1`

### `process_snapshot.ps1`
- **Subcategoría:** `system/`
- **Descripción:** Snapshot de procesos activos exportado a CSV con PID, nombre y uso de CPU/RAM.
- **Comando de ejemplo:** `pwsh -File powershell/system/process_snapshot.ps1 -Output reports/processes.csv`

### `service_report.ps1`
- **Subcategoría:** `system/`
- **Descripción:** Exporta servicios del sistema con estado, tipo de inicio y ruta del ejecutable.
- **Comando de ejemplo:** `pwsh -File powershell/system/service_report.ps1 -Output reports/services.csv`

### `scheduled_tasks_export.ps1`
- **Subcategoría:** `system/`
- **Descripción:** Exporta tareas programadas con nombre, trigger, acción y estado.
- **Comando de ejemplo:** `pwsh -File powershell/system/scheduled_tasks_export.ps1 -Output reports/tasks.json`

### `startup_audit.ps1`
- **Subcategoría:** `system/`
- **Descripción:** Revisa elementos de arranque del sistema (registro, carpetas de inicio).
- **Comando de ejemplo:** `pwsh -File powershell/system/startup_audit.ps1 -Output reports/startup.csv`

### `env_snapshot.ps1`
- **Subcategoría:** `system/`
- **Descripción:** Exporta variables de entorno del sistema y del usuario actual.
- **Comando de ejemplo:** `pwsh -File powershell/system/env_snapshot.ps1 -Output reports/env.csv`

### `installed_software_report.ps1`
- **Subcategoría:** `system/`
- **Descripción:** Exporta software instalado con nombre, versión y fabricante.
- **Comando de ejemplo:** `pwsh -File powershell/system/installed_software_report.ps1 -Output reports/software.csv`

### `list_local_users.ps1`
- **Subcategoría:** `system/`
- **Descripción:** Lista usuarios locales con nombre, estado y última fecha de inicio de sesión.
- **Comando de ejemplo:** `pwsh -File powershell/system/list_local_users.ps1 -Output reports/users.csv`

### `hotfix_report.ps1`
- **Subcategoría:** `system/`
- **Descripción:** Exporta hotfixes instalados con KB, descripción y fecha de instalación.
- **Comando de ejemplo:** `pwsh -File powershell/system/hotfix_report.ps1 -Output reports/hotfixes.csv`

### `local_groups_report.ps1`
- **Subcategoría:** `system/`
- **Descripción:** Lista grupos locales con nombre y miembros.
- **Comando de ejemplo:** `pwsh -File powershell/system/local_groups_report.ps1 -Output reports/groups.csv`

## 2. files/

### `desktop_inventory.ps1`
- **Subcategoría:** `files/`
- **Descripción:** Inventario de archivos del escritorio con nombre, tamaño y fecha de modificación.
- **Comando de ejemplo:** `pwsh -File powershell/files/desktop_inventory.ps1 -Output reports/desktop.csv`

### `large_files_finder.ps1`
- **Subcategoría:** `files/`
- **Descripción:** Busca archivos por encima de un tamaño mínimo configurable en MB.
- **Comando de ejemplo:** `pwsh -File powershell/files/large_files_finder.ps1 -Path $HOME -MinMb 100`

### `extension_summary.ps1`
- **Subcategoría:** `files/`
- **Descripción:** Resume extensiones de archivo por carpeta con conteo y tamaño total.
- **Comando de ejemplo:** `pwsh -File powershell/files/extension_summary.ps1 -Path $HOME\Downloads`

### `duplicate_name_report.ps1`
- **Subcategoría:** `files/`
- **Descripción:** Encuentra nombres de archivo repetidos en un directorio y sus subdirectorios.
- **Comando de ejemplo:** `pwsh -File powershell/files/duplicate_name_report.ps1 -Path $HOME`

### `recent_files_report.ps1`
- **Subcategoría:** `files/`
- **Descripción:** Exporta archivos modificados en los últimos N días.
- **Comando de ejemplo:** `pwsh -File powershell/files/recent_files_report.ps1 -Path $HOME -Days 3 -Output reports/recent.csv`

### `hash_inventory.ps1`
- **Subcategoría:** `files/`
- **Descripción:** Calcula hashes SHA256 de archivos en un directorio dado.
- **Comando de ejemplo:** `pwsh -File powershell/files/hash_inventory.ps1 -Path $HOME\Desktop -Output reports/hashes.csv`

### `folder_size_report.ps1`
- **Subcategoría:** `files/`
- **Descripción:** Resume el tamaño total por subcarpeta de un directorio.
- **Comando de ejemplo:** `pwsh -File powershell/files/folder_size_report.ps1 -Path $HOME`

### `downloads_inventory.ps1`
- **Subcategoría:** `files/`
- **Descripción:** Inventario de la carpeta Descargas con nombre, extensión y fecha.
- **Comando de ejemplo:** `pwsh -File powershell/files/downloads_inventory.ps1 -Output reports/downloads.csv`

### `top_largest_files.ps1`
- **Subcategoría:** `files/`
- **Descripción:** Lista los N archivos más grandes de un directorio ordenados por tamaño.
- **Comando de ejemplo:** `pwsh -File powershell/files/top_largest_files.ps1 -Path $HOME -Top 25`

## 3. network/

### `local_network_snapshot.ps1`
- **Subcategoría:** `network/`
- **Descripción:** Foto rápida de la red local: interfaces, IPs, gateway y DNS.
- **Comando de ejemplo:** `pwsh -File powershell/network/local_network_snapshot.ps1 -Output reports/network.json`

### `net_connections_report.ps1`
- **Subcategoría:** `network/`
- **Descripción:** Exporta conexiones TCP/UDP activas con PID, estado y dirección remota.
- **Comando de ejemplo:** `pwsh -File powershell/network/net_connections_report.ps1 -Output reports/connections.csv`

### `ping_sweep.ps1`
- **Subcategoría:** `network/`
- **Descripción:** Barrido de ping sobre un rango de IPs configurable.
- **Comando de ejemplo:** `pwsh -File powershell/network/ping_sweep.ps1 -Base 192.168.1 -Start 1 -End 20`

### `dns_cache_report.ps1`
- **Subcategoría:** `network/`
- **Descripción:** Exporta la caché DNS del sistema con nombre, tipo y TTL.
- **Comando de ejemplo:** `pwsh -File powershell/network/dns_cache_report.ps1 -Output reports/dns.csv`

### `port_check_list.ps1`
- **Subcategoría:** `network/`
- **Descripción:** Comprueba conectividad a una lista de hosts y puertos.
- **Comando de ejemplo:** `pwsh -File powershell/network/port_check_list.ps1 -Hosts 127.0.0.1,192.168.1.1 -Ports 80,443,3389`

### `adapter_report.ps1`
- **Subcategoría:** `network/`
- **Descripción:** Exporta adaptadores de red con nombre, estado, MAC e IP.
- **Comando de ejemplo:** `pwsh -File powershell/network/adapter_report.ps1 -Output reports/adapters.csv`

### `route_table_export.ps1`
- **Subcategoría:** `network/`
- **Descripción:** Exporta la tabla de rutas del sistema.
- **Comando de ejemplo:** `pwsh -File powershell/network/route_table_export.ps1 -Output reports/routes.csv`

### `firewall_profile_report.ps1`
- **Subcategoría:** `network/`
- **Descripción:** Exporta perfiles de firewall activos con reglas habilitadas.
- **Comando de ejemplo:** `pwsh -File powershell/network/firewall_profile_report.ps1 -Output reports/firewall.csv`

### `wifi_profiles_list.ps1`
- **Subcategoría:** `network/`
- **Descripción:** Lista perfiles Wi-Fi guardados en el sistema.
- **Comando de ejemplo:** `pwsh -File powershell/network/wifi_profiles_list.ps1`

### `share_report.ps1`
- **Subcategoría:** `network/`
- **Descripción:** Exporta recursos compartidos SMB con nombre, ruta y permisos.
- **Comando de ejemplo:** `pwsh -File powershell/network/share_report.ps1 -Output reports/shares.csv`

## 4. reporting/

### `markdown_table_from_csv.ps1`
- **Subcategoría:** `reporting/`
- **Descripción:** Convierte un CSV a tabla Markdown para incluir en informes.
- **Comando de ejemplo:** `pwsh -File powershell/reporting/markdown_table_from_csv.ps1 -Input data.csv -Output table.md`

### `json_to_markdown.ps1`
- **Subcategoría:** `reporting/`
- **Descripción:** Convierte un JSON a Markdown simple con estructura de lista.
- **Comando de ejemplo:** `pwsh -File powershell/reporting/json_to_markdown.ps1 -Input data.json -Output data.md`

### `lab_session_template.ps1`
- **Subcategoría:** `reporting/`
- **Descripción:** Crea una plantilla Markdown de sesión de laboratorio con fecha y título.
- **Comando de ejemplo:** `pwsh -File powershell/reporting/lab_session_template.ps1 -Output session.md -Title "Lab web"`

### `csv_summary_card.ps1`
- **Subcategoría:** `reporting/`
- **Descripción:** Genera un resumen corto de un CSV con estadísticas básicas.
- **Comando de ejemplo:** `pwsh -File powershell/reporting/csv_summary_card.ps1 -Input reports/software.csv`

### `directory_markdown_index.ps1`
- **Subcategoría:** `reporting/`
- **Descripción:** Genera un índice Markdown de los ficheros de un directorio.
- **Comando de ejemplo:** `pwsh -File powershell/reporting/directory_markdown_index.ps1 -Path . -Output index.md`

### `html_list_from_csv.ps1`
- **Subcategoría:** `reporting/`
- **Descripción:** Convierte un CSV a lista HTML simple para informes web.
- **Comando de ejemplo:** `pwsh -File powershell/reporting/html_list_from_csv.ps1 -Input reports/software.csv -Output reports/software.html`

### `json_summary_card.ps1`
- **Subcategoría:** `reporting/`
- **Descripción:** Genera un resumen corto de un JSON con campos clave.
- **Comando de ejemplo:** `pwsh -File powershell/reporting/json_summary_card.ps1 -Input reports/network.json`

## 5. fun/

### `ascii_status_card.ps1`
- **Subcategoría:** `fun/`
- **Descripción:** Genera una tarjeta ASCII de estado con título y valor configurable.
- **Comando de ejemplo:** `pwsh -File powershell/fun/ascii_status_card.ps1 -Title LAB -Status ACTIVE`

### `random_lab_name.ps1`
- **Subcategoría:** `fun/`
- **Descripción:** Genera nombres aleatorios para labs combinando adjetivos y sustantivos.
- **Comando de ejemplo:** `pwsh -File powershell/fun/random_lab_name.ps1 -Count 5`

### `matrix_console.ps1`
- **Subcategoría:** `fun/`
- **Descripción:** Efecto matrix en consola con caracteres aleatorios en cascada.
- **Comando de ejemplo:** `pwsh -File powershell/fun/matrix_console.ps1 -Lines 40 -Width 60`

### `fake_update_screen.ps1`
- **Subcategoría:** `fun/`
- **Descripción:** Simula una pantalla de actualización del sistema paso a paso.
- **Comando de ejemplo:** `pwsh -File powershell/fun/fake_update_screen.ps1 -Steps 12`

### `rainbow_table.ps1`
- **Subcategoría:** `fun/`
- **Descripción:** Imprime texto con colores arcoíris en la consola PowerShell.
- **Comando de ejemplo:** `pwsh -File powershell/fun/rainbow_table.ps1 -Text "LAB ACTIVE"`

### `lab_countdown.ps1`
- **Subcategoría:** `fun/`
- **Descripción:** Cuenta atrás configurable para arrancar una sesión de laboratorio.
- **Comando de ejemplo:** `pwsh -File powershell/fun/lab_countdown.ps1 -Seconds 5`

### `typewriter_banner.ps1`
- **Subcategoría:** `fun/`
- **Descripción:** Imprime texto carácter a carácter imitando una máquina de escribir.
- **Comando de ejemplo:** `pwsh -File powershell/fun/typewriter_banner.ps1 -Text "LAB READY"`

### `random_status_message.ps1`
- **Subcategoría:** `fun/`
- **Descripción:** Muestra un mensaje de estado aleatorio con tono hacker/laboratorio.
- **Comando de ejemplo:** `pwsh -File powershell/fun/random_status_message.ps1`

## 6. Flujos y documentación
- Ejecuta siempre los scripts desde la raíz del repositorio para que las rutas relativas funcionen correctamente.
- Guarda los outputs generados en `reports/` con nombre descriptivo y fecha.
- Si un script requiere permisos elevados, documéntalo en el comentario de cabecera del script.
- Para scripts de `fun/`, no se requieren permisos especiales ni dependencias externas.
