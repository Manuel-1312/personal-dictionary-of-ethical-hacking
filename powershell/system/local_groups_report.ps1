param([string]$Output = 'local_groups.csv')
Get-LocalGroup |
  Select-Object Name, Description |
  Export-Csv -NoTypeInformation -Encoding UTF8 -Path $Output
Write-Host "Grupos locales exportados a $Output"
