from .persona import Persona


class Cliente(Persona):
    def __init__(self, nombre, email, password, direccion, telefono):
        super().__init__(nombre, email, password)
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f'{super().__str__()}, Dirección: {self.direccion}, Teléfono: {self.telefono}'


class ClientePersona(Cliente):
    def __init__(self, nombre, email, password, direccion, telefono, dni):
        super().__init__(nombre, email, password, direccion, telefono)
        self.dni = dni

    def __str__(self):
        return f'{super().__str__()}, DNI: {self.dni}'


class ClienteCorporativo(Cliente):
    def __init__(self, nombre, email, password, direccion, telefono, cuit):
        super().__init__(nombre, email, password, direccion, telefono)
        self.cuit = cuit

    def __str__(self):
        return f'{super().__str__()}, CUIT: {self.cuit}'
