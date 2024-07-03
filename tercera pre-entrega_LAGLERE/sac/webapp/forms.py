# webapp/forms.py
from datetime import datetime

from django import forms

from .models import Cliente, Empleado, Compra
from .models import Producto


# webapp/forms.py

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
        fields = ['numero_funcionario', 'nombre', 'apellido', 'edad', 'ciudad', 'puesto', 'salario',
                  'fecha_contratacion']
        widgets = {
            'fecha_contratacion': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmpleadoForm, self).__init__(*args, **kwargs)
        self.fields['fecha_contratacion'].initial = datetime.today().strftime('%Y-%m-%d')


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['cliente', 'producto', 'fecha', 'cantidad']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        self.fields['fecha'].initial = datetime.today().strftime('%Y-%m-%d')


class BuscarForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)
