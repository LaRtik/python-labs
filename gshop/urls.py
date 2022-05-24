from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('cats/<int:catid>/', categories),
    path('products/<int:productid>/', product),
    path('products/', all_products),
    path('about/', about)
]
