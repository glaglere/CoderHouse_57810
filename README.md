# Sistema de Gestión de Clientes, Administradores y Compras

Este sistema está diseñado para gestionar clientes (tanto personas como corporativos), administradores, productos y compras. Permite realizar operaciones como agregar clientes, administradores, productos, gestionar carritos de compras y concretar compras.

## Autor

Ginette Laglere

## Repositorio

https://github.com/glaglere/CoderHouse_57810.git

## Funcionalidades

### 1. Gestión de Clientes

El sistema permite agregar, eliminar y mostrar clientes. Los clientes pueden ser personas o corporativos.

#### Clientes Persona

- **Agregar Cliente Persona**: Permite agregar un nuevo cliente persona con atributos como nombre, email, contraseña, dirección, teléfono y DNI.
- **Eliminar Cliente Persona**: Permite eliminar un cliente persona existente.
- **Mostrar Clientes Persona**: Muestra la lista de todos los clientes persona registrados.

#### Clientes Corporativo

- **Agregar Cliente Corporativo**: Permite agregar un nuevo cliente corporativo con atributos como nombre, email, contraseña, dirección, teléfono y CUIT.
- **Eliminar Cliente Corporativo**: Permite eliminar un cliente corporativo existente.
- **Mostrar Clientes Corporativos**: Muestra la lista de todos los clientes corporativos registrados.

### 2. Gestión de Administradores

El sistema permite agregar, eliminar y mostrar administradores.

- **Agregar Administrador**: Permite agregar un nuevo administrador con atributos como nombre, email, contraseña y código de funcionario.
- **Eliminar Administrador**: Permite eliminar un administrador existente.
- **Mostrar Administradores**: Muestra la lista de todos los administradores registrados.

### 3. Gestión de Productos

El sistema permite agregar, eliminar y mostrar productos.

- **Agregar Producto**: Permite agregar un nuevo producto con atributos como nombre, descripción, categoría y precio.
- **Eliminar Producto**: Permite eliminar un producto existente.
- **Mostrar Productos**: Muestra la lista de todos los productos registrados.

### 4. Gestión de Carrito y Compras

Los clientes pueden gestionar su carrito de compras y concretar compras.

- **Agregar Producto al Carrito**: Permite a un cliente agregar productos a su carrito.
- **Mostrar Carrito**: Permite a un cliente ver los productos en su carrito.
- **Quitar Producto del Carrito**: Permite a un cliente quitar productos de su carrito.
- **Concretar Compra**: Permite a un cliente concretar la compra de los productos en su carrito.
- **Ver Historial de Compras**: Permite a un cliente visualizar su historial de compras.

### 5. Listado de Productos

Los clientes pueden listar productos disponibles en el sistema.

- **Listar Todos los Productos**: Muestra la lista de todos los productos disponibles en el sistema.
- **Listar Productos por Categoría**: Permite a un cliente listar productos según una categoría específica.

### 6. Funcionalidades Adicionales para Administradores

Los administradores tienen la capacidad de visualizar el historial de compras de todos los clientes.

- **Ver Historial de Compras de Todos los Clientes**: Permite a un administrador visualizar el historial de compras de todos los clientes registrados en el sistema.

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

## Estructura del Proyecto

El proyecto está organizado en los siguientes módulos:

- **models**: Contiene las clases que representan los modelos principales del sistema (Persona, ClientePersona, ClienteCorporativo, Administrador, Producto, Compra).
- **services**: Contiene el núcleo del sistema que maneja la lógica de negocio (Sistema) y las ayudas para la interacción con el usuario (helpers).
- **administrador_menu.py**: Contiene las operaciones disponibles para los administradores.
- **cliente_menu.py**: Contiene las operaciones disponibles para los clientes.
- **main.py**: El punto de entrada del sistema que maneja el flujo principal del programa.

## Ejecución del Sistema

Para ejecutar el sistema, se debe ejecutar el archivo `main.py`. Esto mostrará el menú principal desde donde se pueden acceder a las operaciones de clientes y administradores.

```bash
python main.py
```

## Bibliotecas de Terceros Utilizadas
- **tabulate**: Se utiliza para imprimir tablas de manera legible en la terminal. Esta biblioteca facilita la visualización de datos tabulares, lo que mejora la experiencia del usuario al interactuar con el sistema.
