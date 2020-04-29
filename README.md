# e-commerce

## index

1. [Setting up VSCode](#Setting-up-VSCode)








## Setting up VSCode

Start a new workspace e-commerce in VSCode

Open a terminal and install Python 3

`brew install python3`

Create a virtual environment

`python3 -m venv foo`

Initialize git and .gitignore with foo in it

`git init`

`echo 'foo' > .gitignore`

Add ignore tempale for Django from here https://www.gitignore.io/api/django

jussis-imac:e-commerce jussinousiainen$ echo 'foo' > .gitignore
jussis-imac:e-commerce jussinousiainen$ git add .
jussis-imac:e-commerce jussinousiainen$ git commit-m "Initial commit"
git: 'commit-m' is not a git command. See 'git --help'.

The most similar command is
        commit-tree
jussis-imac:e-commerce jussinousiainen$ git commit -m "Initial commit"
[master (root-commit) a91e8b8] Initial commit
 2 files changed, 143 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
jussis-imac:e-commerce jussinousiainen$ git remote add origin https://github.com/Junon72/e_commerce.git
jussis-imac:e-commerce jussinousiainen$ git push -u origin master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.34 KiB | 1.34 MiB/s, done.
Total 4 (delta 0), reused 0 (delta 0)
To https://github.com/Junon72/e_commerce.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
jussis-imac:e-commerce jussinousiainen$ 



In Github create a new depository e_commerce



Activate the environment

`source foo/bin/activate`

Upgrade your pip version

`pip install --upgrade pip`

Install Django

`pip3 install Django`

Install helpers for writing code

`pip3 install pep8 autopep8 pylint`

Create requirements.txt file

`pip3 freeze > requirements.txt`


## Create a django project

`django-admin startproject ecommerce`


