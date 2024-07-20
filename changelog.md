# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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