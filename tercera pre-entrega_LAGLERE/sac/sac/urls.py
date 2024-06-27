# sac/urls.py

from django.contrib import admin
from django.urls import path
from webapp.views import lista_productos, inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', lista_productos, name='lista_productos'),
    path('', inicio, name='inicio'),
]
