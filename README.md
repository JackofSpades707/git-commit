# git_commit.py

* This is a simple tool to automatically standardize generic git commits to be easy to recognize within a repository

## Installation
`pip install git_commit`

## todo
* --todo should parse the repo for any #TODO statements and return then neatly organized displaying the comment & source files full directory 
* request to take ownership of https://github.com/defcube/gitcommit/ & gitcommit on pypi (currently this is called git_commit as a solution)
* Remove the use of sh.git and utilize os to keep things more compatible
* --dryrun arg
* It seems not to apply changes to deleted files for some reason, debug & fix this [I believe I fixed this]
* Consider refining this into a class
* Refactor code
* -b --browse should resolve the http url for the repo & open it in prefered browser
* git push msg should include the repo's http URL

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
```
```
usage: git-commit.py [-h] [-a]
                     [-i [{modified,deleted,untracked,m,d,u} [{modified,deleted,untracked,m,d,u} ...]]]
                     [-v] [-q] [--interactive] [-p] [--passive] [-m MESSAGE]
                     [files [files ...]]

This tool will incrementally add & commit changes to a repository, the args are used as triggers for various settings

positional arguments:
  files

optional arguments:
  -h, --help            show this help message and exit
  -a, --all             make all avaliable commits for all catagories
  -i [{modified,deleted,untracked,m,d,u} [{modified,deleted,untracked,m,d,u} ...]], --include [{modified,deleted,untracked,m,d,u} [{modified,deleted,untracked,m,d,u} ...]]
                        include actions for provided catagories
                        All Avaliable Catagories below
  -v, --verbose         display verbose information
  -q, --quiet           Quiet mode, Disables output
  --interactive         force confirmation prompts
  -p, --push            pushes changes to remote repo
  --passive             Enables passive error handling, displays errors after execution is complete
  -m MESSAGE, --message MESSAGE
                        Custom message to apply to all commits

Catagories: 
   -m, --modified
   -d, --deleted
   -u, --untracked
```
