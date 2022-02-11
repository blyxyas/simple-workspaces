if __name__ == "__main__":
    print("Please, do not run this file directly!")
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

PATH: str

class workspace:
    def __init__(self, id, commands):
        self.id: int = id
        self.commands: list = commands

    def new_command(self, command):
        self.commands.append(command)
    
    def remove_command(self, command_id):
        self.commands.pop(command_id)

def readconfig() -> list:
    try:
        open("config/config")

    except:
        print(f"{FAIL}ERROR: Config file not found. Please run install.py first.{ENDC}")
        exit()
    else:
        with open("config/config", "r") as f:
            SETTINGS = f.read().splitlines()
            PATH = SETTINGS[0].split("=")[1]
            WORKSPACES_PATH = SETTINGS[1].split("=")[1]

    return [PATH, WORKSPACES_PATH]

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

def save(workspaces: list[workspace]) -> None:
    PATH: str = readconfig()[0] + "/simple-workspaces"
    to_write: list = []

    for workspace in workspaces:
        to_write.append(f"@{workspace.id}\n")
        for command in workspace.commands:
            to_write.append(command + "\n")

    with open(PATH, "w") as f:
        f.write("\n".join(to_write))