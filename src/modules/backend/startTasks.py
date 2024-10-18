from modules.commands.krillAbout import make_changelog
from modules.backend.betterLogs.betterLogs import *
from modules.commands.krillVersion import get_filname, compareVersions, getCurVersion
from discord.guild import Guild
from modules.backend.krillJson import initializeFTP

allowReturns = False
def check_allowReturns() -> bool:
    return allowReturns


def get_latestChangelog() -> str:
    print(f'''The current changelog is:\n{make_changelog()}\n\n''')
    return input('Does this look like the correct changelog?')

def create_logsFolders():
    import os

    try:
        os.makedirs('logs/')
    except OSError as e:
        if str(e).endswith("file already exists: 'logs/'"):
            print('Logs folder already exists, doing nothing!')
        if not str(e).endswith("file already exists: 'logs/'"):
            log_error(get_filname(), f'SHIT THERE WAS AN ERROR "{str(e)}"')

    try:
        os.makedirs('logs/old')
    except OSError as e:
        if str(e).endswith("file already exists: 'logs/old'"):
            print('Old logs folder already exists, doing nothing!')
        if not str(e).endswith("file already exists: 'logs/old'"):
            log_error(get_filname(), f'SHIT THERE WAS AN ERROR "{str(e)}"')

    try:
        os.makedirs('serverSettings/')
    except OSError as e:
        if str(e).endswith("file already exists: 'serverSettings/'"):
            print('Server Settings folder already exists, doing nothing!')
        if not str(e).endswith("file already exists: 'serverSettings/'"):
            log_error(get_filname(), f'SHIT THERE WAS AN ERROR "{str(e)}"')


def grab_serverSettings(servers:list[Guild]):
    import os
    isGrabbed = None
    for server in servers:
        path = f'serverSettings/serverID-{str(server.id)}_Settings.json'
        ftp = initializeFTP()
        ftp.cwd('htdocs/krillYouBot_ServerSettings')
        file = open(path, 'rb')
        fileCompare = open(f'serverID-{str(server.id)}_Settings.temp', 'wb')
        try:
            ftp.retrbinary(f'RETR {path}', fileCompare.write); fileCompare.close()
            fileCompare = open(f'serverID-{str(server.id)}_Settings.temp', 'rb')
            if not fileCompare == file:
                print('Files are different, replacing with upstream ver')
                isGrabbed = True
                file = open(path, 'wb'); file.writelines(fileCompare.readlines()); file.close(); fileCompare.close()
        except Exception as e:
            fileCompare.close()
            file.close()
            log_err(get_filname(), f'There was an error trying to grab server settings for {str(server.id)}: "{str(e)}"')
        os.remove(f'serverID-{str(server.id)}_Settings.temp')
    return isGrabbed

def run_startTasks():
    var = get_latestChangelog().lower()
    if var == 'n':
        log_warn(get_filname(), '[STARTUP]: Changelog potentially out of date! Make sure "modules.commands.krillAbout" was properly updated!', False)
    create_logsFolders()
    create_logFile(get_filname(), f'<!-- Created by Krill You Bot v{getCurVersion()}-->')
    if compareVersions() == False:
        log_warn(get_filname(), '[STARTUP]: New Update available! Check the github!', False, True)
    var = input('Allow showing returns of get functions?')
    if var.lower() == 'y':
        allowReturns = True