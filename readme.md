# IMPORTANT - VERSIONING

If you make a new Krill You Bot release the tag has to be readable to the bot, and set to the same version string as the bot's current version.

(e.g 3.2 Hotfix 2's tag has to be 3.2h-2 both in the bot and the tag)

# Krill you bot - A Wacky simple Discord bot for krilling your friends!

### Usage ([My Discord Bot](https://discord.com/oauth2/authorize?client_id=1262532595770589214&permissions=292057852928&integration_type=0&scope=bot))

See [The Readme](readmes/discord_readme.md)

### In case the bot goes offline contact: @annyconducter on Discord.

> [!NOTE]
> ***(Since 3.0)*** the botKey location has been moved to "[Path to EXE/PY script]/botStuff/botKey.txt"
>
> (E.g. if you stored it at "C:/bots/krillYouBot/" the botKey would go into "C:/bots/krillYouBot/botStuff/botKey.txt")

# Usage

Launch the krillyou.exe thats generated by pyinstaller along with an accompanying `botKey.text` in the same folder as the EXE with a [VALID BOTKEY](https://discord.com/developers/docs/quick-start/getting-started)
like `XXXxxXXXXXXXXXXXxxxxxxxxXXXXXXXXX.xxxxxxxXXxxxXXXXXXXxxxxxxxXXXXxxXXxxxx` (why tf would i give you MY botkey lmao)

# Compiling:

> [!NOTE]
> The officially tested python versions are
>
> ***Pre 3.0:*** 3.12.4 -3.12.6
>
> ***Since 3.0:*** 3.12.6, 3.12.7

you need [Python](https://www.python.org/downloads/) and the libraries Found in [Setup.bat](setup.bat)

MAKE SURE TO SET THIS WHEN YOU INSTALL PYTHON!! ![](docs/IMPORTANT.png)

then simply run `build.bat` from the root of the repo with everything downloaded.

> [!NOTE]
>
> discord.py uses a library that is missing in 3.13 and thus this bot cannot be compiled/used with any version 3.13.x right now.

# Randomly common issues:

For some reason it'll occasionally fail to create a logs folder and crash, just simple make a logs folder where you put the EXE and it'll stop crashing as long as the main requirement of having a valid bot key is satisfied. (THIS HAS BEEN FIXED, BUT OLDER VERSIONS OF THE KRILL YOU BOT MIGHT HAVE THIS ISSUE, BEWARE!)