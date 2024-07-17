# This example requires the 'message_content' intent.

import discord
import logging
import atexit
from datetime import datetime
import os

botkeyfile = open('botKey.txt')
botkey = botkeyfile.read()
try:
    os.mkdir('logs/')
except OSError as e:
    message = 'Error Creating Dir! ' + str(e)
    print(message); logging.error(message)

time = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))


def cleanup():
    logging.basicConfig(level=logging.INFO, filename="logs/krillYouBotLog-" + time +".log", filemode="a", format="%(asctime)s %(levelname)s %(message)s")
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
    
    if message.content.startswith('/krill'):
        author = str(message.author) + ' ran the krill command'
        print(author); logging.info(author)

        messageContent = message.content.strip()

        userID = ''

        userID = messageContent.replace('/krill ', '')
 
        strippedUserID = userID.strip()

        finalMessage = ''
        isNull = ''
        noUser = ''
        if strippedUserID.startswith(' ') or strippedUserID.startswith('/krill'):strippedUserID = 'Null'

        if strippedUserID == 'Null':print('is null'); logging.warning('is null');finalMessage = 'Incorrect Useage! Krill Command Useage:\n/krill <@userID>/@user (e.g. <@300020084808744962>)'; isNull = 'true'

        if not strippedUserID.startswith('<') and not isNull == 'true':print('has no user'); logging.warning('has no user');finalMessage = 'No User Specified!\nHow am i supposed to krill an unknown target?\n(Try /krill <@userID>/@user (e.g. <@300020084808744962>))'; noUser = 'true'

        if not isNull == 'true' and not noUser == 'true':finalMessage = 'Krilling ' + userID; print('isNull: ' + isNull + '\nnoUser: ' + noUser)

        #print('userID:"' + strippedUserID + '"')
        #print('messageContent:' + messageContent)
        if not messageContent.strip() == '/krill' and messageContent.startswith('/krill <'):await message.delete()
        await message.channel.send(finalMessage)

    if message.content.startswith('?krill help'):
        author = str(message.author) + ' ran the krill help command'
        print(author); logging.info(author)

        await message.channel.send('Krill Command Useage:\n/krill <@userID>/@user (e.g. <@300020084808744962>)')
        

client.run(botkey)
