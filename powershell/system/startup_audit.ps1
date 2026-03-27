param([string]$Output = 'startup_audit.csv')
$items = @()
$items += Get-CimInstance Win32_StartupCommand | Select-Object Name, Command, Location, User
$items | Export-Csv -NoTypeInformation -Encoding UTF8 -Path $Output
Write-Host "Startup audit exportado a $Output"
