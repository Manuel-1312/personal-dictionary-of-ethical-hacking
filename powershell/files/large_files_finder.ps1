param([string]$Path = $HOME, [int]$MinMb = 100)
Get-ChildItem -LiteralPath $Path -Recurse -File -ErrorAction SilentlyContinue |
    Where-Object { $_.Length -ge ($MinMb * 1MB) } |
    Sort-Object Length -Descending |
    Select-Object FullName, @{n='SizeMB';e={[math]::Round($_.Length / 1MB, 2)}}, LastWriteTime |
    Format-Table -AutoSize
