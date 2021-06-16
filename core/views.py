from django.shortcuts import render, get_object_or_404

from products.models import Product
def index(request):
    latest_products = Product.objects.all() [0:8]
    product = Product.objects.all()

    context ={
        "latest_products": latest_products,
    }
    return render (request, 'core/frontpage.html', context )