param([string]$Base = '192.168.1', [int]$Start = 1, [int]$End = 10)
$results = foreach ($i in $Start..$End) {
    $ip = "$Base.$i"
    $ok = Test-Connection -Count 1 -Quiet -ComputerName $ip -ErrorAction SilentlyContinue
    [pscustomobject]@{ IP = $ip; Reachable = $ok }
}
$results | Format-Table -AutoSize
