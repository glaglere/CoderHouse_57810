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
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def validar_email_unico(email, sistema):
    for cliente in sistema.clientes_personas + sistema.clientes_corporativos + sistema.administradores:
        if cliente.email == email:
            return False
    return True

def validar_dni(dni, sistema):
    if len(dni) < 7 or not dni.isdigit():
        print("El DNI debe tener al menos 7 dígitos y contener solo números.")
        return False
    for cliente in sistema.clientes_personas:
        if cliente.dni == dni:
            print("El DNI ya existe. Por favor ingrese un DNI diferente.")
            return False
    return True

def validar_cuit_unico(cuit, sistema):
    for cliente in sistema.clientes_corporativos:
        if cliente.cuit == cuit:
            return False
    return True

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False
    if not any(char.isdigit() for char in contraseña):
        return False
    if not any(char.isalpha() for char in contraseña):
        return False
    return True

def validar_nombre(nombre):
    if len(nombre) < 5 or not nombre.replace(" ", "").isalpha() or not nombre[0].isalpha():
        return False
    return True

def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) >= 7

def validar_direccion(direccion):
    if len(direccion) < 7:
        return False
    return True

def validar_nombre_producto(nombre_producto, sistema):
    if nombre_producto.strip() == "":
        print("El nombre del producto no puede estar vacío.")
        return False
    for producto in sistema.productos:
        if producto.nombre == nombre_producto:
            print("El producto ya existe. Por favor ingrese un nombre de producto diferente.")
            return False
    return True

def validar_descripcion(descripcion):
    if descripcion.strip() == "":
        print("La descripción del producto no puede estar vacía.")
        return False
    return True

def validar_categoria(categoria):
    if categoria.strip() == "":
        print("La categoría del producto no puede estar vacía.")
        return False
    return True

def validar_precio(precio):
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
    if codigo_funcionario.strip() == "":
        print("El código de funcionario no puede estar vacío.")
        return False
    for admin in sistema.administradores:
        if admin.codigo_funcionario == codigo_funcionario:
            print("El código de funcionario ya existe. Por favor ingrese un código diferente.")
            return False
    return True

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def obtener_dato_unico(mensaje, validar_funcion, sistema):
    while True:
        dato = input(mensaje)
        if validar_funcion(dato, sistema):
            return dato
        print(f"El {mensaje.lower().split()[1]} ya existe. Por favor ingrese un {mensaje.lower().split()[1]} diferente.")

def obtener_contraseña():
    while True:
        contraseña = input("Ingrese contraseña: ")
        if validar_contraseña(contraseña):
            return hash_password(contraseña)
        print("La contraseña debe tener al menos 8 caracteres y contener letras y números. Inténtelo nuevamente.")

def obtener_email(sistema):
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
    while True:
        dni = input("Ingrese DNI: ")
        if dni.strip() == "":
            print("El DNI no puede estar vacío. Por favor ingrese un DNI válido.")
            continue
        if not validar_dni(dni, sistema):
            continue
        return dni

def obtener_cuit(sistema):
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
    while True:
        nombre = input("Ingrese nombre: ")
        if validar_nombre(nombre):
            return nombre
        print("El nombre debe tener al menos 5 caracteres, no contener números, solo letras y espacios en blanco, y debe comenzar con una letra. Inténtelo nuevamente.")

def obtener_telefono():
    while True:
        telefono = input("Ingrese teléfono: ")
        if validar_telefono(telefono):
            return telefono
        print("El teléfono debe contener solo números y tener al menos 7 caracteres. Inténtelo nuevamente.")

def obtener_direccion():
    while True:
        direccion = input("Ingrese dirección: ")
        if validar_direccion(direccion):
            return direccion
        print("La dirección debe tener al menos 7 caracteres, puede ser combinación de números, espacios en blanco y letras. Inténtelo nuevamente.")

def obtener_nombre_producto(sistema):
    while True:
        nombre_producto = input("Ingrese el nombre del producto: ").lower()  # Convertir a minúsculas
        if validar_nombre_producto(nombre_producto, sistema):
            return nombre_producto

def obtener_descripcion():
    while True:
        descripcion = input("Ingrese la descripción del producto: ")
        if validar_descripcion(descripcion):
            return descripcion

def obtener_categoria():
    while True:
        categoria = input("Ingrese la categoría del producto: ")
        if validar_categoria(categoria):
            return categoria

def obtener_precio():
    while True:
        precio = input("Ingrese el precio del producto: ")
        if validar_precio(precio):
            return float(precio)

def obtener_codigo_funcionario(sistema):
    while True:
        codigo_funcionario = input("Ingrese código funcionario: ")
        if validar_codigo_funcionario(codigo_funcionario, sistema):
            return codigo_funcionario

def agregar_cliente(sistema, tipo_cliente):
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
    agregar_cliente(sistema, 'persona')

def agregar_cliente_corporativo(sistema):
    agregar_cliente(sistema, 'corporativo')

def agregar_administrador(sistema):
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
    print_menu(MENU_OPTIONS)

def mostrar_clientes(sistema):
    sistema.mostrar_clientes()

def mostrar_administradores(sistema):
    sistema.mostrar_administradores()

def mostrar_productos(sistema):
    sistema.mostrar_productos()

def eliminar_cliente_persona(sistema):
    email = input("Ingrese el email del cliente persona a eliminar: ")
    if any(cliente.email == email for cliente in sistema.clientes_personas):
        if sistema.eliminar_cliente_persona(email):
            print("Cliente Persona eliminado exitosamente.")
        else:
            print("Error al eliminar Cliente Persona.")
    else:
        print("El cliente persona no existe.")

def eliminar_cliente_corporativo(sistema):
    email = input("Ingrese el email del cliente corporativo a eliminar: ")
    if any(cliente.email == email for cliente in sistema.clientes_corporativos):
        if sistema.eliminar_cliente_corporativo(email):
            print("Cliente Corporativo eliminado exitosamente.")
        else:
            print("Error al eliminar Cliente Corporativo.")
    else:
        print("El cliente corporativo no existe.")

def eliminar_administrador(sistema):
    email = input("Ingrese el email del administrador a eliminar: ")
    if any(admin.email == email for admin in sistema.administradores):
        if sistema.eliminar_administrador(email):
            print("Administrador eliminado exitosamente.")
        else:
            print("Error al eliminar Administrador.")
    else:
        print("El administrador no existe.")

def eliminar_producto(sistema):
    if not sistema.productos:
        print("No hay productos disponibles para eliminar.")
        return

    sistema.mostrar_productos()
    try:
        id_producto = int(input("Ingrese el ID del producto a eliminar: "))
        if sistema.eliminar_producto(id_producto):
            print("Producto eliminado exitosamente.")
        else:
            print("Error al eliminar Producto. Asegúrese de que el ID es correcto.")
    except ValueError:
        print("ID de producto no válido.")

def ver_historial_compras_todos(sistema):
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
