class Persona:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password

    def __str__(self):
        return f'{self.nombre}, Email: {self.email}'

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "email": self.email,
            "password": self.password
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["nombre"], data["email"], data["password"])
