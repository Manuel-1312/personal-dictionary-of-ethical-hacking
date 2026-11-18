param([Alias('Input')][string]$Path)
$data = Get-Content -Raw -Path $Path | ConvertFrom-Json
$count = if ($data) { @($data).Count } else { 0 }
Write-Host '+------------------------------+'
Write-Host ('| File: ' + [IO.Path]::GetFileName($Path)).PadRight(31) + '|'
Write-Host ('| Items: ' + $count).PadRight(31) + '|'
Write-Host '+------------------------------+'
