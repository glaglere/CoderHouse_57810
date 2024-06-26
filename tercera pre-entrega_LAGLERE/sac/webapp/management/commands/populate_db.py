from django.core.management.base import BaseCommand
from faker import Faker
from webapp.models import Cliente, Producto, Empleado, Compra
import random

class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create Clientes
        clientes = []
        for _ in range(50):
            cliente = Cliente.objects.create(
                nombre=fake.first_name(),
                apellido=fake.last_name(),
                edad=fake.random_int(min=1, max=120),
                ciudad=fake.city(),
                email=fake.unique.email(),
                direccion=fake.address(),
                telefono=fake.phone_number()
            )
            clientes.append(cliente)

        # Create Productos
        productos = []
        for _ in range(50):
            producto = Producto.objects.create(
                nombre=fake.unique.catch_phrase(),
                descripcion=fake.text(max_nb_chars=200),
                precio=fake.random_number(digits=5, fix_len=True),
                stock=fake.random_int(min=1, max=100)
            )
            productos.append(producto)

        # Create Empleados
        empleados = []
        for _ in range(50):
            empleado = Empleado.objects.create(
                nombre=fake.first_name(),
                apellido=fake.last_name(),
                edad=fake.random_int(min=1, max=120),
                ciudad=fake.city(),
                numero_funcionario=fake.unique.bothify(text='??######'),
                puesto=fake.job(),
                salario=fake.random_number(digits=5, fix_len=True),
                fecha_contratacion=fake.date_this_decade()
            )
            empleados.append(empleado)

        # Create Compras
        for _ in range(50):
            Compra.objects.create(
                cliente=random.choice(clientes),
                producto=random.choice(productos),
                fecha=fake.date_this_year(),
                cantidad=fake.random_int(min=1, max=10)
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with dummy data'))
