param([string]$Output = 'process_snapshot.csv')
Get-Process |
    Sort-Object CPU -Descending |
    Select-Object Name, Id, CPU, WS, StartTime -ErrorAction SilentlyContinue |
    Export-Csv -NoTypeInformation -Encoding UTF8 -Path $Output
Write-Host "Snapshot guardado en $Output"
