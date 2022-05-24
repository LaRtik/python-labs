from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('cats/<int:catid>/', categories, name="categories"),
    path('products/<int:productid>/', product, name="product"),
    path('products/', all_products, name="all_products"),
    path('about/', about, name="about")
]
