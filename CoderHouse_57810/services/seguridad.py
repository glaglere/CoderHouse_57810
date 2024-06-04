import re

class Seguridad:
    """
    Clase que proporciona métodos de validación para los datos del sistema.
    """

    @staticmethod
    def validar_email(email):
        """
        Valida que el email tenga un formato correcto.

        Args:
            email (str): El email a validar.

        Returns:
            bool: True si el email es válido, False en caso contrario.
        """
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, email) is not None

    @staticmethod
    def validar_password(password):
        """
        Valida que la contraseña tenga al menos 8 caracteres y contenga letras y números.

        Args:
            password (str): La contraseña a validar.

        Returns:
            bool: True si la contraseña es válida, False en caso contrario.
        """
        if len(password) < 8:
            return False
        if not re.search(r'[A-Za-z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        return True

    @staticmethod
    def validar_nombre_usuario(nombre):
        """
        Valida que el nombre de usuario no tenga números, contenga solo letras y espacios en blanco,
        y comience con una letra. El nombre debe tener al menos 5 caracteres.

        Args:
            nombre (str): El nombre de usuario a validar.

        Returns:
            bool: True si el nombre de usuario es válido, False en caso contrario.
        """
        if len(nombre) < 5:
            return False
        return re.match(r'^[A-Za-z][A-Za-z\s]*$', nombre) is not None

    @staticmethod
    def validar_dni(dni):
        """
        Valida que el DNI contenga solo números.

        Args:
            dni (str): El DNI a validar.

        Returns:
            bool: True si el DNI es válido, False en caso contrario.
        """
        return dni.isdigit()

    @staticmethod
    def validar_telefono(telefono):
        """
        Valida que el teléfono contenga solo números y tenga al menos 7 caracteres.

        Args:
            telefono (str): El teléfono a validar.

        Returns:
            bool: True si el teléfono es válido, False en caso contrario.
        """
        return telefono.isdigit() and len(telefono) >= 7

    @staticmethod
    def validar_no_vacio(campo):
        """
        Valida que el campo no esté vacío.

        Args:
            campo (str): El campo a validar.

        Returns:
            bool: True si el campo no está vacío, False en caso contrario.
        """
        return bool(campo.strip())
