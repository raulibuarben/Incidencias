#URLs para aplicación de incidencias
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('incidencias/', views.listar_incidencias, name='listar_incidencias'),
    path('crearincidencia/', views.crear_incidencia, name='crear_incidencia'),
    path('editarincidencia/<int:incidencia_id>/', views.editar_incidencia, name='editar_incidencia'),
    path('pediridincidencia/', views.pedir_id_incidencia, name='pedir_id_incidencia'),
]
