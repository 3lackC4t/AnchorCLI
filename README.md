# AnchorCLI
## A lightweight tool for executing shell commands inside of directories using easily configured aliases

### Description

AnchorCLI allows users to create "Anchors" which are aliases stored in a .yml file. These anchors can then be invoked to execute a shell command without having to move into a directory using cd or memorize the directories filepath.

### Flags

By default AnchorCLI is invoked by typing 'ancr' into a terminal instance, then the alias you wish to execute inside of followed by, in quotes, the shell command you wish to execute.

#### Example
```
ancr home "ls -la | grep *.txt"
```

#### AnchorCLI also supports several optional flags including

-a to add a new flag, -a defaults to the current working directory

```
ancr -a essentials <path to new flag>
```
-l lists the currently configured "Anchors"

```
ancr -l
```

-r resets the "Anchors" to their defaults, the home and .config directories.

```
ancr -r
```

