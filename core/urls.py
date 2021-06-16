from . import views
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static


urlpatterns = [
    path(r'', views.index, name='index'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)