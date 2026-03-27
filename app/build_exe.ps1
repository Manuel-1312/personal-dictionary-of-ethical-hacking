param([string]$Name = 'HackingToolbox')
python -m pip install pyinstaller
pyinstaller --onefile --windowed --name $Name app/main.py
Write-Host "EXE generado en dist/$Name.exe"
