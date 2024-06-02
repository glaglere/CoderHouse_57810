from CoderHouse_57810.models.persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, email, password, direccion, telefono):
        super().__init__(nombre, email, password)
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f'{super().__str__()}, Dirección: {self.direccion}, Teléfono: {self.telefono}'

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "direccion": self.direccion,
            "telefono": self.telefono
        })
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["nombre"], data["email"], data["password"], data["direccion"], data["telefono"])

class ClientePersona(Cliente):
    def __init__(self, nombre, email, password, direccion, telefono, dni):
        super().__init__(nombre, email, password, direccion, telefono)
        self.dni = dni

    def __str__(self):
        return f'{super().__str__()}, DNI: {self.dni}'

    def to_dict(self):
        data = super().to_dict()
        data.update({"dni": self.dni})
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["nombre"], data["email"], data["password"], data["direccion"], data["telefono"], data["dni"])

class ClienteCorporativo(Cliente):
    def __init__(self, nombre, email, password, direccion, telefono, cuit):
        super().__init__(nombre, email, password, direccion, telefono)
        self.cuit = cuit

    def __str__(self):
        return f'{super().__str__()}, CUIT: {self.cuit}'

    def to_dict(self):
        data = super().to_dict()
        data.update({"cuit": self.cuit})
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["nombre"], data["email"], data["password"], data["direccion"], data["telefono"], data["cuit"])
