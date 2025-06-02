from chars_betterlogs.logs import bcolors, Logging
from globalStuff import curVersion, filname, logger as global_logger
import time, shutil, os
from inspect import currentframe, getframeinfo
from datetime import datetime

logger:Logging

#move log files, we don't need to clutter the main folder
def doLogMove():
    dtime = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))
    filename = f'logs/movingLogs/moveLogs-{dtime}.log'
    logger = Logging(f'moveLogs-{dtime}.log', f'<!-- Created by Krill You Bot v{curVersion}-->')
    logger._set_filename(filename)
    try:
        for file in os.listdir('logs/'):
            for extension in ['.xml', '.log']:
                if file.endswith(extension) and file != filname:
                    success = True
                    try:shutil.move('logs/' + file, 'logs/old/' + file, )
                    except shutil.Error as e:
                        message = '[EXIT]: Error Moving File "' + file + '" Error: ' + str(e)
                        #print(message)
                        logger.log( message, '[ERROR]:', False, False, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)
                        success = False
                    if success:
                        logger.log_info(f'[EXIT]: Moved File "{file}" successfully!', False, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)
    except OSError as e:
        message = '[EXIT]: Error Moving logs! "' + str(e) + '"'
        if str(e).endswith("'" + filname + "'"): message = None
        #if message != None:print(bcolors.FAIL + message + bcolors.ENDC)
        if message != None:logger.log(message, '[ERROR]:', False)
    logger.close()

def doExitTasks():
    global_logger.log_info('[EXIT]: CLEANING UP', False)
    global_logger.close()
    doLogMove()
    print('\033[94mClosing in 5 Seconds!')
    time.sleep(5)
    print("closing!" + bcolors.ENDC)