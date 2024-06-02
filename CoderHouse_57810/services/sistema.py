from CoderHouse_57810.models.administrador import Administrador
from CoderHouse_57810.models.cliente import ClientePersona, ClienteCorporativo
from CoderHouse_57810.models.compra import Compra
from CoderHouse_57810.models.producto import Producto


class Sistema:
    def __init__(self):
        self.clientes_personas = []
        self.clientes_corporativos = []
        self.administradores = []
        self.productos = []
        self.carritos = {}
        self.compras = []

    # sistema.py
    def agregar_cliente_persona(self, cliente):
        if isinstance(cliente, ClientePersona):
            self.clientes_personas.append(cliente)
            self.carritos[cliente.email] = []
        else:
            raise TypeError("El cliente debe ser una instancia de ClientePersona")

    def agregar_cliente_corporativo(self, cliente):
        if isinstance(cliente, ClienteCorporativo):
            self.clientes_corporativos.append(cliente)
            self.carritos[cliente.email] = []
        else:
            raise TypeError("El cliente debe ser una instancia de ClienteCorporativo")

    def agregar_administrador(self, nuevo_administrador):
        if isinstance(nuevo_administrador, Administrador):
            self.administradores.append(nuevo_administrador)
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
        self.carritos.pop(email, None)

    def eliminar_cliente_corporativo(self, email):
        self.clientes_corporativos = [c for c in self.clientes_corporativos if c.email != email]
        self.carritos.pop(email, None)

    def eliminar_administrador(self, email):
        self.administradores = [a for a in self.administradores if a.email != email]

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.id_producto != id_producto]

    def agregar_producto_al_carrito(self, email, producto):
        if email in self.carritos:
            self.carritos[email].append(producto)
        else:
            raise ValueError("El cliente no existe")

    def mostrar_carrito(self, email):
        if email in self.carritos:
            return self.carritos[email]
        else:
            raise ValueError("El cliente no existe")

    def concretar_compra(self, email):
        if email in self.carritos and self.carritos[email]:
            compra = Compra(cliente=self.buscar_cliente(email), productos=self.carritos[email])
            self.compras.append(compra)
            self.carritos[email] = []
            return compra
        else:
            raise ValueError("El carrito está vacío o el cliente no existe")

    def buscar_cliente(self, email):
        for cliente in self.clientes_personas + self.clientes_corporativos:
            if cliente.email == email:
                return cliente
        return None