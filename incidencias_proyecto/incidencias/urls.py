#URLs para aplicación de incidencias
from django.urls import path
from . import views

urlpatterns = [
    path('incidencias/', views.listar_incidencias, name='listar_incidencias'),
    path('crearincidencia/', views.crear_incidencia, name='crear_incidencia'),
    path('editarincidencia/<int:incidencia_id>/', views.editar_incidencia, name='editar_incidencia'),
]
