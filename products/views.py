from django.shortcuts import render
from .models import Product

# Create your views here.

def product_page(request):
    """ A view to show all products"""
    
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/product_page.html', context)
