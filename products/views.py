import json

from django.shortcuts import render
from .models import ProductCategory, Product

with open('products/fixtures/products.json', 'r', encoding='utf-8') as f:
    prod = json.load(f)
# Create your views here.


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context=context)


def products(request):
    ppp = ProductCategory.objects.all
    context = {
        'title': 'GeekShop - Каталог',
        'productcategory': ppp,
        'products': prod
    }
    return render(request, 'products/products.html', context)
