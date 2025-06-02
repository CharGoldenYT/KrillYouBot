r'''This python script contains functions meant to handle the processing of Krill You Bot's server specific settings.'''
from ftplib import FTP
import json as pyJson
import os
from discord.client import Client
from globalStuff import logger
from inspect import currentframe, getframeinfo

def legacy_SettingsCheck(gID:int):
    r'''From earlier testing, i used a different file name format so yknow.'''
    path = f'serverSettings/ID-{str(gID)}_settings.format'
    newPath = f'serverSettings/serverID-{str(gID)}_Settings.json'
    if os.path.isfile(path):
        print(f'{path} Exists, renaming!')
        fileToRename = open(path, 'r').read()
        file = open(newPath, 'w'); file.write(fileToRename); file.close
        os.remove(path)

def initializeFTP():
    r'''What the fuck you think this does, makes you suddenly have a giant bowl a' cereal?'''
    try:
        ftpSettings = open('botStuff/settings.txt', 'r').read().split('|'); ftp = FTP(ftpSettings[0], ftpSettings[1], ftpSettings[2]); return ftp
    except Exception as e:
        logger.log_err(f'SHIT THERE WAS AN ERROR! "{str(e)}"', True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno); return None
    
    
from discord.guild import Guild
def initializeSettings(gID:int, cID:int) -> str:
    file = open(f'serverSettings/serverID-{str(gID)}_Settings.json', 'w')
    file.write('''{\n   "serverSettings": {\n       "logsChannel": ''' + str(cID) +''',\n       "sendOnReadyMessage": true,\n       "allowBroadcasts": true,\n       "configPrefix": "?"\n   }\n}''')
    file.close()
    return ('''{\n   "serverSettings": {''' + 
             '''\n       "logsChannel": ''' + str(cID) +
            ''',\n       "newVersionBroadcastChannel": ''' + str(cID) +
            ''',\n       "sendOnReadyMessage": true'''+
            ''',\n       "allowBroadcasts": true'''+
            ''',\n       "configPrefix": "?"\n   }\n}''')


def get_firstAvailableChannel(guild:Guild, client:Client) -> int:
    foundChannel = False
    for channel in guild.channels:
        if not foundChannel:
            cID = channel.id
            permissions = channel.permissions_for(guild.get_member(client.user.id))
            if permissions.send_messages:
                foundChannel = True
                return cID
            
            
# The following are ran when using "?krill settings" or "?krill config"

def new_Json(gID:int, cID:int, bool:bool, prefix:str, allowBroadcasts:bool, newVersionBroadcastChannel:int) -> bool:
    r'''ok so basically, tries to write to a path determined by the gID, if it cant, it returns False, else True.'''
    try:
        file = open(f'serverSettings/serverID-{str(gID)}_Settings.json', 'w')
        file.write('''{\n   "serverSettings": {''' +
                    '''\n       "logsChannel": ''' + str(cID) +
                   ''',\n       "newVersionBroadcastChannel": ''' + str(newVersionBroadcastChannel) +
                   ''',\n       "sendOnReadyMessage": ''' + str(bool).lower() + 
                   ''',\n       "allowBroadcasts": ''' + str(allowBroadcasts).lower() + 
                   ''',\n       "configPrefix": "''' + prefix +
                   '''"\n   }\n}''')
        file.close()
        return True
    except Exception as e:
        print(f'ERROR! "{str(e)}"')
        return False
            
def checkFor_outdatedJsons(path:str, gID:int):
    rawJson = open(path, 'r').read()
    json = pyJson.loads(rawJson)
    json = json['serverSettings']
    try:
        var = json['allowBroadcasts']
        #print(f'{path} is up to date!')
    except Exception as e:
        if str(e).__contains__('allowBroadcasts'):
            print(f'{path} is malformed or outdated!')
            change_setting(gID, json["logsChannel"], json["sendOnReadyMessage"], json["configPrefix"], json["sendOnReadyMessage"], json["logsChannel"])
            return # return since its such an old file it wouldn't have "allowBroadcasts" in it.
    
    try:
        var = json['newVersionBroadcastChannel']
    except Exception as e:
        if str(e).__contains__('newVersionBroadcastChannel'):
            print(f'{path} is malformed or outdated!')
            change_setting(gID, json["logsChannel"], json["sendOnReadyMessage"], json["configPrefix"], json["allowBroadcasts"], json["logsChannel"])
            return # In case of future additions, return since the older file would already be 2 versions behind anyway.



def parse_krillJson(path:str, gID:int, cID:int, client:(None | Client) = None) -> list:
    r'''This makes it possible to read stored server data.'''

    checkFor_outdatedJsons(path, gID)
    try:
        file = open(path, 'r').read()
        json = pyJson.loads(file)
        json = json['serverSettings']
        return [json["logsChannel"], json["sendOnReadyMessage"], json["configPrefix"], json['allowBroadcasts'], json['newVersionBroadcastChannel']]
    except Exception as e:
        print(f'Cant parse {path}! "{e}"')
        firstChannel = get_firstAvailableChannel(client.get_guild(gID))
        if client == None:
            rawJson = initializeSettings(gID, cID)
            json = pyJson.loads(rawJson); json = json['serverSettings']
            return [cID, False, '?', False, firstChannel]
        if not client == None:
            rawJson = initializeSettings(gID, firstChannel, client)
            json = pyJson.loads(rawJson); json = json['serverSettings']
            return [json["logsChannel"], json["sendOnReadyMessage"], json["configPrefix"], json['allowBroadcasts'], json['newVersionBroadcastChannel']]

def write_cloudSettings(gID:int):
    path = f'serverSettings/serverID-{str(gID)}_Settings.json'
    fileToWrite = open(path, 'rb')
    try:
        ftp = initializeFTP(); ftp.cwd('htdocs/krillYouBot_ServerSettings'); ftp.storlines(f'STOR {path}', fileToWrite); ftp.close()
        return None
    except Exception as e:
        return f'SHIT HAD AN ERROR {str(e)}'


def change_setting(gID:int, logsChannel:int, sendOnReadyMessage:bool, prefix:str, allowBroadcasts:bool, newVersionBroadcastChannel:int):
    path = f'serverSettings/serverID-{str(gID)}_Settings.json'
    print(f'Overwriting "{path}"!')
    if new_Json(gID, logsChannel, sendOnReadyMessage, prefix, allowBroadcasts, newVersionBroadcastChannel):
        """ print('Uploading to FTP!')
        var = write_cloudSettings(gID) """ # FTP SHIT BROKEY.
        return None