@echo off
color 0A
python pyinstaller\Lib\site-packages\PyInstaller\__main__.py -F --workpath ./export/build/ --distpath ./export/ --icon=icon.ico krillyou.py
set /p answer=Do you already have your botKey.txt file in the export folder (Y/N)?
if /i "%answer:~,1%" EQU "Y" echo not copying botKey.txt
if /i "%answer:~,1%" EQU "N" copy botKey.txt export
echo DONE
pause