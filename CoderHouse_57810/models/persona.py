class Persona:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password

    def __str__(self):
        return f'{self.nombre}, Email: {self.email}'
