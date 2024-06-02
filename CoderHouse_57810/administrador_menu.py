from services.sistema import Sistema
from CoderHouse_57810.models.cliente import ClientePersona, ClienteCorporativo
from CoderHouse_57810.models.administrador import Administrador
from CoderHouse_57810.models.producto import Producto


def mostrar_menu_administradores():
    print("\nSeleccione una operación de administradores:")
    print("1. Agregar Cliente Persona")
    print("2. Agregar Cliente Corporativo")
    print("3. Agregar Administrador")
    print("4. Agregar Producto")
    print("5. Mostrar Clientes")
    print("6. Mostrar Administradores")
    print("7. Mostrar Productos")
    print("8. Eliminar Cliente Persona")
    print("9. Eliminar Cliente Corporativo")
    print("10. Eliminar Administrador")
    print("11. Eliminar Producto")
    print("12. Regresar al menú principal")


def operaciones_administradores(sistema):
    while True:
        mostrar_menu_administradores()
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            email = input("Ingrese el email: ")
            password = input("Ingrese la contraseña: ")
            direccion = input("Ingrese la dirección: ")
            telefono = input("Ingrese el teléfono: ")
            dni = input("Ingrese el DNI: ")
            cliente = ClientePersona(nombre, email, password, direccion, telefono, dni)
            sistema.agregar_cliente_persona(cliente)
            print("Cliente Persona agregado exitosamente.")
        elif opcion == "2":
            nombre = input("Ingrese el nombre: ")
            email = input("Ingrese el email: ")
            password = input("Ingrese la contraseña: ")
            direccion = input("Ingrese la dirección: ")
            telefono = input("Ingrese el teléfono: ")
            cuit = input("Ingrese el CUIT: ")
            cliente = ClienteCorporativo(nombre, email, password, direccion, telefono, cuit)
            sistema.agregar_cliente_corporativo(cliente)
            print("Cliente Corporativo agregado exitosamente.")
        elif opcion == "3":
            nombre = input("Ingrese el nombre: ")
            email = input("Ingrese el email: ")
            password = input("Ingrese la contraseña: ")
            codigo_funcionario = input("Ingrese el código de funcionario: ")
            admin = Administrador(nombre, email, password, codigo_funcionario)
            sistema.agregar_administrador(admin)
            print("Administrador agregado exitosamente.")
        elif opcion == "4":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            descripcion = input("Ingrese la descripción del producto: ")
            categoria = input("Ingrese la categoría del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, descripcion, categoria, precio)
            sistema.agregar_producto(producto)
            print("Producto agregado exitosamente.")
        elif opcion == "5":
            sistema.mostrar_clientes()
        elif opcion == "6":
            sistema.mostrar_administradores()
        elif opcion == "7":
            sistema.mostrar_productos()
        elif opcion == "8":
            email = input("Ingrese el email del cliente persona a eliminar: ")
            sistema.eliminar_cliente_persona(email)
            print("Cliente Persona eliminado exitosamente.")
        elif opcion == "9":
            email = input("Ingrese el email del cliente corporativo a eliminar: ")
            sistema.eliminar_cliente_corporativo(email)
            print("Cliente Corporativo eliminado exitosamente.")
        elif opcion == "10":
            email = input("Ingrese el email del administrador a eliminar: ")
            sistema.eliminar_administrador(email)
            print("Administrador eliminado exitosamente.")
        elif opcion == "11":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            sistema.eliminar_producto(id_producto)
            print("Producto eliminado exitosamente.")
        elif opcion == "12":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
