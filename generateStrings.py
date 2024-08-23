# This generates specific strings for commands starting with "?krill" 
import urllib.request as urllib
from datetime import datetime
readme = ''
privacyPolicy = ''
tos = ''
errfile = None
# Set the current ver
ver = '2.2-TestVer'
# Make it lowercase if text exists
verLower = ver.lower()
versionString = '# [' + verLower.replace('-testver', '') + ']'

temp = None
try:temp = open('tmp/fileName.txt')
except OSError as e:
    print('Error getting filename! "' + str(e) + '"')

if temp != None: temp = temp.read()
time = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))
if temp == None: temp = 'logs/generateStringslog-' + time + '.log'

def make_changelog():
    changelog = versionString + ''' - 8/23/24 2:37 PM

### Changed

- Implementing a true fix for logging.
- Added a log for when failing to move logs to logs/old.
- Fixed moving logs into logs/old'''
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
    if temp != None:errfile = open(temp, 'a')
    time = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))
    timeString = '[' + time + ']: '
    versionString = ' (' + verLower.replace('-testver', '') + ')'
    url = ''
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/discord_readme.md').read().decode('utf-8'))
    except urllib.HTTPError as e: 
        if errfile != None: errfile.write(timeString + 'shit the readme url handler died lmao: ' + str(e))
        print('shit the readme url handler died lmao: ' + str(e)); url = '-# URL Handler died lmao. '
    readme = 'This was generated with the [GitHub "discord_readme"](https://github.com/gameygu-0213/KrillYouBot/blob/main/discord_readme.md):\n\n' + '# Krill You Bot' + versionString + ' ' + url

    if showGetReturns:print('get_readme returned: ' + readme)
    if errfile != None:errfile.close()
    return readme

def get_privacy_policy(showGetReturns:bool):
    if temp != None:errfile = open(temp, 'a')
    time = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))
    timeString = '[' + time + '] '
    url = ''
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/Privacy%20Policy.md').read().decode('utf-8'))
    except urllib.HTTPError as e: 
        if errfile != None: errfile.write(timeString + 'shit the readme url handler died lmao: ' + str(e))
        print('shit the readme url handler died lmao: ' + str(e)); url = '-# URL Handler died lmao. '
    privacyPolicy = 'This was generated with the [GitHub "Privacy Policy"](https://github.com/gameygu-0213/KrillYouBot/blob/main/Privacy%20Policy.md):\n\n' + url

    if showGetReturns:print('get_privacy_policy returned: ' + privacyPolicy)
    if errfile != None:errfile.close()
    return privacyPolicy

def get_tos(showGetReturns:bool):
    if temp != None:errfile = open(temp, 'a')
    time = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))
    timeString = '[' + time + '] '
    url = ''
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/tos.md').read().decode('utf-8'))
    except urllib.HTTPError as e: 
        if errfile != None: errfile.write(timeString + 'shit the readme url handler died lmao: ' + str(e))
        print('shit the readme url handler died lmao: ' + str(e)); url = '-# URL Handler died lmao. '
    tos = 'This was generated with the [GitHub "tos"](https://github.com/gameygu-0213/KrillYouBot/blob/main/tos.md):\n\n' + url

    if showGetReturns:print('get_readme returned: ' + tos)
    errfile.close()
    return tos

def get_gitVer():
    if temp != None:errfile = open(temp, 'a')
    time = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))
    timeString = '[' + time + '] '
    url = ''
    versionToReturn = None
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/gitVer.txt').read().decode('utf-8'))
    except urllib.HTTPError as e: 
        if errfile != None: errfile.write(timeString + 'shit the readme url handler died lmao: ' + str(e))
        print('shit the readme url handler died lmao: ' + str(e)); url = '-# URL Handler died lmao. '
    if not url == None:versionToReturn = url
    if errfile != None:errfile.close()
    return versionToReturn