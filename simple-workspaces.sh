#!bin/bash

# Script made by Alex G. C aka Blyxyas visit github.com/blyxyas for more information

# This script is the main script!
# It is used to run the main program.

# Colors:
BOLD = '\033[1m'
ORANGE = '\033[33m'
RED = '\033[31m'
BLUE = '\033[34m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
NORMAL = '\033[0m'

# arguments:

# Workspaces:
ws(){
    obj_properties=($2, ())
    #obj_properties[0] = ID
    ID=0
    #obj_properties[1] = Commands
    Commands=1

    ws.addcommand(){
        obj_properties[1][${#$1[@]}] = "$3"
    }

    ws.removecommand(){
        if [ "$2" == "=" ]; then
            # We remove a command from the workspace.
            for ((i=0; i < ${#obj_properties[1][@]}; i++)); do
                if [ "${obj_properties[1][i]}" == "$3" ]; then
                    unset obj_properties[1][i]
                fi
        fi
    }

    ws.listcommands(){
        echo -e "${BOLD}<=======Commands of Workspace: ${obj_properties[0]}=======>${NORMAL}"
        echo "${obj_properties[1][1]}"
    }

    ws.loadws(){
        # We load the workspace.
        for ((i=0; i < ${#obj_properties[1][@]};i++)); do
            eval "${obj_properties[1][i]}"
        done
    }
}

in_workspace = false
filename = "/home/alex/git/simpleworkspaces/workspaces.txt"
workspaces = ()

readfile(){
    while read line; do
        # reading workspace file

        # If the line is a comment or empty, then skip it.
        if [ ${line:0:1} = "#" ] || [ -z "$line" ]; then
            continue
        else
            if [ ${line:0:1} = "@" ]; then
                # The line is a workspace.
                # We need to create the workspace.    
                
                ws workspace "${line:1:1}"

                # We get the ID of the workspace
                
                workspaces[${#workspaces[@]}] = "${line:1}"
                workspace.ID=${line:1:1}
                
                # We get the commands of the workspace
                # now we read the following lines, until we find the end of the workspace.
            
            else
                # The line is a command.
                # We add the command to the workspace.
                workspace.addcommand "${line:0:1}" "${line:1}"
            fi
        fi

    done < $filename
    return workspaces
}

panic(){
    echo -e "${RED}ERROR: Workspace not found!${NORMAL}"
    exit 1
}

findws(){
    for ((i=0; i < ${#workspaces[@]};i++)); do
        if [ "${workspaces[$i]}" == "$1" ]; then
            return $i
        fi
    done
    panic
}

# Main CLI program:

if [ "$1" = "list" ]; then
    # We list the workspaces.
    echo -e "${BOLD}<=======Workspaces=======>${NORMAL}"
    for ((i=0; i < ${#workspaces[@]};i++)); do
        ${workspaces[i]}.listcommands
    done

elif [ "$1" = "load" ]; then
    # We load the workspace.
    idx = findws "$2"
    ${workspaces[idx]}.loadws

elif [ "$1" = "remove" ]; then
    idx = findws "$2"
    unset workspaces[$idx]

elif [ "$1" = "add" ]; then
    workspaces[${#workspaces[@]}] = "$2"

elif [ "$1" = "addcommand" ]; then
        idx = findws "$2"
        ${workspaces[idx]}.addcommand "$3"

elif [ "$1" = "removecommand" ]; then
    {
        idx = findws "$2"
        workspaces[idx].removecommand "$3"
    } || {
        panic
    }
fi
