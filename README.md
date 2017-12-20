# git-commit.py

This is a simple tool to automatically standardize generic git commits to be easy to recognize within a repository

## todo
* Allow interactively working with only edited files
* --dryrun arg

## symbols
[+] Added new file to repo
[!] Updated existing file within repo
[-] removed file from repo

## commit message structure
* $symbol $filename
* If you're still confused, just check out the commit history for this repo :)

## args
```
usage: git-commit.py [-h] [-a]
                     [-i [{modified,deleted,untracked,m,d,u} [{modified,deleted,untracked,m,d,u} ...]]]
                     [-v] [--noconfirm] [--passive]
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
  --noconfirm           no confirmation prompts
  --passive             Enables passive error handling

Catagories: 
   -m, --modified
   -d, --deleted
   -u, --untracked
```
