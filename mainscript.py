from libs.mainutils import *
from sys import argv

config = readconfig(argv[1])

arguments: list = [
    "list",
    "add",
    "remove",
    "load",
    "addcommand",
    "removecommand",
]

# Reading the config
with open(argv[1], "r") as f:
    lines = f.readlines()
    for line in lines:
        if line[0] == "#":
            continue
        else:
            line = line.split("=")
            if line[0] == "PATH":
                path = line[1]
            elif line[0] == "WS_PATH":
                ws_path = line[1] 

# If there's not argument, print the help

if len(argv) < 3:
    print(helpmessage)
    exit()
else:
    arg = argv[2]

workspaces: list = []
wsIDS: list = []

# Reading the workspaces
with open(f"{ws_path}/workspaces", 'r') as f:
    lines = f.readlines()
    for line in lines:
        if line[0] == "#" or line[0] == "\n":
            continue
        else:
            print(line[0], line)
            if line[0] == "@":
                works = ws(int(line[1:-1]), [])
                workspaces.append(works)
                print(workspaces)
            elif len(workspaces) != 0:
                workspaces[-1].addcommand(line)
            else:
                continue

if arg in arguments:
    if arg == "list":
        listing(workspaces)

    elif arg == "add":
        to_add = ws(int(input("Workspace ID: ")), [])
        # Check if the workspace already exists
        
        if index(workspaces, to_add.ID) != None:
            print("Workspace already exists")
            exit()

        workspaces.append(to_add)

        save(workspaces, ws_path)
        print(f"Workspace {to_add.ID} added")
        exit()

    elif arg == "remove":

        if len(argv) < 4:
            print("\033[31mWorkspace ID not provided\n\nsimple-workspace remove <Workspace ID>\033[0m")
            exit()

        ws_id = int(argv[3])
        idx = index(workspaces, ws_id)
        if idx == None:
            panic()

        listing(workspaces, workspaces[idx])
        yn = input("Are you sure? (y/n)").lower()
        if yn == "y":
            del workspaces[idx]
            save(workspaces, ws_path)
        print("Aborted")
        exit()
    
    elif arg == "load":
        if len(argv) < 4:
            print("\033[31mError: No workspace ID given\n\nsimple-workspace load <Workspace ID>\033[0m")
            exit()

        ws_id = argv[3]
        ws_index = workspaces.index(ws_id)
        for command in workspaces[ws_index]:
            os.system(command)
        exit()

    elif arg == "addcommand":
        if len(argv) < 4:
            print("\033[31mError: No workspace ID specified\n\nsimple-workspaces addcommand <Workspace ID>\033[0m")
            exit()

        ws_id = int(argv[3])
        ws_index = index(workspaces, ws_id)
        if ws_index == None:
            panic()
        
        ws = workspaces[ws_index]
        listing(workspaces, ws)

        command = input("Command: ")
        ws.addcommand(command)
        save(workspaces, ws_path)
        exit()

    elif arg == "removecommand":
        # removecommand need 3 arguments: removecommand, workspace id, command id

        if len(argv) < 4:
            print("\033[31mError: Not enough arguments\n\nsimple-workspaces removecommand <Workspace ID> <Command ID>\033[0m")
            exit()

        ws_id = int(argv[3])
        ws_index = index(workspaces, ws_id)
        if ws_index == None:
            panic()

        ws = workspaces[ws_index]
        listing(workspaces, ws)

        for i, command in enumerate(ws.commands):
            print(f"{i} {command}")
        to_remove = int(input("Command ID to remove: "))

        ws.commands.pop(to_remove)
        save(workspaces, ws_path)
        exit()

    # TODO Uninstall

else:
    print(helpmessage)