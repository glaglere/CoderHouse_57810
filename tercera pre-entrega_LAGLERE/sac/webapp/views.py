# webapp/views.py

from django.shortcuts import render, redirect
from .forms import ProductoForm, ClienteForm, EmpleadoForm, CompraForm
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'webapp/lista_productos.html', {'productos': productos})

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
