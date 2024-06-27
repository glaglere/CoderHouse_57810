from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=100, default='Nombre')
    apellido = models.CharField(max_length=100, default='Apellido')
    edad = models.IntegerField(default=0)
    ciudad = models.CharField(max_length=100, default='Ciudad')

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Cliente(Persona):
    email = models.EmailField()
    direccion = models.CharField(max_length=255, default='Direccion')
    telefono = models.CharField(max_length=20, default='0000000000')

    def __str__(self):
        return self.nombre


class Empleado(Persona):
    puesto = models.CharField(max_length=100, default='Puesto')
    salario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fecha_contratacion = models.DateField(default='2000-01-01')

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.puesto}"


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre


class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.cliente} compró {self.cantidad} de {self.producto}"
