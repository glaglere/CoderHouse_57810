# sistema.py
import json
from tabulate import tabulate
from CoderHouse_57810.models.administrador import Administrador
from CoderHouse_57810.models.cliente import ClientePersona, ClienteCorporativo
from CoderHouse_57810.models.compra import Compra
from CoderHouse_57810.models.producto import Producto

class Sistema:
    """
    Clase que representa el sistema principal de gestión.

    Atributos:
        clientes_personas (list): Lista de clientes personas.
        clientes_corporativos (list): Lista de clientes corporativos.
        administradores (list): Lista de administradores.
        productos (list): Lista de productos.
        carritos (dict): Diccionario que relaciona clientes con sus carritos de compras.
        compras (list): Lista de compras realizadas.
        product_id_counter (int): Contador para asignar IDs únicos a los productos.
    """

    def __init__(self):
        """
        Inicializa una instancia de Sistema.
        """
        self.clientes_personas = []
        self.clientes_corporativos = []
        self.administradores = []
        self.productos = []
        self.carritos = {}
        self.compras = []
        self.product_id_counter = 1  # Initialize product ID counter

    def agregar_cliente_persona(self, cliente):
        """
        Agrega un cliente persona al sistema.

        Args:
            cliente (ClientePersona): El cliente persona a agregar.
        """
        if isinstance(cliente, ClientePersona):
            self.clientes_personas.append(cliente)
            self.carritos[cliente.email] = []
        else:
            raise TypeError("El cliente debe ser una instancia de ClientePersona")

    def agregar_cliente_corporativo(self, cliente):
        """
        Agrega un cliente corporativo al sistema.

        Args:
            cliente (ClienteCorporativo): El cliente corporativo a agregar.
        """
        if isinstance(cliente, ClienteCorporativo):
            self.clientes_corporativos.append(cliente)
            self.carritos[cliente.email] = []
        else:
            raise TypeError("El cliente debe ser una instancia de ClienteCorporativo")

    def agregar_administrador(self, nuevo_administrador):
        """
        Agrega un administrador al sistema.

        Args:
            nuevo_administrador (Administrador): El administrador a agregar.
        """
        if isinstance(nuevo_administrador, Administrador):
            self.administradores.append(nuevo_administrador)
        else:
            raise TypeError("El administrador debe ser una instancia de Administrador")

    def agregar_producto(self, producto):
        """
        Agrega un producto al sistema.

        Args:
            producto (Producto): El producto a agregar.
        """
        if isinstance(producto, Producto):
            producto.id_producto = self.product_id_counter  # Assign the next available ID
            self.product_id_counter += 1  # Increment the ID counter
            self.productos.append(producto)
        else:
            raise TypeError("El producto debe ser una instancia de Producto")

    def mostrar_clientes(self):
        """
        Muestra la lista de clientes del sistema.
        """
        print("Clientes Personas:")
        if self.clientes_personas:
            table = [[cliente.nombre, cliente.email, cliente.direccion, cliente.telefono, cliente.dni] for cliente in self.clientes_personas]
            print(tabulate(table, headers=["Nombre", "Email", "Dirección", "Teléfono", "DNI"], tablefmt="pretty"))
        else:
            print("No hay clientes personas registrados.")

        print("\nClientes Corporativos:")
        if self.clientes_corporativos:
            table = [[cliente.nombre, cliente.email, cliente.direccion, cliente.telefono, cliente.cuit] for cliente in self.clientes_corporativos]
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

    def mostrar_productos(self):
        """
        Muestra la lista de productos del sistema.
        """
        print("Productos:")
        if self.productos:
            table = [[producto.id_producto, producto.nombre, producto.descripcion, producto.categoria, producto.precio] for producto in self.productos]
            print(tabulate(table, headers=["ID", "Nombre", "Descripción", "Categoría", "Precio"], tablefmt="pretty"))
        else:
            print("No hay productos registrados.")

    def eliminar_cliente_persona(self, email):
        """
        Elimina un cliente persona del sistema.

        Args:
            email (str): El correo electrónico del cliente persona a eliminar.
        """
        self.clientes_personas = [c for c in self.clientes_personas if c.email != email]
        self.carritos.pop(email, None)

    def eliminar_cliente_corporativo(self, email):
        """
        Elimina un cliente corporativo del sistema.

        Args:
            email (str): El correo electrónico del cliente corporativo a eliminar.
        """
        self.clientes_corporativos = [c for c in self.clientes_corporativos if c.email != email]
        self.carritos.pop(email, None)

    def eliminar_administrador(self, email):
        """
        Elimina un administrador del sistema.

        Args:
            email (str): El correo electrónico del administrador a eliminar.
        """
        self.administradores = [a for a in self.administradores if a.email != email]

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del sistema.

        Args:
            id_producto (int): El ID del producto a eliminar.
        """
        self.productos = [p for p in self.productos if p.id_producto != id_producto]

    def agregar_producto_al_carrito(self, email, producto, cantidad):
        """
        Agrega un producto al carrito de compras de un cliente.

        Args:
            email (str): El correo electrónico del cliente.
            producto (Producto): El producto a agregar.
            cantidad (int): La cantidad del producto a agregar.
        """
        if email in self.carritos:
            self.carritos[email].append({"producto": producto, "cantidad": cantidad})
        else:
            raise ValueError("El cliente no existe")

    def mostrar_carrito(self, email):
        """
        Muestra el carrito de compras de un cliente.

        Args:
            email (str): El correo electrónico del cliente.

        Returns:
            list: La lista de productos en el carrito del cliente.
        """
        if email in self.carritos:
            return self.carritos[email]
        else:
            raise ValueError("El cliente no existe")

    def concretar_compra(self, email):
        """
        Concreta una compra para un cliente.

        Args:
            email (str): El correo electrónico del cliente.

        Returns:
            Compra: La compra realizada.
        """
        if email in self.carritos and self.carritos[email]:
            compra = Compra(cliente=self.buscar_cliente(email), productos=self.carritos[email])
            self.compras.append(compra)
            self.carritos[email] = []
            self.mostrar_recibo(compra)
            return compra
        else:
            raise ValueError("El carrito está vacío o el cliente no existe")

    def buscar_cliente(self, email):
        """
        Busca un cliente por su correo electrónico.

        Args:
            email (str): El correo electrónico del cliente.

        Returns:
            ClientePersona o ClienteCorporativo: El cliente encontrado, None si no se encuentra.
        """
        for cliente in self.clientes_personas + self.clientes_corporativos:
            if cliente.email == email:
                return cliente
        return None

    def obtener_historial_compras_cliente(self, email):
        """
        Obtiene el historial de compras de un cliente.

        Args:
            email (str): El correo electrónico del cliente.

        Returns:
            list: La lista de compras del cliente.
        """
        return [compra for compra in self.compras if compra.cliente.email == email]

    def obtener_historial_compras_todos(self):
        """
        Obtiene el historial de compras de todos los clientes.

        Returns:
            list: La lista de todas las compras realizadas.
        """
        return self.compras

    def guardar_datos(self):
        """
        Guarda los datos del sistema en archivos JSON.
        """
        with open("personas.json", "w", encoding='utf-8') as f:
            json.dump([cliente.to_dict() for cliente in self.clientes_personas + self.clientes_corporativos + self.administradores], f, indent=4, ensure_ascii=False)
        with open("productos.json", "w", encoding='utf-8') as f:
            json.dump([producto.to_dict() for producto in self.productos], f, indent=4, ensure_ascii=False)
        with open("compras.json", "w", encoding='utf-8') as f:
            json.dump([compra.to_dict() for compra in self.compras], f, indent=4, ensure_ascii=False)

    def cargar_datos(self):
        """
        Carga los datos del sistema desde archivos JSON.
        """
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

            with open("productos.json", "r", encoding='utf-8') as f:
                productos_data = json.load(f)
                self.productos = [Producto.from_dict(p) for p in productos_data]
                self.product_id_counter = max([p["id_producto"] for p in productos_data], default=0) + 1  # Update the counter

            with open("compras.json", "r", encoding='utf-8') as f:
                compras_data = json.load(f)
                self.compras = [Compra.from_dict(c) for c in compras_data]
        except FileNotFoundError:
            pass  # No data to load initially

    def mostrar_recibo(self, compra):
        """
        Muestra el recibo de compra.

        Args:
            compra (Compra): La compra realizada.
        """
        print(f"Felicidades por la compra, {compra.cliente.nombre}")
        print(f"Fecha: {compra.fecha.strftime('%Y-%m-%d %H:%M:%S')}\n")
        table = []
        total = 0
        for item in compra.productos:
            producto = item["producto"]
            cantidad = item["cantidad"]
            subtotal = producto.precio * cantidad
            total += subtotal
            table.append([producto.nombre, producto.precio, cantidad, subtotal])
        print(tabulate(table, headers=["Artículo", "Precio Unitario", "Cantidad", "Precio Total"], tablefmt="pretty"))
        print(f"\nTotal de la compra: {total}")
        print(f"Ticket de compra: {compra.ticket}")
