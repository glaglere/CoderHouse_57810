from CoderHouse_57810.services.helpers import print_menu, get_option
from CoderHouse_57810.administrador_menu import operaciones_administradores
from CoderHouse_57810.cliente_menu import operaciones_clientes
from CoderHouse_57810.services.sistema import Sistema

def mostrar_menu(menu_options):
    """
    Muestra el menú principal del sistema.

    Args:
        menu_options (dict): Diccionario de opciones del menú.
    """
    print_menu(list(menu_options.keys()))

def main():
    """
    Función principal del programa. Inicializa el sistema, carga datos y maneja el bucle principal del menú.
    """
    # Creación del sistema
    sistema_principal = Sistema()
    sistema_principal.cargar_datos()

    # Definición de las opciones del menú
    menu_options = {
        "Operaciones de Clientes": lambda: operaciones_clientes(sistema_principal),
        "Operaciones de Administradores": lambda: operaciones_administradores(sistema_principal),
        "Salir": lambda: print("Saliendo del sistema.")
    }

    # Bucle principal del programa
    try:
        while True:
            try:
                mostrar_menu(menu_options)
                opcion = get_option(list(menu_options.keys()))
                action = list(menu_options.values())[opcion - 1]
                action()
                if opcion == len(menu_options):
                    break
            except Exception as e:  # Excepciones generales no atrapadas por otros métodos.
                print(f"Se produjo un error: {e}")
    finally:
        sistema_principal.guardar_datos()

if __name__ == '__main__':
    main()
