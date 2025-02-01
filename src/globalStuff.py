# This is where global functions/variables will go to help prevent circular import errors.

# Imports
from discord.client import Client # technically it's the same thing.
from discord.message import Message
from discord.guild import Guild
from datetime import datetime
from platform import python_version

# Variables
time = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))
filname = "logs/krillYouBotLog-" + time + ".log"

curVersion = 'Unreleased'
lastVersion = '3.3h-3'
ownerIDs = [714247788715573310, 300020084808744962, 940383429529337886,
            1081752556730064936, 428541977298993152] # The Discord User ID's who own the bot, and can use special commands.

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
        serverSettings = parse_krillJson(idToPath(guildID), guildID, channelID)
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
    # Fun fact it seems all 3.12 versions work lmao
    if not python_version().__contains__('3.12') and not python_version().__contains__('3.13'):
        print(f'Krill you bot\'s rewrite was coded and tested with Python 3.12 you may run into problems or unexpected errors!')

        
def compareVersions() -> bool:
    import urllib.request as urllib
    from inspect import currentframe, getframeinfo
    from modules.backend.betterLogs.betterLogs import log_err
    url = ''
    versionToReturn = curVersion
    if not curVersion.lower() == 'unreleased':
        try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/gitVer.txt').read().decode('utf-8'))
        except urllib.HTTPError as e: 
            frameinfo = getframeinfo(currentframe()); log_err(filname, '[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + ']shit the readme url handler died lmao: ' + str(e))
        if not url == None:versionToReturn = url
    return curVersion == versionToReturn

def get_formattedVersion():
    r'''So i dont get circular import errors, i've basically ported the functionality'''
    replace = ''
    if curVersion.endswith('-testver'): replace = '-testver'
    if curVersion.endswith('-TestVer'): replace = '-TestVer'
    versionString = f'## [{curVersion.replace(replace, '')}]'
    return versionString  