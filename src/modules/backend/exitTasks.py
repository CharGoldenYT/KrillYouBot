from modules.backend.betterLogs.betterLogs import *; from modules.commands.krillAbout import get_filname
import time, shutil, os
filename = get_filname()
filname = filename # So i dont have to rename shit

'''
def cleanup():
    import time
    log_info(filname, '[EXIT]: CLEANING UP', False)
    end_log(filname)
    print(bcolors.OKBLUE + 'Closing in 5 Seconds!')
    doLogMove()
    time.sleep(5)
    print("closing!" + bcolors.ENDC)
atexit.register(cleanup)
'''
#move log files, we don't need to clutter the main folder
def doLogMove():
    try:
        for file in os.listdir('logs/'):
            for extension in ['.txt', '.log']:
                if file.endswith(extension) and file != filname:
                    success = True
                    try:shutil.move('logs/' + file, 'logs/old/' + file, )
                    except shutil.Error as e:
                        message = '[EXIT]: Error Moving File "' + file + '" Error: ' + str(e)
                        #print(message)
                        log(filname, message, '[ERROR]:', False)
                        success = False
                    if success:
                        log_info(filename, f'[EXIT]: Moved File "{file}" successfully!', False, True)
    except OSError as e:
        message = '[EXIT]: Error Moving logs! "' + str(e) + '"'
        if str(e).endswith("'" + filname + "'"): message = None
        #if message != None:print(bcolors.FAIL + message + bcolors.ENDC)
        if message != None:log(filname, message, '[ERROR]:', False)

def doExitTasks():
    log_info(filename, '[EXIT]: CLEANING UP', False)
    doLogMove()
    end_log(filename)
    print('\033[94mClosing in 5 Seconds!')
    time.sleep(5)
    print("closing!" + bcolors.ENDC)