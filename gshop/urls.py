from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('products/', AllProducts.as_view(), name="all_products"),
    #path('login/', AllProducts.as_view(), name="login"),
    #path('register/', RegisterUser.as_view(), name="register"),
    path('<slug:category_slug>/', CatProducts.as_view(), name="category"),
    path('<slug:category_slug>/<slug:product_slug>/', UnoProduct.as_view(), name="product"),

]
