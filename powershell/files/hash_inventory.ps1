param([string]$Path = $HOME, [string]$Output = 'hash_inventory.csv')
Get-ChildItem -LiteralPath $Path -Recurse -File -ErrorAction SilentlyContinue |
  ForEach-Object {
    $hash = Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName -ErrorAction SilentlyContinue
    [pscustomobject]@{
      FullName = $_.FullName
      Length = $_.Length
      LastWriteTime = $_.LastWriteTime
      SHA256 = $hash.Hash
    }
  } | Export-Csv -NoTypeInformation -Encoding UTF8 -Path $Output
Write-Host "Inventario hash exportado a $Output"
