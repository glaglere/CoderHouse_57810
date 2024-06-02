from .persona import Persona

class Administrador(Persona):
    def __init__(self, nombre, email, password, codigo_funcionario):
        super().__init__(nombre, email, password)
        self.codigo_funcionario = codigo_funcionario

    def __str__(self):
        return f'{super().__str__()}, Funcionario n°: {self.codigo_funcionario}'
