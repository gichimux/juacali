from . import views
from django.urls import path


urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_details, name='product_details'),
    path('<slug:category_slug>/', views.category, name='category'),
]