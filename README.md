# e-commerce

## index

1. [Setting up VSCode](#Setting-up-VSCode)
2. [Create a django project](#Create-a-django-project)
3. [Reusing An Accounts App](#Reusing-An-Account-App)







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

In settings.py, add ip path

```bash
ALLOWED_HOSTS = [
    '127.0.0.1'
]
```

In Terminal change the manage.py mode to runnable, migrate and run

```bash
chmod 777 ./manage.py

./manage.py migrate

./manage.py runserver 127.0.0.1:8000
```

Open the project in Browser -> The Install Works Successfully!

## Reusing An Accounts App

Import form django_authentication:

```bash
accounts
    _init_py
    admin.py
    app.py
    backends.py
    forms.py
    models.py
    tests.py
    url_reset.py
    urls.py
    views.py
    templates
        index.html
        login.html
        profile.html
        registration.html
```

In ecommerce folder add

```bash
templates
    registration
        password_reset_form.html
    base.html
```

And in root directory add

```bash
static
    css
        custom.css
```

! I changed the name from styles.css to custom.css. In base.html change the link href to custom too.

Install bootstrap for forms

`pip3 install django-forms-bootstrap`

In settings.py add the app and bootstrap to INSTALLED_APPS and create AUTHENTICATION_BACKENDS path to backends.py.
Add the templates path to TEMPLATES > DIRS.

```python
INSTALLED_APPS = [
...
    'accounts',
    'django_forms_bootstrap',

]

TEMPLATES = [
...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.EmailAuth',
]
```

Create a storage for messages (although in the video he said this is something only to do wit clou9.
I did it authentication project and it at least did not brake anything. So, adding it here also.)

```python
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
```

In Terminal migrate all the apps ( )

```bash
python3 manage.py makemigrations

python3 manage.py migrate
```

In Browser check the app still works.

In ecommerce > urls.py add paths to accounts urls and reset_urls

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('accounts.url_reset'))
]
```

Create a superuser

```bash
python3 manage.py createsuperuser`

Username (leave blank to use 'jussinousiainen'): selleri
Email address: juno.athome@gmail.com
Password: su
Password (again):
Superuser created successfully.
```

