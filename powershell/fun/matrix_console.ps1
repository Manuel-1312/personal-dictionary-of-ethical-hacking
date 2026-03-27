param([int]$Lines = 30, [int]$Width = 50)
$chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*'.ToCharArray()
1..$Lines | ForEach-Object {
    $line = -join (1..$Width | ForEach-Object { $chars | Get-Random })
    Write-Host $line -ForegroundColor Green
    Start-Sleep -Milliseconds 40
}
