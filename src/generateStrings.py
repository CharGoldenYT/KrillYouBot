# This generates specific strings for commands starting with "?krill" 
import urllib.request as urllib
from datetime import datetime
import time as PyTime
from getCurVersion import getCurVersion
from betterLogs import *
readme = ''
privacyPolicy = ''
tos = ''
errfile = None

# Set the current ver
ver = getCurVersion()
replace = ''
if ver.endswith('-testver'): replace = '-testver'
if ver.endswith('-TestVer'): replace = '-TestVer'
versionString = '# [' + ver.replace(replace, '') + ']'

time = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))
filname = 'logs/generateStringslog-' + time + '.log'

from getCurVersion import get_filname

try: filname = get_filname()
except Exception as e: print('COULD NOT GET FILENAME "' + str(e) + '"')
PyTime.sleep(1)

def make_changelog():
    changelog = versionString + ''' - 8/23/24 6:45 PM

### Changed

- Added what krill bot version made a log file.
- Changed How i label Hotfixes
- Made it so Hotfix doesnt get changed to hotfix
- Reconsolidated generateStrings.py and main logs
- New "betterLogs.py" script'''
    return changelog

# author: Username of who ran the command
# userID: User ID of who ran the command
# command: which specific command was run (i.e. ?krill about)
# message_content: Self explanatory
# channelID: ID of the channel it ran from
# serverName: Self explanatory
def make_author_string(author:str, userID:int, command:str, message_content:str, channelID:int, serverName:str):
    authorStr = '<@' + str(userID) + '>(' + author + ') Ran the command: "' + command + '" | Full Command Ran: "' + message_content + '" | Channel ID: "' + str(channelID) + '" | Server Ran From: ' + serverName
    return authorStr

def get_readme(showGetReturns:bool):
    versionString = ' (' + ver + ')'
    url = ''
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/readmes/discord_readme.md').read().decode('utf-8'))
    except urllib.HTTPError as e: 
        frameinfo = getframeinfo(currentframe()); log_err(filname, '[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + ']shit the readme url handler died lmao: ' + str(e))
        frameinfo = getframeinfo(currentframe()); print('[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + '] shit the readme url handler died lmao: ' + str(e)); url = '-# URL Handler died lmao. '
    readme = 'This was generated with the [GitHub "discord_readme"](https://github.com/gameygu-0213/KrillYouBot/blob/main/readmes/discord_readme.md):\n\n' + '# Krill You Bot' + versionString + ' ' + url

    if showGetReturns:print('get_readme returned: ' + readme)
    return readme

def get_privacy_policy(showGetReturns:bool):
    url = ''
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/CharGoldenYT/KrillYouBot/main/readmes/Privacy%20Policy.md').read().decode('utf-8'))
    except urllib.HTTPError as e: 
        frameinfo = getframeinfo(currentframe()); log_err(filname, '[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + ']shit the readme url handler died lmao: ' + str(e))
        frameinfo = getframeinfo(currentframe()); print('[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + '] shit the readme url handler died lmao: ' + str(e)); url = '-# URL Handler died lmao. '
    privacyPolicy = 'This was generated with the [GitHub "Privacy Policy"](https://github.com/gameygu-0213/KrillYouBot/blob/main/readmes/Privacy%20Policy.md):\n\n' + url

    if showGetReturns:print('get_privacy_policy returned: ' + privacyPolicy)
    return privacyPolicy

def get_tos(showGetReturns:bool):
    url = ''
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/readmes/tos.md').read().decode('utf-8'))
    except urllib.HTTPError as e: 
        frameinfo = getframeinfo(currentframe()); log_err(filname, '[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + ']shit the readme url handler died lmao: ' + str(e))
        frameinfo = getframeinfo(currentframe()); print('[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + '] shit the readme url handler died lmao: ' + str(e)); url = '-# URL Handler died lmao. '
    tos = 'This was generated with the [GitHub "tos"](https://github.com/gameygu-0213/KrillYouBot/blob/main/readmes/tos.md):\n\n' + url

    if showGetReturns:print('get_readme returned: ' + tos)
    return tos

def get_gitVer():
    url = ''
    versionToReturn = None
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/gitVer.txt').read().decode('utf-8'))
    except urllib.HTTPError as e: 
        frameinfo = getframeinfo(currentframe()); log_err(filname, '[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + ']shit the readme url handler died lmao: ' + str(e))
        frameinfo = getframeinfo(currentframe()); print('[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + '] shit the readme url handler died lmao: ' + str(e)); url = '-# URL Handler died lmao. '
    if not url == None:versionToReturn = url
    return versionToReturn