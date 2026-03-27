param([string]$Input, [string]$Output = 'data.md')
$data = Get-Content -Raw -Path $Input | ConvertFrom-Json
$lines = @('# JSON to Markdown', '')
foreach ($item in $data) {
    $lines += '## Item'
    foreach ($prop in $item.PSObject.Properties) {
        $lines += "- **$($prop.Name):** $($prop.Value)"
    }
    $lines += ''
}
$lines | Set-Content -Encoding UTF8 -Path $Output
Write-Host "Markdown guardado en $Output"
