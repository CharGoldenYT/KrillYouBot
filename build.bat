@echo off
color 0A
call pyinstaller\Scripts\activate.bat
python pyinstaller\Lib\site-packages\PyInstaller\__main__.py -F --workpath ./export/build/ --distpath ./export/ --icon=icon.ico krillyou.py
copy botKey.txt export
echo DONE
pause