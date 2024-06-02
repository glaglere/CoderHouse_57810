# cliente_menu.py
from CoderHouse_57810.services.helpers import print_menu, collect_input, get_option


def mostrar_menu_clientes():
    options = ["Loguearse", "Regresar al menú principal"]
    print_menu(options)


def mostrar_menu_cliente_logueado():
    options = ["Agregar Producto al Carrito", "Mostrar Carrito", "Concretar Compra", "Ver Historial de Compras",
               "Salir"]
    print_menu(options)


def login(email, password, usuarios):
    for usuario in usuarios:
        if usuario.email == email and usuario.password == password:
            return usuario
    return None


def operaciones_clientes(sistema):
    while True:
        mostrar_menu_clientes()
        opcion = get_option(["Loguearse", "Regresar al menú principal"])
        if opcion == 1:
            credentials = collect_input(["email", "contraseña"])
            cliente = login(credentials["email"], credentials["contraseña"],
                            sistema.clientes_personas + sistema.clientes_corporativos)
            if cliente:
                print(f"Bienvenido {cliente.nombre}")
                operaciones_cliente_logueado(sistema, cliente)
            else:
                print("Credenciales incorrectas.")
        elif opcion == 2:
            break


def operaciones_cliente_logueado(sistema, cliente):
    while True:
        mostrar_menu_cliente_logueado()
        opcion = get_option(
            ["Agregar Producto al Carrito", "Mostrar Carrito", "Concretar Compra", "Ver Historial de Compras", "Salir"])
        if opcion == 1:
            if not sistema.productos:
                print("No hay productos disponibles.")
                continue
            sistema.mostrar_productos()
            try:
                id_producto = int(input("Ingrese el ID del producto a agregar al carrito: "))
            except ValueError:
                print("ID de producto no válido.")
                continue
            producto = next((p for p in sistema.productos if p.id_producto == id_producto), None)
            if producto:
                sistema.agregar_producto_al_carrito(cliente.email, producto)
                print("Producto agregado al carrito.")
            else:
                print("Producto no encontrado.")
        elif opcion == 2:
            carrito = sistema.mostrar_carrito(cliente.email)
            if carrito:
                print("Carrito:")
                for producto in carrito:
                    print(producto)
            else:
                print("El carrito está vacío.")
        elif opcion == 3:
            compra = sistema.concretar_compra(cliente.email)
            if compra:
                print("Compra concretada exitosamente.")
                print(compra)
        elif opcion == 4:
            historial_compras = sistema.obtener_historial_compras_cliente(cliente.email)
            if historial_compras:
                print("Historial de Compras:")
                for compra in historial_compras:
                    print(compra)
            else:
                print("No hay compras registradas.")
        elif opcion == 5:
            break
