from tabulate import tabulate
from CoderHouse_57810.services.seguridad import Seguridad

validations = {
    "nombre": ("El nombre debe tener al menos 5 caracteres, no contener números, solo letras y "
               "espacios en blanco, y debe comenzar con una letra.", Seguridad.validar_nombre_usuario),
    "email": ("El email debe tener un formato válido.", Seguridad.validar_email),
    "contraseña": (
        "La contraseña debe tener al menos 8 caracteres y contener letras y números.", Seguridad.validar_password),
    "dirección": ("La dirección no puede estar vacía.", Seguridad.validar_no_vacio),
    "teléfono": ("El teléfono debe contener solo números y tener al menos 7 caracteres.", Seguridad.validar_telefono),
    "DNI": ("El DNI debe contener solo números.", Seguridad.validar_dni),
    "CUIT": ("El CUIT no puede estar vacío.", Seguridad.validar_no_vacio),
    "nombre del producto": ("El nombre del producto debe tener solo letras y espacios, y no puede estar vacío.",
                            Seguridad.validar_nombre_usuario),
    "descripción del producto": (
    "La descripción del producto debe tener solo letras y espacios, y no puede estar vacía.",
    Seguridad.validar_no_vacio),
    "categoría del producto": ("La categoría del producto no puede estar vacía.", Seguridad.validar_no_vacio),
    "precio del producto": (
        "El precio del producto debe ser un número mayor a 0.",
        lambda x: x.replace('.', '', 1).isdigit() and float(x) > 0),
    "código funcionario": ("El código funcionario no puede estar vacío.", Seguridad.validar_no_vacio)
}

def collect_input(fields):
    """
    Recoge la entrada del usuario para una lista de campos especificados.

    Args:
        fields (list): Una lista de nombres de campos.

    Returns:
        dict: Un diccionario con los datos ingresados por el usuario.
    """
    data = {}
    for field in fields:
        error_message, validation = validations[field]
        while True:
            value = input(f"Ingrese {field}: ")
            if validation(value):
                data[field] = value
                break
            else:
                print(f"{error_message} Inténtelo nuevamente.")
    return data

def print_menu(options, title="\nSeleccione una opción:"):
    """
    Muestra un menú con opciones utilizando la biblioteca tabulate.

    Args:
        options (list): Una lista de opciones para el menú.
        title (str): El título del menú.
    """
    print(title)
    table = [[index + 1, option] for index, option in enumerate(options)]
    print(tabulate(table, headers=["Opción", "Descripción"], tablefmt="pretty"))

def get_option(options):
    """
    Solicita al usuario que seleccione una opción del menú.

    Args:
        options (list): Una lista de opciones disponibles.

    Returns:
        int: La opción seleccionada por el usuario.
    """
    while True:
        try:
            option = int(input("Ingrese su opción: "))
            if 1 <= option <= len(options):
                return option
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")
