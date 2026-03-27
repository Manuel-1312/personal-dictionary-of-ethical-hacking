# Dependencias de la librería PowerShell

Esta carpeta intenta mantenerse ligera: la mayoría de scripts funcionan con PowerShell y cmdlets del sistema, sin instalar módulos raros ni medio ecosistema alrededor.

## Requisito base
- **PowerShell 5.1 o PowerShell 7+ (`pwsh`)**
- Windows con los cmdlets habituales de red, sistema y archivos disponibles

## Resumen general
### Sin dependencias extra
La mayor parte de scripts de `powershell/` usan únicamente:
- cmdlets integrados de Windows / PowerShell
- utilidades ya presentes en el sistema (`netsh`, `Get-Net*`, `Get-Service`, etc.)

### Dependencias o matices por categoría

## `system/`
Scripts como:
- `system_report.ps1`
- `process_snapshot.ps1`
- `service_report.ps1`
- `scheduled_tasks_export.ps1`
- `startup_audit.ps1`
- `env_snapshot.ps1`
- `installed_software_report.ps1`
- `list_local_users.ps1`
- `hotfix_report.ps1`
- `local_groups_report.ps1`

**Dependencias:**
- cmdlets y clases estándar de Windows / PowerShell
- algunos scripts requieren privilegios normales de lectura del sistema
- `Get-LocalUser` / `Get-LocalGroup` pueden depender de edición/versiones de Windows compatibles

## `files/`
Scripts como:
- `desktop_inventory.ps1`
- `large_files_finder.ps1`
- `extension_summary.ps1`
- `duplicate_name_report.ps1`
- `recent_files_report.ps1`
- `hash_inventory.ps1`
- `folder_size_report.ps1`
- `downloads_inventory.ps1`
- `top_largest_files.ps1`

**Dependencias:**
- ninguna extra
- para recorridos muy grandes, lo que cambia es el tiempo de ejecución, no los requisitos

## `network/`
Scripts como:
- `local_network_snapshot.ps1`
- `net_connections_report.ps1`
- `ping_sweep.ps1`
- `dns_cache_report.ps1`
- `port_check_list.ps1`
- `adapter_report.ps1`
- `route_table_export.ps1`
- `firewall_profile_report.ps1`
- `wifi_profiles_list.ps1`
- `share_report.ps1`

**Dependencias:**
- cmdlets `Get-Net*`, `Get-DnsClientCache`, `Get-SmbShare`, etc.
- `wifi_profiles_list.ps1` usa `netsh wlan show profiles`
- algunos cmdlets pueden requerir permisos elevados o no estar disponibles igual en todas las ediciones de Windows

## `reporting/`
Scripts como:
- `markdown_table_from_csv.ps1`
- `json_to_markdown.ps1`
- `lab_session_template.ps1`
- `csv_summary_card.ps1`
- `directory_markdown_index.ps1`
- `html_list_from_csv.ps1`
- `json_summary_card.ps1`

**Dependencias:**
- ninguna extra
- funcionan con lectura/escritura básica de archivos y objetos PowerShell

## `fun/`
Scripts como:
- `ascii_status_card.ps1`
- `random_lab_name.ps1`
- `matrix_console.ps1`
- `fake_update_screen.ps1`
- `rainbow_table.ps1`
- `lab_countdown.ps1`
- `typewriter_banner.ps1`
- `random_status_message.ps1`

**Dependencias:**
- ninguna extra
- solo consola y temporizadores básicos

## Recomendaciones prácticas
- Si un script depende de cmdlets de red o SMB, prueba primero en la máquina objetivo porque Windows no siempre trae exactamente lo mismo según edición/version.
- Si más adelante añades módulos externos, mejor separar:
  - `DEPENDENCIES.md` → mapa humano
  - `requirements` o notas de instalación por módulo
- Si un script necesita admin, déjalo explícito en su README o en el comentario inicial.

## Regla simple
Si un helper PowerShell puede hacerse con:
- cmdlets nativos
- salida exportable
- y sin instalar cosas raras

entonces encaja perfecto en esta carpeta.
