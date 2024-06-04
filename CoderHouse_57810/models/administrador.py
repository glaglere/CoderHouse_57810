from CoderHouse_57810.models.persona import Persona

class Administrador(Persona):
    """
    Clase que representa a un administrador, hereda de Persona.

    Atributos:
        codigo_funcionario (str): El código del funcionario.
    """

    def __init__(self, nombre, email, password, codigo_funcionario):
        """
        Inicializa una instancia de Administrador.

        Args:
            nombre (str): El nombre del administrador.
            email (str): El correo electrónico del administrador.
            password (str): La contraseña del administrador.
            codigo_funcionario (str): El código del funcionario.
        """
        super().__init__(nombre, email, password)
        self.codigo_funcionario = codigo_funcionario

    def __str__(self):
        """
        Devuelve una representación en cadena del administrador.

        Returns:
            str: Una cadena que representa al administrador.
        """
        return f'{super().__str__()}, Funcionario n°: {self.codigo_funcionario}'

    def to_dict(self):
        """
        Convierte la instancia de Administrador a un diccionario.

        Returns:
            dict: Un diccionario que representa al administrador.
        """
        data = super().to_dict()
        data.update({"codigo_funcionario": self.codigo_funcionario})
        return data

    @classmethod
    def from_dict(cls, data):
        """
        Crea una instancia de Administrador a partir de un diccionario.

        Args:
            data (dict): Un diccionario con los datos del administrador.

        Returns:
            Administrador: Una instancia de la clase Administrador.
        """
        return cls(data["nombre"], data["email"], data["password"], data["codigo_funcionario"])
