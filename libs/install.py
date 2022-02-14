# Installer library made by Alex G. C aka blyxyas visit github.com/blyxyas/simple-workspaces for more info about licensing and things idk

import subprocess
import os
import sys

def option(
    text: str,
    option1: str,
    option2: str,
) -> None:

    print(f"\033[1m{text}\033[1m\n\n\t1. {option1}<== Recommended\n\t2. {option2}\n\n")
    option = input(f"\033[1m\n\nEnter the number of your choice (Default is 1): \033[0m")

    if option not in "12" or option == "1":
        return option1

    else:
        print("Where do you want to install it?")
        option = input("\n\nEnter the path where you want to install it: ")
        return option

def create_file(
    path: str,
    file_name: str,
    content: str = ""
) -> None:
    try:
        with open(f"{path}/{file_name}", "x") as file:
            file.write(content)
    except FileExistsError:
        with open(f"{path}/{file_name}", "w") as file:
            file.write(content)
    except:
        print("\033[91mSomething went wrong, please open an issue at github.com/blyxyas/simple-workspaces to report the bug.\033[0m")
        exit(1)

def create_dir(path: str) -> None:
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def asksudo():
    print("\033[1mChecking if you are in Linux...\033[0m")
    if sys.platform == "linux" or sys.platform == "linux2":
        pass
    else:
        print("Sorry, this program is only for Linux users, because it uses the Linux filesystem, the Linux Bash Scripting Language, and the Linux Terminal. You can delete this directory manually, for the moment no file was created.")
        exit(1)

    if os.getuid() == 0:
        pass
    else:
        subprocess.call(['sudo', 'python3'] + sys.argv)