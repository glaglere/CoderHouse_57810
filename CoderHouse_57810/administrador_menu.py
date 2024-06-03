from tabulate import tabulate

from CoderHouse_57810.models.administrador import Administrador
from CoderHouse_57810.models.cliente import ClientePersona, ClienteCorporativo
from CoderHouse_57810.models.producto import Producto
from CoderHouse_57810.services.helpers import print_menu, get_option, collect_input

MENU_OPTIONS = [
    "Agregar Cliente Persona", "Agregar Cliente Corporativo", "Agregar Administrador",
    "Agregar Producto", "Mostrar Clientes", "Mostrar Administradores", "Mostrar Productos",
    "Eliminar Cliente Persona", "Eliminar Cliente Corporativo", "Eliminar Administrador",
    "Eliminar Producto", "Ver Historial de Compras de Todos los Clientes",
    "Regresar al menú principal"
]


def mostrar_menu_administradores():
    """
    Muestra el menú principal de administradores.
    """
    print_menu(MENU_OPTIONS)


def agregar_cliente_persona(sistema):
    """
    Agrega un cliente persona al sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    data = collect_input(["nombre", "email", "contraseña", "dirección", "teléfono", "DNI"])
    cliente = ClientePersona(data["nombre"], data["email"], data["contraseña"], data["dirección"],
                             data["teléfono"], data["DNI"])
    if sistema.agregar_cliente_persona(cliente):
        print("Cliente Persona agregado exitosamente.")
    else:
        print("Error al agregar Cliente Persona.")


def agregar_cliente_corporativo(sistema):
    """
    Agrega un cliente corporativo al sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    data = collect_input(["nombre", "email", "contraseña", "dirección", "teléfono", "CUIT"])
    cliente = ClienteCorporativo(data["nombre"], data["email"], data["contraseña"], data["dirección"],
                                 data["teléfono"], data["CUIT"])
    if sistema.agregar_cliente_corporativo(cliente):
        print("Cliente Corporativo agregado exitosamente.")
    else:
        print("Error al agregar Cliente Corporativo.")


def agregar_administrador(sistema):
    """
    Agrega un administrador al sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    data = collect_input(["nombre", "email", "contraseña", "código funcionario"])
    admin = Administrador(data["nombre"], data["email"], data["contraseña"], data["código funcionario"])
    if sistema.agregar_administrador(admin):
        print("Administrador agregado exitosamente.")
    else:
        print("Error al agregar Administrador.")


def agregar_producto(sistema):
    """
    Agrega un producto al sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    try:
        data = collect_input(["nombre del producto", "descripción del producto", "categoría del producto",
                              "precio del producto"])
        producto = Producto(data["nombre del producto"], data["descripción del producto"],
                            data["categoría del producto"], float(data["precio del producto"]))
        if sistema.agregar_producto(producto):
            print("Producto agregado exitosamente.")
        else:
            print("Error al agregar Producto.")
    except ValueError as e:
        print(f"Error al agregar Producto: {e}")


def mostrar_clientes(sistema):
    """
    Muestra todos los clientes del sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    sistema.mostrar_clientes()


def mostrar_administradores(sistema):
    """
    Muestra todos los administradores del sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    sistema.mostrar_administradores()


def mostrar_productos(sistema):
    """
    Muestra todos los productos del sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    sistema.mostrar_productos()


def eliminar_cliente_persona(sistema):
    """
    Elimina un cliente persona del sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    email = input("Ingrese el email del cliente persona a eliminar: ")
    if sistema.eliminar_cliente_persona(email):
        print("Cliente Persona eliminado exitosamente.")
    else:
        print("Error al eliminar Cliente Persona.")


def eliminar_cliente_corporativo(sistema):
    """
    Elimina un cliente corporativo del sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    email = input("Ingrese el email del cliente corporativo a eliminar: ")
    if sistema.eliminar_cliente_corporativo(email):
        print("Cliente Corporativo eliminado exitosamente.")
    else:
        print("Error al eliminar Cliente Corporativo.")


def eliminar_administrador(sistema):
    """
    Elimina un administrador del sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    email = input("Ingrese el email del administrador a eliminar: ")
    if sistema.eliminar_administrador(email):
        print("Administrador eliminado exitosamente.")
    else:
        print("Error al eliminar Administrador.")


def eliminar_producto(sistema):
    """
    Elimina un producto del sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    if not sistema.productos:
        print("No hay productos disponibles para eliminar.")
        return
    id_producto = input("Ingrese el ID del producto a eliminar: ")
    if sistema.eliminar_producto(id_producto):
        print("Producto eliminado exitosamente.")
    else:
        print("Error al eliminar Producto.")


def ver_historial_compras_todos(sistema):
    """
    Muestra el historial de compras de todos los clientes del sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
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


def operaciones_administradores(sistema):
    """
    Maneja las operaciones disponibles para los administradores.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    while True:
        mostrar_menu_administradores()
        opcion = get_option(MENU_OPTIONS)
        if opcion == 1:
            agregar_cliente_persona(sistema)
        elif opcion == 2:
            agregar_cliente_corporativo(sistema)
        elif opcion == 3:
            agregar_administrador(sistema)
        elif opcion == 4:
            agregar_producto(sistema)
        elif opcion == 5:
            mostrar_clientes(sistema)
        elif opcion == 6:
            mostrar_administradores(sistema)
        elif opcion == 7:
            mostrar_productos(sistema)
        elif opcion == 8:
            eliminar_cliente_persona(sistema)
        elif opcion == 9:
            eliminar_cliente_corporativo(sistema)
        elif opcion == 10:
            eliminar_administrador(sistema)
        elif opcion == 11:
            eliminar_producto(sistema)
        elif opcion == 12:
            ver_historial_compras_todos(sistema)
        elif opcion == 13:
            break
