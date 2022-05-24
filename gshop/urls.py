from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('products/<int:productid>/', product, name="product"),
    path('products/', all_products, name="all_products"),
    path('products/category/<int:category_id>', category, name="category"),
    path('about/', about, name="about")
]
