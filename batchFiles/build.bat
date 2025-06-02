@echo off
color 0A
cd ..\src
python compileMarkdown.py
cd ..
pyinstaller -F --workpath ./export/build/ --distpath ./export/ --icon=icon.ico --name "Krill You Bot" src/krillyou.py
echo DONE
pause