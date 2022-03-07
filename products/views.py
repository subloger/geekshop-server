from django.shortcuts import render

from products.models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context=context)


def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 3)
    try:
        products_papaginator = paginator.page(page)
    except PageNotAnInteger:
        products_papaginator = paginator.page(1)
    except EmptyPage:
        products_papaginator = paginator.page(paginator.num_pages)
    context = {
        'title': 'GeekShop - Каталог',
        'productcategory': ProductCategory.objects.all(),
        'products': products_papaginator,
    }
    return render(request, 'products/products.html', context)
