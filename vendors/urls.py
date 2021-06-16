from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static


urlpatterns = [
    path('become-vendor/', views.become_vendor, name='become_vendor'),
    path('vendor-admin/', views.vendor_admin, name='vendor_admin'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='vendors/login.html'), name='login'),

]