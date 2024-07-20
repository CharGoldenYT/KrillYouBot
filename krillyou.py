# This example requires the 'message_content' intent.

import discord
import logging
import atexit
from datetime import datetime
import os
from readme import get_readme
from readme import get_error
from readme import get_privacy_policy
from readme import get_tos
from readme import get_gitVer
from krillcommand import getKrillMessage

ver = '1.3.2h'
changelog = '''# [1.3.2h] - 7/20/24 1:00 AM

### Changed

- Made a log event for if the bot gets rate limited
- Fixed the version string being accidentally done like "text(VersionString)"
- Slightly changed the formatting of the "?krill version" command to make it look a little nicer
- Fixed the changelog's timestamps
- Made the changelog easier to type by making it a multiline string
- added an input message that asks if the changelog looks right.'''

print('the cur_changelog is: \n' + changelog + '\nIf something looks off, or is not the right version, you probably need to edit "cur_changelog.py')

confirm = input('does something look off?')

if confirm == 'y' or confirm == 'yes':changelog = changelog + '\n\n-# This changelog might be off!'; logging.warning('changelog might be inaccurate!')

print('Continuing...')

time = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))
showReadme = True

readme = get_readme()
privacyPolicy = get_privacy_policy()
tos = get_tos()
error = get_error()
try:
    os.mkdir('logs/')
except OSError as e:
    message = 'Error Creating Dir! ' + str(e)
    print(message); logging.error(message)

try:
    logging.basicConfig(level=logging.INFO, filename="logs/krillYouBotLog-" + time +".log", filemode="a", format="%(asctime)s %(levelname)s %(message)s")
except Exception as e:
    print('Error Creating log file! "' + str(e) + '"')

botKeyTxt = open('botKey.txt')
botKey = botKeyTxt.read()
if not error == None: logging.error(error)

def cleanup():
    var = input('Press any key to continue')
    print("closing!"); logging.info('closing!')

atexit.register(cleanup)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    gitVer = get_gitVer()
    if not str(gitVer).strip() == ver:
        if not gitVer == None:print('Update Available! Check the github!'); logging.info('Update available! CurVersion: v' + ver + ' | gitVer: v' + gitVer)
    print(f'Ready to receive and send messages as: {client.user}')

@client.event
async def is_ws_ratelimited():
    logging.warn('Rate Limited!! SHIT') # Because it's useful to know if this bot gets rate limited for troubleshooting

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    

    lowercaseMessage = message.content.lower()

    if lowercaseMessage.startswith('/krill'):
        author = '<@' + str(message.author.id) + '>(@' + str(message.author) + ') ran the krill command | Full command ran: "' + message.content + '"'
        print(author); logging.info(author)

        messageContent = lowercaseMessage.strip()

        userID = ''

        userID = messageContent.replace('/krill ', '')
 
        strippedUserID = userID.strip()

        finalMessage = ''
        isNull = ''
        noUser = ''
        if strippedUserID.startswith(' ') or strippedUserID.startswith('/krill'):strippedUserID = None

        if strippedUserID == None:print('no option specified!'); logging.warning('no option specified!');finalMessage = 'Unknown Command! Got: Null\nuse ?krill about for a list of commands.'

        if not strippedUserID == None and strippedUserID.startswith('<@'):finalMessage = getKrillMessage(strippedUserID)

        #print('userID:"' + strippedUserID + '"')
        #print('messageContent:' + messageContent)
        if lowercaseMessage.startswith('/krill <@'):
            try:await message.delete()
            except:logging.critical("Can't Delete Message! Does the bot have sufficient permissions?"); print("Can't Delete Message! Does the bot have sufficient permissions?")
        try:await message.channel.send(finalMessage)
        except:logging.critical("Can't Send Message! Does the bot have sufficient permissions?"); print("Can't Send Message! Does the bot have sufficient permissions?")

    if lowercaseMessage.startswith('?krill'):
        addReadme = ''
        if showReadme == True:addReadme = ' Imma leave the full readme in the logs lmao\n' + readme
        if lowercaseMessage.startswith('?krill help'):
            author = '<@' + str(message.author.id) + '>(@' + str(message.author) + ') ran the krill help command | Full command ran: "' + message.content + '"'
            print(author); logging.info(author)

            await message.channel.send('Krill Command Useage:\n/krill <@userID>/@user (e.g. <@300020084808744962>)')

        if lowercaseMessage.startswith('?krill about'):
            author = '<@' + str(message.author.id) + '>(@' + str(message.author) + ') ran the krill about command | Full command ran: "' + message.content + '"' + addReadme
            print(author); logging.info(author)

            await message.channel.send(readme, suppress_embeds=(True))
        
        addReadme = ''
        if showReadme == True:addReadme = ' Imma leave the full readme in the logs lmao\n' + privacyPolicy
        if lowercaseMessage.startswith('?krill privacypolicy'):
            author = '<@' + str(message.author.id) + '>(@' + str(message.author) + ') ran the krill privacypolicy command | Full command ran: "' + message.content + '"' + addReadme
            print(author); logging.info(author)

            await message.channel.send(privacyPolicy, suppress_embeds=(True))

        addReadme = ''
        if showReadme == True:addReadme = ' Imma leave the full readme in the logs lmao\n' + tos
        if lowercaseMessage.startswith('?krill tos'):
            author = '<@' + str(message.author.id) + '>(@' + str(message.author) + ') ran the krill tos command | Full command ran: "' + message.content + '"' + addReadme
            print(author); logging.info(author)

            await message.channel.send(tos, suppress_embeds=(True))

        if lowercaseMessage.startswith('?krill version'):

            author = '<@' + str(message.author.id) + '>(@' + str(message.author) + ') ran the krill version command | Full command ran: "' + message.content + '"'
            print(author); logging.info(author)

            try:await message.delete()
            except:logging.critical("Can't Delete Message! Does the bot have sufficient permissions?"); print("Can't Delete Message! Does the bot have sufficient permissions?")
            await message.channel.send('The current version is: v' + ver + '\n\n the current version\'s changelog is:\n\n' + changelog + ' \n\n\nSee the full changelog [here](https://github.com/gameygu-0213/KrillYouBot/blob/main/changelog.md)', suppress_embeds=(True))
            
            
try:client.run(botKey)
except:
    logging.critical('Invalid Bot Key!! got: ' + botKey); print('CRITICAL: Invalid key! got: ' + botKey)