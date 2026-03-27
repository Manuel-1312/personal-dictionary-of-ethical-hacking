param([string]$Path = $HOME)
Get-ChildItem -LiteralPath $Path -Recurse -File -ErrorAction SilentlyContinue |
    Group-Object Name |
    Where-Object { $_.Count -gt 1 } |
    ForEach-Object {
        $_.Group | Select-Object @{n='DuplicateName';e={$_.Name}}, FullName, Length, LastWriteTime
    } |
    Format-Table -AutoSize
