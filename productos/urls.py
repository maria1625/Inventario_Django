from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.producto_list, name='lista'),
    path('productos/crear/', views.producto_create, name='crear'),
    path('productos/<int:pk>/', views.producto_detail, name='detalle'),
    path('productos/<int:pk>/editar/', views.producto_update, name='editar'),
    path('productos/<int:pk>/eliminar/', views.producto_delete, name='eliminar'),
]
