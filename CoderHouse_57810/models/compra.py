# compra.py
from CoderHouse_57810.models.cliente import ClientePersona, ClienteCorporativo
from CoderHouse_57810.models.producto import Producto


class Compra:
    """
    Clase que representa una compra.

    Atributos:
        cliente (ClientePersona o ClienteCorporativo): El cliente que realiza la compra.
        productos (list): Una lista de productos comprados.
    """

    def __init__(self, cliente, productos):
        """
        Inicializa una instancia de Compra.

        Args:
            cliente (ClientePersona o ClienteCorporativo): El cliente que realiza la compra.
            productos (list): Una lista de productos comprados.
        """
        self.cliente = cliente
        self.productos = productos

    def __str__(self):
        """
        Devuelve una representación en cadena de la compra.

        Returns:
            str: Una cadena que representa la compra.
        """
        productos_str = ', '.join([str(producto) for producto in self.productos])
        return f'Cliente: {self.cliente.nombre}, Productos: {productos_str}'

    def to_dict(self):
        """
        Convierte la instancia de Compra a un diccionario.

        Returns:
            dict: Un diccionario que representa la compra.
        """
        return {
            "cliente": self.cliente.to_dict(),
            "productos": [producto.to_dict() for producto in self.productos]
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crea una instancia de Compra a partir de un diccionario.

        Args:
            data (dict): Un diccionario con los datos de la compra.

        Returns:
            Compra: Una instancia de la clase Compra.
        """
        cliente = ClientePersona.from_dict(data["cliente"]) if data["cliente"]["tipo"] == "ClientePersona" else ClienteCorporativo.from_dict(data["cliente"])
        productos = [Producto.from_dict(prod) for prod in data["productos"]]
        return cls(cliente, productos)
