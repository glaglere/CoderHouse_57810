from django.core.management.base import BaseCommand
from faker import Faker

from webapp.models import Cliente, Producto, Empleado


class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create Clientes
        for _ in range(50):
            Cliente.objects.create(
                nombre=fake.first_name(),
                apellido=fake.last_name(),
                edad=fake.random_int(min=18, max=90),
                ciudad=fake.city(),
                email=fake.email(),
                direccion=fake.address(),
                telefono=fake.phone_number()
            )

        # Create Productos
        for _ in range(50):
            Producto.objects.create(
                nombre=fake.word(),
                descripcion=fake.text(),
                precio=fake.random_number(digits=5, fix_len=True),
                stock=fake.random_int(min=1, max=100)
            )

        # Create Empleados
        for _ in range(50):
            Empleado.objects.create(
                nombre=fake.first_name(),
                apellido=fake.last_name(),
                edad=fake.random_int(min=18, max=65),
                ciudad=fake.city(),
                puesto=fake.job(),
                salario=fake.random_number(digits=5, fix_len=True),
                fecha_contratacion=fake.date_this_decade()
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with dummy data'))
