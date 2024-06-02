# main.py
from CoderHouse_57810.services.helpers import print_menu, get_option
from CoderHouse_57810.administrador_menu import operaciones_administradores
from CoderHouse_57810.cliente_menu import operaciones_clientes
from CoderHouse_57810.services.sistema import Sistema


def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    """
    options = ["Operaciones de Clientes", "Operaciones de Administradores", "Salir"]
    print_menu(options)


def main():
    # Creación del sistema
    sistema_principal = Sistema()
    sistema_principal.cargar_datos()

    # Bucle principal del programa
    try:
        while True:
            try:
                mostrar_menu()
                opcion = get_option(["Operaciones de Clientes", "Operaciones de Administradores", "Salir"])
                if opcion == 1:
                    operaciones_clientes(sistema_principal)
                elif opcion == 2:
                    operaciones_administradores(sistema_principal)
                elif opcion == 3:
                    print("Saliendo del sistema.")
                    break
            except Exception as e:  #Excepciones generales no atrapadas por otros metodos.
                print(f"Se produjo un error: {e}")
    finally:
        sistema_principal.guardar_datos()


if __name__ == '__main__':
    main()
