class Producto:
    def __init__(self, id_producto, nombre, descripcion, categoria, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria
        self.precio = precio

    def __str__(self):
        return f'ID: {self.id_producto}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Categoría: {self.categoria}, Precio: {self.precio}'
