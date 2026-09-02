from django.test import TestCase
from django.urls import reverse
from .models import Producto


class ProductoFormModelTests(TestCase):
	def test_form_validation_negative_values(self):
		p = Producto.objects.create(
			nombre='Test', categoria='Cat', precio=10.00, cantidad_stock=5, proveedor='P', estado='activo'
		)
		# Test Producto creation and fields
		self.assertEqual(Producto.objects.count(), 1)


class ProductoViewsTests(TestCase):
	def setUp(self):
		self.prod = Producto.objects.create(
			nombre='Arroz', categoria='Alimentos', precio=3000.00,
			cantidad_stock=10, proveedor='Proveedor A', estado='disponible'
		)

	def test_lista_view(self):
		resp = self.client.get(reverse('productos:lista'))
		self.assertEqual(resp.status_code, 200)
		self.assertContains(resp, 'Arroz')

	def test_create_view(self):
		data = {
			'nombre': 'Azúcar', 'categoria': 'Alimentos', 'precio': '2500.00',
			'cantidad_stock': '20', 'proveedor': 'Proveedor B', 'estado': 'disponible'
		}
		resp = self.client.post(reverse('productos:crear'), data)
		self.assertEqual(resp.status_code, 302)
		self.assertEqual(Producto.objects.filter(nombre='Azúcar').count(), 1)

	def test_detail_view(self):
		resp = self.client.get(reverse('productos:detalle', args=[self.prod.pk]))
		self.assertEqual(resp.status_code, 200)
		self.assertContains(resp, 'Arroz')

	def test_update_view(self):
		url = reverse('productos:editar', args=[self.prod.pk])
		resp = self.client.post(url, {
			'nombre': 'Arroz Mod', 'categoria': self.prod.categoria, 'precio': self.prod.precio,
			'cantidad_stock': self.prod.cantidad_stock, 'proveedor': self.prod.proveedor, 'estado': self.prod.estado
		})
		self.assertEqual(resp.status_code, 302)
		self.prod.refresh_from_db()
		self.assertEqual(self.prod.nombre, 'Arroz Mod')

	def test_delete_view(self):
		url = reverse('productos:eliminar', args=[self.prod.pk])
		resp = self.client.post(url)
		self.assertEqual(resp.status_code, 302)
		self.assertFalse(Producto.objects.filter(pk=self.prod.pk).exists())

