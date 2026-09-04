from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.lista_productos, name='lista'),
    path('productos/crear/', views.crear_producto, name='crear'),
    path('productos/<int:pk>/', views.detalle_producto, name='detalle'),
    path('productos/<int:pk>/editar/', views.editar_producto, name='editar'),
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar'),
]