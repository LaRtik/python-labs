from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('cats/<int:catid>/', categories),
    path('product/<int:productid>/', product),
]
