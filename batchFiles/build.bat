@echo off
color 0A
cd ..
pyinstaller -F --workpath ./export/build/ --distpath ./export/ --icon=icon.ico --name "Krill You Bot" src/krillyou.py
echo DONE
pause
cd export
start ./"Krill You Bot.exe"