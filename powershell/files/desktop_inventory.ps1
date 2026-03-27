param([string]$Path = "$HOME\Desktop", [string]$Output = 'desktop_inventory.csv')
Get-ChildItem -LiteralPath $Path -Force |
    Select-Object Name, FullName, Length, LastWriteTime, Mode |
    Export-Csv -NoTypeInformation -Encoding UTF8 -Path $Output
Write-Host "Inventario exportado a $Output"
