# TODO: MAKE THIS ABLE TO BE READ BY KRILL YOU BOT SO I DONT HAVE TO MANUALLY RETYPE THIS EVERYTIME.

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

> [!NOTE]
> Making bigger, but slower produced updates here on out. So i dont rush it out the door a buggy mess lmao.

### Changed

- Made it to where the PyNaCl error doesn't come before the official start of the log, if it occurs (due to user not having it installed).
- Made it to where there isnt a weird space between `<!-- Created by Krill You Bot v(Version)-->` and `<!-- Log Generator: "Better Logs V2" | Better Logs by Char @annyconducter on Discord | https://github.com/CharGoldenYT/betterLogs -->` in the log file.
- Added a little check to make sure the channel i use doesn't receive update announcements.
- Made the update command DM the user if they try to broadcast `?krill version`.
- Made the version command suppress embeds on broadcast, similarly to how it works normally when not broadcasted.
- Further fixed me forgetting to add required function arguments.
- Made Better Logs handle only having one argument
- Fixed the fact that the changelog is actually slightly incorrect.
- Made it not print so much unneccassary data.
- Removed old code from `src/modules/backend/exitTasks.py`
- Removed printing returns of grabbed github files (e.g. the Readme.)
- Fixed the title not being able to be renamed.
- Fixed the colors of the readme check.

## [3.2h-2] 10/18/24 - 2:29 AM

### Changed

- Added the ability to use the announcements system for announcing a new version of krill you bot (ONLY IF YOU ARE ME.)

## [3.2h] 10/18/24 - 2:14 AM

### Changed

- Fixed a weird crash involving being unable to re-connect to discord due to forgetting to properly setup a logging command.
- CORRECTLY implemented the fix in [3.0 Hotfix 3](https://github.com/CharGoldenYT/KrillYouBot/blob/main/readmes/changelog.md#30-hotfix-3-101624---830-pm) regarding incorrect order of ending logging operations.
- Changed it to where `batchFiles/build.bat` no longer launches krill you bot at the end, and moved that functionality to `batchFiles/test.bat` which also builds the bot, but immediately launches when done.

## [3.2] 10/17/24 - 12:48 PM

### Chaged

- Made a variable for receiving server broadcasts so you can have it to where you can receive announcements even if you dont want a message everytime krill you bot starts.
- Sorted the "change_setting()" function to be easier to read
- Made it possible to check a server's setting by using the configure command
- Made it to where the help page displays regardless of permission

## [3.1h] 10/17/24 - 11:22 AM

### Changed

- Fixed the changelog link finally.
- Added a seperate link to the specific version's Github release
- From here on out the versions will be denoted as `version`h-`hotfix num(if applicable)` with the first hotfix having no number.

## [3.1] 10/17/24 - 11:14 AM
    
### Changed

- Fixed krill broadcast not keeping capitalization.

## [3.0 Hotfix 3] 10/16/24 - 8:30 PM
    
### Changed

- Fixed an error involving the handler for editing messages not being properly updated to match the new check messages code
- Fixed logs ending after being moved making it entirely useless to keep a log, as it gets overwritten by the end of the log afterwards.

# [3.0 Hotfix 2] - 10/14/24 1:52 PM

### Changed

- Fixed the about command not showing the proper prefix.

## [3.0 Hotfix 1] - 10/14/24 1:41 PM

### Chaged

- Made it to where server setting backups actually work.
- Made it to where it wont crash due to missing the `serverSettings` folder.
- Made it to where if the files are regrabbed from upstream it reupdates the list of available channels to send into

## [3.0]  - 10/14/24 12:50 PM

### Changed

- Recoded a buncha shit!
- Added local server settings
- Added a config command that allows you to change a servers settings!
- Slightly changed how the changelog looks.

## [2.6] - 10/4/24 11:24 AM

### Changed

- Made it possible to make a custom krilled message by adding a replace fucntion to remove "<@ " from the final message

## [2.5h] - 9/25/24 12:23 PM

### Changed

- Replaced more default discord.py logs with betterLogs to make sure every warning/error gets logged
- Moved client.py and gateway.py to their own folder to keep it from getting confusing

## [2.5] - 9/2/24 10:59 AM

### Changed

- Added local versions of discord.client and discord.gateway to keep the logs consistent

## [2.4] - 9/1/24 7:18 PM

### Changed

- Added a message that gets sent to my server when the bot is ready, and when it gets closed

## [2.3] - 8/26/24 3:55 PM

### Changed

- Added crude python version check
- Added colors to printed messages
- Made the logging function also print out messages with the ability to toggle off printing.
- Fixed some logs potentially having 2 datetime strings
- Removed unneccasary import from "krillCommand.py"
- Made it easier for troubleshooting by also grabbing the server ID

## [2.2-Hotfix-3] - 8/26/24 12:33 PM

### Changed

- funny window title
- Changed the name of the built executable from Pyinstaller
- Got rid of useless rate limited check

## [2.2-Hotfix-2] - 8/23/24 6:45 PM

### Changed

- Added what krill bot version made a log file.
- Changed How i label Hotfixes
- Made it so Hotfix doesnt get changed to hotfix
- Reconsolidated generateStrings.py and main logs
- New "betterLogs.py" script

## [2.2h] - 8/23/24 3:23 PM

### Changed

- Fixed an old filename being used for generateStrings.py from before it was called that.

## [2.2] - 8/23/24 2:58 PM

### Changed

- Implementing a true fix for logging.
- Added a log for when failing to move logs to logs/old.
- Fixed moving logs into logs/old
- Better Looking Logs/Log Files
- Seperated generateStrings.py logs from main logs

## [2.1h] -  8/23/24 10:58 AM

### Changed

- Fixed an error that happened due to me being an idiot and using the wrong variable for on_message_edit
- Tried to fix logging not being able to make log files.

## [2.1] - 8/3/24 1:58 AM

### Changed

- Added ?levelup
- Fixed a typo making the tos command print the readme lmao. (This caused incorrect logging.)
- Added a secret Message (That isnt so secret because the code is public)

## [2.0] - 7/25/24 6:21 PM

### Changed

- Made it possible to run commands on edit

## [1.5.1h] - 7/24/24 9:34 PM

### Changed

- Added a warning for if it cant access the log file that should have just been created

## [1.5.1] - 7/24/24 8:45 PM

### Changed

- Made it to where it doesnt crash if it doesnt have read access
- Fixed the build.bat being specific to how i was using pyinstaller, as that would cause issues for people building this from source
- Removed the dependency on caching results as files to prevent crashing
- Renamed readme.py to generateStrings.py to accurately reflect how its used
- Moved where typing the latest changelog goes
- Figured out multi imports

## [1.5h] - 7/24/24 6:18 AM

### Changed

- Made it to where old logs get put in a seperate folder to remove clutter and potential issues with widnows being an idiot
- Added some comments in the code lmao

## [1.5] - 7/22/24 11:39 AM

### Changed

- Made it possible to pipebomb people
- Removed Krill Leave
- Fixed Krill Command potentially not returning a message on april fools

## [1.4-UNRELEASED] - 7/20/24 8:35 PM

### Changed

- IDK why but the ability to make the bot leave the server lmao

## [1.3.3h] - 7/20/24 12:50 PM

### Changed

- Updated the privacy policy to reflect the accessing of server name and channel ID

## [1.3.3] - 7/20/24 12:15 PM

### Changed

- Made the logs show which channel, and from what server it was sent, for better troubleshooting
- Added a make author string function in readme.py, so i don't have to keep manually typing it out every new command added
- Made the end of the version command revert to only having 2 newlines, cause it looks weird with 3
- Made the end of the version command change based on if the changelog was set as being off
- Added contact info to "?krill help"
- Added a pause command to "setup.bat"
- Made the github update checker disable if the current version is a test version

## [1.3.2h] - 7/20/24 1:00 AM

### Changed

- Made a log event for if the bot gets rate limited
- Fixed the version string being accidentally done like "text(VersionString)"
- Slightly changed the formatting of the "?krill version" command to make it look a little nicer
- Fixed the changelog's timestamps
- Made the changelog easier to type by making it a multiline string
- added an input message that asks if the changelog looks right.

## [1.3.2] 7/19/24 7:11 PM

### Changed

- Fixed a bug where due to where the makedir function was placed, the log file creator fails to make a log file due to a nonexistant folder.
- Made the update checker only run when the bot is ready to go

## [1.3.1h] - 7/18/24 12:28 PM 

### Added

- A changelog
- A Version command

### Changed

- Removed accidental leftover import from readme.py

## [1.3.1] - 7/17/24 ~5:05 AM

### Added
- New option to enable or disable output in terminal of final files from readme.py
- Logging in readme.py

### Changed

- The version checker now only runs every valid command rather than every message regardless of who sent it.

## [1.3h] - 7/17/24 ~4:08 AM

### added

- The ability to check for a new version

### Changed

- moved krill command into its own py script
- changed how it determines no input specifed, makes the userID string become None type
- Made it so only not specifying a command after /krill will give an error

## [1.3] - 7/17/24 - ~1:53 AM

### Added

- Privacy policy and TOS Commands as a joke really

### Changed

- Added some punctuation 

## [1.2.2] - 7/17/24 1:49 AM

### Changed

- Made a better fallback message
- The readme is now more readable on GitHub

## [1.2.1] - 7/17/24 ~1:20 AM

### Added

- The ability to read off of github the newest version of the readme, with fallbacks

### Changed

- logs contain the full readme now lmao
- Removed the input asking if you wanna see the key because it was dumb
- Made the about command not send an embed

## [1.2 Hotfix] - 7/17/24 ~9:50 PM

### Changed

- Remove a leftover from the main GitHub readme

## [1.2] - 7/17/24 ~9:43 PM

### Added
- An about command

### Changed

- Re-Moved the logging setup to outside of the cleanup function
- Made it wait for an input before closing
- Added a function that makes the incoming messages default to lowercase
- Changed what was put in the logs for an invalid key

## [1.1 - UNRELEASED] - 7/17/24 ~ 7:43PM

### Added

- The ability to read the Bot Key off of a file
- An icon

### Changed

- Made the error for /krill more useful
- moved the logging file setup to the cleanup function

## [1.0] - 7/17/24 ~6:43PM

- Initial release