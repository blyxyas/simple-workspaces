#
# ───────────────────────────────────────────────────────────────────────
#   :::::: I N S T A L L I N G : :  :   :    :     :        :          :
# ───────────────────────────────────────────────────────────────────────
#


from os import getcwd, path, mkdir

HEADER = '\033[95m'
BLUE = '\033[94m'
ORANGE = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

print(f"{BOLD}{UNDERLINE}{ORANGE}<========== Installing... ==========>{ENDC}")
print(f"{BOLD}Where do you want to install simple-workspaces?{ENDC}\n\n\t1. /bin <== Recommended\n\t2. Other")

inp: str = input(f"{BOLD}Enter the number of your choice (Default is 1): {ENDC}")

if inp == "2":
    PATH = input(f"{BOLD}Enter the path where you want to install simple-workspaces (You can edit it in the config/config file later and running update.py): {ENDC}")
else:
    PATH = "/bin"

print(f"\n\n{BOLD}Where do you want to save the workspaces?{ENDC}\n\n\t1. {getcwd()}/workspaces\n\n\t2. Other")
inp = input(f"\n\n{BOLD}Enter the number of your choice (Default is 1: )")

if inp == "2":
    print(f"{FAIL}{BOLD}⚠️ WARNING:{ENDC}{FAIL} Just enter the DIRECTORY, {BOLD}not the file{ENDC}")
    workspace_path = input(f"{BOLD}Enter the path where you want to save the workspaces: {ENDC}")

    if not path.exists(workspace_path):
        print(f"{BLUE}Path does not exit, creating {workspace_path}")
        mkdir(workspace_path)
else:
    workspace_path = getcwd()

# If the directory config does not exist, create it.
try:
    mkdir("config")
except:
    pass

try:
    open("config/config")
except:
    open('config/config', 'x')
    print(f"{BLUE}Creating config/config file!")

with open("config/config", "w") as f:
    data = f.write(f"PATH={PATH}\nWORKSPACES_PATH={workspace_path}")

try:
    open(PATH)
except:
    print(f"{FAIL}ERROR: Path does not exist!")
    exit()
else:
    with open("/usr/bin/simple-workspace", "x") as f:
        f.write(f"#!/bin/sh\n\npython ~/{workspace_path}/mainscript.py $1")

print(f"{BOLD}{HEADER}<========== Installed! ==========>{ENDC}")