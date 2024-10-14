# Better logging system that actually fucking works
# Fuck you python logger!
# Yes its a lot of redirect functions, but fuck you.
from datetime import datetime
from inspect import currentframe, getframeinfo
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

version = '2'

def create_logFile(filename:str, beforeBeginning:str = ''):

    r'''Creates a log file with a given filename, and writes a header to it'''

    try:
        logging = open(filename, 'a')
        if beforeBeginning != '': beforeBeginning = beforeBeginning + '\n'
        logging.write(beforeBeginning + f'<!-- Log Generator: "Better Logs V{version}" | Better Logs by Char @annyconducter on Discord | https://github.com/CharGoldenYT/betterLogs -->\n<!-- START OF LOG -->\n'); logging.close()
    except Exception as e:
       frameinfo = getframeinfo(currentframe()); print('[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + '] Error with file"' + filename + '": "' + str(e) + '"')

def log(filename:str, log:str, level:str = '', showTime:bool = True, isHeader:bool = False, doPrinting:bool = True):

    r'''This Function writes a log with the given level and string to write to the given file.

    filename:String | Self explanatory

    log:String | The log youd wish to write to a file

    level:String | What should appear before the time string (e.g. '[WARN]:')

    showTime:Bool | Whether to show the timestamp before the written log

    isHeader:Bool | Whether, if printing, to override the level color with the header tag

    doPrinting:Bool | Whether to also print the log.'''


    time = str(datetime.today().strftime('%d-%m-%Y %H:%M:%S'))
    timeString = '[' + time + ']: '

    color = ''
    if level == '[INFO]:':color = bcolors.OKBLUE
    if level == '[WARN]:':color = bcolors.WARNING
    if level == '[ERR]:':color = bcolors.FAIL
    if level == '[CRITICAL]:':color = bcolors.FAIL
    if level == '[FATAL]:':color = bcolors.FAIL
    if isHeader:color = bcolors.HEADER

    if not showTime: timeString = ''

    logString = level + timeString + log

    if doPrinting: print(color + logString + bcolors.OKBLUE)

    if logString.__contains__('(Session ID:'):logString = logString.split('(')
    if isinstance(logString, list):logString = logString[0]

    try:
        logging = open(filename, 'a'); logging.write(logString + '\n'); logging.close()
    except Exception as e:
        frameinfo = getframeinfo(currentframe());print('[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + '] Error with file"' + filename + '": "' + str(e) + '"')

def log_info(filename:str, v:any, showTime:bool = True, isHeader:bool = False, doPrinting:bool = True):

    r'''Redirect function to log() as a shortcut to not have to write the level each time.
    
    Refer to log() for the variable purposes'''

    v = str(v)
    log(filename, v, '[INFO]:', showTime, isHeader, doPrinting)

def log_warning(filename:str, v:any, showTime:bool = True, isHeader:bool = False, doPrinting:bool = True):

    r'''Redirect function to log() as a shortcut to not have to write the level each time.
    
    Refer to log() for the variable purposes'''

    v = str(v)
    log(filename, v, '[WARN]:', showTime, isHeader, doPrinting)

def log_warn(filename:str, v:any, showTime:bool = True, isHeader:bool = False, doPrinting:bool = True):

    r'''Redirect function to log_warning() as a shortcut'''

    log_warning(filename, v, showTime, isHeader, doPrinting)

def log_error(filename:str, v:any, showTime:bool = True, isHeader:bool = False, doPrinting:bool = True):

    r'''Redirect function to log() as a shortcut to not have to write the level each time.
    
    Refer to log() for the variable purposes'''

    v = str(v)
    log(filename, v, '[ERR]:', showTime, isHeader, doPrinting)

def log_err(filename:str, v:any, showTime:bool = True, isHeader:bool = False, doPrinting:bool = True):

    r'''Redirect function to log_error() as a shortcut'''

    log_error(filename, v, showTime, isHeader, doPrinting)

def log_critical(filename:str, v:any, showTime:bool = True, isHeader:bool = False, doPrinting:bool = True):

    r'''Redirect function to log() as a shortcut to not have to write the level each time.
    
    Refer to log() for the variable purposes'''

    v = str(v)
    log(filename, v, '[CRITICAL]:', showTime, isHeader, doPrinting)

def log_fatal(filename:str, v:any, showTime:bool = True, isHeader:bool = False, doPrinting:bool = True):

    r'''Redirect function to log() as a shortcut to not have to write the level each time.
    
    Refer to log() for the variable purposes'''

    v = str(v)
    log(filename, v, '[FATAL]:', showTime, isHeader, doPrinting)

def end_log(filename:str):
    try:
        logging = open(filename, 'a'); logging.write('<!--  END OF LOG  -->'); logging.close()
    except Exception as e:
        frameinfo = getframeinfo(currentframe()); print('[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + '] Error with file"' + filename + '": "' + str(e) + '"')
    