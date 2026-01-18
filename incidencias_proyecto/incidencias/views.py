from django.shortcuts import render, redirect

from .forms import IncidenciaForm, IncidenciaEstadoForm, MiFormulario
from .models import Incidencia

# Create your views here.
# Vista para listar incidencias
def listar_incidencias(request):
    incidencias = Incidencia.objects.all()
    return render(request, 'incidencias/listar_incidencias.html', {'incidencias': incidencias})


#Vista para crear una incidencia con el formulario
def crear_incidencia(request):
    if request.method == 'POST':
        form = IncidenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_incidencias')
    else:
        form = IncidenciaForm()
    return render(request, 'incidencias/crear_incidencia.html', {'form': form})


#Vista para formulario de edición de incidencia
def editar_incidencia(request, incidencia_id):
    incidencia = Incidencia.objects.get(id=incidencia_id)
    if request.method == 'POST':
        form = IncidenciaEstadoForm(request.POST, instance=incidencia)
        if form.is_valid():
            form.save()
            return redirect('listar_incidencias')
    else:
        form = IncidenciaEstadoForm(instance=incidencia)
    return render(request, 'incidencias/editar_incidencia.html', {'form': form, 'incidencia': incidencia})


#Vista para la página de inicio
def inicio(request):
    return render(request, 'incidencias/inicio.html')   

#Vista para pedir el id de la incidencia a editar
def pedir_id_incidencia(request):
    if request.method == 'POST':
        form = MiFormulario(request.POST)
        if form.is_valid():
            incidencia_id = form.cleaned_data['titulo'].id
            return redirect('editar_incidencia', incidencia_id=incidencia_id)
    else:
        form = MiFormulario()
    return render(request, 'incidencias/pedir_id_incidencia.html', {'form': form})