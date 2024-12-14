from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('product_page'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QNOEuAWsJngv0aPY7dXSg1pnKjxoeIi6bsaXjNN3BWiESAJ4eytVlnyIcj2fZylwwy7NCaZ5Nlm09x2ZzOxxNis00O66WImVq'
    }

    return render(request, template, context)