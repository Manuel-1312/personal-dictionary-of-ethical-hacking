param([string]$Output = 'env_snapshot.csv')
Get-ChildItem Env: |
    Sort-Object Name |
    Select-Object Name, Value |
    Export-Csv -NoTypeInformation -Encoding UTF8 -Path $Output
Write-Host "Variables de entorno exportadas a $Output"
