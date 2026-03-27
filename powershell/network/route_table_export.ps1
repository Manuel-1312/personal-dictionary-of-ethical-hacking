param([string]$Output = 'routes.csv')
Get-NetRoute |
  Select-Object DestinationPrefix, NextHop, RouteMetric, ifIndex, InterfaceAlias, AddressFamily, State |
  Export-Csv -NoTypeInformation -Encoding UTF8 -Path $Output
Write-Host "Rutas exportadas a $Output"
