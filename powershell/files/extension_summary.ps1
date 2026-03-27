param([string]$Path = "$HOME\Downloads")
Get-ChildItem -LiteralPath $Path -Recurse -File -ErrorAction SilentlyContinue |
    Group-Object Extension |
    Sort-Object Count -Descending |
    Select-Object Name, Count |
    Format-Table -AutoSize
