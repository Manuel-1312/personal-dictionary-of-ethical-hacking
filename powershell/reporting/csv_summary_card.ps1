param([Alias('Input')][string]$Path)
$data = Import-Csv -Path $Path
$count = if ($data) { $data.Count } else { 0 }
$headers = if ($data) { ($data[0].PSObject.Properties.Name -join ', ') } else { '' }
Write-Host '+------------------------------+'
Write-Host ('| File: ' + [IO.Path]::GetFileName($Path)).PadRight(31) + '|'
Write-Host ('| Rows: ' + $count).PadRight(31) + '|'
Write-Host ('| Columns: ' + $headers).Substring(0, [Math]::Min((('| Columns: ' + $headers).Length), 30)).PadRight(31) + '|'
Write-Host '+------------------------------+'
