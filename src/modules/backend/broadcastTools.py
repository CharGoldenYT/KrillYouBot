from discord.guild import Guild
from modules.backend.betterLogs.betterLogs import *
from globalStuff import get_filname


def search_betweenDelimiters(string:str, start:str, end:str):
    start_index = string.find(start)
    if start_index == -1:
        return None

    end_index = string.find(end, start_index)
    if end_index == -1:
        return None

    return string[start_index:end_index]  

def replace_annoncementString(string:str)->str:
    newString = string
    if string.startswith('{&news:newVersion'):
        version = f'v{search_betweenDelimiters(string, '[', ']')}'.replace('[', '')
        if search_betweenDelimiters(string, '[', ']') == None:
            version = 'Not Specified'
        newString = f'Testing has begun for a new version, {version}! make sure to report bugs to the [Github](https://github.com/CharGoldenYT/KrillYouBot/issues)\n-# This message was generated with `?krill broadcast {string}` | Beta releases will not have a date on the changelog.'

    return newString

async def broadcast_readyMessage(servers:list[Guild], channels:list[int]):
    pos = -1
    for server in servers:
        pos += 1
        channel = server.get_channel(channels[pos])
        try:
            await channel.send('Krill You Bot online!')
        except Exception as e:
            log_err(get_filname(), f'Could not send message for server {channel.guild.id}({channel.guild.name})! {str(e)}')

async def broadcast_closeMessage(servers:list[Guild], channels:list[int]):
    pos = -1
    for server in servers:
        pos += 1
        channel = server.get_channel(channels[pos])
        try:
            await channel.send('Krill You Bot is down!')
        except Exception as e:
            log_err(get_filname(), f'Could not send message for server {channel.guild.id}({channel.guild.name})! {str(e)}')

# The feature that started this whole recode.
async def broadcast_announcement(servers:list[Guild], channels:list[int], message:str, suppressEmbeds:bool = False):
    pos = -1
    for server in servers:
        pos += 1
        channel = server.get_channel(channels[pos])
        try:
            await channel.send(replace_annoncementString(message), suppress_embeds=suppressEmbeds)
        except Exception as e:
            log_err(get_filname(), f'Could not send message! {str(e)}')