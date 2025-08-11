r'''This script handles the processing of messages to match it to a valid command!'''
from discord.message import Message
from modules.discordpy.client import Client
from globalStuff import logger, curVersion, idToPath, ownerIDs as permittedUserIDs, lockdownIDs, isDebugMode, get_permittedServers, get_permittedServers_version
from modules.backend.krilljson.krillJson import parse_krillJson
from modules.commands.krillAbout import get_readme, get_tos, get_privacy_policy, make_author_string, make_changelog
from modules.commands.krill import getKrillMessage
from modules.backend.broadcastTools import *
from modules.commands.components.confighelp import getCommands
from modules.commands.krillConfigure import configure_setting as configCommand
import random

def replace_krillBroadcast(string:str):
    import re
    finalString = re.sub('krill broadcast ', '', string, flags=re.I)
    return finalString



async def checkMessage(message:Message, client:Client):
    serverSettings = parse_krillJson(message.guild.id, message.channel.id)

    settingsPrefix = serverSettings[2]

    messageLower = message.content.lower()

    cmd = None

    curServer = message.channel.guild.id

    if curServer == None or (isDebugMode and not lockdownIDs.__contains__(curServer)):
        try:
            await message.channel.send("Krill You Bot is currently in debug testing, you cannot use this bot at the moment")
        except:
            logger.log_err("Can't send a message! are there appropriate permissions?", True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)

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

        if messageLower.startswith("/rolldice"):
            cmd = "/rolldice"
            diceTypes:list[str] = ["d4", "d6", "d8", "d10", "d12", "d20", "d100"]

            finalMessage = "Invalid dice type! the valid values are `d4, d6, d8, d10, d12, d20, d100`"
            diceType = messageLower.replace("/rolldice ", "")
            rawNum = messageLower.replace("/rolldice d", "")
            print(diceType)
            if diceTypes.__contains__(diceType):
                varRandInt = random.randint(1, int(rawNum))
                finalMessage = "Rolled a " + str(varRandInt) + "!"

            try:
                await message.channel.send(finalMessage)
            except:
                logger.log_err("Can't send a message! are there appropriate permissions?", True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)
            author = make_author_string(str(message.author), message.author.id, cmd, message.content, message.channel.id, message.guild.name, message.guild.id)
            logger.log_info(author, True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)

    if messageLower.startswith(settingsPrefix):
        suppressEmbeds = True

        command = messageLower.replace(settingsPrefix, '', 1).rstrip().lstrip()

        finalMessage = None

        if command.startswith("cmd"):
            if not permittedUserIDs.__contains__(message.author.id): finalMessage = "Why would I let random people run random commands on my computer?"
            commandList = command.replace("cmd", "", 1).split()

            from modules.backend.commandInterpreter import ReprCommand, runCommand
            runCommand(ReprCommand(commandList.pop(0), commandList))

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

            return configCommand(commandList, idToPath(message.guild.id), message.guild.id, message.channel.id, serverSettings, settingsPrefix)

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