from CoderHouse_57810.models.persona import Persona

class Administrador(Persona):
    def __init__(self, nombre, email, password, codigo_funcionario):
        super().__init__(nombre, email, password)
        self.codigo_funcionario = codigo_funcionario

    def __str__(self):
        return f'{super().__str__()}, Funcionario n°: {self.codigo_funcionario}'

    def to_dict(self):
        data = super().to_dict()
        data.update({"codigo_funcionario": self.codigo_funcionario})
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["nombre"], data["email"], data["password"], data["codigo_funcionario"])
