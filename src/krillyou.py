# holy SHIT i cleaned up the main code a lot.


# Imports
from os import system
import discord,atexit
from modules.commands.krill import getKrillMessage
from modules.commands.krillVersion import *
from modules.backend.betterLogs.betterLogs import *
from platform import python_version
from modules.backend.exitTasks import doExitTasks
from modules.backend.broadcastTools import *
from modules.commands.checkMessage import checkMessage, get_permittedServers, get_firstAvailableChannel

# Setup
system('title Krill You Bot | A discord bot to krill your friends!')

botKey = None
try:
    botKey = open('botStuff/botKey.txt').read()
except:
    print('Error finding the botkey! make sure it is in a folder named "botStuff" where you launched the exe/script!')
    exit(1)

filename = get_filname()

from modules.discordpy.client import Client

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def close():
    doExitTasks()
atexit.register(close)

# Main code
isRunning = True

@client.event
async def on_ready():
    log_info(filename, f'[STARTUP]: CLIENT READY: Ready to receive and send messages as: {client.user}{bcolors.ENDC}', False)
    yuh = get_permittedServers(client, None)
    await broadcast_readyMessage(yuh[0], yuh[1])

@client.event
async def on_message(message:discord.Message):
    if message.author == client.user:
        return
    if not message.author == client.user:
        await checkMessage(message, client)
    
@client.event
async def on_message_edit(before:discord.Message, after:discord.Message):
    #print('MESSAGE EDITED, OLDMESSAGE: "' + oldMessage.content + '" NEWMESSAGE: "' + message.content + '"')
    if not before.content == after.content:
        if after.author == client.user:
            return
        if not after.author == client.user:
            await checkMessage(after)

from discord.guild import Guild
@client.event
async def on_guild_join(guild:Guild):
    yuh = get_firstAvailableChannel(guild, client)
    yuh = guild.get_channel(yuh)
    await yuh.send('Krill You Bot requires more customization, run `?krill configure help` to see all settings.')

def initialize_bot():
    check_pythonVersion()
    from modules.backend.startTasks import run_startTasks
    run_startTasks()
    try:
        client.run(botKey)
    except Exception as e:
        log_fatal(filename, f'[STARTUP]: Could not start/restart the Bot! "{e}"', False, True)

@client.event
async def close():
    yuh = get_permittedServers(client, None)
    await broadcast_closeMessage(yuh[0], yuh[1])

# LETS SEE IF THIS WORKS! - Me every time i do something that could potentially fail catastrophically.
initialize_bot()