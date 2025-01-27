!#/bin/bash/

cd ..
echo "This script makes a new environment, installs the required libraries, and then removes the bot environment folder."
read -p "Press any key to continue. or close this terminal if you did not mean to run this."
python3 -m venv bot-env
source ./bot-env/bin/activate
pip install -U discord
pip install -U pyinstaller
pyinstaller -F --workpath ./export/build-linux/ --distpath ./export/Linux/ --icon=icon.ico --name "KrillYouBot" src/krillyou.py
# Don't need the build directory post-build.
rm -rf ./export/build-linux/
rm -rf ./bot-env/
echo "DONE"
read -p "Press any key to continue."
# So the paths and shit go back to normal
reset
echo "You may have (bot-env) at the beginning now, but python will still work normally, and links to the systemwide python."