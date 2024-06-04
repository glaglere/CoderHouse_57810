import json
from tabulate import tabulate
from CoderHouse_57810.models.administrador import Administrador
from CoderHouse_57810.models.cliente import ClientePersona, ClienteCorporativo
from CoderHouse_57810.models.compra import Compra
from CoderHouse_57810.models.producto import Producto
from CoderHouse_57810.services.seguridad import Seguridad

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
        self.product_id_counter = 1  # Inicializa el contador de IDs de productos

    def obtener_categorias_productos(self):
        """
        Obtiene una lista de categorías de productos disponibles.

        Returns:
            list: Lista de categorías de productos.
        """
        categorias = set(producto.categoria for producto in self.productos)
        return list(categorias)

    def mostrar_productos_por_categoria(self, categoria):
        """
        Muestra los productos de una categoría específica.

        Args:
            categoria (str): La categoría de los productos a mostrar.
        """
        productos_filtrados = [producto for producto in self.productos if producto.categoria == categoria]
        if productos_filtrados:
            print(f"Productos en la categoría '{categoria}':")
            table = [[producto.id_producto, producto.nombre, producto.descripcion, producto.categoria, producto.precio]
                     for producto in productos_filtrados]
            print(tabulate(table, headers=["ID", "Nombre", "Descripción", "Categoría", "Precio"], tablefmt="pretty"))
        else:
            print(f"No hay productos disponibles en la categoría '{categoria}'.")

    def email_exists(self, email):
        """
        Verifica si un email ya existe en el sistema.

        Args:
            email (str): El email a verificar.

        Returns:
            bool: True si el email existe, False en caso contrario.
        """
        return any(email == c.email for c in self.clientes_personas + self.clientes_corporativos + self.administradores)

    def dni_exists(self, dni):
        """
        Verifica si un DNI ya existe en el sistema.

        Args:
            dni (str): El DNI a verificar.

        Returns:
            bool: True si el DNI existe, False en caso contrario.
        """
        return any(dni == c.dni for c in self.clientes_personas)

    def cuit_exists(self, cuit):
        """
        Verifica si un CUIT ya existe en el sistema.

        Args:
            cuit (str): El CUIT a verificar.

        Returns:
            bool: True si el CUIT existe, False en caso contrario.
        """
        return any(cuit == c.cuit for c in self.clientes_corporativos)

    def agregar_cliente_persona(self, cliente):
        """
        Agrega un ClientePersona al sistema.

        Args:
            cliente (ClientePersona): El cliente a agregar.

        Returns:
            bool: True si el cliente se agrega exitosamente, False en caso contrario.

        Raises:
            ValueError: Si alguna de las validaciones falla o si el email/DNI ya existe.
            TypeError: Si el argumento no es una instancia de ClientePersona.
        """
        result = False
        try:
            if not isinstance(cliente, ClientePersona):
                raise TypeError("El cliente debe ser una instancia de ClientePersona")

            if self.email_exists(cliente.email):
                raise ValueError("El email ya existe en el sistema.")

            if self.dni_exists(cliente.dni):
                raise ValueError("El DNI ya existe en el sistema.")

            if not Seguridad.validar_nombre_usuario(cliente.nombre):
                raise ValueError("El nombre del cliente persona no es válido.")

            if not Seguridad.validar_email(cliente.email):
                raise ValueError("El email del cliente persona no es válido.")

            if not Seguridad.validar_password(cliente.password):
                raise ValueError("La contraseña del cliente persona no es válida.")

            if not Seguridad.validar_no_vacio(cliente.direccion):
                raise ValueError("La dirección del cliente persona no puede estar vacía.")

            if not Seguridad.validar_telefono(cliente.telefono):
                raise ValueError("El teléfono del cliente persona no es válido.")

            if not Seguridad.validar_dni(cliente.dni):
                raise ValueError("El DNI del cliente persona no es válido.")

            self.clientes_personas.append(cliente)
            self.carritos[cliente.email] = []
            result = True
        except (ValueError, TypeError) as e:
            print(f"Error al agregar cliente persona: {e}")
        return result

    def agregar_cliente_corporativo(self, cliente):
        """
        Agrega un ClienteCorporativo al sistema.

        Args:
            cliente (ClienteCorporativo): El cliente a agregar.

        Returns:
            bool: True si el cliente se agrega exitosamente, False en caso contrario.

        Raises:
            ValueError: Si alguna de las validaciones falla o si el email ya existe.
            TypeError: Si el argumento no es una instancia de ClienteCorporativo.
        """
        result = False
        try:
            if not isinstance(cliente, ClienteCorporativo):
                raise TypeError("El cliente debe ser una instancia de ClienteCorporativo")

            if self.email_exists(cliente.email):
                raise ValueError("El email ya existe en el sistema.")

            if self.cuit_exists(cliente.cuit):
                raise ValueError("El CUIT ya existe en el sistema.")

            if not Seguridad.validar_nombre_usuario(cliente.nombre):
                raise ValueError("El nombre del cliente corporativo no es válido.")

            if not Seguridad.validar_email(cliente.email):
                raise ValueError("El email del cliente corporativo no es válido.")

            if not Seguridad.validar_password(cliente.password):
                raise ValueError("La contraseña del cliente corporativo no es válida.")

            if not Seguridad.validar_no_vacio(cliente.direccion):
                raise ValueError("La dirección del cliente corporativo no puede estar vacía.")

            if not Seguridad.validar_telefono(cliente.telefono):
                raise ValueError("El teléfono del cliente corporativo no es válido.")

            if not Seguridad.validar_no_vacio(cliente.cuit):
                raise ValueError("El CUIT del cliente corporativo no puede estar vacío.")

            self.clientes_corporativos.append(cliente)
            self.carritos[cliente.email] = []

            result = True
        except (ValueError, TypeError) as e:
            print(f"Error al agregar cliente corporativo: {e}")
        return result

    def agregar_administrador(self, nuevo_administrador):
        """
        Agrega un Administrador al sistema.

        Args:
            nuevo_administrador (Administrador): El administrador a agregar.

        Returns:
            bool: True si el administrador se agrega exitosamente, False en caso contrario.

        Raises:
            ValueError: Si alguna de las validaciones falla o si el email ya existe.
            TypeError: Si el argumento no es una instancia de Administrador.
        """
        result = False
        try:
            if not isinstance(nuevo_administrador, Administrador):
                raise TypeError("El administrador debe ser una instancia de Administrador")

            if self.email_exists(nuevo_administrador.email):
                raise ValueError("El email ya existe en el sistema.")

            if not Seguridad.validar_nombre_usuario(nuevo_administrador.nombre):
                raise ValueError("El nombre del administrador no es válido.")

            if not Seguridad.validar_email(nuevo_administrador.email):
                raise ValueError("El email del administrador no es válido.")

            if not Seguridad.validar_password(nuevo_administrador.password):
                raise ValueError("La contraseña del administrador no es válida.")

            if not Seguridad.validar_no_vacio(nuevo_administrador.codigo_funcionario):
                raise ValueError("El código de funcionario del administrador no puede estar vacío.")

            self.administradores.append(nuevo_administrador)
            result = True
        except (ValueError, TypeError) as e:
            print(f"Error al agregar Administrador: {e}")
        return result

    def agregar_producto(self, producto):
        """
        Agrega un producto al sistema.

        Args:
            producto (Producto): El producto a agregar.

        Returns:
            bool: True si el producto se agrega exitosamente, False en caso contrario.

        Raises:
            ValueError: Si alguna de las validaciones del producto falla.
            TypeError: Si el argumento producto no es una instancia de Producto.
        """
        result = False
        try:
            if isinstance(producto, Producto):
                if any(p.nombre == producto.nombre for p in self.productos):
                    raise ValueError("El producto ya existe en el sistema.")
                if not Seguridad.validar_no_vacio(producto.nombre):
                    raise ValueError("El nombre del producto no puede estar vacío.")
                if not Seguridad.validar_no_vacio(producto.descripcion):
                    raise ValueError("La descripción del producto no puede estar vacía.")
                if not Seguridad.validar_no_vacio(producto.categoria):
                    raise ValueError("La categoría del producto no puede estar vacía.")
                if producto.precio <= 0:
                    raise ValueError("El precio del producto debe ser mayor a 0.")
                producto.id_producto = self.product_id_counter  # Asigna el siguiente ID disponible
                self.product_id_counter += 1  # Incrementa el contador de IDs
                self.productos.append(producto)
                result = True
            else:
                raise TypeError("El producto debe ser una instancia de Producto")
        except (ValueError, TypeError) as e:
            print(f"Error al agregar producto: {e}")
        return result

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

    def mostrar_productos(self):
        """
        Muestra la lista de productos del sistema.
        """
        print("Productos:")
        if self.productos:
            table = [[producto.id_producto, producto.nombre, producto.descripcion, producto.categoria, producto.precio]
                     for producto in self.productos]
            print(tabulate(table, headers=["ID", "Nombre", "Descripción", "Categoría", "Precio"], tablefmt="pretty"))
        else:
            print("No hay productos registrados.")

    def eliminar_cliente_persona(self, email):
        """
        Elimina un ClientePersona del sistema.

        Args:
            email (str): El email del cliente a eliminar.

        Returns:
            bool: True si el cliente se elimina exitosamente, False en caso contrario.
        """
        result = False
        try:
            self.clientes_personas = [c for c in self.clientes_personas if c.email != email]
            self.carritos.pop(email, None)
            result = True
        except Exception as e:
            print(f"Error al eliminar cliente persona: {e}")
        return result

    def eliminar_cliente_corporativo(self, email):
        """
        Elimina un ClienteCorporativo del sistema.

        Args:
            email (str): El email del cliente a eliminar.

        Returns:
            bool: True si el cliente se elimina exitosamente, False en caso contrario.
        """
        result = False
        try:
            self.clientes_corporativos = [c for c in self.clientes_corporativos if c.email != email]
            self.carritos.pop(email, None)
            result = True
        except Exception as e:
            print(f"Error al eliminar cliente corporativo: {e}")
        return result

    def eliminar_administrador(self, email):
        """
        Elimina un Administrador del sistema.

        Args:
            email (str): El email del administrador a eliminar.

        Returns:
            bool: True si el administrador se elimina exitosamente, False en caso contrario.
        """
        result = False
        try:
            self.administradores = [a for a in self.administradores if a.email != email]
            result = True
        except Exception as e:
            print(f"Error al eliminar administrador: {e}")
        return result

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del sistema.

        Args:
            id_producto (int): El ID del producto a eliminar.

        Returns:
            bool: True si el producto se elimina exitosamente, False en caso contrario.
        """
        result = False
        try:
            producto_a_eliminar = next((p for p in self.productos if p.id_producto == id_producto), None)
            if producto_a_eliminar:
                self.productos.remove(producto_a_eliminar)
                result = True
        except Exception as e:
            print(f"Error al eliminar producto: {e}")
        return result

    def agregar_producto_al_carrito(self, email, producto, cantidad):
        """
        Agrega un producto al carrito de compras de un cliente.

        Args:
            email (str): El correo electrónico del cliente.
            producto (Producto): El producto a agregar.
            cantidad (int): La cantidad del producto a agregar.

        Returns:
            bool: True si el producto se agrega exitosamente al carrito, False en caso contrario.

        Raises:
            ValueError: Si el cliente no existe.
        """
        result = False
        try:
            if email in self.carritos:
                self.carritos[email].append({"producto": producto, "cantidad": cantidad})
                result = True
            else:
                raise ValueError("El cliente no existe")
        except (ValueError, TypeError) as e:
            print(f"Error al agregar producto al carrito: {e}")
        return result

    def quitar_producto_del_carrito(self, email_cliente, id_producto, cantidad):
        """
        Quita una cantidad específica de un producto del carrito de un cliente.

        Args:
            email_cliente (str): El email del cliente.
            id_producto (int): El ID del producto a quitar.
            cantidad (int): La cantidad a quitar del producto.

        Raises:
            ValueError: Si el producto no se encuentra en el carrito o si la cantidad a quitar es mayor que la cantidad en el carrito.
        """
        carrito = self.carritos.get(email_cliente, [])
        for item in carrito:
            if item["producto"].id_producto == id_producto:
                if item["cantidad"] < cantidad:
                    raise ValueError("Cantidad a quitar es mayor que la cantidad en el carrito.")
                item["cantidad"] -= cantidad
                if item["cantidad"] == 0:
                    carrito.remove(item)
                self.carritos[email_cliente] = carrito
                return
        raise ValueError("Producto no encontrado en el carrito.")

    def mostrar_carrito(self, email):
        """
        Muestra el carrito de compras de un cliente.

        Args:
            email (str): El correo electrónico del cliente.

        Returns:
            list: La lista de productos en el carrito del cliente, o una lista vacía en caso de error.
        """
        try:
            if email in self.carritos:
                return self.carritos[email]
            else:
                raise ValueError("El cliente no existe")
        except (ValueError, TypeError) as e:
            print(f"Error al mostrar el carrito: {e}")
            return []

    def concretar_compra(self, email):
        """
        Concreta una compra para un cliente.

        Args:
            email (str): El correo electrónico del cliente.

        Returns:
            Compra: La compra realizada, o None en caso de error.

        Raises:
            ValueError: Si el carrito está vacío o el cliente no existe.
        """
        try:
            if email in self.carritos and self.carritos[email]:
                compra = Compra(cliente=self.buscar_cliente(email), productos=self.carritos[email])
                self.compras.append(compra)
                self.carritos[email] = []
                self.mostrar_recibo(compra)
                return compra
            else:
                raise ValueError("El carrito está vacío o el cliente no existe")
        except (ValueError, TypeError) as e:
            print(f"Error al concretar compra: {e}")
            return None

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
            json.dump([cliente.to_dict() for cliente in
                       self.clientes_personas + self.clientes_corporativos + self.administradores], f, indent=4,
                      ensure_ascii=False)
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
                self.product_id_counter = max([p["id_producto"] for p in productos_data],
                                              default=0) + 1  # Actualiza el contador

            with open("compras.json", "r", encoding='utf-8') as f:
                compras_data = json.load(f)
                self.compras = [Compra.from_dict(c) for c in compras_data]
        except FileNotFoundError:
            pass  # No hay datos que cargar inicialmente

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
