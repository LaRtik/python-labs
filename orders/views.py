from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    default_data = {"first_name": request.user.first_name, "last_name":
            request.user.last_name, "address": "Ваш адрес"}

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            if len(cart) == 0:
                return redirect('all_products')
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/after_checkout.html',
                          {'order': order})
    else:
        form = OrderCreateForm(default_data)
    return render(request, 'orders/checkout.html',
                  {'cart': cart, 'form': form, 'user': request.user, "title":"Оформление заказа"})
