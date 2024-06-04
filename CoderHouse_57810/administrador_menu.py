import bcrypt
import re
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

def validar_email_formato(email):
    """
    Valida que el email tenga un formato correcto.

    Args:
        email (str): El email a validar.

    Returns:
        bool: True si el email es válido, False en caso contrario.
    """
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def validar_email_unico(email, sistema):
    """
    Valida que el email sea único en el sistema.

    Args:
        email (str): El email a validar.
        sistema (Sistema): La instancia del sistema.

    Returns:
        bool: True si el email es único, False en caso contrario.
    """
    for cliente in sistema.clientes_personas + sistema.clientes_corporativos + sistema.administradores:
        if cliente.email == email:
            return False
    return True

def validar_dni(dni, sistema):
    """
    Valida que el DNI tenga al menos 7 dígitos, contenga solo números y sea único en el sistema.

    Args:
        dni (str): El DNI a validar.
        sistema (Sistema): La instancia del sistema.

    Returns:
        bool: True si el DNI es válido y único, False en caso contrario.
    """
    if len(dni) < 7 or not dni.isdigit():
        print("El DNI debe tener al menos 7 dígitos y contener solo números.")
        return False
    for cliente in sistema.clientes_personas:
        if cliente.dni == dni:
            print("El DNI ya existe. Por favor ingrese un DNI diferente.")
            return False
    return True

def validar_cuit_unico(cuit, sistema):
    """
    Valida que el CUIT sea único en el sistema.

    Args:
        cuit (str): El CUIT a validar.
        sistema (Sistema): La instancia del sistema.

    Returns:
        bool: True si el CUIT es único, False en caso contrario.
    """
    for cliente in sistema.clientes_corporativos:
        if cliente.cuit == cuit:
            return False
    return True

def validar_contraseña(contraseña):
    """
    Valida que la contraseña tenga al menos 8 caracteres, contenga letras y números.

    Args:
        contraseña (str): La contraseña a validar.

    Returns:
        bool: True si la contraseña es válida, False en caso contrario.
    """
    if len(contraseña) < 8:
        return False
    if not any(char.isdigit() for char in contraseña):
        return False
    if not any(char.isalpha() for char in contraseña):
        return False
    return True

def validar_nombre(nombre):
    """
    Valida que el nombre tenga al menos 5 caracteres, no contenga números, solo letras y espacios en blanco,
    y comience con una letra.

    Args:
        nombre (str): El nombre a validar.

    Returns:
        bool: True si el nombre es válido, False en caso contrario.
    """
    if len(nombre) < 5 or not nombre.replace(" ", "").isalpha() or not nombre[0].isalpha():
        return False
    return True

def validar_telefono(telefono):
    """
    Valida que el teléfono contenga solo números y tenga al menos 7 caracteres.

    Args:
        telefono (str): El teléfono a validar.

    Returns:
        bool: True si el teléfono es válido, False en caso contrario.
    """
    return telefono.isdigit() and len(telefono) >= 7

def validar_direccion(direccion):
    """
    Valida que la dirección tenga al menos 7 caracteres.

    Args:
        direccion (str): La dirección a validar.

    Returns:
        bool: True si la dirección es válida, False en caso contrario.
    """
    if len(direccion) < 7:
        return False
    return True

def validar_nombre_producto(nombre_producto, sistema):
    """
    Valida que el nombre del producto no esté vacío y sea único en el sistema.

    Args:
        nombre_producto (str): El nombre del producto a validar.
        sistema (Sistema): La instancia del sistema.

    Returns:
        bool: True si el nombre del producto es válido y único, False en caso contrario.
    """
    if nombre_producto.strip() == "":
        print("El nombre del producto no puede estar vacío.")
        return False
    for producto in sistema.productos:
        if producto.nombre == nombre_producto:
            print("El producto ya existe. Por favor ingrese un nombre de producto diferente.")
            return False
    return True

def validar_descripcion(descripcion):
    """
    Valida que la descripción del producto no esté vacía.

    Args:
        descripcion (str): La descripción del producto a validar.

    Returns:
        bool: True si la descripción es válida, False en caso contrario.
    """
    if descripcion.strip() == "":
        print("La descripción del producto no puede estar vacía.")
        return False
    return True

def validar_categoria(categoria):
    """
    Valida que la categoría del producto no esté vacía.

    Args:
        categoria (str): La categoría del producto a validar.

    Returns:
        bool: True si la categoría es válida, False en caso contrario.
    """
    if categoria.strip() == "":
        print("La categoría del producto no puede estar vacía.")
        return False
    return True

def validar_precio(precio):
    """
    Valida que el precio del producto sea un número mayor a 0.

    Args:
        precio (str): El precio del producto a validar.

    Returns:
        bool: True si el precio es válido, False en caso contrario.
    """
    try:
        precio_float = float(precio)
        if precio_float <= 0:
            print("El precio del producto debe ser mayor a 0.")
            return False
        return True
    except ValueError:
        print("El precio debe ser un número.")
        return False

def validar_codigo_funcionario(codigo_funcionario, sistema):
    """
    Valida que el código de funcionario no esté vacío y sea único en el sistema.

    Args:
        codigo_funcionario (str): El código de funcionario a validar.
        sistema (Sistema): La instancia del sistema.

    Returns:
        bool: True si el código de funcionario es válido y único, False en caso contrario.
    """
    if codigo_funcionario.strip() == "":
        print("El código de funcionario no puede estar vacío.")
        return False
    for admin in sistema.administradores:
        if admin.codigo_funcionario == codigo_funcionario:
            print("El código de funcionario ya existe. Por favor ingrese un código diferente.")
            return False
    return True

def hash_password(password):
    """
    Genera un hash de la contraseña utilizando bcrypt.

    Args:
        password (str): La contraseña a hashear.

    Returns:
        str: El hash de la contraseña.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def obtener_dato_unico(mensaje, validar_funcion, sistema):
    """
    Solicita al usuario ingresar un dato único y lo valida.

    Args:
        mensaje (str): El mensaje a mostrar al usuario.
        validar_funcion (function): La función de validación del dato.
        sistema (Sistema): La instancia del sistema.

    Returns:
        str: El dato válido ingresado por el usuario.
    """
    while True:
        dato = input(mensaje)
        if validar_funcion(dato, sistema):
            return dato
        print(f"El {mensaje.lower().split()[1]} ya existe. Por favor ingrese un {mensaje.lower().split()[1]} diferente.")

def obtener_contraseña():
    """
    Solicita al usuario ingresar una contraseña y la valida.

    Returns:
        str: El hash de la contraseña válida ingresada por el usuario.
    """
    while True:
        contraseña = input("Ingrese contraseña: ")
        if validar_contraseña(contraseña):
            return hash_password(contraseña)
        print("La contraseña debe tener al menos 8 caracteres y contener letras y números. Inténtelo nuevamente.")

def obtener_email(sistema):
    """
    Solicita al usuario ingresar un email y lo valida.

    Args:
        sistema (Sistema): La instancia del sistema.

    Returns:
        str: El email válido ingresado por el usuario.
    """
    while True:
        email = input("Ingrese el email: ")
        if not validar_email_formato(email):
            print("El formato del email es incorrecto. Por favor ingrese un email válido.")
            continue
        if not validar_email_unico(email, sistema):
            print("El email ya existe. Por favor ingrese un email diferente.")
            continue
        return email

def obtener_dni(sistema):
    """
    Solicita al usuario ingresar un DNI y lo valida.

    Args:
        sistema (Sistema): La instancia del sistema.

    Returns:
        str: El DNI válido ingresado por el usuario.
    """
    while True:
        dni = input("Ingrese DNI: ")
        if dni.strip() == "":
            print("El DNI no puede estar vacío. Por favor ingrese un DNI válido.")
            continue
        if not validar_dni(dni, sistema):
            continue
        return dni

def obtener_cuit(sistema):
    """
    Solicita al usuario ingresar un CUIT y lo valida.

    Args:
        sistema (Sistema): La instancia del sistema.

    Returns:
        str: El CUIT válido ingresado por el usuario.
    """
    while True:
        cuit = input("Ingrese CUIT: ")
        if cuit.strip() == "":
            print("El CUIT no puede estar vacío. Por favor ingrese un CUIT válido.")
            continue
        if not validar_cuit_unico(cuit, sistema):
            print("El CUIT ya existe. Por favor ingrese un CUIT diferente.")
            continue
        return cuit

def obtener_nombre():
    """
    Solicita al usuario ingresar un nombre y lo valida.

    Returns:
        str: El nombre válido ingresado por el usuario.
    """
    while True:
        nombre = input("Ingrese nombre: ")
        if validar_nombre(nombre):
            return nombre
        print("El nombre debe tener al menos 5 caracteres, no contener números, solo letras y espacios en blanco, y debe comenzar con una letra. Inténtelo nuevamente.")

def obtener_telefono():
    """
    Solicita al usuario ingresar un teléfono y lo valida.

    Returns:
        str: El teléfono válido ingresado por el usuario.
    """
    while True:
        telefono = input("Ingrese teléfono: ")
        if validar_telefono(telefono):
            return telefono
        print("El teléfono debe contener solo números y tener al menos 7 caracteres. Inténtelo nuevamente.")

def obtener_direccion():
    """
    Solicita al usuario ingresar una dirección y la valida.

    Returns:
        str: La dirección válida ingresada por el usuario.
    """
    while True:
        direccion = input("Ingrese dirección: ")
        if validar_direccion(direccion):
            return direccion
        print("La dirección debe tener al menos 7 caracteres, puede ser combinación de números, espacios en blanco y letras. Inténtelo nuevamente.")

def obtener_nombre_producto(sistema):
    """
    Solicita al usuario ingresar el nombre de un producto y lo valida.

    Args:
        sistema (Sistema): La instancia del sistema.

    Returns:
        str: El nombre del producto válido ingresado por el usuario.
    """
    while True:
        nombre_producto = input("Ingrese el nombre del producto: ").lower()  # Convertir a minúsculas
        if validar_nombre_producto(nombre_producto, sistema):
            return nombre_producto

def obtener_descripcion():
    """
    Solicita al usuario ingresar la descripción de un producto y la valida.

    Returns:
        str: La descripción del producto válida ingresada por el usuario.
    """
    while True:
        descripcion = input("Ingrese la descripción del producto: ")
        if validar_descripcion(descripcion):
            return descripcion

def obtener_categoria():
    """
    Solicita al usuario ingresar la categoría de un producto y la valida.

    Returns:
        str: La categoría del producto válida ingresada por el usuario.
    """
    while True:
        categoria = input("Ingrese la categoría del producto: ")
        if validar_categoria(categoria):
            return categoria

def obtener_precio():
    """
    Solicita al usuario ingresar el precio de un producto y lo valida.

    Returns:
        float: El precio del producto válido ingresado por el usuario.
    """
    while True:
        precio = input("Ingrese el precio del producto: ")
        if validar_precio(precio):
            return float(precio)

def obtener_codigo_funcionario(sistema):
    """
    Solicita al usuario ingresar el código de funcionario y lo valida.

    Args:
        sistema (Sistema): La instancia del sistema.

    Returns:
        str: El código de funcionario válido ingresado por el usuario.
    """
    while True:
        codigo_funcionario = input("Ingrese código funcionario: ")
        if validar_codigo_funcionario(codigo_funcionario, sistema):
            return codigo_funcionario

def agregar_cliente(sistema, tipo_cliente):
    """
    Agrega un cliente al sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
        tipo_cliente (str): El tipo de cliente a agregar ('persona' o 'corporativo').
    """
    email = obtener_email(sistema)
    nombre = obtener_nombre()
    contraseña = obtener_contraseña()
    direccion = obtener_direccion()
    telefono = obtener_telefono()

    if tipo_cliente == 'persona':
        dni = obtener_dni(sistema)
        cliente = ClientePersona(nombre, email, contraseña, direccion, telefono, dni)
        if sistema.agregar_cliente_persona(cliente):
            print("Cliente Persona agregado exitosamente.")
        else:
            print("Error al agregar Cliente Persona.")
    elif tipo_cliente == 'corporativo':
        cuit = obtener_cuit(sistema)
        cliente = ClienteCorporativo(nombre, email, contraseña, direccion, telefono, cuit)
        if sistema.agregar_cliente_corporativo(cliente):
            print("Cliente Corporativo agregado exitosamente.")
        else:
            print("Error al agregar Cliente Corporativo.")

def agregar_cliente_persona(sistema):
    """
    Agrega un ClientePersona al sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    agregar_cliente(sistema, 'persona')

def agregar_cliente_corporativo(sistema):
    """
    Agrega un ClienteCorporativo al sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    agregar_cliente(sistema, 'corporativo')

def agregar_administrador(sistema):
    """
    Agrega un Administrador al sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    email = obtener_email(sistema)
    nombre = obtener_nombre()
    contraseña = obtener_contraseña()
    codigo_funcionario = obtener_codigo_funcionario(sistema)

    admin = Administrador(nombre, email, contraseña, codigo_funcionario)
    if sistema.agregar_administrador(admin):
        print("Administrador agregado exitosamente.")
    else:
        print("Error al agregar Administrador.")

def agregar_producto(sistema):
    """
    Agrega un Producto al sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    nombre_producto = obtener_nombre_producto(sistema)
    descripcion = obtener_descripcion()
    categoria = obtener_categoria()
    precio = obtener_precio()

    producto = Producto(nombre_producto, descripcion, categoria, precio)
    if sistema.agregar_producto(producto):
        print("Producto agregado exitosamente.")
    else:
        print("Error al agregar Producto.")

def mostrar_menu_administradores():
    """
    Muestra el menú principal de administradores.
    """
    print_menu(MENU_OPTIONS)

def mostrar_clientes(sistema):
    """
    Muestra la lista de clientes del sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    sistema.mostrar_clientes()

def mostrar_administradores(sistema):
    """
    Muestra la lista de administradores del sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    sistema.mostrar_administradores()

def mostrar_productos(sistema):
    """
    Muestra la lista de productos del sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    sistema.mostrar_productos()

def eliminar_cliente_persona(sistema):
    """
    Elimina un ClientePersona del sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    email = input("Ingrese el email del cliente persona a eliminar: ")
    if any(cliente.email == email for cliente in sistema.clientes_personas):
        if sistema.eliminar_cliente_persona(email):
            print("Cliente Persona eliminado exitosamente.")
        else:
            print("Error al eliminar Cliente Persona.")
    else:
        print("El cliente persona no existe.")

def eliminar_cliente_corporativo(sistema):
    """
    Elimina un ClienteCorporativo del sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    email = input("Ingrese el email del cliente corporativo a eliminar: ")
    if any(cliente.email == email for cliente in sistema.clientes_corporativos):
        if sistema.eliminar_cliente_corporativo(email):
            print("Cliente Corporativo eliminado exitosamente.")
        else:
            print("Error al eliminar Cliente Corporativo.")
    else:
        print("El cliente corporativo no existe.")

def eliminar_administrador(sistema):
    """
    Elimina un Administrador del sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    email = input("Ingrese el email del administrador a eliminar: ")
    if any(admin.email == email for admin in sistema.administradores):
        if sistema.eliminar_administrador(email):
            print("Administrador eliminado exitosamente.")
        else:
            print("Error al eliminar Administrador.")
    else:
        print("El administrador no existe.")

def eliminar_producto(sistema):
    """
    Elimina un Producto del sistema.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    if not sistema.productos:
        print("No hay productos disponibles para eliminar.")
        return

    sistema.mostrar_productos()
    try:
        id_producto = int(input("Ingrese el ID del producto a eliminar: "))
        if any(producto.id_producto == id_producto for producto in sistema.productos):
            if sistema.eliminar_producto(id_producto):
                print("Producto eliminado exitosamente.")
            else:
                print("Error al eliminar Producto.")
        else:
            print("Producto no encontrado.")
    except ValueError:
        print("ID de producto no válido.")

def ver_historial_compras_todos(sistema):
    """
    Muestra el historial de compras de todos los clientes.

    Args:
        sistema (Sistema): La instancia del sistema.
    """
    compras = sistema.obtener_historial_compras_todos()
    if compras:
        print("Historial de Compras de Todos los Clientes:")
        table = []
        for compra in compras:
            productos_str = ", ".join([f"{prod['producto'].nombre} x{prod['cantidad']}" for prod in compra.productos])
            precio_total = sum([prod['producto'].precio * prod['cantidad'] for prod in compra.productos])
            table.append([compra.cliente.nombre, compra.cliente.email, productos_str, precio_total, compra.fecha.strftime('%Y-%m-%d %H:%M:%S')])
        print(tabulate(table, headers=["Cliente", "Email", "Productos", "Precio Total", "Fecha de Compra"], tablefmt="pretty"))
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
