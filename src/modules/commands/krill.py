from datetime import datetime
import random

def getKrillMessage(userID:str):
    userID = userID.replace('<@ ', '')
    dateNow = str(datetime.today().strftime('%m/%d'))
    integer = 0
    message = ''
    message = 'Krilled ' + userID
    
    if dateNow == '04/01':
        integer = random.randrange(0,9,1); print('the random int is' + str(integer))
        if integer < 3:message = 'Not so shrimple now is it' + userID + '?'
        if integer < 6 and integer > 3:message = 'Krilled' + userID + '\n its as shrimple as that.'
        if integer < 10 and integer > 6:message = 'Shot' + userID + " :3"
    return message 
    