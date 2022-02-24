from django.shortcuts import render

from products.models import ProductCategory, Product


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context=context)


def products(request):
    categories = ProductCategory.objects.all()
    context = {
        'title': 'GeekShop - Каталог',
        'productcategory': categories,
        'products': Product.objects.all()
    }
    return render(request, 'products/products.html', context)
