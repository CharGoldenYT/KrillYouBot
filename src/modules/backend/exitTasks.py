from modules.backend.betterLogs.betterLogs import *
from globalStuff import curVersion, get_filname
import time, shutil, os
from datetime import datetime
filname = get_filname()


#move log files, we don't need to clutter the main folder
def doLogMove():
    dtime = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))
    filename = f'logs/movingLogs/moveLogs-{dtime}.log'
    try:
        create_logFile(filename, f'<!-- Created by Krill You Bot v{curVersion}-->')
        for file in os.listdir('logs/'):
            for extension in ['.txt', '.log']:
                if file.endswith(extension) and file != filname:
                    success = True
                    try:shutil.move('logs/' + file, 'logs/old/' + file, )
                    except shutil.Error as e:
                        message = '[EXIT]: Error Moving File "' + file + '" Error: ' + str(e)
                        #print(message)
                        log(filename, message, '[ERROR]:', False)
                        success = False
                    if success:
                        log_info(filename, f'[EXIT]: Moved File "{file}" successfully!', False, True)
        end_log(filename)
    except OSError as e:
        message = '[EXIT]: Error Moving logs! "' + str(e) + '"'
        if str(e).endswith("'" + filname + "'"): message = None
        #if message != None:print(bcolors.FAIL + message + bcolors.ENDC)
        if message != None:log(filname, message, '[ERROR]:', False)

def doExitTasks():
    log_info(filname, '[EXIT]: CLEANING UP', False)
    end_log(filname)
    doLogMove()
    print('\033[94mClosing in 5 Seconds!')
    time.sleep(5)
    print("closing!" + bcolors.ENDC)