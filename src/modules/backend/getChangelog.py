import urllib.request as urllib
from inspect import currentframe, getframeinfo
from modules.backend.betterLogs.betterLogs import *
from modules.commands.krillVersion import get_filname, getCurVersion, lastVersion
from modules.backend.broadcastTools import search_betweenDelimiters

def get_formattedVersion():
    r'''So i dont get circular import errors, i've basically ported the functionality'''
    replace = ''
    if getCurVersion().endswith('-testver'): replace = '-testver'
    if getCurVersion().endswith('-TestVer'): replace = '-TestVer'
    versionString = f'## [{getCurVersion().replace(replace, '')}]'
    return versionString  

def get_changelog() -> str:
    url = ''
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/CharGoldenYT/KrillYouBot/refs/heads/main/readmes/changelog.md').read().decode('utf-8'))
    except urllib.HTTPError as e:
        frameinfo = getframeinfo(currentframe()); log_err(get_filname(), '[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + '] shit the readme url handler died lmao: ' + str(e)); url = '-# URL Handler died lmao. '

    try:
        url = search_betweenDelimiters(url, get_formattedVersion(), '## [' + lastVersion + ']')
        if url == None:
            url = f'-# Failed to retrieve changelog!'
    except Exception as e:
        log_err(get_filname(), f'SHIT HAD AN ERROR GETTING THAT! {str(e)}')
        url = f'-# Failed to retrieve changelog! {str(e)}'

    return url.rstrip().lstrip().replace('> [!NOTE]\n', '').replace('> ', '-# ')
