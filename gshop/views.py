from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
menu = ["О магазине", "Каталог товаров", "Войти", "Корзина", "Обратная связь"]
template_args = {
    "menu": menu,
    "title": "Default page"
}


def index(request):
    args = template_args
    args["title"] = "Добро пожаловать!"
    return render(request, 'gshop/index.html', args)


def about(request):
    args = template_args
    args["title"] = "О магазине"
    return render(request, 'gshop/about.html', {"menu": menu, "title": "О магазине"})


def categories(request, catid):
    return HttpResponse(f"<h1>category page {catid}</h1>")


def product(request, productid):
    args = template_args
    try:
        item = Product.objects.get(pk=productid)
    except models.ObjectDoesNotExist:
        return all_products(request)
    args["title"] = f"{item.name}"
    args["name"] = item.name
    args["price"] = item.price
    args["description"] = item.description
    args["product"] = item
    return render(request, 'gshop/product.html', args)


def all_products(request):
    args = template_args
    args["title"] = "Полный список товаров"
    args["products"] = [item for item in Product.objects.all()]
    return render(request, 'gshop/all_products.html', args)
