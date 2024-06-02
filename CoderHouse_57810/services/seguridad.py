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
        Valida que el nombre de usuario tenga al menos 3 caracteres.

        Args:
            nombre (str): El nombre de usuario a validar.

        Returns:
            bool: True si el nombre de usuario es válido, False en caso contrario.
        """
        return len(nombre) >= 3

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

    @staticmethod
    def validar_cliente_persona(cliente):
        """
        Valida los atributos de un cliente persona.

        Args:
            cliente (ClientePersona): El cliente persona a validar.

        Raises:
            ValueError: Si algún atributo no es válido.
        """
        if not Seguridad.validar_no_vacio(cliente.nombre) or not Seguridad.validar_nombre_usuario(cliente.nombre):
            raise ValueError("El nombre del cliente persona no es válido.")
        if not Seguridad.validar_email(cliente.email):
            raise ValueError("El email del cliente persona no es válido.")
        if not Seguridad.validar_password(cliente.password):
            raise ValueError("La contraseña del cliente persona no es válida.")
        if not Seguridad.validar_no_vacio(cliente.direccion):
            raise ValueError("La dirección del cliente persona no puede estar vacía.")
        if not Seguridad.validar_telefono(cliente.telefono):
            raise ValueError("El teléfono del cliente persona no es válido.")
        if not Seguridad.validar_dni(cliente.dni):
            raise ValueError("El DNI del cliente persona no es válido.")

    @staticmethod
    def validar_cliente_corporativo(cliente):
        """
        Valida los atributos de un cliente corporativo.

        Args:
            cliente (ClienteCorporativo): El cliente corporativo a validar.

        Raises:
            ValueError: Si algún atributo no es válido.
        """
        if not Seguridad.validar_no_vacio(cliente.nombre) or not Seguridad.validar_nombre_usuario(cliente.nombre):
            raise ValueError("El nombre del cliente corporativo no es válido.")
        if not Seguridad.validar_email(cliente.email):
            raise ValueError("El email del cliente corporativo no es válido.")
        if not Seguridad.validar_password(cliente.password):
            raise ValueError("La contraseña del cliente corporativo no es válida.")
        if not Seguridad.validar_no_vacio(cliente.direccion):
            raise ValueError("La dirección del cliente corporativo no puede estar vacía.")
        if not Seguridad.validar_telefono(cliente.telefono):
            raise ValueError("El teléfono del cliente corporativo no es válido.")
        if not Seguridad.validar_no_vacio(cliente.cuit):
            raise ValueError("El CUIT del cliente corporativo no puede estar vacío.")

    @staticmethod
    def validar_administrador(administrador):
        """
        Valida los atributos de un administrador.

        Args:
            administrador (Administrador): El administrador a validar.

        Raises:
            ValueError: Si algún atributo no es válido.
        """
        if not Seguridad.validar_no_vacio(administrador.nombre) or not Seguridad.validar_nombre_usuario(administrador.nombre):
            raise ValueError("El nombre del administrador no es válido.")
        if not Seguridad.validar_email(administrador.email):
            raise ValueError("El email del administrador no es válido.")
        if not Seguridad.validar_password(administrador.password):
            raise ValueError("La contraseña del administrador no es válida.")
        if not Seguridad.validar_no_vacio(administrador.codigo_funcionario):
            raise ValueError("El código de funcionario del administrador no puede estar vacío.")
