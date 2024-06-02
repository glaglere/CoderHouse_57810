from services.sistema import Sistema
from cliente_menu import operaciones_clientes
from administrador_menu import operaciones_administradores


def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Operaciones de Clientes")
    print("2. Operaciones de Administradores")
    print("3. Salir")


if __name__ == '__main__':
    # Creación del sistema
    sistema_principal = Sistema()

    # Bucle principal del programa
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            operaciones_clientes(sistema_principal)
        elif opcion == "2":
            operaciones_administradores(sistema_principal)
        elif opcion == "3":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
