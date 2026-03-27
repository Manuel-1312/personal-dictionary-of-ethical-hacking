param([string]$Output = 'dns_cache.csv')
Get-DnsClientCache |
    Select-Object Entry, Name, Data, Status, Type |
    Export-Csv -NoTypeInformation -Encoding UTF8 -Path $Output
Write-Host "Cache DNS exportada a $Output"
