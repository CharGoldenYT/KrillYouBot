from modules.commands.krillAbout import make_changelog
from inspect import currentframe, getframeinfo
from globalStuff import get_filname, compareVersions, curVersion, logger
from discord.guild import Guild
from modules.backend.krillJson import pullServerSettings, initSite

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

allowReturns = False
def check_allowReturns() -> bool:
    return allowReturns


def get_latestChangelog() -> str:
    print(f'''{bcolors.OKBLUE}The current changelog is:\n{make_changelog()}\n\n''')
    return input('Does this look like the correct changelog?')

def create_logsFolders():
    import os

    try:
        os.makedirs('logs/')
    except OSError as e:
        if str(e).endswith("file already exists: 'logs/'"):
            print('Logs folder already exists, doing nothing!')
        if not str(e).endswith("file already exists: 'logs/'"):
            logger.log_error(f'SHIT THERE WAS AN ERROR "{str(e)}"', True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)

    try:
        os.makedirs('logs/old')
    except OSError as e:
        if str(e).endswith("file already exists: 'logs/old'"):
            print('Old logs folder already exists, doing nothing!')
        if not str(e).endswith("file already exists: 'logs/old'"):
            logger.log_error(f'SHIT THERE WAS AN ERROR "{str(e)}"', True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)
            
    try:
        os.makedirs('logs/movingLogs')
    except OSError as e:
        if str(e).endswith("file already exists: 'logs/movingLogs'"):
            print('Old logs folder already exists, doing nothing!')
        if not str(e).endswith("file already exists: 'logs/movingLogs'"):
            logger.log_error(f'SHIT THERE WAS AN ERROR "{str(e)}"', True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)

    try:
        os.makedirs('serverSettings/')
    except OSError as e:
        if str(e).endswith("file already exists: 'serverSettings/'"):
            print('Server Settings folder already exists, doing nothing!')
        if not str(e).endswith("file already exists: 'serverSettings/'"):
            logger.log_error(f'SHIT THERE WAS AN ERROR "{str(e)}"', True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)


def grab_serverSettings(servers:list[Guild]):
    return pullServerSettings()

def run_startTasks():
    create_logsFolders()
    initSite()

    result = get_latestChangelog().lower()
    if result == 'n':
        logger.log_warn('[STARTUP]: Changelog potentially out of date! Make sure "modules.commands.krillAbout" was properly updated!', False)

    if compareVersions() == False:
        logger.log_header('[STARTUP]: New Update available! Check the github!', 'warn', False)