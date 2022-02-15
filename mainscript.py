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
            if line[:4] == "PATH":
                path = line[6:]
            elif line[:7] == "WS_PATH":
                ws_path = line[9:]

# If there's not argument, print the help

if len(argv) < 3:
    print(helpmessage)
    exit()
else:
    arg = argv[2]

workspaces: list = []

# Reading the workspaces
with open(ws_path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        if line[0] == "#" or line[0] == "\n":
            continue
        else:
            if line[0] == "@":
                workspaces.append(ws(line[1:], []))
            else:
                workspaces[-1].addcommand(line)

if arg in arguments:
    if arg == "list":
        print("\033[1m<======= Workspaces =======>\033[0m")

        for ws in workspaces:
            print(f"\033[34m<=== Workspace: {ws.ID} ===>\033[0m")
            for command in ws:
                print(command)

        print("\033[1m<======= End of Workspaces =======>\033[0m")

    elif arg == "add":
        workspaces.append(ws(input("Workspace ID: "), []))

    elif arg == "remove":

        if len(argv) < 4:
            print("\033[31mWorkspace ID not provided\n\nsimple-workspace remove <Workspace ID>\033[0m")
            exit()

        ws_id = argv[3]
        workspaces.remove(workspaces.index(ws_id))
    
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

        ws_id = argv[3]
        ws_index = workspaces.index(ws_id)
        command = input("Command: ")
        workspaces[ws_index].addcommand(command)

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