# holy SHIT i cleaned up the main code a lot.


# Imports
from os import system
import discord,atexit
from modules.commands.krill import getKrillMessage
from platform import python_version
from modules.backend.exitTasks import doExitTasks
from modules.backend.broadcastTools import *
from modules.commands.checkMessage import checkMessage
from globalStuff import get_permittedServers, get_firstAvailableChannel, check_pythonVersion, logger

# Setup
system('title Krill You Bot "A discord bot to krill your friends!"')

botKey = None
try:
    botKey = open('botStuff/botKey.txt').read()
except:
    print('Error finding the botkey! make sure it is in a folder named "botStuff" where you launched the exe/script!')
    exit(1)

from modules.backend.startTasks import run_startTasks; run_startTasks()

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
    logger.log_info(f'[STARTUP]: CLIENT READY: Ready to receive and send messages as: {client.user}', False, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)
    from modules.backend.startTasks import grab_serverSettings
    yuh = get_permittedServers(client, None)
    yuh2 = grab_serverSettings(yuh[0])
    if not yuh2 == None:get_permittedServers(client, None)
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
            await checkMessage(after, client)

from discord.guild import Guild
@client.event
async def on_guild_join(guild:Guild):
    yuh = get_firstAvailableChannel(guild, client)
    yuh = guild.get_channel(yuh)
    await yuh.send('Krill You Bot requires more customization, run `?krill configure help` to see all settings.')

def initialize_bot():
    check_pythonVersion()
    client.run(botKey)
        

@client.event
async def close():
    yuh = get_permittedServers(client, None)
    await broadcast_closeMessage(yuh[0], yuh[1])

def die():
    file = open('script.py', 'w'); file.write('''# Discord setup
import discord
from discord.client import Client

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)

# botkey
botKey = None
try:
    botKey = open('botStuff/botKey.txt').read()
except:
    print('Error finding the botkey! make sure it is in a folder named "botStuff" where you launched the exe/script!')
    exit(1)

# actual shit to do.
@client.event
async def on_ready():
# This gets ID's from my server then sends a message and closes!
#                             My server ID              krill-bot-status Channel ID
    await client.get_guild(991595497376714832).get_channel(1279923362923151401).send('Krill You Bot is Down!')
    exit()

client.run()'''); file.close()
    import subprocess
    process = subprocess.run(['cmd /c', 'python', 'script.py'])
    print(process.stdout.decode())
    exit()


# LETS SEE IF THIS WORKS! - Me every time i do something that could potentially fail catastrophically.
while True: # While true it to HOPEFULLY not commit die on insignificant, recoverabale errors.
    try:
        initialize_bot()
    except:
        die()