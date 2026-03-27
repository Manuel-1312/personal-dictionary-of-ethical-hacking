param([string]$Output = 'service_report.csv')
Get-Service |
    Sort-Object Status, DisplayName |
    Select-Object Name, DisplayName, Status, StartType |
    Export-Csv -NoTypeInformation -Encoding UTF8 -Path $Output
Write-Host "Servicios exportados a $Output"
