param([string]$Input, [string]$Output = 'report.html')
$data = Import-Csv -Path $Input
$html = @('<html><body><h1>CSV Report</h1><ul>')
foreach ($row in $data) {
  $html += '<li>' + (($row.PSObject.Properties | ForEach-Object { "$($_.Name): $($_.Value)" }) -join ' | ') + '</li>'
}
$html += '</ul></body></html>'
$html | Set-Content -Encoding UTF8 -Path $Output
Write-Host "HTML guardado en $Output"
