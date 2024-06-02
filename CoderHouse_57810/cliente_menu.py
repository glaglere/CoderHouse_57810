# cliente_menu.py

from tabulate import tabulate

from CoderHouse_57810.services.helpers import print_menu, get_option, collect_input


def mostrar_menu_clientes():
    """
    Muestra el menú principal de clientes.
    """
    options = ["Loguearse", "Regresar al menú principal"]
    print_menu(options)


def mostrar_menu_cliente_logueado():
    """
    Muestra el menú de opciones para clientes logueados.
    """
    options = [
        "Agregar Producto al Carrito", "Mostrar Carrito", "Quitar Producto del Carrito",
        "Concretar Compra", "Ver Historial de Compras", "Listar Todos los Productos",
        "Listar Productos por Categoría", "Salir"
    ]
    print_menu(options)


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
        opcion = get_option(["Loguearse", "Regresar al menú principal"])
        if opcion == 1:
            credentials = collect_input(["email", "contraseña"])
            cliente = login(credentials["email"], credentials["contraseña"], sistema.clientes_personas + sistema.clientes_corporativos)
            if cliente:
                print(f"Bienvenido {cliente.nombre}")
                operaciones_cliente_logueado(sistema, cliente)
            else:
                print("Credenciales incorrectas.")
        elif opcion == 2:
            break


def operaciones_cliente_logueado(sistema, cliente):
    """
    Maneja las operaciones disponibles para un cliente logueado.

    Args:
        sistema (Sistema): La instancia del sistema.
        cliente (ClientePersona o ClienteCorporativo): El cliente logueado.
    """
    while True:
        mostrar_menu_cliente_logueado()
        opcion = get_option([
            "Agregar Producto al Carrito", "Mostrar Carrito", "Quitar Producto del Carrito",
            "Concretar Compra", "Ver Historial de Compras", "Listar Todos los Productos",
            "Listar Productos por Categoría", "Salir"
        ])
        if opcion == 1:
            if not sistema.productos:
                print("No hay productos disponibles.")
                continue
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
        elif opcion == 2:
            carrito = sistema.mostrar_carrito(cliente.email)
            if carrito:
                print("Carrito:")
                table = [[item["producto"].id_producto, item["producto"].nombre, item["producto"].descripcion,
                          item["producto"].categoria, item["producto"].precio, item["cantidad"]] for item in carrito]
                print(tabulate(table, headers=["ID", "Nombre", "Descripción", "Categoría", "Precio", "Cantidad"], tablefmt="pretty"))
            else:
                print("El carrito está vacío.")
        elif opcion == 3:
            try:
                id_producto = int(input("Ingrese el ID del producto a quitar del carrito: "))
                sistema.quitar_producto_del_carrito(cliente.email, id_producto)
                print("Producto quitado del carrito.")
            except ValueError as e:
                print(e)
        elif opcion == 4:
            try:
                compra = sistema.concretar_compra(cliente.email)
                if compra:
                    print("Compra concretada exitosamente.")
            except ValueError as e:
                print(e)
        elif opcion == 5:
            historial_compras = sistema.obtener_historial_compras_cliente(cliente.email)
            if historial_compras:
                print("Historial de Compras:")
                for compra in historial_compras:
                    print(compra)
            else:
                print("No hay compras registradas.")
        elif opcion == 6:
            sistema.mostrar_productos()
        elif opcion == 7:
            categorias = sistema.obtener_categorias_productos()
            if not categorias:
                print("No hay categorías disponibles.")
                continue
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
        elif opcion == 8:
            break
