#Literally only here so that i dont get import errors for looping imports
from datetime import datetime; from platform import python_version
#set up logging with current time
time = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))
filname = "logs/krillYouBotLog-" + time + ".log"
acceptedVers = ['3.12.6']

# REMINDER TO KEEP THIS ALL LOWERCASE!
def getCurVersion():
    return '3.0'

def compareVersions() -> bool:
    import urllib.request as urllib
    from inspect import currentframe, getframeinfo
    from modules.backend.betterLogs.betterLogs import log_err
    url = ''
    versionToReturn = None
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
    if python_version() not in acceptedVers:
        testedVersions = ''
        pos = 0
        if acceptedVers.__len__() > 1:
            for version in acceptedVers:
                pos += 1
                if not pos == acceptedVers.__len__():
                    testedVersions += f'{version}, '
                if pos == acceptedVers.__len__():
                    testedVersions += version
        if acceptedVers.__len__() <= 1:
            testedVersions = acceptedVers[0]
        print(f'Krill you bot\'s rewrite was coded and tested with {testedVersions} you may run into problems or unexpected errors!')