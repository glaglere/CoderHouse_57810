class Producto:
    """
    Clase que representa a un producto.

    Atributos:
        id_producto (int): El ID del producto.
        nombre (str): El nombre del producto.
        descripcion (str): La descripción del producto.
        categoria (str): La categoría del producto.
        precio (float): El precio del producto.
    """

    def __init__(self, nombre, descripcion, categoria, precio, id_producto=None):
        """
        Inicializa una instancia de Producto.

        Args:
            nombre (str): El nombre del producto.
            descripcion (str): La descripción del producto.
            categoria (str): La categoría del producto.
            precio (float): El precio del producto.
            id_producto (int, opcional): El ID del producto. Por defecto es None.
        """
        self.id_producto = id_producto
        self.nombre = nombre.lower()  # Convertir el nombre a minúsculas
        self.descripcion = descripcion
        self.categoria = categoria
        self.precio = precio

    def __str__(self):
        """
        Devuelve una representación en cadena del producto.

        Returns:
            str: Una cadena que representa al producto.
        """
        return f'ID: {self.id_producto}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Categoría: {self.categoria}, Precio: {self.precio}'

    def to_dict(self):
        """
        Convierte la instancia de Producto a un diccionario.

        Returns:
            dict: Un diccionario que representa al producto.
        """
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "categoria": self.categoria,
            "precio": self.precio
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crea una instancia de Producto a partir de un diccionario.

        Args:
            data (dict): Un diccionario con los datos del producto.

        Returns:
            Producto: Una instancia de la clase Producto.
        """
        return cls(data["nombre"], data["descripcion"], data["categoria"], data["precio"], int(data["id_producto"]))
