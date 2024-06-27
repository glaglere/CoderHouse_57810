from django.contrib import admin
from .models import Producto, Cliente, Empleado, Compra

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Compra)
