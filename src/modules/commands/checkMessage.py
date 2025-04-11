r'''This script handles the processing of messages to match it to a valid command!'''
from discord.message import Message
from modules.discordpy.client import Client
from globalStuff import logger, curVersion, idToPath, ownerIDs as permittedUserIDs, get_permittedServers, get_permittedServers_version
from modules.backend.krillJson import parse_krillJson, new_Json
from modules.commands.krillAbout import get_readme, get_tos, get_privacy_policy, make_author_string, make_changelog
from modules.commands.krill import getKrillMessage
from modules.backend.broadcastTools import *
from modules.commands.components.confighelp import getCommands

def get_setting(setting:str, path:str, gID:int, cID:int) -> (str | list[str]):
    try:
        settings = parse_krillJson(path, gID, cID)
        if setting == 'logschannel':
            return str(settings[0])
        if setting == 'sendonreadymessage':
            return str(settings[1])
        if setting == 'configprefix':
            return str(settings[2])
        if setting == 'allowbroadcasts':
            return str(settings[3])
        if setting == 'newversionbroadcastchannel':
            return str(settings[4])
    except Exception as e:
        return [f'Could not get setting `{setting}`: "`', str(e), '`"']

def set_setting(setting:str, v:str, gID:int, globalSettings:list):
    from modules.backend.krillJson import change_setting
    if setting == 'configprefix':
        return change_setting(gID, globalSettings[0], globalSettings[1], v, globalSettings[3], globalSettings[4])
        
    if setting == 'logschannel':
        try:
            int(v)
        except Exception as e:
            return f'Had an error setting `logsChannel`! "{str(e)}"'
        if globalSettings[4] == globalSettings[0]:
            return change_setting(gID, int(v), globalSettings[1], globalSettings[2], globalSettings[3], int(v))
        return change_setting(gID, int(v), globalSettings[1], globalSettings[2], globalSettings[3], globalSettings[4])
        
    if setting == 'newversionbroadcastchannel':
        try:
            int(v)
        except Exception as e:
            return f'Had an error setting `newversionbroadcastchannel`! "{str(e)}"'
        
        return change_setting(gID, globalSettings[0], globalSettings[1], globalSettings[2], globalSettings[3], int(v))
        
    if setting == 'sendonreadymessage':
        if not v == 'true' and not v == 'false':
            return f'Only valid options for `sendOnReadyMessage` are "true" or "false"! got {v}'
        if v == 'true':
            return change_setting(gID, globalSettings[0], True, globalSettings[2], globalSettings[3], globalSettings[4])
        if v == 'false':
            return change_setting(gID, globalSettings[0], False, globalSettings[2], globalSettings[3], globalSettings[4])
        
    if setting == 'allowbroadcasts':
        if not v == 'true' and not v == 'false':
            return f'Only valid options for `allowBroadcasts` are "true" or "false"! got {v}'
        if v == 'true':
            return change_setting(gID, globalSettings[0], globalSettings[1], globalSettings[2], True, globalSettings[4])
        if v == 'false':
            return change_setting(gID, globalSettings[0], globalSettings[1], globalSettings[2], False, globalSettings[4])
        
    return f"That's not a valid setting! `{setting}`"
        

def replace_krillBroadcast(string:str):
    import re
    finalString = re.sub('krill broadcast ', '', string, flags=re.I)
    return finalString



async def checkMessage(message:Message, client:Client):
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
                logger.log_error("Can't delete that message! are there appropriate permissions?", True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)
            try:
                await message.channel.send(finalMessage)
            except:
                logger.log_err("Can't send a message! are there appropriate permissions?", True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)
            author = make_author_string(str(message.author), message.author.id, cmd, message.content, message.channel.id, message.guild.name, message.guild.id)
            logger.log_info(author, True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)

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
                logger.log_err("Can't send a message! are there appropriate permissions?", True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)
            author = make_author_string(str(message.author), message.author.id, cmd, message.content, message.channel.id, message.guild.name, message.guild.id)
            logger.log_info(author, True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)



            

    if messageLower.startswith(settingsPrefix):
        suppressEmbeds = True

        command = messageLower.replace(settingsPrefix, '', 1).rstrip().lstrip()

        finalMessage = None

        if command.startswith('levelup'):
            cmd = settingsPrefix + 'levelup'
            finalMessage = 'I dunno :3c=L\n-# You Level up by simply talking'

        if command.startswith('krill about'):
            cmd = settingsPrefix + 'krill about'
            finalMessage = get_readme().replace('`?', f'`{settingsPrefix}')

        if command.startswith('krill tos'):
            cmd = settingsPrefix + 'krill tos'
            finalMessage = get_tos()

        if command.startswith('krill privacypolicy'):
            cmd = settingsPrefix + 'krill privacypolicy'
            finalMessage = get_privacy_policy()

        if command.startswith('krill version'):
            try:
                await message.delete()
            except:
                logger.log_error("Can't delete that message! are there appropriate permissions?", True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)
            cmd = settingsPrefix + 'krill version'
            if command == 'krill version true':
                
                if message.author.id in permittedUserIDs and not message.channel.id == 1279923362923151401:
                    yuh = get_permittedServers_version(client, message)
                    await broadcast_announcement(yuh[0], yuh[1], f'Krill You Bot has updated! ***v{curVersion}*** with the changelog of:\n\n{make_changelog()}\n\n\n-# See the full changelog [here](https://github.com/CharGoldenYT/KrillYouBot/blob/main/readmes/changelog.md) | See this versions release page [here](https://github.com/CharGoldenYT/KrillYouBot/releases/tag/v{curVersion})', True)
                
                if not message.author.id in permittedUserIDs:
                    member = message.guild.get_member(message.author.id)
                    try:
                        await member.send(f'You dont have permission to broadcast `{settingsPrefix}krill version`')

                    except Exception as e:
                        logger.log_err(f'User {str(message.author.id)}({message.author.name}) tried to broadcast "{settingsPrefix}krill version"!', True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)
                        user = client.get_user(714247788715573310)
                        # Sends me an alert.
                        user.send(f'User {str(message.author.id)}({message.author.name}) tried to broadcast "{settingsPrefix}krill version"!')

            if not curVersion.__contains__('b'):
                finalMessage = f'The current version is ***v{curVersion}*** with the changelog of:\n\n{make_changelog()}\n\n\n-# See the full changelog [here](https://github.com/CharGoldenYT/KrillYouBot/blob/main/readmes/changelog.md) | See this versions release page [here](https://github.com/CharGoldenYT/KrillYouBot/releases/tag/v{curVersion})'
            if curVersion.__contains__('b'):
                finalMessage = f'The current version is ***v{curVersion}*** with the changelog of:\n\n{make_changelog()}\n\n\n-# See the full changelog [here](https://github.com/CharGoldenYT/KrillYouBot/blob/main/readmes/changelog.md)'

        permission = message.channel.permissions_for(message.author).manage_channels or message.channel.permissions_for(message.author).manage_messages

        if command.startswith('krill configure'):
                    
            if not message.channel.permissions_for(message.author).manage_channels and not message.channel.permissions_for(message.author).manage_messages:
                finalMessage = 'You must have manage channels or manage messages to mess with these settings'

            cmd = settingsPrefix + 'krill configure'
            commandList = command.replace('krill configure', '').rstrip().lstrip().split(' ')
            #print(commandList)

            if commandList[0] == 'help':
                suppressEmbeds = False
                finalMessage = getCommands(settingsPrefix)
                
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
                        logger.log_err("Couldn't delete that message, does the bot have sufficient permissions?", True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)

                yuh = get_permittedServers(client, message, True)
                await broadcast_announcement(yuh[0], yuh[1], replace_krillBroadcast(message.content.replace(settingsPrefix, '', 1)), False)

        if finalMessage != None:
            if finalMessage.__len__() < 2000:
                await message.channel.send(str(finalMessage), suppress_embeds=(suppressEmbeds))
            else:
                message2 = 'The message that was generated was 2000+!'
                if cmd == settingsPrefix + 'krill version':
                    message2 += f'\n -# But theres a new [version](https://github.com/CharGoldenYT/KrillYouBot/releases/tag/v{curVersion})'
                await message.channel.send(message2, suppress_embeds=(suppressEmbeds))

        if not cmd == None:
            author = make_author_string(str(message.author), message.author.id, cmd, message.content, message.channel.id, message.guild.name, message.guild.id)
            logger.log_info(author, True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)