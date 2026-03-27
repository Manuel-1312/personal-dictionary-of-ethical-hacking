param([string]$Path = $HOME, [int]$Days = 7, [string]$Output = 'recent_files.csv')
$limit = (Get-Date).AddDays(-$Days)
Get-ChildItem -LiteralPath $Path -Recurse -File -ErrorAction SilentlyContinue |
    Where-Object { $_.LastWriteTime -ge $limit } |
    Select-Object FullName, Length, LastWriteTime |
    Export-Csv -NoTypeInformation -Encoding UTF8 -Path $Output
Write-Host "Archivos recientes exportados a $Output"
