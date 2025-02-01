import urllib.request as urllib
from inspect import currentframe, getframeinfo
from modules.backend.betterLogs.betterLogs import *
from globalStuff import get_filname, lastVersion, get_formattedVersion
from modules.backend.broadcastTools import search_betweenDelimiters

failMessage = '# Could not retrieve changelog! Might be a test version, the URL handler died, or the URL has been moved.'

def get_changelog() -> str:
    url = ''
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/CharGoldenYT/KrillYouBot/refs/heads/main/readmes/changelog.md').read().decode('utf-8'))
    except urllib.HTTPError as e:
        frameinfo = getframeinfo(currentframe()); log_err(get_filname(), '[' + str(frameinfo.filename) + '] [' + str(frameinfo.lineno) + '] shit the readme url handler died lmao: ' + str(e)); url = '-# URL Handler died lmao. '

    try:
        url = search_betweenDelimiters(url, get_formattedVersion(), '## [' + lastVersion + ']')
        if url == None:
            url = failMessage
    except Exception as e:
        log_err(get_filname(), f'SHIT HAD AN ERROR GETTING THAT! {str(e)}')
        url = f'{failMessage} {str(e)}'

    return url.rstrip().lstrip().replace('> [!NOTE]\n', '').replace('> ', '-# ')
