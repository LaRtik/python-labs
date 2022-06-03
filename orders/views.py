from django.shortcuts import render
from django.views.generic import CreateView

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST, initial={"first_name": request.user.first_name, "last_name":
            request.user.last_name})
        if form.is_valid():
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
        form = OrderCreateForm
    return render(request, 'orders/checkout.html',
                  {'cart': cart, 'form': form, 'user': request.user})
