from discord.guild import Guild
from modules.backend.betterLogs.betterLogs import *
from modules.commands.krillVersion import get_filname

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
        channel = server.get_channel(channels[pos]); 
        try:
            await channel.send(message, suppress_embeds=suppressEmbeds)
        except Exception as e:
            log_err(get_filname(), f'Could not send message! {str(e)}')