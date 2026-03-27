param([string]$Path = $HOME, [int]$Top = 20)
Get-ChildItem -LiteralPath $Path -Recurse -File -ErrorAction SilentlyContinue |
  Sort-Object Length -Descending |
  Select-Object -First $Top FullName, @{n='SizeMB';e={[math]::Round($_.Length / 1MB, 2)}}, LastWriteTime |
  Format-Table -AutoSize
