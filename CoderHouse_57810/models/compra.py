# compra.py
from datetime import datetime
import random
import string

from CoderHouse_57810.models.cliente import ClientePersona, ClienteCorporativo
from CoderHouse_57810.models.producto import Producto


class Compra:
    """
    Clase que representa una compra.

    Atributos:
        cliente (ClientePersona o ClienteCorporativo): El cliente que realiza la compra.
        productos (list): Una lista de productos comprados.
        fecha (datetime): La fecha en que se realizó la compra.
        ticket (str): El número de ticket de la compra.
    """

    def __init__(self, cliente, productos):
        """
        Inicializa una instancia de Compra.

        Args:
            cliente (ClientePersona o ClienteCorporativo): El cliente que realiza la compra.
            productos (list): Una lista de productos comprados (con cantidades).
        """
        self.cliente = cliente
        self.productos = productos
        self.fecha = datetime.now()
        self.ticket = self.generar_numero_ticket()

    def __str__(self):
        """
        Devuelve una representación en cadena de la compra.

        Returns:
            str: Una cadena que representa la compra.
        """
        productos_str = ', '.join([f"{producto['producto'].nombre} x{producto['cantidad']}" for producto in self.productos])
        return f'Cliente: {self.cliente.nombre}, Productos: {productos_str}, Fecha: {self.fecha}, Ticket: {self.ticket}'

    def to_dict(self):
        """
        Convierte la instancia de Compra a un diccionario.

        Returns:
            dict: Un diccionario que representa la compra.
        """
        return {
            "cliente": self.cliente.to_dict(),
            "productos": [{"producto": producto['producto'].to_dict(), "cantidad": producto['cantidad']} for producto in self.productos],
            "fecha": self.fecha.isoformat(),
            "ticket": self.ticket
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
        productos = [{"producto": Producto.from_dict(prod["producto"]), "cantidad": prod["cantidad"]} for prod in data["productos"]]
        compra = cls(cliente, productos)
        compra.fecha = datetime.fromisoformat(data["fecha"])
        compra.ticket = data["ticket"]
        return compra

    def generar_numero_ticket(self):
        """
        Genera un número de ticket aleatorio.

        Returns:
            str: Un número de ticket aleatorio.
        """
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choice(caracteres) for _ in range(10))
