class SiteFile:
    path:str; isDirectory:bool
    def __init__(self, path:str, isDirectory:bool) -> None:
        self.path = path; self.isDirectory = isDirectory

    def copy(self): return self