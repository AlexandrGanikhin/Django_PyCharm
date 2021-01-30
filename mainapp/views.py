from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mainapp.models import ProductCategory, Product


def index(request):
    context = {
        'title': '- главная',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id).order_by('price')
    else:
        products = Product.objects.all().order_by('price')

    context = {
        'title': '- товары',
        'products': products,
        'category': ProductCategory.objects.all(),
    }
    paginator=Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator(paginator.num_pages)

    context.update({'products': products_paginator})

    return render(request, 'mainapp/products.html', context)
