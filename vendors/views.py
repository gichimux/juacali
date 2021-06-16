from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Vendor
# Create your views here.

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
    context = {
        "vendor":vendor
    }
    return render (request, 'vendors/vendor-admin.html', context)