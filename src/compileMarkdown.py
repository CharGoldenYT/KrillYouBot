import os, sys
from time import sleep
from io import TextIOWrapper
from versionShit import curSemVersion, lastSemVersion

if curSemVersion.identifier == '-testver': curSemVersion.identifier = None

def search_betweenDelimiters(string:str, start:str, end:str):
    start_index = string.find(start)
    if start_index == -1:
        return None

    end_index = string.find(end, start_index)
    if end_index == -1:
        return None

    return string[start_index:end_index]  

def getChangelog(rawChangelog:str)->str:
    changelog = search_betweenDelimiters(rawChangelog, f'## [{curSemVersion.toString()}]', f'## [{lastSemVersion.toString()}]')

    if (changelog == None): changelog = f"## Could not compile changelog for `{curSemVersion.toString()}`"

    return changelog.rstrip().lstrip().replace('> [!NOTE]\n', '').replace('> ', '-# ')

print('This script will re insert all available readmes into a python script callable by krill you bot!')

relativeReadmePath = '../readmes/'

outputPath = './modules/backend/readmes/'
files:list[TextIOWrapper] = [open(f'{relativeReadmePath}changelog.md', 'r'), open(f'{relativeReadmePath}discord_readme.md', 'r'), open(f'{relativeReadmePath}tos.md', 'r'), open(f'{relativeReadmePath}Privacy Policy.md', 'r')]

changelog = getChangelog(files[0].read())
readme = files[1].read()
tos = files[2].read()
pPolicy = files[3].read()

asslog = open(f'{outputPath}changelog.py', 'w')
asslog.write(f"changelog = '''{changelog}'''")
asslog.close()

shitme = open(f'{outputPath}discord_readme.py', 'w')
shitme.write(f"dREADME = '''{readme}'''")
shitme.close()

termsOfShitvice = open(f'{outputPath}tos.py', 'w')
termsOfShitvice.write(f"tos = '''{tos}'''")
termsOfShitvice.close()

pissPolicy = open(f'{outputPath}privacy_policy.py', 'w')
pissPolicy.write(f"pPolicy = '''{pPolicy}'''")
pissPolicy.close()

print('Finished compiling to py!')
sleep(5)