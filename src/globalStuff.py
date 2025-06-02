# This is where global functions/variables will go to help prevent circular import errors.

# Imports
from discord.client import Client # technically it's the same thing.
from discord.message import Message
from discord.guild import Guild
from datetime import datetime
from platform import python_version
from chars_betterlogs.logs import Logging
from modules.backend.semver import SemVer, fromString
from time import sleep
from versionShit import *

# Variables
time = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))
filname = "logs/krillYouBotLog-" + time + ".xml"

curVersion = curSemVersion.toString()
lastVersion = lastSemVersion.toString()
ownerIDs = [714247788715573310, 300020084808744962, 940383429529337886, 1081752556730064936, 428541977298993152]
# The Discord User ID's who own the bot, or that I trust, and can use special commands.

logger:Logging = Logging('tempLog_' + time + '.xml', f'<!-- Created by Krill You Bot v{curVersion}-->')
logger._set_filename(filname)

# Functions
def get_firstAvailableChannel(guild:Guild, client:Client) -> int:
    foundChannel = False
    for channel in guild.channels:
        if not foundChannel:
            cID = channel.id
            permissions = channel.permissions_for(guild.get_member(client.user.id))
            if permissions.send_messages:
                foundChannel = True
                return cID

def get_permittedServers(client:Client, message:Message, isBroadcastCommand:bool = False, versionCommand:bool = False) -> list[list]:
    allowedServers :list[Guild] = []
    serverChannels:list[int] = []
    channelID:int = 0
    if not message == None:
        channelID = message.channel.id
    for guild in client.guilds:
        if message == None:
            channelID = get_firstAvailableChannel(guild, client)
        guildID = guild.id
        from modules.backend.krillJson import parse_krillJson
        serverSettings = parse_krillJson(guildID, channelID)
        if not isBroadcastCommand:
            if serverSettings[1]:
                allowedServers.append(guild)
                serverChannels.append(serverSettings[0])
        if isBroadcastCommand:
            if serverSettings[3]:
                allowedServers.append(guild)
                serverChannels.append(serverSettings[0])
        if versionCommand:
            if serverSettings[3]:
                allowedServers.append(guild)
                serverChannels.append(serverSettings[4])
            
                
    return [allowedServers, serverChannels]

def get_permittedServers_version(client:Client, message:Message) -> list[list]:
    return get_permittedServers(client, message, False, True)

def idToPath(gID:int) -> str:
    return f'serverSettings/serverID-{str(gID)}_Settings.json'

def get_filname():
    return filname

def check_pythonVersion():
    from inspect import currentframe, getframeinfo
    pyVerList = python_version().split('.')
    pyVer = f'{pyVerList[0]}.{pyVerList[1]}'

    match pyVer:
        case '3.12' | '3.13':msg = 'Well guess yer\' safe. Fer\' now.'
        case _:
            semPyVer = SemVer(int(pyVerList[0]), int(pyVerList[1]), int(pyVerList[2]))
            if semPyVer.lessThan(SemVer(3, 10, 0)): logger.log_fatal("Python version is lower than 3.10! please update your python version and run this script again!"); exit(1)
            frameinfo = getframeinfo(currentframe()); logger.log_warn('Krill you bot\'s rewrite was coded and tested with Python 3.12 you may run into problems or unexpected errors!', True, frameinfo.filename, frameinfo.lineno)
        
def compareVersions() -> bool:
    import urllib.request as urllib
    from inspect import currentframe, getframeinfo
    url = ''
    versionToReturn = curVersion
    if not curVersion.lower() == 'unreleased':
        try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/gitVer.txt').read().decode('utf-8'))
        except urllib.HTTPError as e: 
            frameinfo = getframeinfo(currentframe()); logger.log_err('shit the readme url handler died lmao: ' + str(e), True, frameinfo.filename, frameinfo.lineno)
        if url != None:versionToReturn = url
    return curSemVersion.isEqual(fromString(versionToReturn))

def get_formattedVersion():
    r'''So i dont get circular import errors, i've basically ported the functionality'''
    replace = ''
    if curVersion.endswith('-testver'): replace = '-testver'
    if curVersion.endswith('-TestVer'): replace = '-TestVer'
    versionString = f'## [{curVersion.replace(replace, '')}]'
    return versionString  