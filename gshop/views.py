from django.shortcuts import render, redirect
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


def category(request, category_slug):
    cat = Category.objects.get(slug=category_slug)
    context = {
        "menu": menu,
        "title": cat,
        "products": Product.objects.filter(category__slug=category_slug),
        "cat_selected": cat.id,
    }
    return render(request, 'gshop/all_products.html', context=context)


def product(request, product_slug):
    try:
        item = Product.objects.get(slug=product_slug)
    except models.ObjectDoesNotExist:
        return redirect(all_products)
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
