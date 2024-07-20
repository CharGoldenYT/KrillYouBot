# This generates the Readme used in the main krillyou.py
import logging
import os
import urllib.request as urllib
readme = ''
error = None
privacyPolicy = ''
tos = ''

# author: Username of who ran the command
# userID: User ID of who ran the command
# command: which specific command was run (i.e. ?krill about)
# message_content: Self explanatory
# channelID: ID of the channel it ran from
# serverName: Self explanatory
def make_author_string(author:str, userID:int, command:str, message_content:str, channelID:int, serverName:str):
    authorStr = '<@' + str(userID) + '>(' + author + ') Ran the command: "' + command + '" | Full Command Ran: "' + message_content + '" | Channel ID: "' + str(channelID) + '" | Server Ran From: ' + serverName
    return authorStr

def get_readme():
    showGetReturns = False
    if os.path.exists('toggleShowGetReturns.txt'):
        txt = open('toggleShowGetReturns.txt'); txt = txt.read()
        if str(txt.lower()).strip() == 'true': showGetReturns = True
        else:showGetReturns = False
    url = ''
    writeToFile = True
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/discord_readme.md').read().decode('utf-8'))
    except urllib.HTTPError as e: print('shit the readme url handler died lmao: ' + str(e)); logging.error('shit the readme url handler died lmao: ' + str(e)); writeToFile = False
    if writeToFile == True:file = open('discord_readme.md', 'w'); file.write(url); file.close()

    if os.path.exists('discord_readme.md'): readme = open('discord_readme.md'); readme = 'This was generated with the [GitHub "discord_readme"](https://github.com/gameygu-0213/KrillYouBot/blob/main/discord_readme.md):\n\n' + readme.read()
    
    if not os.path.exists('discord_readme.md'): print('discord_readme.md not found!');readme = "Message @annyconducter, the readme broke lmao.\n`/krill <@userID>/@user` Krill someone\n`?Krill help` tells you how to use /krill\n`?krill about` Shows this message"

    if showGetReturns:print('get_readme returned: ' + readme)
    return readme


def get_error():
    error = ''
    if not os.path.exists('discord_readme.md'): error += "Couldn't find 'discord_readme.md' using hardcoded string!\n"
    if not os.path.exists('privacyPolicy.md'): error += "Couldn't find 'privacyPolicy.md' using hardcoded string!\n"
    if not os.path.exists('tos.md'): error += "Couldn't find 'tos.md' using hardcoded string!\n"
    if os.path.exists('discord_readme.md') and os.path.exists('privacyPolicy.md') and os.path.exists('tos.md'): error = None #just to be safe
    return error

def get_privacy_policy():
    showGetReturns = False
    if os.path.exists('toggleShowGetReturns.txt'):
        txt = open('toggleShowGetReturns.txt'); txt = txt.read()
        if str(txt.lower()).strip() == 'true': showGetReturns = True
        else:showGetReturns = False
    url = ''
    writeToFile = True
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/Privacy%20Policy.md').read().decode('utf-8'))
    except urllib.HTTPError as e: print('shit the privacyPolicy url handler died lmao: ' + str(e)); logging.error('shit the privacyPolicy url handler died lmao: ' + str(e)); writeToFile = False
    if writeToFile == True:file = open('privacyPolicy.md', 'w'); file.write(url); file.close()

    if os.path.exists('privacyPolicy.md'): privacyPolicy = open('privacyPolicy.md'); privacyPolicy = 'This was generated with the [GitHub "Privacy Policy.md"](https://github.com/gameygu-0213/KrillYouBot/blob/main/Privacy%20Policy.md):\n\n' + privacyPolicy.read()
    
    if not os.path.exists('privacyPolicy.md'): print('privacyPolicy.md not found!'); privacyPolicy = "Message @annyconducter, the privacyPolicy def broke lmao.\n[View it online](https://github.com/gameygu-0213/KrillYouBot/blob/main/Privacy%20Policy.md)"

    if showGetReturns:print('get_privacy_policy returned: ' + privacyPolicy)
    return privacyPolicy

def get_tos():
    showGetReturns = False
    if os.path.exists('toggleShowGetReturns.txt'):
        txt = open('toggleShowGetReturns.txt'); txt = txt.read()
        if str(txt.lower()).strip() == 'true': showGetReturns = True
        else:showGetReturns = False
    url = ''
    writeToFile = True
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/tos.md').read().decode('utf-8'))
    except urllib.HTTPError as e: print('shit the tos url handler died lmao: ' + str(e)); logging.error('shit the tos url handler died lmao: ' + str(e)); writeToFile = False
    if writeToFile == True:file = open('tos.md', 'w'); file.write(url); file.close()

    if os.path.exists('tos.md'): tos = open('tos.md'); tos = 'This was generated with the [GitHub "tos.md"](https://github.com/gameygu-0213/KrillYouBot/blob/main/tos.md):\n\n' + tos.read()
    
    if not os.path.exists('tos.md'): print('tos.md not found!'); tos = "Message @annyconducter, the tos def broke lmao.\n[View it online](https://github.com/gameygu-0213/KrillYouBot/blob/main/tos.md)"

    if showGetReturns:print('get_tos returned: ' + tos)
    return tos

def get_gitVer():
    url = ''
    versionToReturn = None
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/gitVer.txt').read().decode('utf-8'))
    except urllib.HTTPError as e: print('shit the gitVer url handler died lmao: ' + str(e)); logging.error('shit the gitver url handler died lmao: ' + str(e)); url = None
    if not url == None:versionToReturn = url
    return versionToReturn