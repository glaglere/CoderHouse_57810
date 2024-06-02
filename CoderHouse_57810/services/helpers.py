# helpers.py

from tabulate import tabulate


def collect_input(fields):
    """
    Recopila la entrada del usuario para una lista de campos.

    Args:
        fields (list): Una lista de nombres de campos.

    Returns:
        dict: Un diccionario con los valores ingresados por el usuario.
    """
    data = {}
    for field in fields:
        data[field] = input(f"Ingrese {field}: ")
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
