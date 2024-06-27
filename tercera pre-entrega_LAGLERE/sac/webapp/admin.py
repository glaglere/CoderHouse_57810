from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Producto, Cliente, Persona, Compra

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Persona)
admin.site.register(Compra)