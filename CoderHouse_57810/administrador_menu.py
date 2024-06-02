
from tabulate import tabulate

from CoderHouse_57810.models.administrador import Administrador
from CoderHouse_57810.models.cliente import ClientePersona, ClienteCorporativo
from CoderHouse_57810.models.producto import Producto
from CoderHouse_57810.services.helpers import print_menu, get_option, collect_input


def mostrar_menu_administradores():
    """
    Muestra el menú principal de administradores.
    """
    options = [
        "Agregar Cliente Persona", "Agregar Cliente Corporativo", "Agregar Administrador",
        "Agregar Producto", "Mostrar Clientes", "Mostrar Administradores", "Mostrar Productos",
        "Eliminar Cliente Persona", "Eliminar Cliente Corporativo", "Eliminar Administrador",
        "Eliminar Producto", "Ver Historial de Compras de Todos los Clientes",
        "Regresar al menú principal"
    ]
    print_menu(options)


def operaciones_administradores(sistema):
    """
    Maneja las operaciones disponibles para los administradores.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    while True:
        mostrar_menu_administradores()
        opcion = get_option([
            "Agregar Cliente Persona", "Agregar Cliente Corporativo", "Agregar Administrador",
            "Agregar Producto", "Mostrar Clientes", "Mostrar Administradores", "Mostrar Productos",
            "Eliminar Cliente Persona", "Eliminar Cliente Corporativo", "Eliminar Administrador",
            "Eliminar Producto", "Ver Historial de Compras de Todos los Clientes",
            "Regresar al menú principal"
        ])
        if opcion == 1:
            data = collect_input(["nombre", "email", "contraseña", "dirección", "teléfono", "DNI"])
            cliente = ClientePersona(data["nombre"], data["email"], data["contraseña"], data["dirección"],
                                     data["teléfono"], data["DNI"])
            if sistema.agregar_cliente_persona(cliente):
                print("Cliente Persona agregado exitosamente.")
            else:
                print("Error al agregar Cliente Persona.")
        elif opcion == 2:
            data = collect_input(["nombre", "email", "contraseña", "dirección", "teléfono", "CUIT"])
            cliente = ClienteCorporativo(data["nombre"], data["email"], data["contraseña"], data["dirección"],
                                         data["teléfono"], data["CUIT"])
            if sistema.agregar_cliente_corporativo(cliente):
                print("Cliente Corporativo agregado exitosamente.")
            else:
                print("Error al agregar Cliente Corporativo.")
        elif opcion == 3:
            data = collect_input(["nombre", "email", "contraseña", "código funcionario"])
            admin = Administrador(data["nombre"], data["email"], data["contraseña"], data["código funcionario"])
            if sistema.agregar_administrador(admin):
                print("Administrador agregado exitosamente.")
            else:
                print("Error al agregar Administrador.")
        elif opcion == 4:
            data = collect_input(["nombre del producto", "descripción del producto", "categoría del producto",
                                  "precio del producto"])
            producto = Producto(data["nombre del producto"], data["descripción del producto"],
                                data["categoría del producto"], float(data["precio del producto"]))
            if sistema.agregar_producto(producto):
                print("Producto agregado exitosamente.")
            else:
                print("Error al agregar Producto.")
        elif opcion == 5:
            sistema.mostrar_clientes()
        elif opcion == 6:
            sistema.mostrar_administradores()
        elif opcion == 7:
            sistema.mostrar_productos()
        elif opcion == 8:
            email = input("Ingrese el email del cliente persona a eliminar: ")
            if sistema.eliminar_cliente_persona(email):
                print("Cliente Persona eliminado exitosamente.")
            else:
                print("Error al eliminar Cliente Persona.")
        elif opcion == 9:
            email = input("Ingrese el email del cliente corporativo a eliminar: ")
            if sistema.eliminar_cliente_corporativo(email):
                print("Cliente Corporativo eliminado exitosamente.")
            else:
                print("Error al eliminar Cliente Corporativo.")
        elif opcion == 10:
            email = input("Ingrese el email del administrador a eliminar: ")
            if sistema.eliminar_administrador(email):
                print("Administrador eliminado exitosamente.")
            else:
                print("Error al eliminar Administrador.")
        elif opcion == 11:
            if not sistema.productos:
                print("No hay productos disponibles para eliminar.")
                continue
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            if sistema.eliminar_producto(id_producto):
                print("Producto eliminado exitosamente.")
            else:
                print("Error al eliminar Producto.")
        elif opcion == 12:
            compras = sistema.obtener_historial_compras_todos()
            if compras:
                print("Historial de Compras de Todos los Clientes:")
                table = []
                for compra in compras:
                    productos_str = ", ".join(
                        [f"{prod['producto'].nombre} x{prod['cantidad']}" for prod in compra.productos])
                    precio_total = sum([prod['producto'].precio * prod['cantidad'] for prod in compra.productos])
                    table.append([compra.cliente.nombre, compra.cliente.email, productos_str, precio_total,
                                  compra.fecha.strftime('%Y-%m-%d %H:%M:%S')])
                print(tabulate(table, headers=["Cliente", "Email", "Productos", "Precio Total", "Fecha de Compra"],
                               tablefmt="pretty"))
            else:
                print("No hay compras registradas.")
        elif opcion == 13:
            break
