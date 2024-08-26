# This example requires the 'message_content' intent.

import discord,atexit,os,random,shutil,maskpass
from os import system
system('title Krill You Bot')
from krillcommand import getKrillMessage
from getCurVersion import getCurVersion, get_filname
from betterLogs import *
#set up logging
filname = get_filname()

try:
    os.mkdir('logs/')
except OSError as e:
    message = 'Error Creating Dir: "' + str(e) + '"'
    if message.endswith("file already exists: 'logs/'\""): message = None
    if message != None:print(message)

create_logFile(filname, '<!-- Log created with Krill You Bot v' + getCurVersion() + ' -->')

try:
    os.mkdir('logs/old/')
except OSError as e:
    message = 'Error Creating Dir: "' + str(e) + '"'
    if message.endswith("file already exists: 'logs/old/'\""): message = None
    if message != None:print(message); 
    if message != None:log(filname, '[STARTUP]: ' + message, '[ERROR]:', False)


from generateStrings import get_readme,get_privacy_policy,get_tos,get_gitVer,make_author_string,ver,make_changelog

# Set accepted file extensions for moving logs
acceptedFileTypes = ['.txt', '.log']
# The changelog for the current version
changelog = make_changelog()

print('the cur_changelog is: \n' + changelog + '\n\nIf something looks off, or is not the right version, you probably need to edit "generateStrings.py"')
# Ask the user if the changelog looks off
confirm = input('does something look off?')
# and add text based on that
confirm2 = None
if confirm == 'y' or confirm == 'yes':
    changelog = changelog + '\n\n-# This changelog might be off! | See the full changelog [here](https://github.com/gameygu-0213/KrillYouBot/blob/main/changelog.md)';  
    log(filname, '[STARTUP]: changelog might be inaccurate!', '[INFO]:', False); confirm2 = ''
if confirm2 == None:
    changelog = changelog + '\n\n-# See the full changelog [here](https://github.com/gameygu-0213/KrillYouBot/blob/main/changelog.md)'
# Make it clear that a bot is on the test version of the current version
if ver.endswith('-testver'): changelog = changelog + ' | This is a test version!'

print('Continuing...')

showReadme = True
#Grab the botkey from a text file
try:
    botKeyTxt = open('botKey.txt')
    botKey = botKeyTxt.read()
except Exception as e:
    print('ERROR OPENING BOTKEY FILE: ' + str(e))
    log_err(filname, 'ERROR OPENING BOTKEY FILE: ' + str(e))
    botKey = maskpass.askpass('Error opening botkey! Enter/Copy Paste key here!', '#')

printReturns = False
confirm = input('Show return of url functions for the readme, TOS, etc?')
if confirm == 'y' or confirm == 'yes': printReturns = True
#on exit, do this.

def cleanup():
    import time
    log(filname, '[EXIT]: CLEANING UP', '', False)
    end_log(filname)
    print('Closing in 5 Seconds!')
    doLogMove()
    time.sleep(5)
    print("closing!")
atexit.register(cleanup)

#move log files, we don't need to clutter the main folder
def doLogMove():
    try:
        for file in os.listdir('logs/'):
            for extension in acceptedFileTypes:
                if file.endswith(extension) and file != filname:
                    success = True
                    try:shutil.move('logs/' + file, 'logs/old/' + file, )
                    except shutil.Error as e:
                        message = '[EXIT]: Error Moving File "' + file + '" Error: ' + str(e)
                        print(message)
                        log(filname, message, '[ERROR]:', False)
                        success = False
                    if success:print('Moved file: "' + file + '"')
    except OSError as e:
        message = '[EXIT]: Error Moving logs! "' + str(e) + '"'
        if str(e).endswith("'" + filname + "'"): message = None
        if message != None:print(message)
        if message != None:log(filname, message, '[ERROR]:', False)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    if not ver.endswith('-testver'):
        gitVer = get_gitVer()
        if not str(gitVer).strip() == ver:
            if not gitVer == None:print('Update Available! Check the github!'); log(filname, '[STARTUP]: Update available! CurVersion: v' + ver + ' | gitVer: v' + gitVer, '[INFO]:', False)
    print(f'Ready to receive and send messages as: {client.user}');  
    log(filname, '[STARTUP]: CLIENT READY!', '[INFO]:', False)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if not message.author == client.user:await checkMessage(message)

@client.event
async def on_message_edit(before, after):
    #print('MESSAGE EDITED, OLDMESSAGE: "' + oldMessage.content + '" NEWMESSAGE: "' + message.content + '"')
    if not before.content == after.content:
        if after.author == client.user:
            return
        if not after.author == client.user:await checkMessage(after)
    
async def checkMessage(message):
    time = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))
    timeString = '[' + time + ']: '
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
        print(author); 
        log_info(filname, timeString + author)

        success = True
        try:await message.channel.send(Finalmessage)
        except: print("Can't Send Message! Does the bot have sufficient permissions?"); log_critical(timeString + "Can't Send Message! Does the bot have sufficient permissions?")

    # The command that started it all
    if lowercaseMessage.startswith('/krill'):
        # author = '<@' + str(message.author.id) + '>(@' + str(message.author) + ') ran the krill command | Full command ran: "' + message.content
        author = make_author_string(str(message.author), message.author.id, 'krill', message.content, message.channel.id, message.guild.name)
        print(author); 
        log_info(filname, timeString + author)

        messageContent = lowercaseMessage.strip()

        userID = ''

        userID = messageContent.replace('/krill ', '')
 
        strippedUserID = userID.strip()

        finalMessage = ''
        isNull = ''
        noUser = ''
        if strippedUserID.startswith(' ') or strippedUserID.startswith('/krill'):strippedUserID = None

        if strippedUserID == None:print('no option specified!'); finalMessage = 'Unknown Command! Got: Null\nuse ?krill about for a list of commands.'

        if not strippedUserID == None and strippedUserID.startswith('<@'):finalMessage = getKrillMessage(strippedUserID)

        #print('userID:"' + strippedUserID + '"')
        #print('messageContent:' + messageContent)
        if lowercaseMessage.startswith('/krill <@'):
            try:await message.delete()
            except:
                log_critical(filname, "Can't Delete Message! Does the bot have sufficient permissions?"); 
                print("Can't Delete Message! Does the bot have sufficient permissions?")
        try:await message.channel.send(finalMessage)
        except:
            log_critical(filname, "Can't Send Message! Does the bot have sufficient permissions?") 
            print("Can't Send Message! Does the bot have sufficient permissions?")

#Funny Command
    if lowercaseMessage.startswith('?levelup'):
        #author = '<@' + str(message.author.id) + '>(@' + str(message.author) + ') ran the krill help command | Full command ran: "' + message.content + '"'
        author = make_author_string(str(message.author), message.author.id, 'levelup', message.content, message.channel.id, message.guild.name)
        print(author); 
        log_info(filname, timeString + author)

        try:await message.channel.send('I dunno\n-# You Level up by simply talking :3c')
        except:
            log_critical(filname, "Can't Send Message! Does the bot have sufficient permissions?")
            print(timeString + "Can't Send Message! Does the bot have sufficient permissions?")
        

#info and help commands
    if lowercaseMessage.startswith('?krill'):
        #Check the date, and if its my birthday, add a subtext formatted message!
        birthdaymsg = ''
        dateNow = str(datetime.today().strftime('%m/%d'))
        if dateNow == '08/18':birthdaymsg = '\n-# Today is Char\'s Birthday (The guy who coded this bot.)'

        if lowercaseMessage.startswith('?krill help'):
            #author = '<@' + str(message.author.id) + '>(@' + str(message.author) + ') ran the krill help command | Full command ran: "' + message.content + '"'
            author = make_author_string(str(message.author), message.author.id, 'krill help', message.content, message.channel.id, message.guild.name)
            print(author); 
            log_info(filname, author)

            try:await message.channel.send('Krill Command Useage:\n/krill <@userID>/@user (e.g. <@300020084808744962>)\n\n-# For problems with the krill you bot, please dm me at @annyconducter, with your problem, and your server\'s name')
            except:
                log_critical(filname, "Can't Send Message! Does the bot have sufficient permissions?") 
                print("Can't Send Message! Does the bot have sufficient permissions?")

        if lowercaseMessage.startswith('?krill about'):
            readme = get_readme(True)
            
            
            author = make_author_string(str(message.author), message.author.id, 'krill about', message.content, message.channel.id, message.guild.name)
            print(author); 
            log_info(filname, author)

            try:await message.channel.send(readme + birthdaymsg, suppress_embeds=(True))
            except:
                log_critical(filname, "Can't Send Message! Does the bot have sufficient permissions?")
                print(timeString + "Can't Send Message! Does the bot have sufficient permissions?")
        
        
        if lowercaseMessage.startswith('?krill privacypolicy'):
            privacyPolicy = get_privacy_policy(True)
            
            author = make_author_string(str(message.author), message.author.id, 'krill privacypolicy', message.content, message.channel.id, message.guild.name)
            print(author); 
            log_info(filname, author)

            try:await message.channel.send(privacyPolicy, suppress_embeds=(True))
            except:
                log_critical(filname, "Can't Send Message! Does the bot have sufficient permissions?")
                print(timeString + "Can't Send Message! Does the bot have sufficient permissions?")

        if lowercaseMessage.startswith('?krill tos'):
            tos = get_tos(True)
            
            author = make_author_string(str(message.author), message.author.id, 'krill tos', message.content, message.channel.id, message.guild.name)
            print(author); 
            log_info(filname, author)

            try:await message.channel.send(tos, suppress_embeds=(True))
            except:
                log_critical(filname, "Can't Send Message! Does the bot have sufficient permissions?")
                print(timeString + "Can't Send Message! Does the bot have sufficient permissions?")

        if lowercaseMessage.startswith('?krill version'):
            isOutdated = False
            if not ver.endswith('-testver'):
                gitVer = get_gitVer()
                if not str(gitVer).strip() == ver:
                    if not gitVer == None:print('Update Available! Check the github!'); 
                    log_info(filname, 'Update available! CurVersion: v' + ver + ' | gitVer: v' + gitVer)
                    isOutdated = True

            author = make_author_string(str(message.author), message.author.id, 'krill version', message.content, message.channel.id, message.guild.name)
            print(author); 
            log_info(filname, author)

            isOutdatedString = ''
            if isOutdated:isOutdatedString = '\n-# This Version may be outdated, a testing version, or github is being annoying and not properly updating'

            print('isOutdated? ' + str(isOutdated))

            try:await message.delete()
            except:
                log_critical(filname, "Can't Delete Message! Does the bot have sufficient permissions?")
                print(timeString + "Can't Delete Message! Does the bot have sufficient permissions?")
            try:await message.channel.send('The current version is: v' + ver + '\n\n the current version\'s changelog is:\n\n' + changelog + birthdaymsg + isOutdatedString, suppress_embeds=(True))
            except:
                log_critical(filname, "Can't Send Message! Does the bot have sufficient permissions?")
                print(timeString + "Can't Send Message! Does the bot have sufficient permissions?")
            
            
try:client.run(botKey)
except:
    log(filname, '[STARTUP]: Invalid Bot Key!! got: ' + botKey, '[FATAL]:', False)
    print('[STARTUP]: FATAL: Invalid key! got: ' + botKey)