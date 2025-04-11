import urllib.request as urllib
from inspect import currentframe, getframeinfo
from globalStuff import logger, lastVersion, get_formattedVersion
from modules.backend.broadcastTools import search_betweenDelimiters

failMessage = '# Could not retrieve changelog! Might be a test version, the URL handler died, or the URL has been moved.'

def get_changelog() -> str:
    url = ''
    try:url = str(urllib.urlopen('https://raw.githubusercontent.com/CharGoldenYT/KrillYouBot/refs/heads/main/readmes/changelog.md').read().decode('utf-8'))
    except urllib.HTTPError as e:
        logger.log_err('shit the readme url handler died lmao: ' + str(e), True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno); url = '-# URL Handler died lmao. '

    try:
        url = search_betweenDelimiters(url, get_formattedVersion(), '## [' + lastVersion + ']')
        if url == None:
            url = failMessage
    except Exception as e:
        logger.log_err(f'SHIT HAD AN ERROR GETTING THAT! {str(e)}', True, getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)
        url = f'{failMessage} {str(e)}'

    return url.rstrip().lstrip().replace('> [!NOTE]\n', '').replace('> ', '-# ')
