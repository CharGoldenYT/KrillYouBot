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
versionString = '## [' + ver.replace(replace, '') + ']'

time = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))
filname = 'logs/generateStringslog-' + time + '.log'

from modules.commands.krillVersion import get_filname

try: filname = get_filname()
except Exception as e: print('COULD NOT GET FILENAME "' + str(e) + '"')
PyTime.sleep(1)

def make_changelog():
    changelog = versionString + '''

### Changed

- Made it to where the PyNaCl error doesn't come before the official start of the log, if it occurs (due to user not having it installed).
- Made it to where there isnt a weird space between `<!-- Created by Krill You Bot v(Version)-->` and `<!-- Log Generator: "Better Logs V2" | Better Logs by Char @annyconducter on Discord | https://github.com/CharGoldenYT/betterLogs -->` in the log file.
- Added a little check to make sure the channel i use doesn't receive update announcements.
- Made the update command DM the user if they try to broadcast `?krill version`.
- Made the version command suppress embeds on broadcast, similarly to how it works normally when not broadcasted.
- Further fixed me forgetting to add required function arguments.
- Made Better Logs handle only having one argument
- Making bigger, but slower produced updates here on out. So i dont rush it out the door a buggy mess lmao.
- Fixed the fact that the changelog is actually slightly incorrect.
- Made it not print so much unneccassary data.
- Removed old code from `src/modules/backend/exitTasks.py`
- Removed printing returns of grabbed github files (e.g. the Readme.)
- Fixed the title not being able to be renamed.
- Fixed the colors of the readme check.'''
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

    #if showGetReturns:print('get_readme returned: ' + readme)
    return readme

def get_privacy_policy(showGetReturns:bool):
    url = ''
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/CharGoldenYT/KrillYouBot/main/readmes/Privacy%20Policy.md').read().decode('utf-8'))
    except urllib.HTTPError as e: 
        frameinfo = getframeinfo(currentframe()); log_err(filname, '[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + ']shit the readme url handler died lmao: ' + str(e))
        frameinfo = getframeinfo(currentframe()); print('[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + '] shit the readme url handler died lmao: ' + str(e)); url = '-# URL Handler died lmao. '
    privacyPolicy = 'This was generated with the [GitHub "Privacy Policy"](https://github.com/gameygu-0213/KrillYouBot/blob/main/readmes/Privacy%20Policy.md):\n\n' + url

    #if showGetReturns:print('get_privacy_policy returned: ' + privacyPolicy)
    return privacyPolicy

def get_tos(showGetReturns:bool):
    url = ''
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/readmes/tos.md').read().decode('utf-8'))
    except urllib.HTTPError as e: 
        frameinfo = getframeinfo(currentframe()); log_err(filname, '[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + ']shit the readme url handler died lmao: ' + str(e))
        frameinfo = getframeinfo(currentframe()); print('[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + '] shit the readme url handler died lmao: ' + str(e)); url = '-# URL Handler died lmao. '
    tos = 'This was generated with the [GitHub "tos"](https://github.com/gameygu-0213/KrillYouBot/blob/main/readmes/tos.md):\n\n' + url

    #if showGetReturns:print('get_readme returned: ' + tos)
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