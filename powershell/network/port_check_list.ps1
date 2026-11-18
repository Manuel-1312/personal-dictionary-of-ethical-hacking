param([string[]]$Hosts = @('127.0.0.1'), [int[]]$Ports = @(80,443))
$results = foreach ($targetHost in $Hosts) {
    foreach ($port in $Ports) {
        $ok = Test-NetConnection -ComputerName $targetHost -Port $port -InformationLevel Quiet
        [pscustomobject]@{ Host = $targetHost; Port = $port; Open = $ok }
    }
}
$results | Format-Table -AutoSize
