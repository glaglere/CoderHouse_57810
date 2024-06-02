class Compra:
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos

    def __str__(self):
        productos_str = ', '.join([str(producto) for producto in self.productos])
        return f'Cliente: {self.cliente.nombre}, Productos: {productos_str}'
