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
    "addcommand"
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

if len(argv) == 2:
    if argv[1] in arguments or argv[1].isnumeric():

        if argv[1].isnumeric():
            inp = input(f"{S}Are you sure? (y/n): {E}")
            if inp.lower() == "y":
                print(f"{B}Loading workspace... {argv[1]}")
                workspaces = update.update()
                for workspace in workspaces:
                    if workspace.id == int(argv[1]):
                        workspace.load()
                        print(f"{B}Workspace loaded!{E}")
                        break

                print("{B}Done!{E}")
                system(workspace.commands.join("; "))
                exit()


        # * Listing workspaces & info
        elif argv[1] == "list":
            update.listinfo()
            exit()

        # * Adding command to workspace
        elif argv[1] == "addcommand":
            workspaces = update.update()
            for workspace in workspaces:
                if workspace.id == int(argv[2]):
                    workspace.new_command(argv[3])
                    print(f"{B}Done!{E}")
                    exit()
            update.save(workspaces)

        # * Removing command from workspace
        elif argv[1] == "removecommand":
            workspaces = update.update()
            for workspace in workspaces:
                if workspace.id == int(argv[2]):
                    workspace.remove_command(argv[3])
                    print(f"{B}Done!{E}")
                    exit()
            update.save(workspaces)
        

        # * Listing commands
        elif argv[1] == "listcommands":
            workspaces = update.update()
            for workspace in workspaces:
                if workspace.id == int(argv[2]):
                    print(workspace.commands)
                    print(f"{B}Done!{E}")
                    exit()
            update.save(workspaces)
            
        # * Removing workspace
        elif argv[1] == "remove":
            inp = input(f"{S}Are you sure? (y/n): {E}")
            if inp.lower() == "y":
                workspaces = update.update()
                for workspace in workspaces:
                    if workspace.id == int(argv[2]):
                        del workspace
            update.save(workspaces)

        # * Adding workspace           
        elif argv[1] == "add":
            inp = input(f"{S}Are you sure? (y/n): {E}")
            if inp.lower() == "y":
                workspaces = update.update()
                workspaces.append(update.workspace(argv[2]))
                print(f"{B}Done!{E}")
                update.save(workspaces)
    else:
        print(helpmessage)
else:
    print(helpmessage)
    exit()