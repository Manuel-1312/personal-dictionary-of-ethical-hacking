param([string]$Title = 'LAB', [string]$Status = 'ACTIVE')
$line = '+' + ('-' * 30) + '+'
Write-Host $line
Write-Host ('| ' + $Title.PadRight(28) + '|')
Write-Host ('| ' + $Status.PadRight(28) + '|')
Write-Host $line
