from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.producto_list, name='lista'),
    path('crear/', views.producto_create, name='crear'),
    path('<int:pk>/', views.producto_detail, name='detalle'),
    path('<int:pk>/editar/', views.producto_update, name='editar'),
    path('<int:pk>/eliminar/', views.producto_delete, name='eliminar'),
    path('inicio/', views.inicio, name='inicio'),
]
