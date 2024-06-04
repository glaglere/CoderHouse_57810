from CoderHouse_57810.models.persona import Persona

class Cliente(Persona):
    """
    Clase que representa a un cliente, hereda de Persona.

    Atributos:
        direccion (str): La dirección del cliente.
        telefono (str): El teléfono del cliente.
    """

    def __init__(self, nombre, email, password, direccion, telefono):
        """
        Inicializa una instancia de Cliente.

        Args:
            nombre (str): El nombre del cliente.
            email (str): El correo electrónico del cliente.
            password (str): La contraseña del cliente.
            direccion (str): La dirección del cliente.
            telefono (str): El teléfono del cliente.
        """
        super().__init__(nombre, email, password)
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        """
        Devuelve una representación en cadena del cliente.

        Returns:
            str: Una cadena que representa al cliente.
        """
        return f'{super().__str__()}, Dirección: {self.direccion}, Teléfono: {self.telefono}'

    def to_dict(self):
        """
        Convierte la instancia de Cliente a un diccionario.

        Returns:
            dict: Un diccionario que representa al cliente.
        """
        data = super().to_dict()
        data.update({
            "direccion": self.direccion,
            "telefono": self.telefono
        })
        return data

    @classmethod
    def from_dict(cls, data):
        """
        Crea una instancia de Cliente a partir de un diccionario.

        Args:
            data (dict): Un diccionario con los datos del cliente.

        Returns:
            Cliente: Una instancia de la clase Cliente.
        """
        return cls(data["nombre"], data["email"], data["password"], data["direccion"], data["telefono"])

class ClientePersona(Cliente):
    """
    Clase que representa a un cliente persona, hereda de Cliente.

    Atributos:
        dni (str): El DNI del cliente persona.
    """

    def __init__(self, nombre, email, password, direccion, telefono, dni):
        """
        Inicializa una instancia de ClientePersona.

        Args:
            nombre (str): El nombre del cliente persona.
            email (str): El correo electrónico del cliente persona.
            password (str): La contraseña del cliente persona.
            direccion (str): La dirección del cliente persona.
            telefono (str): El teléfono del cliente persona.
            dni (str): El DNI del cliente persona.
        """
        super().__init__(nombre, email, password, direccion, telefono)
        self.dni = dni

    def __str__(self):
        """
        Devuelve una representación en cadena del cliente persona.

        Returns:
            str: Una cadena que representa al cliente persona.
        """
        return f'{super().__str__()}, DNI: {self.dni}'

    def to_dict(self):
        """
        Convierte la instancia de ClientePersona a un diccionario.

        Returns:
            dict: Un diccionario que representa al cliente persona.
        """
        data = super().to_dict()
        data.update({"dni": self.dni})
        return data

    @classmethod
    def from_dict(cls, data):
        """
        Crea una instancia de ClientePersona a partir de un diccionario.

        Args:
            data (dict): Un diccionario con los datos del cliente persona.

        Returns:
            ClientePersona: Una instancia de la clase ClientePersona.
        """
        return cls(data["nombre"], data["email"], data["password"], data["direccion"], data["telefono"], data["dni"])

class ClienteCorporativo(Cliente):
    """
    Clase que representa a un cliente corporativo, hereda de Cliente.

    Atributos:
        cuit (str): El CUIT del cliente corporativo.
    """

    def __init__(self, nombre, email, password, direccion, telefono, cuit):
        """
        Inicializa una instancia de ClienteCorporativo.

        Args:
            nombre (str): El nombre del cliente corporativo.
            email (str): El correo electrónico del cliente corporativo.
            password (str): La contraseña del cliente corporativo.
            direccion (str): La dirección del cliente corporativo.
            telefono (str): El teléfono del cliente corporativo.
            cuit (str): El CUIT del cliente corporativo.
        """
        super().__init__(nombre, email, password, direccion, telefono)
        self.cuit = cuit

    def __str__(self):
        """
        Devuelve una representación en cadena del cliente corporativo.

        Returns:
            str: Una cadena que representa al cliente corporativo.
        """
        return f'{super().__str__()}, CUIT: {self.cuit}'

    def to_dict(self):
        """
        Convierte la instancia de ClienteCorporativo a un diccionario.

        Returns:
            dict: Un diccionario que representa al cliente corporativo.
        """
        data = super().to_dict()
        data.update({"cuit": self.cuit})
        return data

    @classmethod
    def from_dict(cls, data):
        """
        Crea una instancia de ClienteCorporativo a partir de un diccionario.

        Args:
            data (dict): Un diccionario con los datos del cliente corporativo.

        Returns:
            ClienteCorporativo: Una instancia de la clase ClienteCorporativo.
        """
        return cls(data["nombre"], data["email"], data["password"], data["direccion"], data["telefono"], data["cuit"])
