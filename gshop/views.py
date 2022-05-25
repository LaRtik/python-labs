from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
menu = [{"title": "Home", "url_name": "home"},
        {"title": "О магазине", "url_name": "about"},
        {"title": "Каталог товаров", "url_name": "all_products"},
        {"title": "Корзина", "url_name": "home"},  # todo: cart
        {"title": "Обратная связь", "url_name": "home"},  # todo: contact
]


def index(request):
    context = {
        "menu": menu,
        "title": "Добро пожаловать!"
    }
    return render(request, 'gshop/index.html', context=context)


def about(request):
    context = {
        "menu": menu,
        "title": "О магазине",
    }
    return render(request, 'gshop/about.html', context=context)


def category(request, category_id):
    context = {
        "menu": menu,
        "title": Category.objects.get(pk=category_id),
        "products": Product.objects.filter(category_id=category_id),
        "categories": Category.objects.all(),
    }
    return render(request, 'gshop/all_products.html', context=context)


def product(request, productid):
    try:
        item = Product.objects.get(pk=productid)
    except models.ObjectDoesNotExist:
        return all_products(request)
    context = {
        "menu": menu,
        "title": item.name,
        "product": item
    }
    return render(request, 'gshop/product.html', context=context)


def all_products(request):
    context = {
        "menu": menu,
        "title": "Полный список товаров",
        "products": [item for item in Product.objects.all()],
        "categories": Category.objects.all(),
    }

    return render(request, 'gshop/all_products.html', context=context)
