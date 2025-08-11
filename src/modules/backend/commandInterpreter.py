import subprocess as cmd

class ReprCommand:
    executable:str; args:list[str]

    def __init__(self, file:str, args:str):
        self.executable = file, self.args = args

def runCommand(cmnd:ReprCommand)->int:
    cmndline = cmnd.args
    cmndline.insert(0, cmnd.executable)
    return cmd.run(cmndline)