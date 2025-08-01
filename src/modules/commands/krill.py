from datetime import datetime
import random

def getKrillMessage(userID:str):
    userID = userID.replace('<@ ', '').replace("<@", "").replace("/krill", "")
    dateNow = str(datetime.today().strftime('%m/%d'))
    integer = 0
    message = ''
    message = 'Krilled ' + userID
    
    if dateNow == '04/01':
        integer = random.randrange(0,9,1); print('the random int is' + str(integer))

        match integer:
            case 1 | 2 | 3:message = 'Not so shrimple now is it' + userID + '?'
            case 4 | 5 | 6:message = 'Krilled' + userID + '\n its as shrimple as that.'
            case _:message = 'Shot' + userID + " :3"
    return message 
    