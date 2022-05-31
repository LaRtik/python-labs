import rest_framework.status as status
from rest_framework.test import APITestCase
from django.urls import resolve, reverse_lazy, reverse
from gshop.models import Product, Category
from django.contrib.auth.models import User


class TestOrders(APITestCase):
    def test_order_create_post(self):
        # create cat and product
        cat = Category.objects.create(name="pizza", slug="pizza")
        prod = Product.objects.create(name="vetchina", slug="vetchina", description="test", price=123.0, category=cat)

        # create and login user
        url = reverse_lazy('login')
        User.objects.create_user({"username": "testbro", "password": "blahblahblah"})
        self.client.post(url, {"username": "testbro", "password": "blahblahblah"})  # user login

        # add to cart
        url = reverse_lazy('cart_add', args=(prod.pk,))
        self.client.post(url)

        # checkout cart
        url = reverse_lazy('checkout')
        code = self.client.post(url, {"first_name": "ilya", "second_name": "lazuk", "email": "i.lazuk@bk.ru",
                                      "address": "blablabla", "postal_code": "212025", "city": "new-york"}).status_code
        self.assertEqual(status.HTTP_200_OK, code)



