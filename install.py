# First, we try to see if the user is in Linux, and if they are sudo, we continue

import os
import sys
import subprocess

if sys.platform == "linux" or sys.platform == "linux2":
    pass
else:
    print("Sorry, this program is only for Linux users, because it uses the Linux filesystem, the Linux Bash Scripting Language, and the Linux Terminal. You can delete this directory manually, for the moment no file was created.")
    exit(1)

if os.getuid() == 0:
    pass
else:
    subprocess.call(['sudo', 'python3'] + sys.argv)
    exit(0)

print("\033[1mChecking if you are in Linux...\033[0m")
# Script made by: Alex G. C aka Blyxyas, visit github.com/blyxyas/simple-workspaces for more info about licensing and things idk

#
# ───────────────────────────────────────────────────────────────────────
#   :::::: I N S T A L L I N G : :  :   :    :     :        :          :
# ───────────────────────────────────────────────────────────────────────
#

print("\033[92;1mInstalling!\033[0m")

import os
from libs.modinstall import *


# Then we create the main directory, where the config file is located, and I strongly recommend to store also the workspaces.

config_path = f"/home/{os.getlogin()}/.config/simple-workspaces"
create_dir(config_path)

# Now, we create the workspaces file.

workspaces_path: str = option("Where do you want to save your workspaces? Enter the directory", config_path, "Other")

create_dir(workspaces_path)
create_file(workspaces_path, "workspaces", "This is the workspaces file!\n# You can edit this manually, but I don't recommend it, you can use the command 'simple-workspaces' to see a help message.\n\n# If you want to manually edit this file, just use a @ symbol, then a number, the id of the workspace id, then just add the commands you want to run every time you run the command.\n\n#<======EXAMPLE======>\n\n# # This is my workspace for programming!\n\n# @1\ngoogle-chrome-stable\n# code-insider\n# bash\n\n#<======END OF EXAMPLE======>\n\n# WARNING! Do not use the '#' symbol at the start of each line, these are comments, if you want your code executed, do not put a '#' symbol!\n")

# Now, we see where the Binary is going to be installed, I strongly recommend to be in /usr/bin

path: str = option("Where do you want to install the binary? Enter the directory", "/usr/bin", "Other")

# Now, we create the config file.

print(f"\033[93mCreating config file in /home/{os.getlogin()}/.config/simple-workspaces\033[0m")
create_dir(f"/home/{os.getlogin()}/.config/simple-workspaces")
create_file(f"/home/{os.getlogin()}/.config/simple-workspaces", "config", f"# This is the config file, not intended to be edited manually, or edited in general, if you want to edit this file, use the Python installer at the original location.\n\nPATH={path}\nWS_PATH={workspaces_path}\n")

#  create the binary (In development, we copy the binary, but in the future we'll move it.)

print("\033[95mCreating executable\033[0m")
os.system(f"sudo cp ./simple-workspaces {path}")

# Now, make it executable

print("\033[95mMaking it executable\033[0m")
os.system(f"sudo chmod +x {path}/simple-workspaces")

# Now, we're finished!

print("\033[92;1mInstalled!\033[0m")