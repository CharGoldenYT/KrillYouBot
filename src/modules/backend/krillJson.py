r'''This python script contains functions meant to handle the processing of Krill You Bot's server specific settings.'''
from modules.backend.neocitiesHandler import NeocitiesHandler
import json as pyJson
import os
from discord.client import Client
from globalStuff import logger
from inspect import currentframe, getframeinfo
from modules.backend.broadcastTools import search_betweenDelimiters

def initSite()->NeocitiesHandler:
    try:
        rawJson = open('botStuff/neocitiesSettings.json', 'r')
        json = pyJson.loads(rawJson.read()); rawJson.close()
        return NeocitiesHandler(json['name'], json['pass'], json["fullURL"])
    except Exception as e:
        logger.log_err(f'SHIT THERE WAS AN ERROR! "{str(e)}"', True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)

ncSite:NeocitiesHandler = initSite()
    
from discord.guild import Guild
def get_firstAvailableChannel(guild:Guild, client:Client) -> int:
    foundChannel = False
    for channel in guild.channels:
        if not foundChannel:
            cID = channel.id
            permissions = channel.permissions_for(guild.get_member(client.user.id))
            if permissions.send_messages:
                foundChannel = True
                return cID

def legacy_SettingsCheck(gID:int):
    r'''From earlier testing, i used a different file name format so yknow.'''
    path = f'serverSettings/ID-{str(gID)}_settings.format'
    newPath = f'serverSettings/serverID-{str(gID)}_Settings.json'
    if os.path.isfile(path):
        print(f'{path} Exists, renaming!')
        fileToRename = open(path, 'r').read()
        file = open(newPath, 'w'); file.write(fileToRename); file.close
        os.remove(path)

def retrieveSettings(gID:int):
    if ncSite == None: logger.log_warn('HEY, YOU DIDN\'T PROVIDE NEOCITIES SITE DETAILS, YOU CANNOT ACCESS A BACKUP!', True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno); return
    newSettings = ncSite.retrieveText(f'serverSettings/serverID-{str(gID)}_Settings.json')
    if newSettings == None: return

    file = open(f'serverSettings/serverID-{str(gID)}_Settings.json', 'w')
    file.write(newSettings)
    file.close()

def updateRemoteSettings(gID:str):
    if ncSite == None: logger.log_warn('HEY, YOU DIDN\'T PROVIDE NEOCITIES SITE DETAILS, YOU CANNOT MAKE A BACKUP!', True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno); return
    return ncSite.addFile(f'serverSettings/serverID-{str(gID)}_Settings.json')


def write_serverSettings(gID:int, cID:int, bool:bool, prefix:str, allowBroadcasts:bool, newVersionBroadcastChannel:int)->bool:
    retrieveSettings(gID) # Always update the local copy BEFORE writing.

    try: os.read('serverSettings/')
    except:
        try:os.mkdir('serverSettings/')
        except OSError as e: pass
    file = open(f'serverSettings/serverID-{str(gID)}_Settings.json', 'w')
    file.write('''{\n   "serverSettings": {''' +
                    '''\n       "logsChannel": ''' + str(cID) +
                   ''',\n       "newVersionBroadcastChannel": ''' + str(newVersionBroadcastChannel) +
                   ''',\n       "sendOnReadyMessage": ''' + str(bool).lower() + 
                   ''',\n       "allowBroadcasts": ''' + str(allowBroadcasts).lower() + 
                   ''',\n       "configPrefix": "''' + prefix +
                   '''"\n   }\n}''')
    file.close()
    
    updateRemoteSettings(gID)
    return None

def pullServerSettings():
    try: os.read('./serverSettings/')
    except OSError as e: logger.log_err(f'COULD NOT OPEN FOLDER `./serverSettings/` "{e}"!', True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno); return False
    
    for file in os.read('./serverSettings/'):
        gID = search_betweenDelimiters(file, 'serverID-', '_Settings.json')
        if gID != None: retrieveSettings(gID)

def get_Json(gID:int)->(str|None):
    try:
        file = open(f'serverSettings/serverID-{str(gID)}_Settings.json', 'r')
        s = file.read(); file.close()
        return s
    except Exception as e:
        logger.log_err('Could not open `' + f'serverSettings/serverID-{str(gID)}_Settings.json' + '`!', True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno); return None

def checkSettings(gID):
    try:
        file = open(f'serverSettings/serverID-{str(gID)}_Settings.json', 'r')
        json = pyJson.loads(file.read())['serverSettings']; file.close()

        try: test = json["allowBroadcasts"]
        except Exception as e: write_serverSettings((gID, json["logsChannel"], json["sendOnReadyMessage"], json["configPrefix"], json["sendOnReadyMessage"], json["logsChannel"]))
    
        try: test = json['newVersionBroadcastChannel']
        except Exception as e: write_serverSettings(gID, json["logsChannel"], json["sendOnReadyMessage"], json["configPrefix"], json["allowBroadcasts"], json["logsChannel"])
    
    except Exception as e:
        logger.log_err('Could not open `' + f'serverSettings/serverID-{str(gID)}_Settings.json' + '`!', True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno); return

def parse_krillJson(gID:int, cID:int, client:(None | Client) = None) -> list:
    legacy_SettingsCheck(gID)
    checkSettings(gID)
    
    json = get_Json(gID)

    if json == None:
        write_serverSettings(gID, cID, True, '?', True, cID)
        json = get_Json(gID)

    json = pyJson.loads(json)["serverSettings"]

    return [json["logsChannel"], json["sendOnReadyMessage"], json["configPrefix"], json['allowBroadcasts'], json['newVersionBroadcastChannel']]