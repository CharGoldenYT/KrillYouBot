# This generates specific strings for commands starting with "?krill" 
import urllib.request as urllib
from datetime import datetime
import time as PyTime
from globalStuff import curVersion as ver, logger
from modules.backend.getChangelog import get_changelog
from inspect import currentframe, getframeinfo
readme = ''
privacyPolicy = ''
tos = ''
errfile = None

# Set the current ver
replace =''
if ver.endswith('-testver'): replace = '-testver'
if ver.endswith('-TestVer'): replace = '-TestVer'
versionString = '## [' + ver.replace(replace, '') + ']'

make_changelog = get_changelog

# author: Username of who ran the command
# userID: User ID of who ran the command
# command: which specific command was run (i.e. ?krill about)
# message_content: Self explanatory
# channelID: ID of the channel it ran from
# serverName: Self explanatory
def make_author_string(author:str, userID:int, command:str, message_content:str, channelID:int, serverName:str, serverID:int):
    authorStr = '<@' + str(userID) + '>(' + author + ') Ran the command: "' + command + '" | Full Command Ran: "' + message_content + '" | Channel ID: "' + str(channelID) + '" | Server Ran From: "' + serverName + '" | Server ID: "' + str(serverID) + '"'
    return authorStr

def get_readme(): from modules.backend.readmes.discord_readme import dREADME; return dREADME

def get_privacy_policy(): from modules.backend.readmes.privacy_policy import pPolicy; return pPolicy

def get_tos():from modules.backend.readmes.tos import tos; return tos

def get_gitVer():
    url = ''
    versionToReturn = None
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/gitVer.txt').read().decode('utf-8'))
    except urllib.HTTPError as e: 
        logger.log_err('shit the readme url handler died lmao: ' + str(e), True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno); url = '-# URL Handler died lmao. '
    if not url == None:versionToReturn = url
    return versionToReturn