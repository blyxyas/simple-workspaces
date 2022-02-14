# Script made by: Alex G. C aka Blyxyas, visit github.com/blyxyas/simple-workspaces for more info about licensing and things idk

#
# ───────────────────────────────────────────────────────────────────────
#   :::::: I N S T A L L I N G : :  :   :    :     :        :          :
# ───────────────────────────────────────────────────────────────────────
#

import os
import subprocess
import sys

# First, we see if the user is in linux
print("Checking if you are in Linux...")
if sys.platform == "linux" or sys.platform == "linux2":
    pass
else:
    print("Sorry, this program is only for Linux users, because it uses the Linux filesystem, the Linux Bash Scripting Language, and the Linux Terminal. You can delete this directory manually, for the moment no file was created.")
    sys.exit(1)

if os.geteuid() == 0:

    HEADER = '\033[95m'
    BLUE = '\033[94m'
    ORANGE = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    print(f"{BOLD}{UNDERLINE}{ORANGE}<========== Installing... ==========>{ENDC}")
    print(f"{BOLD}Where do you want to install simple-workspaces?{ENDC}\n\n\t1. /usr/bin <== Recommended\n\t2. Other")

    inp: str = input(f"{BOLD}Enter the number of your choice (Default is 1): {ENDC}")

    if inp == "2":
        PATH = input(f"{BOLD}Enter the path where you want to install simple-workspaces: {ENDC}")
    else:
        PATH = "/usr/bin"

    os.system("clear")
    print(f"{BOLD}{UNDERLINE}{ORANGE}<========== Installing... ==========>{ENDC}")

    print(f"\n\n{BOLD}Where do you want to save the workspaces?{ENDC}\n\n\t1. ~/.config/simple-workspaces/ <== Recommended\n\n\t2. Other")
    inp = input(f"\n\n{BOLD}Enter the number of your choice (Default is 1: )")

    if inp == "2":
        print(f"{FAIL}{BOLD}⚠️ WARNING:{ENDC}{FAIL} Just enter the DIRECTORY, {BOLD}not the file{ENDC}")
        workspace_path = input(f"{BOLD}Enter the path where you want to save the workspaces: {ENDC}")

        if not os.path.exists(workspace_path):
            print(f"{BLUE}Path does not exists, creating {workspace_path}")
            os.mkdir(workspace_path)
    else:
        workspace_path = f"/home/{os.getlogin()}/.config/simple-workspaces/"

    os.system("clear")
    print(f"{BOLD}{UNDERLINE}{ORANGE}<========== Installing... ==========>{ENDC}")

    # If the directory config does not exist, create it.
    try:
        os.mkdir("config")
    except:
        pass

    config_path = f"/home/{os.getlogin()}/.config/simple-workspaces/"

    # If the config file does not exist, create it.
    try:
        os.makedirs(config_path)
    except:
        pass

    try:
        with open(f"{config_path}/config.conf", "x") as f:
            f.write(f"PATH = {PATH}\nWS_PATH = {workspace_path}workspaces\n")

    except FileExistsError:
        with open(f"{config_path}/config.conf", "w") as f:
            f.write(f"PATH={PATH}\nWS_PATH={workspace_path}workspaces\n")

    print(f"{BLUE}The config file was created in ~/.config/simple-workspaces/config.conf{ENDC}")

    print(f"{BOLD}Installing binary...{ENDC}")

    # First, we create the binary

    print(f"{ORANGE}Moving binary...{ENDC}")
    os.system(f"sudo cp ./simple-workspaces {PATH}")
    # * For the production use: os.system(f"sudo mv ./simple-workspaces {PATH}")

    # And then we make it executable
    print(f"{ORANGE}Making it executable...{ENDC}")
    os.system(f"sudo chmod +x {PATH}/simple-workspaces")

    # Now, we create the workspaces directory
    try:
        os.mkdir(workspace_path)
    except:
        try:
            open(f"{workspace_path}workspaces")
        except:
            try:
                open(f"{workspace_path}workspaces", "x")
            except:
                print(f"{FAIL}ERROR: Cannot open directory{ENDC}")
                exit()
        else:
            with open(f"{workspace_path}workspaces", "w") as f:
                f.write("This is the workspaces file!\n# You can edit this manually, but I don't recommend it, you can use the command 'simple-workspaces' to see a help message.\n\n# If you want to manually edit this file, just use a @ symbol, then a number, the id of the workspace id, then just add the commands you want to run every time you run the command.\n\n#<======EXAMPLE======>\n\n# # This is my workspace for programming!\n\n# @1\ngoogle-chrome-stable\n# code-insider\n# bash\n\n#<======END OF EXAMPLE======>\n\n# WARNING! Do not use the '#' symbol at the start of each line, these are comments, if you want your code executed, do not put a '#' symbol!\n")

    print(f"{BOLD}{HEADER}<========== Installed! ==========>{ENDC}")

    print("{BOLD}You can now use the command 'simple-workspaces' to see the help message. Or enter the repo at github.com/blyxyas/simple-workspaces{ENDC}")
else:
    subprocess.call(['sudo', 'python3'] + sys.argv)