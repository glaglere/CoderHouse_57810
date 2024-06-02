from CoderHouse_57810.services.helpers import encriptar_password


class Persona:
    """
    Clase base que representa a una persona con atributos básicos.

    Atributos:
        nombre (str): El nombre de la persona.
        email (str): El correo electrónico de la persona.
        password (str): La contraseña de la persona.
    """

    def __init__(self, nombre, email, password):
        """
        Inicializa una instancia de Persona.

        Args:
            nombre (str): El nombre de la persona.
            email (str): El correo electrónico de la persona.
            password (str): La contraseña de la persona.
        """
        self.nombre = nombre
        self.email = email
        self.password = encriptar_password(password)

    def __str__(self):
        """
        Devuelve una representación en cadena de la persona.

        Returns:
            str: Una cadena que representa a la persona.
        """
        return f'{self.nombre}, Email: {self.email}'

    def to_dict(self):
        """
        Convierte la instancia de Persona a un diccionario.

        Returns:
            dict: Un diccionario que representa a la persona.
        """
        return {
            "tipo": self.__class__.__name__,
            "nombre": self.nombre,
            "email": self.email,
            "password": self.password
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crea una instancia de Persona a partir de un diccionario.

        Args:
            data (dict): Un diccionario con los datos de la persona.

        Returns:
            Persona: Una instancia de la clase Persona.
        """
        return cls(data["nombre"], data["email"], data["password"])