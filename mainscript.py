from sys import argv
from os import system
import update

B = '\033[93m\033[1m'
E = '\033[0m'
A = '\033[95m'
S = '\033[94m'
FAIL = '\033[91m'

arguments: list = [
    "list",
    "addcommand",
    "add"
]


# ─── MAIN ───────────────────────────────────────────────────────────────────────

helpmessage: str = f"""

\033[93mSimple Workspaces\033[0m

Simple Workspaces is a simple workspace manager.
It allows you to create workspaces and save them in a file.
You can load them in the terminal at any moment.

Just add some commands to a workspace and you're done! Use it whenever you want!

Usage:

==> simple-workspace {B}[workspace_id]{E}
Opens a workspace with the given id.

==> simple-workspace {B}help | -h | --help | ?{E}
Shows this help message

==> simple-workspace {B}addcommand {A}[workspace_id] {S}[command]{E}
Adds a command to the workspace with the given id.

==> simple-workspace {B}removecommand {A}[workspace_id] {S}[command_id]{E}
Removes a command with the given id from the workspace with the given id.

==> simple-workspace {B}list{E}
Lists all the workspaces.

==> simple-workspace {B}listcommands {A}[workspace_id]{E}

==> simple-workspace {B}remove {A}[workspace_id]{E}
Removes the workspace with the given id.

You can manually edit the file to {B}add / edit / remove{E} workspaces, you can add comments with '#', but if you want to modify the workspaces using the program, the comments will be removed.
"""

workspaces_comment: str = f"""
# This is the workspaces file!\n# You can edit this manually, but I don't recommend it, you can use the command 'simple-workspaces' to see a help message.\n\n# If you want to manually edit this file, just use a @ symbol, then a number, the id of the workspace id, then just add the commands you want to run every time you run the command.\n\n#<======EXAMPLE======>\n\n# # This is my workspace for programming!\n\n# @1 google-chrome-stable\n# code-insider\n# bash\n\n#<======END OF EXAMPLE======>\n\n# WARNING! Do not use the '#' symbol at the start of each line, these are comments, if you want your code executed, do not put a '#' symbol!
"""

if len(argv) >= 2:
    cli_argument = argv[2]
    if cli_argument in arguments or cli_argument.isnumeric():

        if cli_argument.isnumeric():
            inp = input(f"{S}Are you sure? (y/n): {E}")
            if inp.lower() == "y":
                print(f"{B}Loading workspace... {cli_argument}")
                workspaces = update.update()
                for workspace in workspaces:
                    if workspace.id == int(cli_argument):
                        workspace.load()
                        print(f"{B}Workspace loaded!{E}")
                        break

                print("{B}Done!{E}")
                system(workspace.commands.join("; "))
                exit()


        # * Listing workspaces & info
        elif cli_argument == "list":
            update.listinfo()
            exit()

        # * Adding command to workspace
        elif cli_argument == "addcommand":
            workspaces = update.update()
            for workspace in workspaces:
                if workspace.id == int(argv[3]):
                    workspace.new_command(argv[3])
                    print(f"{B}Done!{E}")
                    exit()
            update.save(workspaces)
            exit()

        # * Removing command from workspace
        elif cli_argument == "removecommand":
            workspaces = update.update()
            for workspace in workspaces:
                if workspace.id == int(argv[3]):
                    workspace.remove_command(argv[3])
                    print(f"{B}Done!{E}")
                    exit()
            update.save(workspaces)
            exit()
        

        # * Listing commands
        elif cli_argument == "listcommands":
            workspaces = update.update()
            for workspace in workspaces:
                if workspace.id == int(argv[3]):
                    print(workspace.commands)
                    print(f"{B}Done!{E}")
                    exit()
            update.save(workspaces)
            exit()
            
        # * Removing workspace
        elif cli_argument == "remove":
            inp = input(f"{S}Are you sure? (y/n): {E}")
            if inp.lower() == "y":
                workspaces = update.update()
                for i, workspace in enumerate(workspaces):
                    if workspace.id == int(argv[3]):
                        workspaces.pop(workspace)
            update.save(workspaces)
            exit()

        # * Adding workspace           
        elif cli_argument == "add":
            print("ADD")
            if argv[-1] != "-confirmYES":
                inp = input(f"{S}Are you sure? (y/n): {E}")
                if inp.lower() == "y":
                    workspaces = update.update()
                    for ws in workspaces:
                        if ws.id == argv[3]:
                            print("Workspace already exists! Try with another ID.")
                            exit()
                    workspaces.append(update.workspace(argv[3], []))
                    print(f"{B}Done!{E}")
            update.save(workspaces)

    else:
        print(helpmessage)
else:
    print(helpmessage)
    exit()