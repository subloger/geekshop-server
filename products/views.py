from django.shortcuts import render
from django.conf import settings
from django.core.cache import cache

from products.models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context=context)


def get_products(category=None):
    if settings.LOW_CACHE:
        key = 'products'
        if not category is None:
            key = f'products_{category}'
        products = cache.get(key)
        if products is None:
            products = Product.objects.all()
        else:
            products = Product.objects.all()
            cache.set(key, products)
        return products


def products(request, category_id=None, page=1):
    if category_id:
        products = get_products()  # Product.objects.filter(category_id=category_id)
    else:
        products = get_products()  # Product.objects.all()

    for i in products:
        new_price = i.price - (i.price * i.discount/100)
        i.discount_price = new_price
        i.save()

    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context = {
        'title': 'GeekShop - Каталог',
        'productcategory': ProductCategory.objects.all(),
        'products': products_paginator,
    }
    return render(request, 'products/products.html', context)
