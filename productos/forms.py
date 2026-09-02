from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'categoria',
            'precio',
            'cantidad_stock',
            'proveedor',
            'estado',
        ]

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio < 0:
            raise forms.ValidationError('El precio no puede ser negativo.')
        return precio

    def clean_cantidad_stock(self):
        cantidad = self.cleaned_data.get('cantidad_stock')
        if cantidad is not None and cantidad < 0:
            raise forms.ValidationError('La cantidad en stock no puede ser negativa.')
        return cantidad
