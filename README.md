# git_commit.py

* This is a simple tool to automatically standardize generic git commits to be easy to recognize within a repository

## Installation
`pip install git_commit`

## Suggestion
* I highly suggest doing something like the following in your ~/.bashrc or ~/.zshrc:
`alias GC=/usr/bin/git_commit`

## Dependencies
* python-sh
* git
* python-argparse
* python3 (python2 not currently supported)
* hub (optional for -b flag)

## todo
* --todo should parse the repo for any #TODO statements and return then neatly organized displaying the comment & source files full directory 
* request to take ownership of https://github.com/defcube/gitcommit/ & gitcommit on pypi (currently this is called git_commit as a solution) (I Have been granted permission to take ownership of gitcommit on pypi, I will do so once I port over all the functionality of that package into this package)
* Remove the use of sh.git and utilize os to keep things more compatible
* --dryrun arg
* It seems not to apply changes to deleted files for some reason, debug & fix this [I believe I fixed this]
* Consider refining this into a class
* Refactor code
* -b --browse should resolve the http url for the repo & open it in prefered browser
* git push msg should include the repo's http URL
* Port over this functionality to an arg: https://hastebin.com/utefupiyin.bash

## todo-done
* Ignores filenames matching $repo/.gitignore
* --interactive prompts between every commit
* output is pretty
* -p | --push pushes commits to repo (and auto handles new repo's requiring --set-upstream origin master)
* -b | --browse opens repo in webbrowser (requires hub currently)
* passing filenames directly works now
* -s | --status outputs $(git status) to stdout

## symbols
* [+] Added new file to repo
* [!] Updated existing file within repo
* [-] removed file from repo

## commit message structure
* $symbol $filename
* If you're still confused, just check out the commit history for this repo :)

## usage
```
Examples:
>_ git-commit.py -a
[+] New_File_In_Repo
[!] Modified_File_In_Repo
[-] File_Removed_From_Repo

>_ git-commit.py -p
pushed to repo

>_ git-commit.py SomeModifiedFile SomeNewFile -p
[!] SomeModifiedFile
[+] SomeNewFile
pushed to repo
```
```

usage: git-commit.py [-h] [-a] [-b] [-d]
                     [-i [{modified,deleted,untracked,m,d,u} [{modified,deleted,untracked,m,d,u} ...]]]
                     [-m MESSAGE] [-p] [-q] [-s] [-v] [--interactive]
                     [--passive]
                     [files [files ...]]

This tool will incrementally add & commit changes to a repository, the args are used as triggers for various settings

positional arguments:
  files

optional arguments:
  -h, --help            show this help message and exit
  -a, --all             make all avaliable commits for all catagories
  -b, --browse          Opens repo with preferred webbrowser
  -d, --debug           Displays debug information to make editing src easier
  -i [{modified,deleted,untracked,m,d,u} [{modified,deleted,untracked,m,d,u} ...]], --include [{modified,deleted,untracked,m,d,u} [{modified,deleted,untracked,m,d,u} ...]]
                        include actions for provided catagories
                        All Avaliable Catagories below
  -m MESSAGE, --message MESSAGE
                        Custom message to apply to all commits
  -p, --push            pushes changes to remote repo
  -q, --quiet           Quiet mode, Disables output
  -s, --status          Displays git status and exits
  -v, --verbose         display verbose information
  --interactive         force confirmation prompts
  --passive             Enables passive error handling, displays errors after execution is complete

Catagories: 
   -m, --modified
   -d, --deleted
   -u, --untracked
```
