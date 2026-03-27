param([string]$Path = "$HOME\Downloads", [string]$Output = 'downloads_inventory.csv')
Get-ChildItem -LiteralPath $Path -Recurse -File -ErrorAction SilentlyContinue |
  Select-Object Name, DirectoryName, Length, Extension, LastWriteTime |
  Export-Csv -NoTypeInformation -Encoding UTF8 -Path $Output
Write-Host "Inventario de descargas exportado a $Output"
