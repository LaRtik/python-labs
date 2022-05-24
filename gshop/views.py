from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("shop main page")


def categories(request, catid):
    return HttpResponse(f"<h1>category page {catid}</h1>")


def product(request, productid):
    return HttpResponse(f"product {productid}")


