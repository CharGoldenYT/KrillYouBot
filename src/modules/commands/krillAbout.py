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

def make_changelog():
    r'''Redirect function cause im too lazy :3'''
    changelog = get_changelog()
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

def get_readme():
    versionString = ' (' + ver + ')'
    url = ''
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/readmes/discord_readme.md').read().decode('utf-8'))
    except urllib.HTTPError as e: 
        logger.log_err('shit the readme url handler died lmao: ' + str(e), True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno); url = '-# URL Handler died lmao. '
    readme = 'This was generated with the [GitHub "discord_readme"](https://github.com/gameygu-0213/KrillYouBot/blob/main/readmes/discord_readme.md):\n\n' + '# Krill You Bot' + versionString + ' ' + url

    return readme

def get_privacy_policy():
    url = ''
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/CharGoldenYT/KrillYouBot/main/readmes/Privacy%20Policy.md').read().decode('utf-8'))
    except urllib.HTTPError as e: 
        logger.log_err('shit the readme url handler died lmao: ' + str(e), True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno); url = '-# URL Handler died lmao. '
    privacyPolicy = 'This was generated with the [GitHub "Privacy Policy"](https://github.com/gameygu-0213/KrillYouBot/blob/main/readmes/Privacy%20Policy.md):\n\n' + url

    return privacyPolicy

def get_tos():
    url = ''
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/readmes/tos.md').read().decode('utf-8'))
    except urllib.HTTPError as e: 
        logger.log_err('shit the readme url handler died lmao: ' + str(e), True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno); url = '-# URL Handler died lmao. '
    tos = 'This was generated with the [GitHub "tos"](https://github.com/gameygu-0213/KrillYouBot/blob/main/readmes/tos.md):\n\n' + url

    return tos

def get_gitVer():
    url = ''
    versionToReturn = None
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/gitVer.txt').read().decode('utf-8'))
    except urllib.HTTPError as e: 
        logger.log_err('shit the readme url handler died lmao: ' + str(e), True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno); url = '-# URL Handler died lmao. '
    if not url == None:versionToReturn = url
    return versionToReturn