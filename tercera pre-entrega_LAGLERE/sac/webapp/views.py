# webapp/views.py

from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import ProductoForm, ClienteForm, EmpleadoForm, CompraForm
from .models import Producto, Cliente, Empleado, Compra


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'webapp/lista_productos.html', {'productos': productos})


def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'webapp/lista_clientes.html', {'clientes': clientes})


def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'webapp/lista_empleados.html', {'empleados': empleados})


def lista_compras(request):
    compras = Compra.objects.all()
    return render(request, 'webapp/lista_compras.html', {'compras': compras})


def inicio(request):
    return render(request, 'webapp/inicio.html')


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'webapp/agregar_producto.html', {'form': form})


def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ClienteForm()
    return render(request, 'webapp/agregar_cliente.html', {'form': form})


def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EmpleadoForm()
    return render(request, 'webapp/agregar_empleado.html', {'form': form})


def agregar_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CompraForm()
    return render(request, 'webapp/agregar_compra.html', {'form': form})


def buscar(request):
    query = request.GET.get('query')
    productos = Producto.objects.filter(nombre__iexact=query)
    clientes = Cliente.objects.filter(nombre__iexact=query)
    empleados = Empleado.objects.filter(nombre__iexact=query)
    compras = Compra.objects.filter(Q(cliente__nombre__iexact=query) | Q(producto__nombre__iexact=query))
    context = {
        'productos': productos,
        'clientes': clientes,
        'empleados': empleados,
        'compras': compras,
        'query': query
    }
    return render(request, 'webapp/resultados_busqueda.html', context)
