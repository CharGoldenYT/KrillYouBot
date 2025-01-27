#Literally only here so that i dont get import errors for looping imports
from datetime import datetime; from platform import python_version
#set up logging with current time
time = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))
filname = "logs/krillYouBotLog-" + time + ".log"
acceptedVers:list[str] = ['3.12.0', '3.12.1', '3.12.2', '3.12.3', '3.12.4', '3.12.5', '3.12.6', '3.12.7']

lastVersion = '3.3h-2'

# REMINDER TO KEEP THIS ALL LOWERCASE!
def getCurVersion():
    return '3.3h-3'

def compareVersions() -> bool:
    import urllib.request as urllib
    from inspect import currentframe, getframeinfo
    from modules.backend.betterLogs.betterLogs import log_err
    url = ''
    versionToReturn = getCurVersion()
    if not getCurVersion().lower() == 'unreleased':
        try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/gitVer.txt').read().decode('utf-8'))
        except urllib.HTTPError as e: 
            frameinfo = getframeinfo(currentframe()); log_err(filname, '[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + ']shit the readme url handler died lmao: ' + str(e))
        if not url == None:versionToReturn = url
    return getCurVersion() == versionToReturn

def get_filname():
    import os
    if not os.path.exists('logs/'):
        try:os.makedirs('logs/')
        except OSError as e:print(f'Could not make the logs directory! "{e}"')
    return filname


def check_pythonVersion():
    # Fun fact it seems all 3.12 versions work lmao
    if not python_version().__contains__('3.12') and not python_version().__contains__('3.13'):
        print(f'Krill you bot\'s rewrite was coded and tested with Python 3.12 you may run into problems or unexpected errors!')