param([string]$Output = 'local_users.csv')
Get-LocalUser |
  Select-Object Name, Enabled, LastLogon, PasswordRequired, PasswordExpires, UserMayChangePassword |
  Export-Csv -NoTypeInformation -Encoding UTF8 -Path $Output
Write-Host "Usuarios locales exportados a $Output"
