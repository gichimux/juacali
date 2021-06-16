from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from .models import Vendor
from products.models import Product
from .forms import ProductForm


def become_vendor(request):
   
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid ():
            user = form.save()
            login (request, user)
            vendor = Vendor.objects.create(name=user.username, created_by=user)
            return redirect ('index')
    else:
        form = UserCreationForm()
         
    context ={
        "form": form,
    }
    return render (request, 'vendors/become-vendor.html', context )

@login_required
def vendor_admin(request):
    vendor = request.user.vendor
    products = vendor.products.all()
    context = {
        "vendor":vendor,
        "products":products,
    }
    return render (request, 'vendors/vendor-admin.html', context)

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.title)
            product.save()

            return redirect('vendor_admin')
    else:
        form = ProductForm()
    context = {
        "form":form,
    }
    return render(request, 'vendors/add-product.html', context)