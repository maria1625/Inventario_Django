from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm


def inicio(request):
	return render(request, 'productos/inicio.html')


def producto_list(request):
	productos = Producto.objects.all()
	return render(request, 'productos/lista.html', {'productos': productos})


def producto_detail(request, pk):
	producto = get_object_or_404(Producto, pk=pk)
	return render(request, 'productos/detalle.html', {'producto': producto})


def producto_create(request):
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('productos:lista')
	else:
		form = ProductoForm()
	return render(request, 'productos/formulario.html', {'form': form, 'accion': 'Crear'})


def producto_update(request, pk):
	producto = get_object_or_404(Producto, pk=pk)
	if request.method == 'POST':
		form = ProductoForm(request.POST, instance=producto)
		if form.is_valid():
			form.save()
			return redirect('productos:detalle', pk=producto.pk)
	else:
		form = ProductoForm(instance=producto)
	return render(request, 'productos/formulario.html', {'form': form, 'accion': 'Editar'})


def producto_delete(request, pk):
	producto = get_object_or_404(Producto, pk=pk)
	if request.method == 'POST':
		producto.delete()
		return redirect('productos:lista')
	return render(request, 'productos/eliminar.html', {'producto': producto})
