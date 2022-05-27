from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('products/<slug:product_slug>/', product, name="product"),
    path('products/', all_products, name="all_products"),
    path('products/category/<slug:category_slug>', category, name="category"),
    path('about/', about, name="about")
]
