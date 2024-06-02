def mostrar_menu_clientes():
    print("\nSeleccione una operación de clientes:")
    print("1. Loguearse")
    print("2. Regresar al menú principal")

def mostrar_menu_cliente_logueado():
    print("\nSeleccione una operación:")
    print("1. Agregar Producto al Carrito")
    print("2. Mostrar Carrito")
    print("3. Concretar Compra")
    print("4. Salir")

def login(email, password, usuarios):
    for usuario in usuarios:
        if usuario.email == email and usuario.password == password:
            return usuario
    return None

def operaciones_clientes(sistema):
    while True:
        mostrar_menu_clientes()
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            email = input("Ingrese el email: ")
            password = input("Ingrese la contraseña: ")
            cliente = login(email, password, sistema.clientes_personas + sistema.clientes_corporativos)
            if cliente:
                print(f"Bienvenido {cliente.nombre}")
                operaciones_cliente_logueado(sistema, cliente)
            else:
                print("Credenciales incorrectas.")
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def operaciones_cliente_logueado(sistema, cliente):
    while True:
        mostrar_menu_cliente_logueado()
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            sistema.mostrar_productos()
            id_producto = input("Ingrese el ID del producto a agregar al carrito: ")
            producto = next((p for p in sistema.productos if p.id_producto == id_producto), None)
            if producto:
                sistema.agregar_producto_al_carrito(cliente.email, producto)
                print("Producto agregado al carrito.")
            else:
                print("Producto no encontrado.")
        elif opcion == "2":
            carrito = sistema.mostrar_carrito(cliente.email)
            if carrito:
                print("Carrito:")
                for producto in carrito:
                    print(producto)
            else:
                print("El carrito está vacío.")
        elif opcion == "3":
            compra = sistema.concretar_compra(cliente.email)
            if compra:
                print("Compra concretada exitosamente.")
                print(compra)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
