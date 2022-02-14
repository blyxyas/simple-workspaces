from dataclasses import dataclass
from typing import Union
import os

@dataclass
class ws:
    ID: int
    commands: list[str]

    def addcommand(self,
    newcommand: str):
        self.commands.append(newcommand)
    
    def removecommand(self,
    command: Union[str, int]):
        if isinstance(command, str):
            self.commands.remove(command)
        elif isinstance(command, int):
            self.commands.pop(command)

    def list(self):
        print("\033[1m<======= Commands of Workspace: {}=======>\033[0m") 
        for command in self.commands:
            print(f"{command}")
        print("\033[1m<======= End of Commands =======>\033[0m")

    def load(self):
        for command in self.commands:
            os.system(command)

def readconfig(path: str) -> tuple(str, str):
    with open(path, 'r') as f:
        for line in f:
            if line[:5] == "PATH=":
                path = line[5:]
            elif line[:8] == "WS_PATH=":
                ws_path = line[8:]
    return (path, ws_path)

def save(wss: list[ws], ws_path: str):
    with open(ws_path, 'w') as f:
        f.write("")
        f.close()
    with open(ws_path, "a") as f:
        for ws in wss:
            f.write(f"\n\n@{ws.ID}")
            for command in ws.commands:
                f.write(f"\n{command}")
        f.close()

# Secondary functions

def findindex(
    ID: int,
    wss: list[ws]
) -> int:
    for ws in ws:
            if ws.ID == ID:
                return ws

    print("\033[31mWorkspace not found!\033[0m")
    exit()

helpmessage = "\033[93mSimple Workspaces\033[0m\nSimple Workspaces is a simple workspace manager.\nIt allows you to create workspaces and save them in a file\nYou can load them in the terminal at any moment.\nJust add some commands to a workspace and you're done! Use it whenever you want!\nUsage:\n\n==> simple-workspace \033[94m\033[1mload\033[1m\033[95m[Workspace ID]\033[0m\nOpens a workspace with the given id\n\n==> simple-workspace \033[1m\033[94mhelp | -h | --help | ?\033[0m\nShows this help message\n\n==> simple-workspace \033[1m\033[94maddcommand \033[93m[Workspace ID] \033[95m[command]\033[0m\nAdds a command to the workspace with the given id.\n\n==> simple-workspace \033[1m\033[94mremovecommand \033[93m[Workspace ID] \033[95m[Command]\033[0m\nRemoves a command with the given id from the workspace with the given id.\n\n==> simple-workspace \033[1m\033[94mlist\033[0m\nLists all the workspaces.\n\n==> simple-workspace \033[1m\033[94mlistcommands \033[93m[Workspace ID]\033[0m\n\n==> simple-workspace \033[1m\033[94mremove \033[93m[Workspace ID]\033[0m nRemoves the workspace with the given id\n\nYou can manually edit the file to \033[1m\033[94madd / edit / remove\033[0m workspaces, you can add comments with '#', but if you want to modify the workspaces using the program, the comments will be removed."