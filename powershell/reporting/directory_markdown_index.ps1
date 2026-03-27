param([string]$Path = '.', [string]$Output = 'directory-index.md')
$lines = @('# Directory Index', '')
Get-ChildItem -LiteralPath $Path -Recurse -File -ErrorAction SilentlyContinue |
  ForEach-Object {
    $rel = Resolve-Path -Relative $_.FullName
    $lines += "- `$rel`"
  }
$lines | Set-Content -Encoding UTF8 -Path $Output
Write-Host "Índice Markdown guardado en $Output"
