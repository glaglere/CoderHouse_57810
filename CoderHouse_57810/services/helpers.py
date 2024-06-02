# helpers.py
from tabulate import tabulate


def collect_input(fields):
    data = {}
    for field in fields:
        data[field] = input(f"Ingrese {field}: ")
    return data


def print_menu(options, title="\nSeleccione una opción:"):
    print(title)
    table = [[index + 1, option] for index, option in enumerate(options)]
    print(tabulate(table, headers=["Opción", "Descripción"], tablefmt="pretty"))


def get_option(options):
    while True:
        try:
            option = int(input("Ingrese su opción: "))
            if 1 <= option <= len(options):
                return option
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")
