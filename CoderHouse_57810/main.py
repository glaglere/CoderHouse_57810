class Persona:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password

    def __str__(self):
        return f'{self.nombre}, Email: {self.email}'


class Cliente(Persona):
    def __init__(self, nombre, email, password, direccion, telefono):
        super().__init__(nombre, email, password)
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f'{super().__str__()}, Dirección: {self.direccion}, Teléfono: {self.telefono}'


class ClientePersona(Cliente):
    def __init__(self, nombre, email, password, direccion, telefono, dni):
        super().__init__(nombre, email, password, direccion, telefono)
        self.dni = dni

    def __str__(self):
        return f'{super().__str__()}, DNI: {self.dni}'


class ClienteCorporativo(Cliente):
    def __init__(self, nombre, email, password, direccion, telefono, cuit):
        super().__init__(nombre, email, password, direccion, telefono)
        self.cuit = cuit

    def __str__(self):
        return f'{super().__str__()}, CUIT: {self.cuit}'


class Administrador(Persona):
    def __init__(self, nombre, email, password, codigo_funcionario):
        super().__init__(nombre, email, password)
        self.codigo_funcionario = codigo_funcionario

    def __str__(self):
        return f'{super().__str__()}, Funcionario n°: {self.codigo_funcionario}'


class Producto:
    def __init__(self, id_producto, nombre, descripcion, categoria, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria
        self.precio = precio

    def __str__(self):
        return f'ID: {self.id_producto}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Categoría: {self.categoria}, Precio: {self.precio}'


class Sistema:
    def __init__(self):
        self.clientes_personas = []
        self.clientes_corporativos = []
        self.administradores = []
        self.productos = []

    def agregar_cliente_persona(self, cliente):
        if isinstance(cliente, ClientePersona):
            self.clientes_personas.append(cliente)
        else:
            raise TypeError("El cliente debe ser una instancia de ClientePersona")

    def agregar_cliente_corporativo(self, cliente):
        if isinstance(cliente, ClienteCorporativo):
            self.clientes_corporativos.append(cliente)
        else:
            raise TypeError("El cliente debe ser una instancia de ClienteCorporativo")

    def agregar_administrador(self, administrador):
        if isinstance(administrador, Administrador):
            self.administradores.append(administrador)
        else:
            raise TypeError("El administrador debe ser una instancia de Administrador")

    def agregar_producto(self, producto):
        if isinstance(producto, Producto):
            self.productos.append(producto)
        else:
            raise TypeError("El producto debe ser una instancia de Producto")

    def mostrar_clientes(self):
        print("Clientes Personas:")
        for cliente in self.clientes_personas:
            print(cliente)
        print("\nClientes Corporativos:")
        for cliente in self.clientes_corporativos:
            print(cliente)

    def mostrar_administradores(self):
        print("Administradores:")
        for admin in self.administradores:
            print(admin)

    def mostrar_productos(self):
        print("Productos:")
        for producto in self.productos:
            print(producto)

    def eliminar_cliente_persona(self, email):
        self.clientes_personas = [c for c in self.clientes_personas if c.email != email]

    def eliminar_cliente_corporativo(self, email):
        self.clientes_corporativos = [c for c in self.clientes_corporativos if c.email != email]

    def eliminar_administrador(self, email):
        self.administradores = [a for a in self.administradores if a.email != email]

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.id_producto != id_producto]


def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Operaciones de Clientes")
    print("2. Operaciones de Administradores")
    print("3. Salir")


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


def mostrar_menu_clientes():
    print("\nSeleccione una operación de clientes:")
    print("1. Loguearse")
    print("2. Regresar al menú principal")


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
            else:
                print("Credenciales incorrectas.")
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


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


if __name__ == '__main__':

    # Creación del sistema
    sistema_principal = Sistema()

    # Bucle principal del programa
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            operaciones_clientes(sistema_principal)
        elif opcion == "2":
            operaciones_administradores(sistema_principal)
        elif opcion == "3":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
