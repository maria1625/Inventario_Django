from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_stock = models.PositiveIntegerField()
    proveedor = models.CharField(max_length=100)
    estado = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
