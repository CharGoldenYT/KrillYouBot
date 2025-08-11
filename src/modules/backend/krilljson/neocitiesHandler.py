import neocities
from neocities import NeoCities
from modules.backend.krilljson.siteFile import SiteFile
import urllib.request as urllib
from globalStuff import logger
from inspect import currentframe, getframeinfo

class NCError(Exception):
    errcode:int; message:str

class NeocitiesHandler:
    sitename:str; password:str; fullURL:str
    site:NeoCities
    files:list[SiteFile] = []

    def __init__(self, name:str, password:str, fullURL:str) -> None:
        self.sitename = name; self.password = password; self.fullURL = fullURL
        self.site = NeoCities(name, password)

    def getFiles(self)->list[SiteFile]:
        rawFiles = self.site.listitems()
        for file in rawFiles["files"]:
            self.files.append(SiteFile(file["path"], file["is_directory"]))

        return self.files
    
    def fileExists(self, path:str)->bool:
        files:list[str] = []
        rawFiles = self.getFiles()

        for file in rawFiles:
            files.append(file.path)

        return files.__contains__(path)

    def removeFile(self, path:str):
        self.site.delete(path)

    def addFile(self, path:str):
        print(path)
        if (self.fileExists(path)): self.removeFile(path)
        self.site.upload((path, path))

    def retrieveText(self, path:str)->(str | None):
        url = 'Could not fetch file'
        rawURL = self.fullURL
        if not rawURL.endswith('/'): rawURL += '/'
        print(f"{rawURL}{path}")

        try:url = str(urllib.urlopen(f'{rawURL}{path}').read().decode('utf-8'))
        except Exception as e:
            strThing = str(e).split(":")[0]
            print(NCError(int(strThing.replace("HTTP Error ", "")), str(e)).__repr__())

        return url