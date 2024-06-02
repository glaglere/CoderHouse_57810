import json

from tabulate import tabulate

from CoderHouse_57810.models.administrador import Administrador
from CoderHouse_57810.models.cliente import ClientePersona, ClienteCorporativo
from CoderHouse_57810.services.helpers import verificar_password


class ClienteService:
    def __init__(self):
        self.clientes_personas = []
        self.clientes_corporativos = []
        self.administradores = []
        self.carritos = {}

    def agregar_cliente_persona(self, cliente):
        self.clientes_personas.append(cliente)
        self.carritos[cliente.email] = []

    def agregar_cliente_corporativo(self, cliente):
        self.clientes_corporativos.append(cliente)
        self.carritos[cliente.email] = []

    def agregar_administrador(self, nuevo_administrador):
        self.administradores.append(nuevo_administrador)

    def mostrar_clientes(self):
        """
        Muestra la lista de clientes del sistema.
        """
        print("Clientes Personas:")
        if self.clientes_personas:
            table = [[cliente.nombre, cliente.email, cliente.direccion, cliente.telefono, cliente.dni] for cliente in
                     self.clientes_personas]
            print(tabulate(table, headers=["Nombre", "Email", "Dirección", "Teléfono", "DNI"], tablefmt="pretty"))
        else:
            print("No hay clientes personas registrados.")

        print("\nClientes Corporativos:")
        if self.clientes_corporativos:
            table = [[cliente.nombre, cliente.email, cliente.direccion, cliente.telefono, cliente.cuit] for cliente in
                     self.clientes_corporativos]
            print(tabulate(table, headers=["Nombre", "Email", "Dirección", "Teléfono", "CUIT"], tablefmt="pretty"))
        else:
            print("No hay clientes corporativos registrados.")

    def mostrar_administradores(self):
        """
        Muestra la lista de administradores del sistema.
        """
        print("Administradores:")
        if self.administradores:
            table = [[admin.nombre, admin.email, admin.codigo_funcionario] for admin in self.administradores]
            print(tabulate(table, headers=["Nombre", "Email", "Código Funcionario"], tablefmt="pretty"))
        else:
            print("No hay administradores registrados.")

    def eliminar_cliente_persona(self, email):
        self.clientes_personas = [c for c in self.clientes_personas if c.email != email]
        self.carritos.pop(email, None)

    def eliminar_cliente_corporativo(self, email):
        self.clientes_corporativos = [c for c in self.clientes_corporativos if c.email != email]
        self.carritos.pop(email, None)

    def eliminar_administrador(self, email):
        self.administradores = [a for a in self.administradores if a.email != email]

    def agregar_producto_al_carrito(self, cliente, producto, cantidad):
        self.carritos[cliente.email].append({"producto": producto, "cantidad": cantidad})

    def quitar_producto_del_carrito(self, cliente, id_producto):
        carrito = self.carritos[cliente.email]
        for item in carrito:
            if item["producto"].id_producto == id_producto:
                carrito.remove(item)
                return
        raise ValueError("El producto no está en el carrito")

    def mostrar_carrito(self, cliente):
        return self.carritos[cliente.email]

    def vaciar_carrito(self, cliente):
        self.carritos[cliente.email] = []

    def buscar_cliente(self, email):
        for cliente in self.clientes_personas + self.clientes_corporativos:
            if cliente.email == email:
                return cliente
        return None

    def verificar_credenciales(self, email, password):
        """
        Verifica las credenciales del cliente.

        Args:
            email (str): El correo electrónico del cliente.
            password (str): La contraseña del cliente.

        Returns:
            bool: True si las credenciales son válidas, False en caso contrario.
        """
        cliente = self.buscar_cliente(email)
        if cliente and verificar_password(password, cliente.password):
            return cliente
        return None

    def guardar_datos(self):
        with open("personas.json", "w", encoding='utf-8') as f:
            json.dump([cliente.to_dict() for cliente in
                       self.clientes_personas + self.clientes_corporativos + self.administradores], f, indent=4,
                      ensure_ascii=False)

    def cargar_datos(self):
        try:
            with open("personas.json", "r", encoding='utf-8') as f:
                personas_data = json.load(f)
                for p in personas_data:
                    if p["tipo"] == "ClientePersona":
                        cliente = ClientePersona.from_dict(p)
                        self.clientes_personas.append(cliente)
                        self.carritos[cliente.email] = []
                    elif p["tipo"] == "ClienteCorporativo":
                        cliente = ClienteCorporativo.from_dict(p)
                        self.clientes_corporativos.append(cliente)
                        self.carritos[cliente.email] = []
                    elif p["tipo"] == "Administrador":
                        admin = Administrador.from_dict(p)
                        self.administradores.append(admin)
        except FileNotFoundError:
            pass  # No hay datos que cargar inicialmente
