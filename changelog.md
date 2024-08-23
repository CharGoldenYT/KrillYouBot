# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

# [2.2] - 8/23/24 2:58 PM

### Changed

- Implementing a true fix for logging.
- Added a log for when failing to move logs to logs/old.
- Fixed moving logs into logs/old
- Better Looking Logs/Log Files
- Seperated generateStrings.py logs from main logs

# [2.1h] -  8/23/24 10:58 AM

### Changed

- Fixed an error that happened due to me being an idiot and using the wrong variable for on_message_edit
- Tried to fix logging not being able to make log files.

# [2.1] - 8/3/24 1:58 AM

### Changed

- Added ?levelup
- Fixed a typo making the tos command print the readme lmao. (This caused incorrect logging.)
- Added a secret Message (That isnt so secret because the code is public)

# [2.0] - 7/25/24 6:21 PM

### Changed

- Made it possible to run commands on edit

# [1.5.1h] - 7/24/24 9:34 PM

### Changed

- Added a warning for if it cant access the log file that should have just been created

# [1.5.1] - 7/24/24 8:45 PM

### Changed

- Made it to where it doesnt crash if it doesnt have read access
- Fixed the build.bat being specific to how i was using pyinstaller, as that would cause issues for people building this from source
- Removed the dependency on caching results as files to prevent crashing
- Renamed readme.py to generateStrings.py to accurately reflect how its used
- Moved where typing the latest changelog goes
- Figured out multi imports

# [1.5h] - 7/24/24 6:18 AM

### Changed

- Made it to where old logs get put in a seperate folder to remove clutter and potential issues with widnows being an idiot
- Added some comments in the code lmao

# [1.5] - 7/22/24 11:39 AM

### Changed

- Made it possible to pipebomb people
- Removed Krill Leave
- Fixed Krill Command potentially not returning a message on april fools

# [1.4-UNRELEASED] - 7/20/24 8:35 PM

### Changed

- IDK why but the ability to make the bot leave the server lmao

# [1.3.3h] - 7/20/24 12:50 PM

### Changed

- Updated the privacy policy to reflect the accessing of server name and channel ID

# [1.3.3] - 7/20/24 12:15 PM

### Changed

- Made the logs show which channel, and from what server it was sent, for better troubleshooting
- Added a make author string function in readme.py, so i don't have to keep manually typing it out every new command added
- Made the end of the version command revert to only having 2 newlines, cause it looks weird with 3
- Made the end of the version command change based on if the changelog was set as being off
- Added contact info to "?krill help"
- Added a pause command to "setup.bat"
- Made the github update checker disable if the current version is a test version

# [1.3.2h] - 7/20/24 1:00 AM

### Changed

- Made a log event for if the bot gets rate limited
- Fixed the version string being accidentally done like "text(VersionString)"
- Slightly changed the formatting of the "?krill version" command to make it look a little nicer
- Fixed the changelog's timestamps
- Made the changelog easier to type by making it a multiline string
- added an input message that asks if the changelog looks right.

# [1.3.2] 7/19/24 7:11 PM

### Changed

- Fixed a bug where due to where the makedir function was placed, the log file creator fails to make a log file due to a nonexistant folder.
- Made the update checker only run when the bot is ready to go

# [1.3.1h] - 7/18/24 12:28 PM 

### Added

- A changelog
- A Version command

### Changed

- Removed accidental leftover import from readme.py

# [1.3.1] - 7/17/24 ~5:05 AM

### Added
- New option to enable or disable output in terminal of final files from readme.py
- Logging in readme.py

### Changed

- The version checker now only runs every valid command rather than every message regardless of who sent it.

# [1.3h] - 7/17/24 ~4:08 AM

### added

- The ability to check for a new version

### Changed

- moved krill command into its own py script
- changed how it determines no input specifed, makes the userID string become None type
- Made it so only not specifying a command after /krill will give an error

# [1.3] - 7/17/24 - ~1:53 AM

### Added

- Privacy policy and TOS Commands as a joke really

### Changed

- Added some punctuation 

# [1.2.2] - 7/17/24 1:49 AM

### Changed

- Made a better fallback message
- The readme is now more readable on GitHub

# [1.2.1] - 7/17/24 ~1:20 AM

### Added

- The ability to read off of github the newest version of the readme, with fallbacks

### Changed

- logs contain the full readme now lmao
- Removed the input asking if you wanna see the key because it was dumb
- Made the about command not send an embed

# [1.2 Hotfix] - 7/17/24 ~9:50 PM

### Changed

- Remove a leftover from the main GitHub readme

# [1.2] - 7/17/24 ~9:43 PM

### Added
- An about command

### Changed

- Re-Moved the logging setup to outside of the cleanup function
- Made it wait for an input before closing
- Added a function that makes the incoming messages default to lowercase
- Changed what was put in the logs for an invalid key

# [1.1 - UNRELEASED] - 7/17/24 ~ 7:43PM

### Added

- The ability to read the Bot Key off of a file
- An icon

### Changed

- Made the error for /krill more useful
- moved the logging file setup to the cleanup function

# [1.0] - 7/17/24 ~6:43PM

- Initial release