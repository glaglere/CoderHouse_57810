from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator


class Persona(models.Model):
    """
    Clase abstracta que representa una persona.
    """
    nombre = models.CharField(max_length=100, default='Nombre')
    apellido = models.CharField(max_length=100, default='Apellido')
    edad = models.PositiveIntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(120)],
        default=18
    )
    ciudad = models.CharField(max_length=100, default='Ciudad')

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Cliente(Persona):
    """
    Clase que representa un cliente.
    """
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=255, default='Direccion')
    telefono = models.CharField(max_length=20, default='0000000000')

    def __str__(self):
        return self.nombre


class Empleado(Persona):
    """
    Clase que representa un empleado.
    """
    numero_funcionario = models.CharField(max_length=20, unique=True)
    puesto = models.CharField(max_length=100, default='Puesto')
    salario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fecha_contratacion = models.DateField(default='2000-01-01')

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.puesto}"


class Producto(models.Model):
    """
    Clase que representa un producto.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre


class Compra(models.Model):
    """
    Clase que representa una compra realizada por un cliente.
    """
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateField()
    cantidad = models.IntegerField()

    # Nuevas clases para manejar los usuarios


class UsuarioManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("El usuario debe tener un nombre de usuario.")
        if not password:
            raise ValueError("El usuario debe tener una contraseña.")

        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'


def __str__(self):
    return f"{self.cliente} compró {self.cantidad} de {self.producto}"
