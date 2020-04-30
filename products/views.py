from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products():
    products = Products.objects.all()
    return render(request, "products.html", ("products", products))