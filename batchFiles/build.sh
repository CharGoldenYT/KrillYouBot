!#/bin/bash/

cd ..
pyinstaller -F --workpath ./export/build-linux/ --distpath ./export/Linux/ --icon=icon.ico --name "KrillYouBot" src/krillyou.py
# Don't need the build directory post-build.
rm -rf ./export/build-linux/
echo "DONE\nYou may have to use a python environment to build this since the basic system wide package seems to be broken."
read -p "Press any key to continue."