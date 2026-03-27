param([int]$Steps = 10)
1..$Steps | ForEach-Object {
    $pct = [int](($_ / $Steps) * 100)
    Write-Host "Instalando actualizaciones críticas... $pct%" -ForegroundColor Cyan
    Start-Sleep -Milliseconds 200
}
Write-Host 'No te asustes: era una demo 😌' -ForegroundColor Yellow
