# main.py
from CoderHouse_57810.services.helpers import print_menu, get_option
from administrador_menu import operaciones_administradores
from cliente_menu import operaciones_clientes
from services.sistema import Sistema


def mostrar_menu():
    options = ["Operaciones de Clientes", "Operaciones de Administradores", "Salir"]
    print_menu(options)


if __name__ == '__main__':
    # Creación del sistema
    sistema_principal = Sistema()
    sistema_principal.cargar_datos()

    # Bucle principal del programa
    try:
        while True:
            mostrar_menu()
            opcion = get_option(["Operaciones de Clientes", "Operaciones de Administradores", "Salir"])
            if opcion == 1:
                operaciones_clientes(sistema_principal)
            elif opcion == 2:
                operaciones_administradores(sistema_principal)
            elif opcion == 3:
                print("Saliendo del sistema.")
                break
    finally:
        sistema_principal.guardar_datos()
