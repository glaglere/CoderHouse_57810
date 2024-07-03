# Gloria - Sistema de Gestión de Compras

## Descripción General

Gloria es un sistema de gestión de compras diseñado para facilitar la administración de productos, clientes, empleados y compras en una organización. 
Este sistema web está desarrollado utilizando Django y proporciona una interfaz amigable para realizar diversas operaciones relacionadas con la gestión de inventarios y personal.

## Autor

Ginette Laglere

## Repositorio

https://github.com/glaglere/CoderHouse_57810.git

## Ubicacion
Como se pide en la letra, todo lo de la tercer pre entrega se encuentra en:
```
\tercera pre-entrega_LAGLERE
```
## Funcionalidades

### Página de Inicio

- **URL:** `/`
- **Descripción:** Página de bienvenida que ofrece enlaces a las diferentes secciones de la aplicación. Muestra una introducción al sistema Gloria y proporciona accesos directos a las funcionalidades principales.
- **Archivo HTML:** `inicio.html`

### Gestión de Productos

- **Lista de Productos**
  - **URL:** `/productos/`
  - **Descripción:** Muestra una lista de todos los productos disponibles en el inventario.
  - **Archivo HTML:** `lista_productos.html`

- **Agregar Producto**
  - **URL:** `/agregar_producto/`
  - **Descripción:** Permite agregar nuevos productos al inventario mediante un formulario.
  - **Archivo HTML:** `agregar_producto.html`

### Gestión de Clientes

- **Lista de Clientes**
  - **URL:** `/clientes/`
  - **Descripción:** Muestra una lista de todos los clientes registrados en el sistema.
  - **Archivo HTML:** `lista_clientes.html`

- **Agregar Cliente**
  - **URL:** `/agregar_cliente/`
  - **Descripción:** Permite registrar nuevos clientes mediante un formulario.
  - **Archivo HTML:** `agregar_cliente.html`

### Gestión de Empleados

- **Lista de Empleados**
  - **URL:** `/empleados/`
  - **Descripción:** Muestra una lista de todos los empleados registrados en el sistema.
  - **Archivo HTML:** `lista_empleados.html`

- **Agregar Empleado**
  - **URL:** `/agregar_empleado/`
  - **Descripción:** Permite registrar nuevos empleados mediante un formulario.
  - **Archivo HTML:** `agregar_empleado.html`

### Gestión de Compras

- **Lista de Compras**
  - **URL:** `/compras/`
  - **Descripción:** Muestra una lista de todas las compras realizadas.
  - **Archivo HTML:** `lista_compras.html`

- **Agregar Compra**
  - **URL:** `/agregar_compra/`
  - **Descripción:** Permite registrar nuevas compras mediante un formulario. Se puede seleccionar el cliente y el producto para la compra.
  - **Archivo HTML:** `agregar_compra.html`

### Búsqueda

- **URL:** `/buscar/`
  - **Descripción:** Permite buscar productos, clientes, empleados y compras en el sistema utilizando palabras clave.
  - **Archivo HTML:** `resultados_busqueda.html`

## Archivos Importantes

- `base.html`: Plantilla base que define la estructura general de las páginas web.
- `views.py`: Contiene las vistas de Django que manejan la lógica del servidor y renderizan las plantillas HTML.
- `models.py`: Define los modelos de datos para Producto, Cliente, Empleado y Compra.
- `forms.py`: Define los formularios utilizados para agregar o editar productos, clientes, empleados y compras.
- `urls.py`: Mapea las URLs a las vistas correspondientes.

## Instalación

1. Clonar el repositorio.
2. Crear un entorno virtual y activarlo.
3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt


## Licencia

Este proyecto está bajo la licencia MIT. Vea el archivo `LICENSE` para más detalles.
