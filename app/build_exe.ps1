param([string]$Name = 'HackingToolbox')
python -m pip install -r app/requirements-build.txt
python -m PyInstaller --onefile --windowed --name $Name app/main.py
Write-Host "EXE generado en dist/$Name.exe"
