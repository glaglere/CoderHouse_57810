# administrador_menu.py
from CoderHouse_57810.models.administrador import Administrador
from CoderHouse_57810.models.cliente import ClientePersona, ClienteCorporativo
from CoderHouse_57810.models.producto import Producto
from CoderHouse_57810.services.helpers import print_menu, get_option, collect_input


def mostrar_menu_administradores():
    options = ["Agregar Cliente Persona", "Agregar Cliente Corporativo", "Agregar Administrador", "Agregar Producto",
               "Mostrar Clientes", "Mostrar Administradores", "Mostrar Productos", "Eliminar Cliente Persona",
               "Eliminar Cliente Corporativo", "Eliminar Administrador", "Eliminar Producto",
               "Ver Historial de Compras de Todos los Clientes", "Regresar al menú principal"]
    print_menu(options)


def operaciones_administradores(sistema):
    while True:
        mostrar_menu_administradores()
        opcion = get_option(["Agregar Cliente Persona", "Agregar Cliente Corporativo", "Agregar Administrador",
                             "Agregar Producto", "Mostrar Clientes", "Mostrar Administradores", "Mostrar Productos",
                             "Eliminar Cliente Persona", "Eliminar Cliente Corporativo", "Eliminar Administrador",
                             "Eliminar Producto", "Ver Historial de Compras de Todos los Clientes",
                             "Regresar al menú principal"])
        if opcion == 1:
            data = collect_input(["nombre", "email", "contraseña", "dirección", "teléfono", "DNI"])
            cliente = ClientePersona(data["nombre"], data["email"], data["contraseña"], data["dirección"],
                                     data["teléfono"], data["DNI"])
            sistema.agregar_cliente_persona(cliente)
            print("Cliente Persona agregado exitosamente.")
        elif opcion == 2:
            data = collect_input(["nombre", "email", "contraseña", "dirección", "teléfono", "CUIT"])
            cliente = ClienteCorporativo(data["nombre"], data["email"], data["contraseña"], data["dirección"],
                                         data["teléfono"], data["CUIT"])
            sistema.agregar_cliente_corporativo(cliente)
            print("Cliente Corporativo agregado exitosamente.")
        elif opcion == 3:
            data = collect_input(["nombre", "email", "contraseña", "código de funcionario"])
            admin = Administrador(data["nombre"], data["email"], data["contraseña"], data["código de funcionario"])
            sistema.agregar_administrador(admin)
            print("Administrador agregado exitosamente.")
        elif opcion == 4:
            data = collect_input(
                ["nombre del producto", "descripción del producto", "categoría del producto", "precio del producto"])
            producto = Producto(data["nombre del producto"], data["descripción del producto"],
                                data["categoría del producto"], float(data["precio del producto"]))
            sistema.agregar_producto(producto)
            print("Producto agregado exitosamente.")
        elif opcion == 5:
            sistema.mostrar_clientes()
        elif opcion == 6:
            sistema.mostrar_administradores()
        elif opcion == 7:
            sistema.mostrar_productos()
        elif opcion == 8:
            email = input("Ingrese el email del cliente persona a eliminar: ")
            sistema.eliminar_cliente_persona(email)
            print("Cliente Persona eliminado exitosamente.")
        elif opcion == 9:
            email = input("Ingrese el email del cliente corporativo a eliminar: ")
            sistema.eliminar_cliente_corporativo(email)
            print("Cliente Corporativo eliminado exitosamente.")
        elif opcion == 10:
            email = input("Ingrese el email del administrador a eliminar: ")
            sistema.eliminar_administrador(email)
            print("Administrador eliminado exitosamente.")
        elif opcion == 11:
            if not sistema.productos:
                print("No hay productos disponibles para eliminar.")
                continue
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            sistema.eliminar_producto(id_producto)
            print("Producto eliminado exitosamente.")
        elif opcion == 12:
            compras = sistema.obtener_historial_compras_todos()
            if compras:
                print("Historial de Compras de Todos los Clientes:")
                for compra in compras:
                    print(compra)
            else:
                print("No hay compras registradas.")
        elif opcion == 13:
            break
