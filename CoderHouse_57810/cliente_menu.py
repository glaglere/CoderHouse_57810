# cliente_menu.py

from tabulate import tabulate

from CoderHouse_57810.services.helpers import print_menu, get_option, collect_input
from CoderHouse_57810.models.cliente import ClientePersona, ClienteCorporativo

MENU_OPTIONS_CLIENTE = ["Registrar Cliente", "Loguearse", "Regresar al menú principal"]
MENU_OPTIONS_CLIENTE_LOGUEADO = [
    "Agregar Producto al Carrito", "Mostrar Carrito", "Quitar Producto del Carrito",
    "Concretar Compra", "Ver Historial de Compras", "Listar Todos los Productos",
    "Listar Productos por Categoría", "Salir"
]

def validar_email_unico(email, sistema):
    """
    Verifica si un email es único en el sistema.

    Args:
        email (str): El correo electrónico a validar.
        sistema (Sistema): La instancia del sistema.

    Returns:
        bool: True si el email es único, False en caso contrario.
    """
    for cliente in sistema.clientes_personas + sistema.clientes_corporativos:
        if cliente.email == email:
            return False
    return True

def registrar_cliente(sistema):
    """
    Permite a un nuevo cliente registrarse en el sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    while True:
        email = input("Ingrese el email: ")
        if validar_email_unico(email, sistema):
            break
        print("El email ya existe. Por favor ingrese un email diferente.")

    tipo_cliente = input("Ingrese el tipo de cliente (1 para Persona, 2 para Corporativo): ")

    if tipo_cliente == '1':
        data = collect_input(["nombre", "contraseña", "dirección", "teléfono", "DNI"])
        cliente = ClientePersona(data["nombre"], email, data["contraseña"], data["dirección"], data["teléfono"],
                                 data["DNI"])
        if sistema.agregar_cliente_persona(cliente):
            print("Cliente Persona registrado exitosamente.")
        else:
            print("Error al registrar Cliente Persona.")
    elif tipo_cliente == '2':
        data = collect_input(["nombre", "contraseña", "dirección", "teléfono", "CUIT"])
        cliente = ClienteCorporativo(data["nombre"], email, data["contraseña"], data["dirección"], data["teléfono"],
                                     data["CUIT"])
        if sistema.agregar_cliente_corporativo(cliente):
            print("Cliente Corporativo registrado exitosamente.")
        else:
            print("Error al registrar Cliente Corporativo.")
    else:
        print("Tipo de cliente no válido. Intente nuevamente.")

def mostrar_menu_clientes():
    """
    Muestra el menú principal de clientes.
    """
    print_menu(MENU_OPTIONS_CLIENTE)

def mostrar_menu_cliente_logueado():
    """
    Muestra el menú de opciones para clientes logueados.
    """
    print_menu(MENU_OPTIONS_CLIENTE_LOGUEADO)

def login(email, password, usuarios):
    """
    Realiza el login de un cliente.

    Args:
        email (str): El correo electrónico del cliente.
        password (str): La contraseña del cliente.
        usuarios (list): La lista de usuarios registrados.

    Returns:
        Usuario: El usuario que se loguea, None si no se encuentra.
    """
    for usuario in usuarios:
        if usuario.email == email and usuario.password == password:
            return usuario
    return None

def operaciones_clientes(sistema):
    """
    Maneja las operaciones disponibles para los clientes.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    while True:
        mostrar_menu_clientes()
        opcion = get_option(MENU_OPTIONS_CLIENTE)
        if opcion == 1:
            registrar_cliente(sistema)
        elif opcion == 2:
            credentials = collect_input(["email", "contraseña"])
            cliente = login(credentials["email"], credentials["contraseña"],
                            sistema.clientes_personas + sistema.clientes_corporativos)
            if cliente:
                print(f"Bienvenido {cliente.nombre}")
                operaciones_cliente_logueado(sistema, cliente)
            else:
                print("Credenciales incorrectas.")
        elif opcion == 3:
            break

def agregar_producto_al_carrito(sistema, cliente):
    """
    Permite al cliente agregar varios productos al carrito.

    Args:
        sistema (Sistema): La instancia del sistema.
        cliente (ClientePersona o ClienteCorporativo): El cliente logueado.
    """
    if not sistema.productos:
        print("No hay productos disponibles.")
        return

    while True:
        sistema.mostrar_productos()
        try:
            id_producto = int(input("Ingrese el ID del producto a agregar al carrito: "))
            cantidad = int(input("Ingrese la cantidad del producto a agregar al carrito: "))
        except ValueError:
            print("ID o cantidad de producto no válidos.")
            continue
        producto = next((p for p in sistema.productos if p.id_producto == id_producto), None)
        if producto:
            sistema.agregar_producto_al_carrito(cliente.email, producto, cantidad)
            print("Producto agregado al carrito.")
        else:
            print("Producto no encontrado.")

        continuar = input("¿Desea agregar otro producto? (s/n): ")
        if continuar.lower() != 's':
            break

def mostrar_carrito(sistema, cliente):
    """
    Muestra el contenido del carrito del cliente.

    Args:
        sistema (Sistema): La instancia del sistema.
        cliente (ClientePersona o ClienteCorporativo): El cliente logueado.
    """
    carrito = sistema.mostrar_carrito(cliente.email)
    if carrito:
        print("Carrito:")
        table = [[item["producto"].id_producto, item["producto"].nombre, item["producto"].descripcion,
                  item["producto"].categoria, item["producto"].precio, item["cantidad"]] for item in carrito]
        print(tabulate(table, headers=["ID", "Nombre", "Descripción", "Categoría", "Precio", "Cantidad"],
                       tablefmt="pretty"))
    else:
        print("El carrito está vacío.")

def quitar_producto_del_carrito(sistema, cliente):
    """
    Permite al cliente quitar un producto del carrito.

    Args:
        sistema (Sistema): La instancia del sistema.
        cliente (ClientePersona o ClienteCorporativo): El cliente logueado.
    """
    try:
        id_producto = int(input("Ingrese el ID del producto a quitar del carrito: "))
        sistema.quitar_producto_del_carrito(cliente.email, id_producto)
        print("Producto quitado del carrito.")
    except ValueError as e:
        print(e)

def concretar_compra(sistema, cliente):
    """
    Permite al cliente concretar la compra de los productos en el carrito.

    Args:
        sistema (Sistema): La instancia del sistema.
        cliente (ClientePersona o ClienteCorporativo): El cliente logueado.
    """
    try:
        compra = sistema.concretar_compra(cliente.email)
        if compra:
            print("Compra concretada exitosamente.")
    except ValueError as e:
        print(e)

def ver_historial_de_compras(sistema, cliente):
    """
    Muestra el historial de compras del cliente.

    Args:
        sistema (Sistema): La instancia del sistema.
        cliente (ClientePersona o ClienteCorporativo): El cliente logueado.
    """
    historial_compras = sistema.obtener_historial_compras_cliente(cliente.email)
    if historial_compras:
        print("Historial de Compras:")
        table = []
        for compra in historial_compras:
            productos_str = ", ".join([f"{prod['producto'].nombre} x{prod['cantidad']}" for prod in compra.productos])
            precio_total = sum([prod['producto'].precio * prod['cantidad'] for prod in compra.productos])
            table.append([compra.fecha.strftime('%Y-%m-%d %H:%M:%S'), productos_str, precio_total])
        print(tabulate(table, headers=["Fecha de Compra", "Productos", "Precio Total"], tablefmt="pretty"))
    else:
        print("No hay compras registradas.")

def listar_todos_los_productos(sistema):
    """
    Lista todos los productos disponibles en el sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    sistema.mostrar_productos()

def listar_productos_por_categoria(sistema):
    """
    Lista los productos disponibles en el sistema por categoría.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    categorias = sistema.obtener_categorias_productos()
    if not categorias:
        print("No hay categorías disponibles.")
        return
    print("Categorías:")
    table = [[index + 1, categoria] for index, categoria in enumerate(categorias)]
    print(tabulate(table, headers=["Opción", "Categoría"], tablefmt="pretty"))
    try:
        opcion_categoria = int(input("Seleccione una categoría: ")) - 1
        if 0 <= opcion_categoria < len(categorias):
            sistema.mostrar_productos_por_categoria(categorias[opcion_categoria])
        else:
            print("Opción no válida.")
    except ValueError:
        print("Entrada no válida.")

def operaciones_cliente_logueado(sistema, cliente):
    """
    Maneja las operaciones disponibles para un cliente logueado.

    Args:
        sistema (Sistema): La instancia del sistema.
        cliente (ClientePersona o ClienteCorporativo): El cliente logueado.
    """
    while True:
        mostrar_menu_cliente_logueado()
        opcion = get_option(MENU_OPTIONS_CLIENTE_LOGUEADO)
        if opcion == 1:
            agregar_producto_al_carrito(sistema, cliente)
        elif opcion == 2:
            mostrar_carrito(sistema, cliente)
        elif opcion == 3:
            quitar_producto_del_carrito(sistema, cliente)
        elif opcion == 4:
            concretar_compra(sistema, cliente)
        elif opcion == 5:
            ver_historial_de_compras(sistema, cliente)
        elif opcion == 6:
            listar_todos_los_productos(sistema)
        elif opcion == 7:
            listar_productos_por_categoria(sistema)
        elif opcion == 8:
            break
