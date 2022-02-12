# simple-workspaces

simple-workspaces is a lightweight CLI tool to change between workspaces. **What is a workspace?** With a workspace you can quicly execute various commands. With simple-workspaces you can have unlimited light workspaces, which you can add, remove or modify with the CLI tool or manually, in the file.

# Installation

**Requirements:** `Python` & `Git`

To install simple-workspaces you just clone the git repository into a directory.

```
git clone https://github.com/blyxyas/simple-workspaces.git
```

Now, just use:

```
python install.py
```

This will ask we a few questions and then move to the desired path, I strongly recommend this desired path to be `/usr/bin`.

If one of the paths doesn't exists, then the script will create it. Probably you'll need to give sudo permissions for this phase.

**Installed**, now read carefully, you can delete / move this directory **if** the workspaces path isn't in it. **If the workspaces path is in the directory, do not delete it**

# Uninstallation

To uninstall simple-workspaces, just use simple-workspaces uninstall, this will remove the following things:

* The binary
* The `workspaces` file in the workspaces path, it will not remove the directory. However, you can remove it manually, because while uninstall it 