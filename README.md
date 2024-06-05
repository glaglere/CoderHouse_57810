
# Sistema de Gestión de Clientes, Administradores y Compras

Este sistema está diseñado para gestionar clientes (tanto personas como corporativos), administradores, productos y compras. Permite realizar operaciones como agregar clientes, administradores, productos, gestionar carritos de compras y concretar compras.

## Autor

Ginette Laglere

## Repositorio

https://github.com/glaglere/CoderHouse_57810.git

## Funcionalidades

### Operaciones de Clientes

1. **Registrar Cliente Persona**: Permite registrar un cliente persona solicitando los datos personales y validando la unicidad del DNI.
2. **Registrar Cliente Corporativo**: Permite registrar un cliente corporativo solicitando los datos corporativos y validando la unicidad del CUIT.
3. **Loguearse**: Permite a un cliente loguearse en el sistema con su correo electrónico y contraseña.
4. **Agregar Producto al Carrito**: Permite agregar productos al carrito de compras del cliente logueado.
5. **Mostrar Carrito**: Muestra el contenido del carrito del cliente logueado.
6. **Quitar Producto del Carrito**: Permite quitar productos del carrito del cliente logueado.
7. **Concretar Compra**: Permite concretar la compra de los productos en el carrito del cliente logueado.
8. **Ver Historial de Compras**: Muestra el historial de compras del cliente logueado.
9. **Listar Todos los Productos**: Muestra una lista de todos los productos disponibles en el sistema.
10. **Listar Productos por Categoría**: Permite listar los productos disponibles por categoría.

### Operaciones de Administradores

1. **Agregar Cliente Persona**: Permite a un administrador agregar un cliente persona al sistema.
2. **Agregar Cliente Corporativo**: Permite a un administrador agregar un cliente corporativo al sistema.
3. **Agregar Administrador**: Permite a un administrador agregar otro administrador al sistema.
4. **Agregar Producto**: Permite a un administrador agregar un nuevo producto al sistema.
5. **Mostrar Clientes**: Muestra la lista de todos los clientes (personas y corporativos) registrados en el sistema.
6. **Mostrar Administradores**: Muestra la lista de todos los administradores registrados en el sistema.
7. **Mostrar Productos**: Muestra la lista de todos los productos disponibles en el sistema.
8. **Eliminar Cliente Persona**: Permite eliminar un cliente persona del sistema.
9. **Eliminar Cliente Corporativo**: Permite eliminar un cliente corporativo del sistema.
10. **Eliminar Administrador**: Permite eliminar un administrador del sistema.
11. **Eliminar Producto**: Permite eliminar un producto del sistema.
12. **Ver Historial de Compras de Todos los Clientes**: Muestra el historial de compras de todos los clientes registrados en el sistema.

### Validaciones

1. **Validar Email**: Verifica que el formato del email sea correcto.
2. **Validar Contraseña**: Verifica que la contraseña tenga al menos 8 caracteres y contenga letras y números.
3. **Validar Nombre de Usuario**: Verifica que el nombre de usuario no tenga números, contenga solo letras y espacios en blanco, y comience con una letra.
4. **Validar DNI**: Verifica que el DNI contenga solo números y sea único en el sistema.
5. **Validar Teléfono**: Verifica que el teléfono contenga solo números y tenga al menos 7 caracteres.
6. **Validar No Vacío**: Verifica que un campo no esté vacío.

### Helpers

1. **Collect Input**: Recoge la entrada del usuario para una lista de campos especificados.
2. **Print Menu**: Muestra un menú con opciones utilizando la biblioteca `tabulate`.
3. **Get Option**: Solicita al usuario que seleccione una opción del menú.

## Persistencia

Los datos se guardan y cargan automáticamente desde los siguientes archivos JSON:
- `personas.json`
- `productos.json`
- `compras.json`

## Estructura del Proyecto

El proyecto está organizado en los siguientes módulos:

- **models**: Contiene las clases que representan los modelos principales del sistema (Persona, ClientePersona, ClienteCorporativo, Administrador, Producto, Compra).
- **services**: Contiene el núcleo del sistema que maneja la lógica de negocio (Sistema) y las ayudas para la interacción con el usuario (helpers).
- **administrador_menu.py**: Contiene las operaciones disponibles para los administradores.
- **cliente_menu.py**: Contiene las operaciones disponibles para los clientes.
- **main.py**: El punto de entrada del sistema que maneja el flujo principal del programa.


## Instalación

### Instalación desde el paquete `.tar.gz`

Para instalar el paquete desde el archivo `.tar.gz`, siga los siguientes pasos:

1. Descargue el archivo `57810_segunda_pre_entrega_laglere.tar.gz` a su máquina local.
2. Ejecute el siguiente comando en su terminal:

```bash
pip install 57810_segunda_pre_entrega_laglere.tar.gz
```

### Instalación desde el paquete `.whl`

Para instalar el paquete desde el archivo `.whl`, siga los siguientes pasos:

1. Descargue el archivo `57810_segunda_pre_entrega_laglere.whl` a su máquina local.
2. Ejecute el siguiente comando en su terminal:

```bash
pip install 57810_segunda_pre_entrega_laglere.whl
```

### Requisitos

Asegúrese de tener instaladas las siguientes dependencias:

- bcrypt==4.1.3
- setuptools==70.0.0
- tabulate==0.9.0
- wheel==0.43.0
- windows-curses==2.3.3

Puede instalar las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

## Ejecución del Sistema

Para ejecutar el sistema, se debe ejecutar el archivo `main.py`. Esto mostrará el menú principal desde donde se pueden acceder a las operaciones de clientes y administradores.

```bash
python main.py
```

## Bibliotecas de Terceros Utilizadas
- **tabulate**: Se utiliza para imprimir tablas de manera legible en la terminal. Esta biblioteca facilita la visualización de datos tabulares, lo que mejora la experiencia del usuario al interactuar con el sistema.

## Datos Generados

### Clientes

Se han generado los siguientes clientes:

#### Clientes Persona

1. Lorenzo Lopez
2. Ana González
3. Carlos Pérez
4. Beatriz Diaz
5. Daniela Ruiz
6. Pedro Fernández

#### Clientes Corporativos

1. Corp Tech
2. Global Solutions
3. Innovative Ideas
4. Tech Innovators
5. Future Enterprises

#### Administradores

1. Admin User
2. Super Admin
3. Manager Admin

### Compras

Cada cliente ha realizado 2 compras, registrando la fecha de la compra y generando un número de ticket aleatorio para cada compra.



## Licencia

Este proyecto está bajo la licencia MIT. Vea el archivo `LICENSE` para más detalles.
