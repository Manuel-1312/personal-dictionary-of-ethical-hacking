param([Alias('Input')][string]$Path, [string]$Output = 'table.md')
$rows = Import-Csv -Path $Path
if (-not $rows) { 'Sin datos.' | Set-Content -Path $Output; exit }
$headers = $rows[0].PSObject.Properties.Name
$lines = @()
$lines += '| ' + ($headers -join ' | ') + ' |'
$lines += '| ' + (($headers | ForEach-Object { '---' }) -join ' | ') + ' |'
foreach ($row in $rows) {
    $values = foreach ($h in $headers) { [string]$row.$h }
    $lines += '| ' + ($values -join ' | ') + ' |'
}
$lines | Set-Content -Encoding UTF8 -Path $Output
Write-Host "Markdown guardado en $Output"
