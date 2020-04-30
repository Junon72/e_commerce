# e-commerce

## index

1. [Setting up VSCode](#Setting-up-VSCode)
2. [Create a django project](#Create-a-django-project)
3. [Reusing an accounts app](#Reusing-an-account-app)
4. [Create apps home and products](#Create-apps-home-and-products)
5. [Creating and testing product models](#Creating-and-testing-product-models)
6. [Products views and urls](#Products-views-and-urls)






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

[Top](#index)

## Reusing an accounts app

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

In browser type http://127.0.0.1:8000/accounts/register/ - app is working

[Top](#index)

## Create apps home and products

Create an app home and register it in INSTALLED_APPS

`python3 manage.py startapp home`

In home > views.py create a index page path

```python
# Create your views here.
def index(request):
    """A view that display django index page"""
    return render(request, 'index.html')
```

Create a templates directory within home with a index.html

```html
{% extends 'base.html' %}

{% block content %}
{% endblock %}
```

Create app products

`python3 manage.py startapp products`

In settings.py register the app in INSTALLED_APPS

[Top](#index)

## Creating and testing product models

In products > models.py create a product model

```python
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="images")
 
    def __str__(self):
        return self.name
```

In products admin.py, import and register Product

```python
from .models import Product
admin.site.register(Product)
```

In tests.py create a test for the module

```python
from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTests(TestCase):
    """
    Here we'll define the tests
    that we'll run against our Product models
    """

    def test_str(self):
        test_name = Product(name="A Product")
        self.assertEqual(str(test_name), 'A Product')
```

Install Pillow to allow uploading of images.

**When working with Mac and Django3 first `brew install libjpeg`

`pip3 install Pillow`

`pip3 freeze > requirements.txt`

Migrate products app

`python3 manage.py makemigrations products`

`python3 manage.py migrate products`

Test products - test passed

`python3 manage.py test products`

```bash
OK
Destroying test database for alias 'default'...
```

[Top](#index)

## Products views and urls

In products > views.py create a route for all products

```python
from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products():
    products = Products.objects.all()
    return render(request, "products.html", ("products", products))
```

In products create urls.py file and register all_products path

```python
from django.urls import path, include
from .views import all_products


urlpatterns = [
    path('', all_products, name="products")
]
```

In products create templates directory and in it products.html

```html
{% extends 'base.html' %}

{% block content %}

<div class="row row-flex">
    {% for product in products %}

    <div class="col-xs-10 col-xs-offset-1 col-sm-offset-0 col-sm-6 col-md-4 display panel panel-default">

        <div class="panel-body">
            <div class="product" style="background-image: url('{{ MEDIA_URL }}{{ products_image }}')"></div>

            <h3>{{ product.name }}</h3>
            <p class="products-description">{{ products.description }}</p>
            <p>{{ product.price }}</p>

            <form method="post" action="{% url 'add_to_cart' product.id %">
            {% csrf_token %}
            <div class=" input-group">
                <input name="quantity" type="number" min="1" max="999" class="form-control" placeholder="Quantity">
                <span class="input-group-button">
                    <button class="btn btn-success" type="submit">Add</button>
                </span>
            </div>
        </form>
    </div>
</div>
{% endfor %}
</div>
{% endblock %}
```

In settings.py TEMPLATES add context processor for media

```python
'django.template.context_processors.media',
```