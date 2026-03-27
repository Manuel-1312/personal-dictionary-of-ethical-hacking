param([string]$Output = 'adapter_report.csv')
Get-NetAdapter |
  Select-Object Name, InterfaceDescription, Status, LinkSpeed, MacAddress |
  Export-Csv -NoTypeInformation -Encoding UTF8 -Path $Output
Write-Host "Adaptadores exportados a $Output"
