from modules.commands.krillAbout import make_changelog
from modules.backend.betterLogs.betterLogs import *
from modules.commands.krillVersion import get_filname, compareVersions, getCurVersion

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
            log_error(f'SHIT THERE WAS AN ERROR "{str(e)}"')

    try:
        os.makedirs('logs/old')
    except OSError as e:
        if str(e).endswith("file already exists: 'logs/old'"):
            print('Old logs folder already exists, doing nothing!')
        if not str(e).endswith("file already exists: 'logs/old'"):
            log_error(f'SHIT THERE WAS AN ERROR "{str(e)}"')

def run_startTasks():
    var = get_latestChangelog().lower()
    if var == 'n':
        log_warn(get_filname(), '[STARTUP]: Changelog potentially out of date! Make sure "modules.commands.krillAbout" was properly updated!', False)
    create_logsFolders()
    create_logFile(get_filname(), f'<!-- Created by Krill You Bot v{getCurVersion()}-->\n')
    if compareVersions() == False:
        log_warn(get_filname(), '[STARTUP]: New Update available! Check the github!', False, True)
    var = input('Allow showing returns of get functions?')
    if var.lower() == 'y':
        allowReturns = True