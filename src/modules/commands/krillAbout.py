# This generates specific strings for commands starting with "?krill" 
import urllib.request as urllib
from datetime import datetime
import time as PyTime
from modules.commands.krillVersion import getCurVersion
from modules.backend.betterLogs.betterLogs import *
from inspect import currentframe, getframeinfo
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

from modules.commands.krillVersion import get_filname

try: filname = get_filname()
except Exception as e: print('COULD NOT GET FILENAME "' + str(e) + '"')
PyTime.sleep(1)

def make_changelog():
    changelog = versionString + ''' 10/18/24 - 2:14 AM

### Changed

- Fixed a weird crash involving being unable to re-connect to discord due to forgetting to properly setup a logging command.
- CORRECTLY implemented the fix in [3.0 Hotfix 3](https://github.com/CharGoldenYT/KrillYouBot/blob/main/readmes/changelog.md#30-hotfix-3-101624---830-pm) regarding incorrect order of ending logging operations.
-# Pretty dumb lmao
- Changed it to where `batchFiles/build.bat` no longer launches krill you bot at the end, and moved that functionality to `batchFiles/test.bat` which also builds the bot, but immediately launches when done.'''
    return changelog

# author: Username of who ran the command
# userID: User ID of who ran the command
# command: which specific command was run (i.e. ?krill about)
# message_content: Self explanatory
# channelID: ID of the channel it ran from
# serverName: Self explanatory
def make_author_string(author:str, userID:int, command:str, message_content:str, channelID:int, serverName:str, serverID:int):
    authorStr = '<@' + str(userID) + '>(' + author + ') Ran the command: "' + command + '" | Full Command Ran: "' + message_content + '" | Channel ID: "' + str(channelID) + '" | Server Ran From: "' + serverName + '" | Server ID: "' + str(serverID) + '"'
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
        frameinfo = getframeinfo(currentframe()); print('[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + '] shit the readme url handler died lmao: ' + str(e))
    if not url == None:versionToReturn = url
    return versionToReturn