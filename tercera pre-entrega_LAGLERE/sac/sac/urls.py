# sac/urls.py

from django.contrib import admin
from django.urls import path
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('compras/', views.lista_compras, name='lista_compras'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('agregar_empleado/', views.agregar_empleado, name='agregar_empleado'),
    path('agregar_compra/', views.agregar_compra, name='agregar_compra'),
    path('buscar/', views.buscar, name='buscar'),
    path('', views.inicio, name='inicio'),
]
