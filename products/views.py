from django.shortcuts import render

from products.models import ProductCategory, Product


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context=context)


def products(request, category_id=None):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    context = {
        'title': 'GeekShop - Каталог',
        'productcategory': ProductCategory.objects.all(),
        'products': products,
    }
    return render(request, 'products/products.html', context)
