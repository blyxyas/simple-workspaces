# simple-workspaces

simple-workspaces is a lightweight CLI tool to change between workspaces. **What is a workspace?** A workspace is a list of commands easily available in just one command. With simple-workspaces you can have unlimited light workspaces, which you can add, remove or modify with the CLI tool or manually, in the file.

# Installation

**Requirements:** `Python` & `Git`

To install simple-workspaces you just clone the git repository into a directory.

```bash
git clone https://github.com/blyxyas/simple-workspaces.git
```

Now, just use:

```bash
python install.py
```

This will ask we a few questions and then move to the desired path, I strongly recommend this desired path to be `/usr/bin`.

If one of the paths doesn't exists, then the script will create it. Probably you'll need to give sudo permissions for this phase.

**Installed**, now read carefully, you can delete / move this directory **if** the workspaces path isn't in it. **If the workspaces path is in the directory, do not delete it**

# Uninstallation

To uninstall simple-workspaces, just use `simple-workspaces uninstall`, this will remove the following things:

* The binary
* The `workspaces` file in the workspaces path, it will not remove the directory with the workspaces, however, it'll output the directory path if you want to delete it manually.
* The `~/.config/simple-workspaces/` directory

# Usage

Using simple-workspaces is very easy, you can see the integrated help with `simple-workspaces help` or with `simple-workspaces *` being `*` any command not registered. The commands are:

* `add [Workspace ID]`

This command creates a workspace with the given ID, if the workspace ID is already registered, it'll abort the command.

* `remove [Workspace ID]`

This command removes a workspace with the given ID, if the workspace does not exist, it'll abort the command.

* `load [Workspace ID]`

Loads all the command inside a workspace. It will **not** kill your current apps, it will **just** execute the commands in the workspace.

* `addcommand [Workspace ID] [Command]`

Adds a command to the workspace with the given ID.

* `removecommand [Workspace ID] [Command ID]`

As you can probably notice, a command **does not have an ID**, so with `Command ID` I refer to the index in which the command is executed.

**Example:**
We want to remove the command `google-chrome-stable` from the workspace `1`, as we can see, the command is in the **second index**, because it is the **second command to be executed**, then we just use:

```bash
simple-workspaces removecommand 1 2
```

* `list`

Prints a list with the workspaces, their commands, and other information.

* `*`

It prints the integrated help message.

* `uninstall`

It uninstalls the program. This command will ask if you're sure about the uninstallation, then ask for `sudo` permissions. See [the uninstallation section](#uninstallation) for more information.

# License & Credits

Simple-workspaces have the GNU General Public License v3.0, see [the license](https://github.com/blyxyas/simple-workspaces/blob/master/LICENSE) for more information. Long story short, this is a free software, you can use it, modify it, redistribute it, etc. But, you must credit me as the creator of this software, and your modification must be open source.

simple-workspaces was created by [Blyxyas](https://github.com/blyxyas). Thanks for using it, if you have any suggestions, let me know, opening an issue or a pull request is always welcome.


# Disclaimer

Obviously, I cannot guarantee that simple-workspace will work properly in your Linux distro, I tried to make that the end user can customize almost everything, but some things need to be known, that's how software works! If you have any problem, you can help the project, even in various ways.

See [Contributions sections](#contributions) for more information.

simple-workspaces was developed in Arch Linux, but it should work in any Linux distro, as long as it has the following.

* Python (3.6+)
* Git for cloning the repo.
* A `.config` directory in the home directory.

As far as my knowledge goes, I think most Linux distro meets the requirements (except Git).

# Contributions


If you catch a bug, [report it](https://github.com/Blyxyas/simple-workspaces/issues), that's the most helpful act you can do to a project. You can even do a [pull request](https://github.com/Blyxyas/simple-workspaces/pulls), a pull request can be a lot of things, not only code, it can be documentation, propositions to change the style of the CLI, or **even just a typo!**
