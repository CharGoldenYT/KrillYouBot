# This generates the Readme used in the main krillyou.py
import os
import urllib.request as urllib
readme = ''
error = None

def get_readme():
    url = ''
    writeToFile = True
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/gameygu-0213/KrillYouBot/main/discord_readme.md').read().decode('utf-8'))
    except urllib.HTTPError as e: print('shit the url handler died lmao: ' + str(e)); writeToFile = False
    if writeToFile == True:file = open('discord_readme.md', 'w'); print('final file: "' + url + '"'); file.write(url); file.close()

    if os.path.exists('discord_readme.md'): readme = open('discord_readme.md'); readme = 'This was generated with the [GitHub "discord_readme"](https://github.com/gameygu-0213/KrillYouBot/blob/main/discord_readme.md):\n\n' + readme.read()
    
    if not os.path.exists('discord_readme.md'): print('discord_readme.md not found!'); error = "Couldn't find 'discord_readme.md'"; readme = "# Krill you bot (V1.2.1) - A Wacky simple Discord bot for krilling your friends!\n\n### Usage:\n`/krill <@userID>/@user` Krill any user\n`?krill help` Tells you how to use the bot\n`?krill about` Displays this message\n### In case the bot goes offline contact: @annyconducter on Discord.\n\n[GitHub](https://github.com/gameygu-0213/KrillYouBot)"

    print('get_readme returned: ' + readme)
    return readme


def get_error():
    if not os.path.exists('readme.md'): error = "Couldn't find 'discord_readme.md' using hardcoded string!"
    if os.path.exists('readme.md'): error = 'None' #just to be safe
    return error