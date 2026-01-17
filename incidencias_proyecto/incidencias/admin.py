from django.contrib import admin

from .models import Categoria, Incidencia

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Incidencia)