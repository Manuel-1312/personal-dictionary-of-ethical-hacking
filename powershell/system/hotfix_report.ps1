param([string]$Output = 'hotfixes.csv')
Get-HotFix |
  Select-Object HotFixID, Description, InstalledBy, InstalledOn |
  Sort-Object InstalledOn -Descending |
  Export-Csv -NoTypeInformation -Encoding UTF8 -Path $Output
Write-Host "Hotfixes exportados a $Output"
