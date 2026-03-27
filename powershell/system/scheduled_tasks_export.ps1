param([string]$Output = 'scheduled_tasks.json')
Get-ScheduledTask |
    Select-Object TaskName, TaskPath, State, Author, Description |
    ConvertTo-Json -Depth 3 |
    Set-Content -Encoding UTF8 -Path $Output
Write-Host "Tareas exportadas a $Output"
