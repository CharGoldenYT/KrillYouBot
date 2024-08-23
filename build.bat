@echo off
color 0A
pyinstaller -F --workpath ./export/build/ --distpath ./export/ --icon=icon.ico krillyou.py
set /p answer=Do you already have your botKey.txt file in the export folder (Y/N)?
if /i "%answer:~,1%" EQU "Y" echo not copying botKey.txt
if /i "%answer:~,1%" EQU "N" copy botKey.txt export
set /p answer=Do you wanna see the extra files it grabs in the output? (i.e. ?krill about uses discord_readme.md) (Y/N)?
if /i "%answer:~,1%" EQU "Y" copy toggleShowGetReturns.txt export
if /i "%answer:~,1%" EQU "N" echo not enabling
if /i "%answer:~,1%" EQU "N" del "export/toggleShowGetReturns.txt"
echo DONE
pause
cd export
start krillyou.exe