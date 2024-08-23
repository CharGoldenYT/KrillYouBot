# Better logging system that actually fucking works
# Fuck you python logger!
# Yes its a lot of redirect functions, but fuck you.
from datetime import datetime
from inspect import currentframe, getframeinfo

def create_logFile(filename:str, beforeBeginning:str = ''):
    try:
        logging = open(filename, 'a')
        if beforeBeginning != '': beforeBeginning = beforeBeginning + '\n'
        logging.write(beforeBeginning + '<!-- Better Logs by Char @annyconducter on Discord -->\n<!-- START OF LOG -->\n'); logging.close()
    except Exception as e:
       frameinfo = getframeinfo(currentframe()); print('[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + '] Error with file"' + filename + '": "' + str(e) + '"')

def log(filename:str, log:str, level:str = '', showTime:bool = True):
    time = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))
    timeString = '[' + time + ']: '
    if not showTime: timeString = ''
    try:
        logging = open(filename, 'a'); logging.write(level + timeString + log + '\n'); logging.close()
    except Exception as e:
        frameinfo = getframeinfo(currentframe());print('[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + '] Error with file"' + filename + '": "' + str(e) + '"')

def log_info(filename:str, v:any, showTime:bool = True):
    v = str(v)
    log(filename, v, '[INFO]:', showTime)

def log_warning(filename:str, v:any, showTime:bool = True):
    v = str(v)
    log(filename, v, '[WARN]:', showTime)

def log_warn(filename:str, v:any, showTime:bool = True):
    log_warning(filename, v, showTime)

def log_error(filename:str, v:any, showTime:bool = True):
    v = str(v)
    log(filename, v, '[ERR]:', showTime)

def log_err(filename:str, v:any, showTime:bool = True):
    log_error(filename, v, showTime)

def log_critical(filename:str, v:any, showTime:bool = True):
    v = str(v)
    log(filename, v, '[CRITICAL]:', showTime)

def log_fatal(filename:str, v:any, showTime:bool = True):
    v = str(v)
    log(filename, v, '[FATAL]:', showTime)

def end_log(filename:str):
    try:
        logging = open(filename, 'a'); logging.write('<!--  END OF LOG  -->'); logging.close()
    except Exception as e:
        frameinfo = getframeinfo(currentframe()); print('[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + '] Error with file"' + filename + '": "' + str(e) + '"')
    