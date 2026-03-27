param([string]$Output = 'firewall_profiles.csv')
Get-NetFirewallProfile |
  Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction, AllowInboundRules, AllowLocalFirewallRules |
  Export-Csv -NoTypeInformation -Encoding UTF8 -Path $Output
Write-Host "Perfiles de firewall exportados a $Output"
