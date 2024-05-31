class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f'{self.nombre}, Email: {self.email}'


class Cliente(Persona):
    def __init__(self, nombre, email, direccion, telefono):
        super().__init__(nombre, email)
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f'{super().__str__()}, Dirección: {self.direccion}, Teléfono: {self.telefono}'


class ClientePersona(Cliente):
    def __init__(self, nombre, email, direccion, telefono, dni):
        super().__init__(nombre, direccion, telefono, email)
        self.dni = dni

    def __str__(self):
        return f'{super().__str__()}, DNI: {self.dni}'


class ClienteCorporativo(Cliente):
    def __init__(self, nombre, email, direccion, telefono, cuit):
        super().__init__(nombre, direccion, telefono, email)
        self.cuit = cuit

    def __str__(self):
        return f'{super().__str__()}, CUIT: {self.cuit}'


class Administrador(Persona):
    def __init__(self, nombre, email, codigo_funcionario):
        super().__init__(nombre, email)
        self.nombre = nombre
        self.email = email
        self.codigo_funcionario = codigo_funcionario

    def __str__(self):
        return f'{super().__str__()}, Funcionario n°: {self.codigo_funcionario}'


class Sistema:
    def __init__(self):
        self.clientes_personas = []
        self.clientes_corporativos = []
        self.administradores = []

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


def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Operaciones de Clientes")
    print("2. Operaciones de Administradores")
    print("3. Salir")


def mostrar_menu_clientes():
    print("\nSeleccione una operación de clientes:")
    print("1. Agregar Cliente Persona")
    print("2. Agregar Cliente Corporativo")
    print("3. Mostrar Clientes")
    print("4. Regresar al menú principal")


def mostrar_menu_administradores():
    print("\nSeleccione una operación de administradores:")
    print("1. Agregar Administrador")
    print("2. Mostrar Administradores")
    print("3. Regresar al menú principal")


def operaciones_clientes(sistema):
    while True:
        mostrar_menu_clientes()
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            email = input("Ingrese el email: ")
            direccion = input("Ingrese la dirección: ")
            telefono = input("Ingrese el teléfono: ")
            dni = input("Ingrese el DNI: ")
            cliente = ClientePersona(nombre, email, direccion, telefono, dni)
            sistema.agregar_cliente_persona(cliente)
            print("Cliente Persona agregado exitosamente.")
        elif opcion == "2":
            nombre = input("Ingrese el nombre: ")
            email = input("Ingrese el email: ")
            direccion = input("Ingrese la dirección: ")
            telefono = input("Ingrese el teléfono: ")
            cuit = input("Ingrese el CUIT: ")
            cliente = ClienteCorporativo(nombre, email, direccion, telefono, cuit)
            sistema.agregar_cliente_corporativo(cliente)
            print("Cliente Corporativo agregado exitosamente.")
        elif opcion == "3":
            sistema.mostrar_clientes()
        elif opcion == "4":
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
            codigo_funcionario = input("Ingrese el código de funcionario: ")
            admin = Administrador(nombre, email, codigo_funcionario)
            sistema.agregar_administrador(admin)
            print("Administrador agregado exitosamente.")
        elif opcion == "2":
            sistema.mostrar_administradores()
        elif opcion == "3":
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
