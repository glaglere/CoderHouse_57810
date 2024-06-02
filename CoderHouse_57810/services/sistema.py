from CoderHouse_57810.models.administrador import Administrador
from CoderHouse_57810.models.cliente import ClientePersona, ClienteCorporativo
from CoderHouse_57810.models.producto import Producto


class Sistema:
    def __init__(self):
        self.clientes_personas = []
        self.clientes_corporativos = []
        self.administradores = []
        self.productos = []

    def agregar_cliente_persona(self, cliente):
        if isinstance(cliente, ClientePersona):
            self.clientes_personas.append(cliente)
        else:
            raise TypeError("El cliente debe ser una instancia de ClientePersona")

    def agregar_cliente_corporativo(self, cliente):
        if isinstance(cliente, ClienteCorporativo):
            self.clientes_corporativos.append(cliente)
        else:
            raise TypeError("El cliente debe ser una instancia de ClienteCorporativo")

    def agregar_administrador(self, administrador):
        if isinstance(administrador, Administrador):
            self.administradores.append(administrador)
        else:
            raise TypeError("El administrador debe ser una instancia de Administrador")

    def agregar_producto(self, producto):
        if isinstance(producto, Producto):
            self.productos.append(producto)
        else:
            raise TypeError("El producto debe ser una instancia de Producto")

    def mostrar_clientes(self):
        print("Clientes Personas:")
        for cliente in self.clientes_personas:
            print(cliente)
        print("\nClientes Corporativos:")
        for cliente in self.clientes_corporativos:
            print(cliente)

    def mostrar_administradores(self):
        print("Administradores:")
        for admin in self.administradores:
            print(admin)

    def mostrar_productos(self):
        print("Productos:")
        for producto in self.productos:
            print(producto)

    def eliminar_cliente_persona(self, email):
        self.clientes_personas = [c for c in self.clientes_personas if c.email != email]

    def eliminar_cliente_corporativo(self, email):
        self.clientes_corporativos
