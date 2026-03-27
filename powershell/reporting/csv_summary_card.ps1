param([string]$Input)
$data = Import-Csv -Path $Input
$count = if ($data) { $data.Count } else { 0 }
$headers = if ($data) { ($data[0].PSObject.Properties.Name -join ', ') } else { '' }
Write-Host '+------------------------------+'
Write-Host ('| File: ' + [IO.Path]::GetFileName($Input)).PadRight(31) + '|'
Write-Host ('| Rows: ' + $count).PadRight(31) + '|'
Write-Host ('| Columns: ' + $headers).Substring(0, [Math]::Min((('| Columns: ' + $headers).Length), 30)).PadRight(31) + '|'
Write-Host '+------------------------------+'
