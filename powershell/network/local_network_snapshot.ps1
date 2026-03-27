param([string]$Output = 'local_network_snapshot.json')
$data = [pscustomobject]@{
    Adapters    = Get-NetIPConfiguration | Select-Object InterfaceAlias, IPv4Address, IPv4DefaultGateway, DNSServer
    Connections = Get-NetTCPConnection -State Established | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State
}
$data | ConvertTo-Json -Depth 5 | Set-Content -Encoding UTF8 -Path $Output
Write-Host "Snapshot de red guardado en $Output"
