# webapp/forms.py

from django import forms
from .models import Producto, Cliente, Empleado, Compra


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'edad', 'ciudad', 'email', 'direccion', 'telefono']


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'edad', 'ciudad', 'puesto', 'salario', 'fecha_contratacion']


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['cliente', 'producto', 'fecha', 'cantidad']


class BuscarForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)
