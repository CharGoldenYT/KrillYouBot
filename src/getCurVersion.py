#Literally only here so that i dont get import errors for looping imports
from datetime import datetime
#set up logging with current time
time = str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S'))
filname = "logs/krillYouBotLog-" + time + ".log"

def getCurVersion():
    return '2.2 Hotfix 2'

def get_filname():
    return filname