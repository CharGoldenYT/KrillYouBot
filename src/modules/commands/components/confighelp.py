# This file here to keep checkMessage from being too confusing looking, and to make it easier to add new commands.

commands:list[str] = [
    '# Krill Options',

    '''`logsChannel` changes the channel where broadcasted messages (Like on ready messages for example) go! 
-# ***MUST BE THE CHANNEL'S ID NUMBER*** https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID''',

'''`newVersionBroadcastChannel` changes the channel where new version announcements go! 
-# ***MUST BE THE CHANNEL'S ID NUMBER*** https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID''',

    '`sendOnReadyMessage` Whether to allow sending a message when the krill you bot goes online!',

    "`configPrefix` Change the system command's prefix (such as how right now this very command is `<settingsPrefix>krill configure help`)",

    '`allowBroadcasts` Whether you want to receive broadcasted messages.',

    '# These settings (and this help page) are able to be viewed by anyone in the server! just add a ? or help to the end (e.g. `<settingsPrefix>krill configure logsChannel ?`)',

    '-# If you need help, or settings dont seem to actually work, contact @annyconducter on discord! or visit https://github.com/CharGoldenYT/KrillYouBot/issues'
]

def replaceWithPrefix(string:str, sub:str, prefix:str) -> str:
    r'''Replaces part of a string with a prefix

    `sub`: The part of the string to replace

    `prefix`: what prefix to replace it with.'''
    return string.replace(sub, prefix)


def getCommands(settingsPrefix:str):
    finalString = ''
    for command in commands:
        command = replaceWithPrefix(command, '<settingsPrefix>', settingsPrefix)
        finalString += f'{command}\n\n'
    return finalString.rstrip().lstrip()

