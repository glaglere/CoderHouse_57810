from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import ProductoForm, ClienteForm, EmpleadoForm, CompraForm
from .models import Producto, Cliente, Empleado, Compra


def lista_productos(request):
    """
    Vista para listar todos los productos.
    """
    productos = Producto.objects.all()
    return render(request, 'webapp/lista_productos.html', {'productos': productos})


def lista_clientes(request):
    """
    Vista para listar todos los clientes.
    """
    clientes = Cliente.objects.all()
    return render(request, 'webapp/lista_clientes.html', {'clientes': clientes})


def lista_empleados(request):
    """
    Vista para listar todos los empleados.
    """
    empleados = Empleado.objects.all()
    return render(request, 'webapp/lista_empleados.html', {'empleados': empleados})


def lista_compras(request):
    """
    Vista para listar todas las compras.
    """
    compras = Compra.objects.all()
    return render(request, 'webapp/lista_compras.html', {'compras': compras})


def inicio(request):
    """
    Vista para la página de inicio.
    """
    return render(request, 'webapp/inicio.html')


def agregar_producto(request):
    """
    Vista para agregar un nuevo producto.
    """
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'webapp/agregar_producto.html', {'form': form})


def agregar_cliente(request):
    """
    Vista para agregar un nuevo cliente.
    """
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ClienteForm()
    return render(request, 'webapp/agregar_cliente.html', {'form': form})


def agregar_empleado(request):
    """
    Vista para agregar un nuevo empleado.
    """
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EmpleadoForm()
    return render(request, 'webapp/agregar_empleado.html', {'form': form})


def agregar_compra(request):
    """
    Vista para agregar una nueva compra.
    """
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CompraForm()

    # Obtener todos los clientes para mostrar en el combo box
    clientes = Cliente.objects.all()
    return render(request, 'webapp/agregar_compra.html', {'form': form, 'clientes': clientes})


def buscar(request):
    """
    Vista para realizar una búsqueda en productos, clientes, empleados y compras.
    """
    query = request.GET.get('query')
    productos = Producto.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query))

    search_terms = query.split()
    if len(search_terms) == 2:
        nombre, apellido = search_terms
        clientes = Cliente.objects.filter(Q(nombre__icontains=nombre) & Q(apellido__icontains=apellido))
    else:
        clientes = Cliente.objects.filter(Q(nombre__icontains=query) | Q(apellido__icontains=query))

    empleados = Empleado.objects.filter(Q(nombre__icontains=query))

    compras = Compra.objects.filter(
        Q(cliente__nombre__icontains=query) |
        Q(cliente__apellido__icontains=query) |
        Q(producto__nombre__icontains=query) |
        Q(fecha__icontains=query)
    )

    context = {
        'productos': productos,
        'clientes': clientes,
        'empleados': empleados,
        'compras': compras,
        'query': query
    }
    return render(request, 'webapp/resultados_busqueda.html', context)
