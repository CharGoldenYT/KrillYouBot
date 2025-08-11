from modules.backend.krilljson.krillJson import parse_krillJson
from modules.commands.components.confighelp import getCommands

def get_setting(setting:str, path:str, gID:int, cID:int) -> (str | list[str]):
    try:
        settings = parse_krillJson(path, gID, cID)
        if setting == 'logschannel':
            return str(settings[0])
        if setting == 'sendonreadymessage':
            return str(settings[1])
        if setting == 'configprefix':
            return str(settings[2])
        if setting == 'allowbroadcasts':
            return str(settings[3])
        if setting == 'newversionbroadcastchannel':
            return str(settings[4])
    except Exception as e:
        return [f'Could not get setting `{setting}`: "`', str(e), '`"']

def set_setting(setting:str, v:str, gID:int, globalSettings:list)->(bool | str):
    from modules.backend.krilljson.krillJson import write_serverSettings as change_setting
    if setting == 'configprefix':
        return change_setting(gID, globalSettings[0], globalSettings[1], v, globalSettings[3], globalSettings[4])
        
    if setting == 'logschannel':
        try:
            int(v)
        except Exception as e:
            return f'Had an error setting `logsChannel`! "{str(e)}"'
        if globalSettings[4] == globalSettings[0]:
            return change_setting(gID, int(v), globalSettings[1], globalSettings[2], globalSettings[3], int(v))
        return change_setting(gID, int(v), globalSettings[1], globalSettings[2], globalSettings[3], globalSettings[4])
        
    if setting == 'newversionbroadcastchannel':
        try:
            int(v)
        except Exception as e:
            return f'Had an error setting `newversionbroadcastchannel`! "{str(e)}"'
        
        return change_setting(gID, globalSettings[0], globalSettings[1], globalSettings[2], globalSettings[3], int(v))
        
    if setting == 'sendonreadymessage':
        if not v == 'true' and not v == 'false':
            return f'Only valid options for `sendOnReadyMessage` are "true" or "false"! got {v}'
        if v == 'true':
            return change_setting(gID, globalSettings[0], True, globalSettings[2], globalSettings[3], globalSettings[4])
        if v == 'false':
            return change_setting(gID, globalSettings[0], False, globalSettings[2], globalSettings[3], globalSettings[4])
        
    if setting == 'allowbroadcasts':
        if not v == 'true' and not v == 'false':
            return f'Only valid options for `allowBroadcasts` are "true" or "false"! got {v}'
        if v == 'true':
            return change_setting(gID, globalSettings[0], globalSettings[1], globalSettings[2], True, globalSettings[4])
        if v == 'false':
            return change_setting(gID, globalSettings[0], globalSettings[1], globalSettings[2], False, globalSettings[4])
        
    return f"That's not a valid setting! `{setting}`"

def configure_setting(commands:list[str], path:str, gID:int, cID:int, serverSettings:list, prefix:str)->(None | bool | str | list[str]):
    length = commands.__len__()
    
    if length > 2:
        return "Too many arguments!"

    if length == 1:
        if ["?", "help"].__contains__(commands[0]):
            return getCommands(prefix)
        return get_setting(commands[0], path, gID, cID)
    

    return set_setting(commands[0], commands[1], gID, serverSettings)
