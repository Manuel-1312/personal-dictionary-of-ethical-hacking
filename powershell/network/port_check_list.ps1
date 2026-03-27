param([string[]]$Hosts = @('127.0.0.1'), [int[]]$Ports = @(80,443))
$results = foreach ($host in $Hosts) {
    foreach ($port in $Ports) {
        $ok = Test-NetConnection -ComputerName $host -Port $port -InformationLevel Quiet
        [pscustomobject]@{ Host = $host; Port = $port; Open = $ok }
    }
}
$results | Format-Table -AutoSize
