# Installer library made by Alex G. C aka blyxyas visit github.com/blyxyas/simple-workspaces for more info about licensing and things idk

import os

def option(
    text: str,
    option1: str,
    option2: str,
) -> None:

    print(f"\033[1m{text}\033[0m\n\n\t\033[93m1. {option1} <== Recommended\n\t\033[0m2. {option2}")
    option = input(f"\033[1m\n\nEnter the number of your choice (Default is 1): \033[0m")

    if option != "2":
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