@echo off
color 0A
cd ..
pyinstaller -F --workpath ./export/build/ --distpath ./export/ --icon=icon.ico src/krillyou.py
echo DONE
pause
cd export
start krillyou.exe