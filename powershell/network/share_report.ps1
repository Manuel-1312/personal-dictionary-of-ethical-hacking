param([string]$Output = 'shares.csv')
Get-SmbShare |
  Select-Object Name, Path, Description, FolderEnumerationMode, CurrentUsers |
  Export-Csv -NoTypeInformation -Encoding UTF8 -Path $Output
Write-Host "Shares exportados a $Output"
