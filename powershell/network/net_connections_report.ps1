param([string]$Output = 'net_connections.csv')
Get-NetTCPConnection |
    Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State, AppliedSetting, OwningProcess |
    Export-Csv -NoTypeInformation -Encoding UTF8 -Path $Output
Write-Host "Conexiones exportadas a $Output"
