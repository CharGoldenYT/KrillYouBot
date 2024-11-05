r'''This script handles the processing of messages to match it to a valid command!'''
from discord.message import Message
from modules.discordpy.client import Client
from modules.backend.betterLogs.betterLogs import log_err, log_error, log_info; from modules.commands.krillVersion import get_filname, getCurVersion
from modules.backend.krillJson import parse_krillJson, new_Json
from modules.commands.krillAbout import get_readme, get_tos, get_privacy_policy, make_author_string, make_changelog
from modules.commands.krill import getKrillMessage
from modules.backend.broadcastTools import *

permittedUserIDs = [714247788715573310, 300020084808744962]
#                      Main Account    |    Alt Account
# "CHAR DONT DOX YOURSELF" Dude, User ID's are public info.

def get_firstAvailableChannel(guild:Guild, client:Client) -> int:
    foundChannel = False
    for channel in guild.channels:
        if not foundChannel:
            cID = channel.id
            permissions = channel.permissions_for(guild.get_member(client.user.id))
            if permissions.send_messages:
                foundChannel = True
                return cID

def get_permittedServers(client:Client, message:Message, isBroadcastCommand:bool = False) -> list[list]:
    allowedServers :list[Guild] = []
    serverChannels:list[int] = []
    channelID:int = 0
    if not message == None:
        channelID = message.channel.id
    for guild in client.guilds:
        if message == None:
            channelID = get_firstAvailableChannel(guild, client)
        guildID = guild.id
        serverSettings = parse_krillJson(idToPath(guildID), guildID, channelID)
        if not isBroadcastCommand:
            if serverSettings[1]:
                allowedServers.append(guild)
                serverChannels.append(serverSettings[0])
        if isBroadcastCommand:
            if serverSettings[3]:
                allowedServers.append(guild)
                serverChannels.append(serverSettings[0])
                
    return [allowedServers, serverChannels]


def idToPath(gID:int) -> str:
    return f'serverSettings/serverID-{str(gID)}_Settings.json'

def get_setting(setting:str, path:str, gID:int, cID:int) -> (str | list[str]):
    try:
        settings = parse_krillJson(path, gID, cID)
        if setting == 'configprefix':
            return settings[2]
        if setting == 'logschannel':
            return str(settings[0])
        if setting == 'sendonreadymessage':
            return str(settings[1])
        if setting == 'allowbroadcasts':
            return str(settings[3])
    except Exception as e:
        return [f'Could not get setting `{setting}`: "`', str(e), '`"']

def set_setting(setting:str, v:str, gID:int, globalSettings:list):
    from modules.backend.krillJson import change_setting
    if setting == 'configprefix':
        return change_setting(gID, globalSettings[0], globalSettings[1], v, globalSettings[3])
        
    if setting == 'logschannel':
        try:
            int(v)
        except Exception as e:
            return f'Had an error setting logsChannel! "{str(e)}"'
        
        return change_setting(gID, int(v), globalSettings[1], globalSettings[2], globalSettings[3])
        
    if setting == 'sendonreadymessage':
        if not v == 'true' and not v == 'false':
            return f'Only valid options for sendOnReadyMessage are "true" or "false"! got {v}'
        if v == 'true':
            return change_setting(gID, globalSettings[0], True, globalSettings[2], globalSettings[3])
        if v == 'false':
            return change_setting(gID, globalSettings[0], False, globalSettings[2], globalSettings[3])
        
    if setting == 'allowbroadcasts':
        if not v == 'true' and not v == 'false':
            return f'Only valid options for allowBroadcasts are "true" or "false"! got {v}'
        if v == 'true':
            return change_setting(gID, globalSettings[0], globalSettings[1], globalSettings[2], True)
        if v == 'false':
            return change_setting(gID, globalSettings[0], globalSettings[1], globalSettings[2], False)
        

def replace_krillBroadcast(string:str):
    import re
    finalString = re.sub('krill broadcast ', '', string, flags=re.I)
    return finalString



async def checkMessage(message:Message, client:Client):
    from modules.backend.startTasks import check_allowReturns

    serverSettings = parse_krillJson(idToPath(message.guild.id), message.guild.id, message.channel.id)

    settingsPrefix = serverSettings[2]

    messageLower = message.content.lower()

    cmd = None

    if messageLower.startswith('/'):

        if messageLower.startswith('/krill'):

            cmd = '/krill'

            userID = messageLower.replace('/krill ', '')

            finalMessage = getKrillMessage(userID)

            if userID.lstrip().rstrip() == '/krill' or userID == '<@':
                userID = None


            if userID == None or not userID.__contains__('<@'):
                finalMessage = 'Invalid command! missing 1 or more people!'

            try:
                await message.delete()
            except:
                log_error(get_filname(), "Can't delete that message! are there appropriate permissions?")
            try:
                await message.channel.send(finalMessage)
            except:
                log_err(get_filname(), "Can't send a message! are there appropriate permissions?")
            author = make_author_string(str(message.author), message.author.id, cmd, message.content, message.channel.id, message.guild.name, message.guild.id)
            log_info(get_filname(), author)

        if messageLower.startswith('/pipebomb'):
            cmd = '/pipebomb'
            import random
            varRandInt = random.randint(0,4)
            Finalmessage = ''
            if varRandInt == 0: Finalmessage = 'KABLOOOEY'
            if varRandInt == 1: Finalmessage = 'KABOOM'
            if varRandInt == 2: Finalmessage = 'BLAMMO'
            if varRandInt == 3: Finalmessage = '***Explodes cutely :3***'
            if varRandInt == 4: Finalmessage = '***Fsssshhhhh....***' # Cant have a pipebomb command without a chance for it to fizzle!

            try:
                await message.channel.send(Finalmessage)
            except:
                log_err(get_filname(), "Can't send a message! are there appropriate permissions?")
            author = make_author_string(str(message.author), message.author.id, cmd, message.content, message.channel.id, message.guild.name, message.guild.id)
            log_info(get_filname(), author)



            

    if messageLower.startswith(settingsPrefix):
        suppressEmbeds = True

        command = messageLower.replace(settingsPrefix, '', 1)
        print(command)

        finalMessage = None

        if command == 'levelUp':
            cmd = settingsPrefix + 'levelup'
            finalMessage = 'I dunno :3c=L\n-# You Level up by simply talking'

        if command == 'krill about':
            cmd = settingsPrefix + 'krill about'
            finalMessage = get_readme(check_allowReturns()).replace('`?', f'`{settingsPrefix}')

        if command == 'krill tos':
            cmd = settingsPrefix + 'krill tos'
            finalMessage = get_tos(check_allowReturns())

        if command == 'krill privacypolicy':
            cmd = settingsPrefix + 'krill privacypolicy'
            finalMessage = get_privacy_policy(check_allowReturns())

        if command.startswith('krill version'):
            try:
                await message.delete()
            except:
                log_err(get_filname(), "Couldn't delete that message, does the bot have sufficient permissions?")
            cmd = settingsPrefix + 'krill version'
            if command == 'krill version true':
                
                if message.author.id in permittedUserIDs and not message.channel.id == 1279923362923151401:
                    yuh = get_permittedServers(client, message, True)
                    await broadcast_announcement(yuh[0], yuh[1], f'Krill You Bot has updated! v{getCurVersion()} with the changelog of:\n\n{make_changelog()}\n\n\n-# See the full changelog [here](https://github.com/CharGoldenYT/KrillYouBot/blob/main/readmes/changelog.md) | See this versions release page [here](https://github.com/CharGoldenYT/KrillYouBot/releases/tag/v{getCurVersion()})', True)
                
                if not message.author.id in permittedUserIDs:
                    member = message.guild.get_member(message.author.id)
                    try:
                        await member.send(f'You dont have permission to broadcast `{settingsPrefix}krill version`')
                    except Exception as e:
                        log_err(get_filname(), f'User {str(message.author.id)}({message.author.name}) tried to broadcast "{settingsPrefix}krill version"!')
            if not getCurVersion().__contains__('b'):
                finalMessage = f'The current version is v{getCurVersion()} with the changelog of:\n\n{make_changelog()}\n\n\n-# See the full changelog [here](https://github.com/CharGoldenYT/KrillYouBot/blob/main/readmes/changelog.md) | See this versions release page [here](https://github.com/CharGoldenYT/KrillYouBot/releases/tag/v{getCurVersion()})'
            if getCurVersion().__contains__('b'):
                finalMessage = f'The current version is v{getCurVersion()} with the changelog of:\n\n{make_changelog()}\n\n\n-# See the full changelog [here](https://github.com/CharGoldenYT/KrillYouBot/blob/main/readmes/changelog.md)'

        permission = message.channel.permissions_for(message.author).manage_channels or message.channel.permissions_for(message.author).manage_messages

        if command.startswith('krill configure'):
                    
            if not message.channel.permissions_for(message.author).manage_channels and not message.channel.permissions_for(message.author).manage_messages:
                finalMessage = 'You must have manage channels or manage messages to mess with these settings'

            cmd = settingsPrefix + 'krill configure'
            commandList = command.replace('krill configure', '').rstrip().lstrip().split(' ')
            print(commandList)

            if commandList[0] == 'help':
                suppressEmbeds = False
                finalMessage = f'''# Krill Options
                
`logsChannel` changes the channel where broadcasted messages (Like on ready messages for example) go! 
-# ***MUST BE THE CHANNEL'S ID NUMBER*** https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID
                
`sendOnReadyMessage` Whether to allow sending a message when the krill you bot goes online!
                
`configPrefix` Change the system command's prefix (such as how right now this very command is `{settingsPrefix}krill configure help`)

`allowBroadcasts` Whether you want to receive broadcasted messages.

# These settings (and this help page) are able to be viewed by anyone in the server! just add a ? or help to the end (e.g. `{settingsPrefix}krill configure logsChannel ?`)
                
-# If you need help, or settings dont seem to actually work, contact @annyconducter on discord! or visit https://github.com/CharGoldenYT/KrillYouBot/issues'''
                
            if not commandList[0] == 'help':
                if commandList[1] == '?' or commandList[1] == 'help':
                            var = get_setting(commandList[0], idToPath(message.guild.id), message.guild.id, message.channel.id)
                            if isinstance(var, str):
                                finalMessage = f'`{commandList[0]}` is "`' + var + '`"'
                            if not isinstance(var, str):
                                finalMessage = var[0] + var[1] + var[2]

                                
                if permission and not commandList[0] == 'help' and not (commandList[1] == '?' or commandList[1] == 'help'):
                    if not commandList[1] == '?' and not commandList[1] == 'help':
                            finalMessage = set_setting(commandList[0], commandList[1], message.guild.id, serverSettings)
                            if finalMessage == None:
                                finalMessage = f'Set setting `{commandList[0]}` to `{commandList[1]}`!'

        if command.startswith('krill broadcast'):
            cmd = settingsPrefix + 'krill broadcast'
            if message.author.id not in permittedUserIDs:
                finalMessage = 'No permissions!'
            if message.author.id in permittedUserIDs:

                if replace_krillBroadcast(message.content.replace(settingsPrefix, '')).startswith('{&news:newVersion'):
                    try:
                        await message.delete()
                    except:
                        log_err(get_filname(), "Couldn't delete that message, does the bot have sufficient permissions?")

                yuh = get_permittedServers(client, message, True)
                await broadcast_announcement(yuh[0], yuh[1], replace_krillBroadcast(message.content.replace(settingsPrefix, '', 1)), False)

        if finalMessage != None and finalMessage.__len__() < 2000:
            await message.channel.send(str(finalMessage), suppress_embeds=(suppressEmbeds))
        else:
            message2 = 'The message that was made is over 2000 characters!'
            if not cmd == None and cmd == settingsPrefix + 'krill version':
                message2 += '\nThere was a new version though! check [here](https://github.com/CharGoldenYT/KrillYouBot/blob/main/readmes/changelog.md) for the new version'
            await message.channel.send(message2, suppress_embeds=(suppressEmbeds))


        if not cmd == None:
            author = make_author_string(str(message.author), message.author.id, cmd, message.content, message.channel.id, message.guild.name, message.guild.id)
            log_info(get_filname(), author)