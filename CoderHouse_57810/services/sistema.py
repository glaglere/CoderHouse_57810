import json
from tabulate import tabulate

from CoderHouse_57810.models.compra import Compra
from CoderHouse_57810.services.cliente_service import ClienteService
from CoderHouse_57810.services.producto_service import ProductoService
from CoderHouse_57810.services.seguridad import Seguridad


class Sistema:
    def __init__(self):
        self.cliente_service = ClienteService()
        self.producto_service = ProductoService()
        self.compras = []

    def agregar_cliente_persona(self, cliente):
        Seguridad.validar_cliente_persona(cliente)
        self.cliente_service.agregar_cliente_persona(cliente)

    def agregar_cliente_corporativo(self, cliente):
        Seguridad.validar_cliente_corporativo(cliente)
        self.cliente_service.agregar_cliente_corporativo(cliente)

    def agregar_administrador(self, nuevo_administrador):
        Seguridad.validar_administrador(nuevo_administrador)
        self.cliente_service.agregar_administrador(nuevo_administrador)

    def agregar_producto(self, producto):
        Seguridad.validar_producto(producto)
        self.producto_service.agregar_producto(producto)

    def mostrar_clientes(self):
        self.cliente_service.mostrar_clientes()

    def mostrar_administradores(self):
        self.cliente_service.mostrar_administradores()

    def mostrar_productos(self):
        productos = self.producto_service.mostrar_productos()
        if productos:
            table = [[producto.id_producto, producto.nombre, producto.descripcion, producto.categoria, producto.precio] for producto in productos]
            print(tabulate(table, headers=["ID", "Nombre", "Descripción", "Categoría", "Precio"], tablefmt="pretty"))
        else:
            print("No hay productos registrados.")

    def eliminar_cliente_persona(self, email):
        self.cliente_service.eliminar_cliente_persona(email)

    def eliminar_cliente_corporativo(self, email):
        self.cliente_service.eliminar_cliente_corporativo(email)

    def eliminar_administrador(self, email):
        self.cliente_service.eliminar_administrador(email)

    def eliminar_producto(self, id_producto):
        self.producto_service.eliminar_producto(id_producto)

    def agregar_producto_al_carrito(self, email, producto, cantidad):
        cliente = self.cliente_service.buscar_cliente(email)
        if cliente:
            self.cliente_service.agregar_producto_al_carrito(cliente, producto, cantidad)
        else:
            raise ValueError("El cliente no existe")

    def quitar_producto_del_carrito(self, email, id_producto):
        cliente = self.cliente_service.buscar_cliente(email)
        if cliente:
            self.cliente_service.quitar_producto_del_carrito(cliente, id_producto)
        else:
            raise ValueError("El cliente no existe")

    def mostrar_carrito(self, email):
        cliente = self.cliente_service.buscar_cliente(email)
        if cliente:
            carrito = self.cliente_service.mostrar_carrito(cliente)
            return carrito
        else:
            raise ValueError("El cliente no existe")

    def concretar_compra(self, email):
        cliente = self.cliente_service.buscar_cliente(email)
        if cliente:
            carrito = self.cliente_service.mostrar_carrito(cliente)
            if carrito:
                compra = Compra(cliente=cliente, productos=carrito)
                self.compras.append(compra)
                self.cliente_service.vaciar_carrito(cliente)
                self.mostrar_recibo(compra)
                return compra
            else:
                raise ValueError("El carrito está vacío.")
        else:
            raise ValueError("El cliente no existe")

    def buscar_cliente(self, email):
        return self.cliente_service.buscar_cliente(email)

    def obtener_historial_compras_cliente(self, email):
        return [compra for compra in self.compras if compra.cliente.email == email]

    def obtener_historial_compras_todos(self):
        return self.compras

    def guardar_datos(self):
        self.cliente_service.guardar_datos()
        self.producto_service.guardar_datos()
        with open("compras.json", "w", encoding='utf-8') as f:
            json.dump([compra.to_dict() for compra in self.compras], f, indent=4, ensure_ascii=False)

    def cargar_datos(self):
        self.cliente_service.cargar_datos()
        self.producto_service.cargar_datos()
        try:
            with open("compras.json", "r", encoding='utf-8') as f:
                compras_data = json.load(f)
                self.compras = [Compra.from_dict(c) for c in compras_data]
        except FileNotFoundError:
            pass  # No hay datos que cargar inicialmente

    def mostrar_recibo(self, compra):
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
