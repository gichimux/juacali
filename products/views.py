import random

from django.db.models import Q 
from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    context = {
        'products': products,
        'query': query,
    }
    return render (request, 'products/search.html', context)

def product_details(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    similar_products = list(product.category.products.exclude(id=product.id))

    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)

    context = {
        'product': product,
        'similar_products': similar_products,
    }
    return render(request, 'products/product-detail.html', context)

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    context = {
        'category': category,
    }
    return render(request, 'products/category.html', context)