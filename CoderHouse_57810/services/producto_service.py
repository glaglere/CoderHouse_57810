import json

from CoderHouse_57810.models.producto import Producto


class ProductoService:
    def __init__(self):
        self.productos = []
        self.product_id_counter = 1

    def agregar_producto(self, producto):
        """
        Agrega un producto al sistema.

        Args:
            producto (Producto): El producto a agregar.
        """
        producto.id_producto = self.product_id_counter
        self.product_id_counter += 1
        self.productos.append(producto)

    def mostrar_productos(self):
        """
        Muestra la lista de productos del sistema.

        Returns:
            list: Lista de productos.
        """
        return self.productos

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del sistema.

        Args:
            id_producto (int): El ID del producto a eliminar.

        Raises:
            ValueError: Si el producto no se encuentra.
        """
        producto = next((p for p in self.productos if p.id_producto == id_producto), None)
        if producto:
            self.productos.remove(producto)
        else:
            raise ValueError("Producto no encontrado")

    def buscar_producto(self, id_producto):
        """
        Busca un producto por su ID.

        Args:
            id_producto (int): El ID del producto a buscar.

        Returns:
            Producto: El producto encontrado, None si no se encuentra.
        """
        return next((p for p in self.productos if p.id_producto == id_producto), None)

    def actualizar_producto(self, id_producto, nombre=None, descripcion=None, categoria=None, precio=None):
        """
        Actualiza los detalles de un producto.

        Args:
            id_producto (int): El ID del producto a actualizar.
            nombre (str, opcional): El nuevo nombre del producto.
            descripcion (str, opcional): La nueva descripción del producto.
            categoria (str, opcional): La nueva categoría del producto.
            precio (float, opcional): El nuevo precio del producto.

        Raises:
            ValueError: Si el producto no se encuentra.
        """
        producto = self.buscar_producto(id_producto)
        if producto:
            if nombre is not None:
                producto.nombre = nombre
            if descripcion is not None:
                producto.descripcion = descripcion
            if categoria is not None:
                producto.categoria = categoria
            if precio is not None:
                producto.precio = precio
        else:
            raise ValueError("Producto no encontrado")

    def guardar_datos(self):
        """
        Guarda los datos de productos en un archivo JSON.
        """
        with open("productos.json", "w", encoding='utf-8') as f:
            json.dump([producto.to_dict() for producto in self.productos], f, indent=4, ensure_ascii=False)

    def cargar_datos(self):
        """
        Carga los datos de productos desde un archivo JSON.
        """
        try:
            with open("productos.json", "r", encoding='utf-8') as f:
                productos_data = json.load(f)
                self.productos = [Producto.from_dict(p) for p in productos_data]
                self.product_id_counter = max([p["id_producto"] for p in productos_data], default=0) + 1  # Actualiza el contador
        except FileNotFoundError:
            pass  # No hay datos que cargar inicialmente
