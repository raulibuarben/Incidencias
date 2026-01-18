# Formularios del proyecto de incidencias
from django import forms
from .models import Incidencia, Categoria

# Formulario para crear una categoría
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre de la categoría'})
        }

# Formulario para crear una incidencia
class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = ['titulo', 'descripcion', 'categoria', 'prioridad']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título de la incidencia'}),
            'descripcion': forms.Textarea(attrs={'placeholder': 'Descripción de la incidencia'}),
            'categoria': forms.Select(),
            'prioridad': forms.Select()
        }


# Formulario para editar únicamente el estado y la prioridad de una incidencia
class IncidenciaEstadoForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = ['estado', 'prioridad']
        widgets = {
            'estado': forms.Select()
        } 

