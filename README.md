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
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
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
                <span class="input-group-btn">
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

In settings.py TEMPLATES add context processor for media and media root

```python
'django.template.context_processors.media',

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```


In ecommmerse > urls.py register path to all_products as the index, and register MEDIA_URL and STATIC_URL path

```python
from django.contrib import admin
from django.urls import path, include
from products.views import all_products
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_products, name="index"),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('accounts.url_reset')),
    path('products/', include('products.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Go to http://127.0.0.1:8000/products/ - there is no products added yet.

In http://127.0.0.1:8000/admin/ add a test product

Open site view - there is no add to cart button

[Top](#index)

## Storing Shopping Cart Items In A Session

Create a new app cart and add it to the INSTALLED_APPS

`python3 manage.py startapp cart`

In cart, create context.py file

- Unlike the products app, where we created a model which then puts products into our database, in this case, the cart items will not go into the database.
They will just be stored in the session when the user is logged in. A user can add products to their cart, but when they log out, that cart will be lost.

```python
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):
    """
    Ensure that the cart contents are available when rendering any page
    """

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})

    return { 'cart_items': cart_items, 'total': total, 'product_count': product_count }
```

In settings.py the cart_contents to the context processor list in TEMPLATES

```python
'cart.context.cart_contents'
```

In cart create urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name="view_cart"),
    path('add/<id>/', views.add_to_cart, name="add_to_cart"),
    path('adjust/<id>/', adjust_cart, name="adjust_cart")
]
```

In cart > views.py add route to the views

```python
from django.shortcuts import render, reverse, redirect

# Create your views here.
def view_cart(request):
    """
    A view that renders the cart contents page
    """
    return render(request, "cart.html")

def add_to_cart(request, id):
    """
    Add a quantity of the specified products to the cart
    """
    quantity=int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified amount
    """
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    retrun redirect(reverse('view_cart'))
```

In cart add a templates folder and cart.html in it

```html
{% extends 'base.html' %}
{% load static %}
{% load bootstrap_tags %}

{% block content %}
<div class="row row-flex">
    {% for item in cart_items %}
    
    <div class="col-xs-10 col-xs-offset-1 col-sm-offset-0 col-sm-6 col-md-4 display panel panel-display">
        
        <div class="product" style="background-image: url('{{ MEDIA_URL }}{{ item.product.image }}')"></div>
        
        <div class="caption">
            <h3>{{ item.product.name }}</h3>
            <p class="product-description">{{ item.product.description }}</p>
            <p>{{ item.product.price }}</p>
            <p>
                
                <form class="form-inline" method="post" action="{% url 'adjust_cart' item.id %}">
                    {% csrf_token %}
                    <div class="form-group">
                        <label for="exampleInputAmount" class="sr-only">New Qty</label>
                        <div class="input-group">
                            <div class="input-group-addon">Qty</div>
                            <input name="quantity" type="number" min="0" max="999" class="form-control">
                            <div class="input-group-addon">{{item.quantity}}</div>
                            <span class="input-group-btn">
                                <button type="submit" class="btn btn-primary"><span class="glyphicon glyphicon-edit"
                                        aria-hidden="true"></span>Amend</button>
                            </span>
                        </div>
                </form>
            </p>
        </div>
    </div>
    {% endfor %}
</div>
<div class="row">
    <p>Total</p>
    <p><span class="glyphicon glyphicon-euro" aria-hidden="true"></span>{{ total }}</p>
    <a href="/" class="btn btn-success" role="button"><span class="glyphicon glyphicon-ok-sign" aria-hidden="true"></span>Checkout</a>
</div>

{% endblock %}
```

Migrate the app

```bash
python3 manage.py makemigrations cart

python3 manage.py migrate cart
```

There's nothing to migrate because there is no model, and there is no database table to create.
A session is stored entirely within your browser memory.

Go to products and try to add a product to the cart.

**Issues:**

```bash
Using the URLconf defined in ecommerce.urls, Django tried these URL patterns, in this order:
    admin/
    [name='index']
    accounts/
    accounts/
    products/
    cart/
    ^static/(?P<path>.*)$
    ^media/(?P<path>.*)$
The current path, {% url 'add_to_cart' product.id %, didn't match any of these.
```

Missing } at {% url 'add_to_cart' product.id % >

`Reverse for ‘add_to_cart’ not found. ‘add_to_cart’ is not a valid view function or pattern name. `

Cart > templates folder name written wrong

In cart > views.py

`return redirect(reverse('view_cart'))` had `('index.html')` instead >

`NoReverseMatch: Reverse for 'add_to_cart' not found. 'add_to_cart' is not a valid view function or pattern name.`

In cart > urls.py

```python
    path('add/<id>', views.add_to_cart, name="add_to_cart"), # >'add/<id>/'
    path('adjust/<id>', adjust_cart, name="adjust_cart") # 'adjust/<id>/'
```



## Searching for a product

Start a new app and add it to the INSTALLED_APPS

`python3 manage.py startapp search`

In search views.py create do_search select2-results__option--highlighted

```python
from django.shortcuts import render
from products.models import Product

# Create your views here.
def do_search(request):
    products = Products.objects.filter(name_icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})
```

We have the model called Product.objects.filter. Filter is a built-in function.
(name_icontains=request.GET['q']), will get whatever 'q' is returned from the form named 'q'.
Whatever you type into that form will then be used to filter the products.

In search urls.py register the path and include the path to ecommerce urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.do_search, name="search")
]
```

`path('search/', include('search.urls')),`

In base.html (search is accessible from everywhere on the site), modify the header and add search link

```html
% load static %}
<!DOCTYPE html>
<html lang="en">

    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Ecommerce</title>
        <!-- Bootstrap CSS -->
        <link rel="stylesheet"
            href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/3.3.7/cerulean/bootstrap.min.css">
        <link rel="stylesheet" href="{% static 'font-awesome/css/font-awesome.min.css' %}">
        <link rel="stylesheet" href="{% static 'css/custom.css' %}">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </head>

    <body>
        <!-- Fixed masthead -->
        <nav class="navbar navbar-masthead navbar-default navbar-fixed-top">
            <div class="container">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar"
                        aria-expanded="false" aria-controls="navbar">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="/">Ecommerce</a>
                </div>
                <div id="navbar" class="navbar-collapse collapse">
                    <ul class="nav navbar-nav navbar-right">
                        {% if user.is_authenticated %}
                        <li><a href="{% url 'profile' %}">Profile</a></li>
                        <li><a href="{% url 'logout' %}">Log Out</a></li>
                        {%  else %}
                        <li><a href="{% url 'register' %}">Register</a></li>
                        <li><a href="{% url 'login' %}">Log In</a></li>
                        {% endif %}
                        <li>
                            <a href="{% url 'view_cart' %}">
                                <i class="fa fa-shipping-cart"></i>Cart
                                {% if product_count > 0 %}
                                <label class="badge badge-warning">{{ product_count }}</label>
                                {% endif %}
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <h1>{% block page_heading %}{% endblock %}</h1>
        {% if messages %}
        <div>
            {% for message in messages %}
            {{ message  }}
            {% endfor %}
        </div>
        {% endif %} {% block content %}{% endblock %}

        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"
            integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous">
        </script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
            integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous">
        </script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"
            integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous">
        </script>
    </body>

</html>
```

[Top](#index)

## Styling

Go to https://fontawesome.com/
Select Start for Free and Download
Select Download for free for Web. Unzip the file.

In static add font-awesome directory and add css folder to it
Copy fontawesome.css and fontawesome.min.css from downloaded css file

In static font-awesome directory add fonts folder
Copy fonts from webfonts to it

In browser check http://127.0.0.1:8000/cart/ - works

In admin add a product.

Check - works

[Top](#index)

## Setting up Stripe

Install Stripe

`pip3 install Stripe`

`pip3 freeze > requirements.txt`

Go to stripe.com and create an account by clicking Start, fill in the form and submit.
After registering, sign-in and got to dashboard. On the left hand side click Developers.
Click API keys. In API keys click Reveal test key token.

In settings.py set path for Publishable key and Secret key

STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')

Create env.py in root directory and add the kay values there

```python
import os

os.environ.setdefault("STRIPE_PUBLISHABLE", "...")
os.environ.setdefault("STRIPE_SECRET", "...")
```

## Checkout app

create a checkout app and add it to INSTALLED_APPS

`python3 manage.py startapp checkout`

`'checkout',`

In checkout > models.py create a model for orders and order line item

```python
from django.db import models
from product.models import Product

# Create your models here.

class Order(models.Model):
    full_name - models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return"{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.PROTECT)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, 
                                self.product.name, self.product.price)
```

Register models in checkout admin.py

```python
from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem

 class OrderAdmin(admin.ModelAdmin):
     inlines = (OrderLineAdminInline, )

admin.siteregister(Order, OrderAdmin)
```

TabularInline subclass defines the template used to render the Order in the admin interface. StackInline is another option.

More about [models](https://docs.djangoproject.com/en/3.0/topics/db/models/) and [registering models in admin](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/)

Migrate the app

`python3 manage.py makemigrations checkout`

`python3 manage.py migrate checkout`

**Error:**

`TypeError: __init__() missing 1 required positional argument: 'on_delete'`

Since Django 2.0 the ForeignKey field requires two positional arguments:

the model to map to
the on_delete argument
categorie = models.ForeignKey('Categorie', on_delete=models.PROTECT)
Here are some methods can used in on_delete

CASCADE
Cascade deletes. Django emulates the behavior of the SQL constraint ON DELETE CASCADE and also deletes the object containing the ForeignKey

PROTECT
Prevent deletion of the referenced object by raising ProtectedError, a subclass of django.db.IntegrityError.

DO_NOTHING
Take no action. If your database backend enforces referential integrity, this will cause an IntegrityError unless you manually add an SQL ON DELETE constraint to the database field.

you can find more about on_delete by reading the [documentation](https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_one/).

**Error:**

`IndentationError: unindent does not match any outer indentation level`

VSCode added a space front of the line 8 and 9

## Checkout forms

In checkout create forms.py and a forms for customers to purchase our products.

```python
from django import forms
from .models import Order

class MakePaymentForm(forms.Form):
    """Payment form allows the user to pay with a credit card"""

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


    class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'country', 'postcode',
            'town_or_city', 'street_address1', 'street_address2',
            'county'
        )
```

Stripe will deal with the encryption of the credit card details through Stripe's JavaScript. Therefore it is possible to do required=false here in Django forms so that the plain text is not transmitted through the browser making it more secure.
It's not visible to people who might be snooping on the webpage.
Stripe requires an ID, and although the input is added into the form, the user won't actually see it. Django has a widget within forms called HiddenInput.
This means that something will be inputted into the form, but it will be hidden from the user.

## Checkout views

In checkout views.py add checkout routes

```python
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product

import stripe

# Create your views here.

stripe_api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save

            cart = request.session.get('cart', [])
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order = order,
                    product = product,
                    quantity = quantity
                    )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
```


## Checkout html

In checkout create urls.py and urls.py create checkout route

```python
from djangourls import path
from . import views

urlpaterns = [
    path('', views.checkout, name='checkout')
]
```

In ecommerce urls.py include checkout urls

```python
path('checkout/', include('checkout.urls'))
```

In checkout add a templates folder and checkout.html file in it

```html
{% extends "base.html" %}
{% load static %}
{% load bootstrap_tags %}

{% block head_js %}
<script type="text/javascript" src="https://js.stripe.com/v2/"></script>
<script type="text/javascript">
    //<![CDATA[
        Stripe.publishableKey = '{{ publishable }}';
    //]]>
</script>
<script type="text/javascript" src="{% static 'js/stripe.js' %}"></script>
{% endblock %}

{% block content %}
<div class="row row-flex">
    {% for item in cart_items %}
        <div class="col-xs-10 col-xs-offset-1 col-sm-offset-0 col-sm-6 col-md-4 display panel panel-default">
            <div class="panel-body">
                <div class="product" style="background-image: url('{{ MEDIA_URL }}{{ item.product.image }}')"></div>

                <div class="caption">
                    <h3>{{ item.product.name }}</h3>
                    <p class="product-description">{{ item.product.descriptio }}</p>
                    <p>{{ item.quantity }}</p>
                    <p>item.product.price</p>
                </div>
            </div>
        </div>
    {% endfor %}
</div>
<div class="row">
    <p>Total</p>
    <p><span class="glyphicon glyphicon-euro" aria-hidden="true"></span>{{ total }}</p>
</div>

<form role="form" method="post" id="payment-form" action="{% url 'checkout' %}">
    <legend>Payment Details</legend>

    <div id="credit-card-errors" style="display: none;">
        <div class="alert-message block-message error" id="stripe-error-message"></div>
    </div>

    <div class="form-group col-md-6">
        {{ order_form | as_bootstrap }}
    </div>

    <div class="form-group col-md-6">
        {{ payment_form | as_bootstrap }}
    </div>

    {% csrf_token %}
    <div class="form-group col-md-12">
        <input class=" btn btn-primary" id="submit_payment_btn" name="commit" type="submit" value="Submit Payment">
    </div>
</form>
{% endblock %}
```

Add a block head_js which contains JavaScript that Stripe requires.

```html
    //<![CDATA[
        Stripe.publishableKey = '{{ publishable }}';
    //]]>
```

Will make the Stripe publishable key available on the page
In base.html add in the block head_js as well, under the script tags, at the end of head section

```html
    {% block head_js %}
    {% endblock head_js %}
```

The Stripe error display is default none, but if there is error it will display the message! > Stripe js

In cart.html change the checkout button

`href="{% url 'checkout' %}"`

[Top](#index)

## Stripe JS

In static create a new directory js and stripe.js file in it

```js
$(function() {
    $("#payment-form").submit(function() {
        var form = this;
        var card = {
            number: $("#id_credit_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear : $("#id_expiry_year").val(),
            cvc: $("#id_cvv").val()
        };
    
    Stripe.createToken(card, function(status, response) {
        if (status === 200) {
            $("#credit-card-errors").hide();
            $("#id_stripe_id").val(response.id);

            //Prevent the Credit card Details from being submitted to our server
            $("#id_credit_card_number").removeAttr('name');
            $("#id_cvv").removeAttr('name');
            $("#id_expiry_month").removeAttr('name');
            $("#id_expiry_year").removeAttr('name');

            form.submit();
        } else {
            $("#stripe-error-message").text(response.error.message);
            $("#credit-card-errors").show();
            $("#validate_card_btn").attr("disabled", false);
        }
    });
    return false;
    });
});
```
