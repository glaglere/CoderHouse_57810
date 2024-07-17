# webapp/forms.py
from datetime import datetime

from django import forms
from django.core.validators import MinLengthValidator, RegexValidator

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

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario

# Validación de la fortaleza de la contraseña
def validate_password_strength(value):
    validators = [
        MinLengthValidator(8),
        RegexValidator(r'\d', 'La contraseña debe contener al menos un dígito.'),
        RegexValidator(r'[A-Z]', 'La contraseña debe contener al menos una letra mayúscula.'),
        RegexValidator(r'[a-z]', 'La contraseña debe contener al menos una letra minúscula.'),
        RegexValidator(r'\W', 'La contraseña debe contener al menos un carácter especial.'),
    ]
    for validator in validators:
        validator(value)

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password_strength])

    class Meta:
        model = Usuario
        fields = ['username', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Usuario.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya existe. Por favor, elija otro.")
        return username

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)