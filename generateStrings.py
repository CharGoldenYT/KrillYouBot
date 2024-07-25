# This generates specific strings for commands starting with "?krill" 
import logging,urllib.request as urllib
readme = ''
privacyPolicy = ''
tos = ''
# Set the current ver
ver = '1.5.1'
# Make it lowercase if text exists
verLower = ver.lower()
versionString = '# [' + verLower.replace('-testver', '') + ']'

def make_changelog():
    changelog = versionString + ''' - 7/24/24 8:45 PM

### Changed

- Made it to where it doesnt crash if it doesnt have read access
- Fixed the build.bat being specific to how i was using pyinstaller, as that would cause issues for people building this from source
- Removed the dependency on caching results as files to prevent crashing
- Renamed readme.py to generateStrings.py to accurately reflect how its used
- Moved where typing the latest changelog goes
- Figured out multi imports'''
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
    versionString = ' (' + verLower.replace('-testver', '') + ')'
    url = ''
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/discord_readme.md').read().decode('utf-8'))
    except urllib.HTTPError as e: print('shit the readme url handler died lmao: ' + str(e)); logging.error('shit the readme url handler died lmao: ' + str(e)); url = '-# URL Handler died lmao. '
    readme = 'This was generated with the [GitHub "discord_readme"](https://github.com/gameygu-0213/KrillYouBot/blob/main/discord_readme.md):\n\n' + '# Krill You Bot' + versionString + ' ' + url

    if showGetReturns:print('get_readme returned: ' + readme)
    return readme

def get_privacy_policy(showGetReturns:bool):
    url = ''
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/Privacy%20Policy.md').read().decode('utf-8'))
    except urllib.HTTPError as e: print('shit the privacy policy url handler died lmao: ' + str(e)); logging.error('shit the readme url handler died lmao: ' + str(e)); url = '-# URL Handler died lmao. '
    privacyPolicy = 'This was generated with the [GitHub "Privacy Policy"](https://github.com/gameygu-0213/KrillYouBot/blob/main/Privacy%20Policy.md):\n\n' + url

    if showGetReturns:print('get_privacy_policy returned: ' + privacyPolicy)
    return privacyPolicy

def get_tos(showGetReturns:bool):
    url = ''
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/tos.md').read().decode('utf-8'))
    except urllib.HTTPError as e: print('shit the tos url handler died lmao: ' + str(e)); logging.error('shit the readme url handler died lmao: ' + str(e)); url = '-# URL Handler died lmao. '
    tos = 'This was generated with the [GitHub "tos"](https://github.com/gameygu-0213/KrillYouBot/blob/main/tos.md):\n\n' + url

    if showGetReturns:print('get_readme returned: ' + readme)
    return tos

def get_gitVer():
    url = ''
    versionToReturn = None
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/gitVer.txt').read().decode('utf-8'))
    except urllib.HTTPError as e: print('shit the gitVer url handler died lmao: ' + str(e)); logging.error('shit the gitver url handler died lmao: ' + str(e)); url = None
    if not url == None:versionToReturn = url
    return versionToReturn