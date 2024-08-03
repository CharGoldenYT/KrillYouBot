# This example requires the 'message_content' intent.

import discord,logging,atexit,os,random,shutil,maskpass
from datetime import datetime
from generateStrings import get_readme,get_privacy_policy,get_tos,get_gitVer,make_author_string,ver,verLower,make_changelog
from krillcommand import getKrillMessage


# Set accepted file extensions for moving logs
acceptedFileTypes = ['.txt', '.log']
# The changelog for the current version
changelog = make_changelog()

print('the cur_changelog is: \n' + changelog + '\nIf something looks off, or is not the right version, you probably need to edit "cur_changelog.py')
# Ask the user if the changelog looks off
confirm = input('does something look off?')
# and add text based on that
confirm2 = None
if confirm == 'y' or confirm == 'yes':
    changelog = changelog + '\n\n-# This changelog might be off! | See the full changelog [here](https://github.com/gameygu-0213/KrillYouBot/blob/main/changelog.md)'; logging.warning('changelog might be inaccurate!'); confirm2 = ''
if confirm2 == None:
    changelog = changelog + '\n\n-# See the full changelog [here](https://github.com/gameygu-0213/KrillYouBot/blob/main/changelog.md)'
# Make it clear that a bot is on the test version of the current version
if verLower.endswith('-testver'): changelog = changelog + ' | This is a test version!'

print('Continuing...')

time = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))
showReadme = True

try:
    os.mkdir('logs/')
except OSError as e:
    message = 'Error Creating Dir: "' + str(e) + '"'
    print(message); logging.error(message)

try:
    os.mkdir('logs/old/')
except OSError as e:
    message = 'Error Creating Dir: "' + str(e) + '"'
    print(message); logging.error(message)
            
#set up logging with current time
filname = "logs/krillYouBotLog-" + time + ".log"
try:
    logging.basicConfig(level=logging.INFO, filename=filname, filemode="a", format="%(asctime)s %(levelname)s %(message)s")
except Exception as e:
    print('Error Creating log file: "' + str(e) + '"')
#test if file can be opened
try:
    tester = open(filname, 'r'); tester.close()
except Exception as e:
    message = 'Error Opening Log File! Log file might not save this session!!! Error: ' + str(e)
    print(message); logging.warn(message)
#Grab the botkey from a text file
try:
    botKeyTxt = open('botKey.txt')
    botKey = botKeyTxt.read()
except Exception as e:
    print('ERROR OPENING BOTKEY FILE: ' + str(e)); logging.critical('ERROR OPENING BOTKEY FILE: ' + str(e))
    botKey = maskpass.askpass('Error opening botkey! Enter/Copy Paste key here!', '#')

printReturns = False
confirm = input('Show return of url functions for the readme, TOS, etc?')
if confirm == 'y' or confirm == 'yes': printReturns = True
#on exit, do this.
def cleanup():
    #move log files we don't need to clutter the main folder
    for file in os.listdir('logs/'):
        #print('The cur file to move is: ' + file + '\n')
        for extension in acceptedFileTypes:
            if file.endswith(extension):
                try:shutil.move('logs/' + file, 'logs/old/' + file, )
                except shutil.Error as e:
                    message = 'Error Moving File "' + file + '" Error: ' + str(e)
                    print(message); logging.error(message)
    var = input('Press any key to continue')
    print("closing!"); logging.info('closing!')

atexit.register(cleanup)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    if not verLower.endswith('-testver'):
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
    if not message.author == client.user:await checkMessage(message)

@client.event
async def on_message_edit(before, after):
    #print('MESSAGE EDITED, OLDMESSAGE: "' + oldMessage.content + '" NEWMESSAGE: "' + message.content + '"')
    if not before.content == after.content:
        if message.author == client.user:
            return
        if not message.author == client.user:await checkMessage(message)
    
async def checkMessage(message):
    #print('checkMessage ran! got' + message.content)
    lowercaseMessage = message.content.lower()

    #PIPEBOMB COMMAND RANDOMIZER LETS GOOOOOOOOOO
    varRandInt = random.randint(0,4)
    Finalmessage = ''
    if varRandInt == 0: Finalmessage = 'KABLOOOEY'
    if varRandInt == 1: Finalmessage = 'KABOOM'
    if varRandInt == 2: Finalmessage = 'BLAMMO'
    if varRandInt == 3: Finalmessage = '***Explodes cutely :3***'
    if varRandInt == 4: Finalmessage = '***Fsssshhhhh....***'

    if lowercaseMessage.startswith('/pipebomb'):
        author = make_author_string(str(message.author), message.author.id, 'pipebomb', message.content, message.channel.id, message.guild.name)
        print(author); logging.info(author)

        try:await message.channel.send(Finalmessage)
        except:logging.critical("Can't Send Message! Does the bot have sufficient permissions?"); print("Can't Send Message! Does the bot have sufficient permissions?")

    # The command that started it all
    if lowercaseMessage.startswith('/krill'):
        # author = '<@' + str(message.author.id) + '>(@' + str(message.author) + ') ran the krill command | Full command ran: "' + message.content
        author = make_author_string(str(message.author), message.author.id, 'krill', message.content, message.channel.id, message.guild.name)
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

#Funny Command
    if lowercaseMessage.startswith('?levelup'):
            #author = '<@' + str(message.author.id) + '>(@' + str(message.author) + ') ran the krill help command | Full command ran: "' + message.content + '"'
            author = make_author_string(str(message.author), message.author.id, 'levelup', message.content, message.channel.id, message.guild.name)
            print(author); logging.info(author)

            try:await message.channel.send('Uh Whats that? I dunno what you\'re talking about :shrug:\n-# You Level up by simply talking :3c')
            except:logging.critical("Can't Send Message! Does the bot have sufficient permissions?"); print("Can't Send Message! Does the bot have sufficient permissions?")
        

#info and help commands
    if lowercaseMessage.startswith('?krill'):

        #Check the date, and if its my birthday, add a subtext formatted message!
        birthdaymsg = ''
        dateNow = str(datetime.today().strftime('%m/%d'))
        if dateNow == '08/18':birthdaymsg = '\n-# Today is Char\'s Birthday (The guy who coded this bot.)'

        if lowercaseMessage.startswith('?krill help'):
            #author = '<@' + str(message.author.id) + '>(@' + str(message.author) + ') ran the krill help command | Full command ran: "' + message.content + '"'
            author = make_author_string(str(message.author), message.author.id, 'krill help', message.content, message.channel.id, message.guild.name)
            print(author); logging.info(author)

            try:await message.channel.send('Krill Command Useage:\n/krill <@userID>/@user (e.g. <@300020084808744962>)\n\n-# For problems with the krill you bot, please dm me at @annyconducter, with your problem, and your server\'s name')
            except:logging.critical("Can't Send Message! Does the bot have sufficient permissions?"); print("Can't Send Message! Does the bot have sufficient permissions?")

        if lowercaseMessage.startswith('?krill about'):
            readme = get_readme(True)
            
            
            author = make_author_string(str(message.author), message.author.id, 'krill about', message.content, message.channel.id, message.guild.name)
            print(author); logging.info(author)

            try:await message.channel.send(readme + birthdaymsg, suppress_embeds=(True))
            except:logging.critical("Can't Send Message! Does the bot have sufficient permissions?"); print("Can't Send Message! Does the bot have sufficient permissions?")
        
        
        if lowercaseMessage.startswith('?krill privacypolicy'):
            privacyPolicy = get_privacy_policy(True)
            
            author = make_author_string(str(message.author), message.author.id, 'krill privacypolicy', message.content, message.channel.id, message.guild.name)
            print(author); logging.info(author)

            try:await message.channel.send(privacyPolicy, suppress_embeds=(True))
            except:logging.critical("Can't Send Message! Does the bot have sufficient permissions?"); print("Can't Send Message! Does the bot have sufficient permissions?")

        if lowercaseMessage.startswith('?krill tos'):
            tos = get_tos(True)
            
            author = make_author_string(str(message.author), message.author.id, 'krill tos', message.content, message.channel.id, message.guild.name)
            print(author); logging.info(author)

            try:await message.channel.send(tos, suppress_embeds=(True))
            except:logging.critical("Can't Send Message! Does the bot have sufficient permissions?"); print("Can't Send Message! Does the bot have sufficient permissions?")

        if lowercaseMessage.startswith('?krill version'):
            author = make_author_string(str(message.author), message.author.id, 'krill version', message.content, message.channel.id, message.guild.name)
            print(author); logging.info(author)

            try:await message.delete()
            except:logging.critical("Can't Delete Message! Does the bot have sufficient permissions?"); print("Can't Delete Message! Does the bot have sufficient permissions?")
            try:await message.channel.send('The current version is: v' + ver + '\n\n the current version\'s changelog is:\n\n' + changelog + birthdaymsg, suppress_embeds=(True))
            except:logging.critical("Can't Send Message! Does the bot have sufficient permissions?"); print("Can't Send Message! Does the bot have sufficient permissions?")
            
            
try:client.run(botKey)
except:
    logging.critical('Invalid Bot Key!! got: ' + botKey); print('CRITICAL: Invalid key! got: ' + botKey)