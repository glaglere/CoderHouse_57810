from CoderHouse_57810.models.cliente import ClientePersona, ClienteCorporativo
from CoderHouse_57810.models.producto import Producto


class Compra:
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos

    def __str__(self):
        productos_str = ', '.join([str(producto) for producto in self.productos])
        return f'Cliente: {self.cliente.nombre}, Productos: {productos_str}'

    def to_dict(self):
        return {
            "cliente": self.cliente.to_dict(),
            "productos": [producto.to_dict() for producto in self.productos]
        }

    @classmethod
    def from_dict(cls, data):
        cliente = ClientePersona.from_dict(data["cliente"]) if "dni" in data["cliente"] else ClienteCorporativo.from_dict(data["cliente"])
        productos = [Producto.from_dict(prod) for prod in data["productos"]]
        return cls(cliente, productos)