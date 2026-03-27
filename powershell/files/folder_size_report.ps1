param([string]$Path = $HOME)
Get-ChildItem -LiteralPath $Path -Directory -ErrorAction SilentlyContinue |
  ForEach-Object {
    $size = (Get-ChildItem -LiteralPath $_.FullName -Recurse -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum
    [pscustomobject]@{
      Folder = $_.FullName
      SizeGB = [math]::Round(($size / 1GB), 3)
    }
  } | Sort-Object SizeGB -Descending | Format-Table -AutoSize
