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

def readconfig(path: str):
    with open(path, 'r') as f:
        for line in f:
            if line[:5] == "PATH=":
                path = line[5:]
            elif line[:8] == "WS_PATH=":
                ws_path = line[8:]
    return path, ws_path

def save(wss: list[ws], ws_path: str):

    # Check if sudo
    if os.geteuid() != 0:
        print("Please run this script with sudo!")
        exit()

    to_write: list = []
    for ws in wss:
        to_write.append(f"@{ws.ID}")
        for command in ws.commands:
            to_write.append(f"\n{command}")

    with open(f"{ws_path}/workspaces", 'w') as f:
        f.write("{}\n".format('\n'.join(to_write)))
        f.close()
    os.system(f"cat {ws_path}/workspaces")

def index(wss: list[ws], ws_id: int):
    for i, ws in enumerate(wss):
        if ws.ID == ws_id:
            return i
    return None

helpmessage = "\033[93mSimple Workspaces\033[0m\nSimple Workspaces is a simple workspace manager.\nIt allows you to create workspaces and save them in a file\nYou can load them in the terminal at any moment.\nJust add some commands to a workspace and you're done! Use it whenever you want!\nUsage:\n\n==> simple-workspace \033[94m\033[1mload\033[1m\033[95m[Workspace ID]\033[0m\nOpens a workspace with the given id\n\n==> simple-workspace \033[1m\033[94mhelp | -h | --help | ?\033[0m\nShows this help message\n\n==> simple-workspace \033[1m\033[94maddcommand \033[93m[Workspace ID] \033[95m[command]\033[0m\nAdds a command to the workspace with the given id.\n\n==> simple-workspace \033[1m\033[94mremovecommand \033[93m[Workspace ID] \033[95m[Command]\033[0m\nRemoves a command with the given id from the workspace with the given id.\n\n==> simple-workspace \033[1m\033[94mlist\033[0m\nLists all the workspaces.\n\n==> simple-workspace \033[1m\033[94mlistcommands \033[93m[Workspace ID]\033[0m\n\n==> simple-workspace \033[1m\033[94mremove \033[93m[Workspace ID]\033[0m nRemoves the workspace with the given id\n\nYou can manually edit the file to \033[1m\033[94madd / edit / remove\033[0m workspaces, you can add comments with '#', but if you want to modify the workspaces using the program, the comments will be removed."