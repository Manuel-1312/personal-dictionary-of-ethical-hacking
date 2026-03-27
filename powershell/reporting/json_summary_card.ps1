param([string]$Input)
$data = Get-Content -Raw -Path $Input | ConvertFrom-Json
$count = if ($data) { @($data).Count } else { 0 }
Write-Host '+------------------------------+'
Write-Host ('| File: ' + [IO.Path]::GetFileName($Input)).PadRight(31) + '|'
Write-Host ('| Items: ' + $count).PadRight(31) + '|'
Write-Host '+------------------------------+'
