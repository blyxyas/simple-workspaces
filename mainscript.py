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
                works = ws(int(line[1:2]), [])
                workspaces.append(works)
                print(workspaces)
            elif len(workspaces) != 0:
                workspaces[-1].addcommand(line)
            else:
                continue

if arg in arguments:
    if arg == "list":
        print("\033[1m<======= Workspaces =======>\033[0m")

        for ws in workspaces:
            print(f"\033[34m<=== Workspace: {ws.ID} ===>\033[0m")
            for command in ws:
                print(command)

        print("\033[1m<======= End of Workspaces =======>\033[0m")

    elif arg == "add":
        to_add = ws(int(input("Workspace ID: ")), [])
        # Check if the workspace already exists
        
        if index(workspaces, to_add.ID) != None:
            print("Workspace already exists")
            exit()

        workspaces.append(to_add)

        save(workspaces, ws_path)
        print(f"Workspace {to_add.ID} added")

    elif arg == "remove":

        if len(argv) < 4:
            print("\033[31mWorkspace ID not provided\n\nsimple-workspace remove <Workspace ID>\033[0m")
            exit()

        ws_id = int(argv[3])
        idx = index(workspaces, ws_id)
        if idx == None:
            print("Workspace not found")
            exit()
        del workspaces[idx]
        save(workspaces, ws_path)
        
    
    elif arg == "load":
        if len(argv) < 4:
            print("\033[31mError: No workspace ID given\n\nsimple-workspace load <Workspace ID>\033[0m")
            exit()

        ws_id = argv[3]
        ws_index = workspaces.index(ws_id)
        for command in workspaces[ws_index]:
            os.system(command)

    elif arg == "addcommand":
        if len(argv) < 4:
            print("\033[31mError: No workspace ID specified\n\nsimple-workspaces addcommand <Workspace ID>\033[0m")
            exit()

        ws_id = int(argv[3])
        print(workspaces, ws_id)
        ws_index = index(workspaces, ws_id)
        if ws_index == None:
            print("Workspace not found")
            exit()

        command = input("Command: ")
        workspaces[ws_index].addcommand(command)
        save(workspaces, ws_path)

    elif arg == "removecommand":
        # removecommand need 3 arguments: removecommand, workspace id, command id

        if len(argv) < 4:
            print("\033[31mError: Not enough arguments\n\nsimple-workspaces removecommand <Workspace ID> <Command ID>\033[0m")
            exit()

        ws_id = argv[3]
        ws_index = workspaces.index(ws_id)
        workspaces[ws_index].pop(int(argv[4]))

    # TODO Uninstall

else:
    print(helpmessage)