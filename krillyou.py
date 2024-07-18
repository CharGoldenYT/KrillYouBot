# This example requires the 'message_content' intent.

import discord
import logging
import atexit
from datetime import datetime
import os

time = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))

logging.basicConfig(level=logging.INFO, filename="logs/krillYouBotLog-" + time +".log", filemode="a", format="%(asctime)s %(levelname)s %(message)s")

try:
    os.mkdir('logs/')
except OSError as e:
    message = 'Error Creating Dir! ' + str(e)
    print(message); logging.error(message)

botKeyTxt = open('botKey.txt')
botKey = botKeyTxt.read()

readme = "# Krill you bot (V1.2.1) - A Wacky simple Discord bot for krilling your friends!\n\n### Usage:\n`/krill <@userID>/@user` Krill any user\n`?krill help` Tells you how to use the bot\n`?krill about` Displays this message\n### In case the bot goes offline contact: @annyconducter on Discord.\n\n[GitHub](https://github.com/gameygu-0213/KrillYouBot)"

def cleanup():
    var = input('Press any key to continue')
    print("closing!"); logging.info('closing!')

atexit.register(cleanup)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Ready to recieve and send messages as: {client.user}')

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
        if strippedUserID.startswith(' ') or strippedUserID.startswith('/krill'):strippedUserID = 'Null'

        if strippedUserID == 'Null':print('no option specified!'); logging.warning('no option specified!');finalMessage = 'Incorrect Useage! Krill Command Useage:\n/krill <@userID>/@user (e.g. <@300020084808744962>)'; isNull = 'true'

        if not strippedUserID.startswith('<') and not isNull == 'true':print('has no user'); logging.warning('has no user');finalMessage = 'No User Specified!\nHow am i supposed to krill an unknown target?\n(Try /krill <@userID>/@user (e.g. <@300020084808744962>))'; noUser = 'true'

        if not isNull == 'true' and not noUser == 'true':finalMessage = 'Krilling ' + userID; print('isNull: ' + isNull + '\nnoUser: ' + noUser)

        #print('userID:"' + strippedUserID + '"')
        #print('messageContent:' + messageContent)
        if not messageContent == '/krill' and messageContent.startswith('/krill <'):
            try:await message.delete()
            except:logging.critical("Can't Delete Message! Does the bot have sufficient permissions?"); print("Can't Delete Message! Does the bot have sufficient permissions?")
        try:await message.channel.send(finalMessage)
        except:logging.critical("Can't Send Message! Does the bot have sufficient permissions?"); print("Can't Send Message! Does the bot have sufficient permissions?")

    if lowercaseMessage.startswith('?krill'):
        if lowercaseMessage.startswith('?krill help'):
            author = '<@' + str(message.author.id) + '>(@' + str(message.author) + ') ran the krill help command | Full command ran: "' + message.content + '"'
            print(author); logging.info(author)

            await message.channel.send('Krill Command Useage:\n/krill <@userID>/@user (e.g. <@300020084808744962>)')

        if lowercaseMessage.startswith('?krill about'):
            author = '<@' + str(message.author.id) + '>(@' + str(message.author) + ') ran the krill about command | Full command ran: "' + message.content + '"'
            print(author); logging.info(author)

botKey = botKeyTxt.read()
string = input("Show key?"); logging.info('Show key?')
            await message.channel.send(readme, suppress_embeds=(True))
            
            
try:client.run(botKey)
except:
    logging.critical('Invalid Bot Key!! got: ' + botKey); print('CRITICAL: Invalid key! got: ' + botKey)