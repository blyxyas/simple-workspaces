from dataclasses import dataclass


if __name__ == "__main__":
    print("Please, do not run this file directly, this is just a module. Run simple-workspaces in your terminal!")
    exit()

HEADER = '\033[95m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
ORANGE = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
filecomment: str = "This is the workspaces file!\n# You can edit this manually, but I don't recommend it, you can use the command 'simple-workspaces' to see a help message.\n\n# If you want to manually edit this file, just use a @ symbol, then a number, the id of the workspace id, then just add the commands you want to run every time you run the command.\n\n#<======EXAMPLE======>\n\n# # This is my workspace for programming!\n\n# @1 google-chrome-stable\n# code-insider\n# bash\n\n#<======END OF EXAMPLE======>\n\n# WARNING! Do not use the '#' symbol at the start of each line, these are comments, if you want your code executed, do not put a '#' symbol!\n"
PATH: str

@dataclass
class workspace:
    id: int
    commands: list

    def new_command(self, command):
        self.commands.append(command)
    
    def remove_command(self, command_id):
        self.commands.pop(command_id)

from sys import argv
def readconfig() -> tuple[str, str]:
    with open(argv[1], "r") as f:
        lines = f.readlines()
        PATH = lines[0].strip().split("=")[1]
        WORKSPACES_PATH = lines[1].strip().split("=")[1]
    return (PATH, WORKSPACES_PATH)

def update():

    PATH: str = readconfig()[1] + "/workspaces"
    with open(PATH, 'r') as f:
        binary = f.read().split("\n")

    # * ─── LET'S INTERPRET THE BINARY ──────────────────────────────────────────────────

    workspaces: list = []

    for command in binary:
        if len(command) < 1:
            continue

        if command.startswith("#"):
            continue

        if command.startswith("@"):
            # * This is a workspace
            # Now we create a workspace object
            workspaces.append(workspace(command[1], []))

        else:
            # * This is a command
            workspaces[-1].new_command(command)
    return workspaces

def listinfo():
    workspaces = update()
    config = readconfig()
    PATH = config[0]
    WORKSPACES_PATH = config[1]
    print(f"\n{BOLD}{UNDERLINE}{HEADER}<========== INFO ==========>{ENDC}")
    print(f"\n{ORANGE}{BOLD}Path: {PATH}")
    print(f"{BOLD}{BLUE}Workspaces path: {WORKSPACES_PATH}") # WORKSPACES_PATH
    print(f"{ORANGE}{BOLD}Number of workspaces: {len(workspaces)}\n{ENDC}")

    for workspace in workspaces:
        print(f"\n{BOLD}{UNDERLINE}{HEADER}==========> WORKSPACE {workspace.id}: <=========={ENDC}")
        print(f"{ORANGE}<========== Commands: ==========>{ENDC}")
        print(*workspace.commands, sep="\n")
        print(f"{ORANGE}<=================================>{ENDC}\n\n")

from os import getuid

class NotSudo(Exception):
    pass

def save(workspaces: list[workspace]) -> None:
    if getuid() != 0:
        raise NotSudo("You must use sudo to run this command! ")

    config = readconfig()
    WORKSPACES_PATH = config[1]
    to_write: list = []

    for workspace in workspaces:
        to_write.append(f"@{workspace.id}\n")
        for command in workspace.commands:
            to_write.append(command + "\n")

    with open(f"{WORKSPACES_PATH}/workspaces", "w") as f:
        f.write(filecomment + "\n" + "\n".join(to_write) + "\n")