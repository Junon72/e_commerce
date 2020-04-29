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

Add ignore template for Django from here https://www.gitignore.io/api/django
Add also .VSCode and env.py to ignore file

Stage Git and commit

```bash
git add .
git commit -m "Initial commit"
```

In Github create a new depository e_commerce and push the project to the repo

```bash
git remote add origin https://github.com/Junon72/e_commerce.git
git push -u origin master
```

Activate the virtual environment

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

`django-admin startproject ecommerce .`


