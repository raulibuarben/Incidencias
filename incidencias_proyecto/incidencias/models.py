from django.db import models

# Create your models here.
# Modelo para Categoría de Incidencia con nombre único
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

class Incidencia(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('En Proceso', 'En Proceso'),
        ('Resuelta', 'Resuelta'),
    ]

    PRIORIDADES = [
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
    ]

    # Corregido: Usamos validator para el mínimo de caracteres
    titulo = models.CharField(
        max_length=200, 
        validators=[MinLengthValidator(5, message="El título debe tener al menos 5 caracteres.")]
    )
    descripcion = models.TextField()
    # Asegúrate de tener el modelo Categoria definido arriba
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    prioridad = models.CharField(max_length=20, choices=PRIORIDADES, default='Media')

    def clean(self):
        """Lógica de validación del modelo"""
        # 1. Validación de resolución sin descripción
        # Nota: Como 'descripcion' es un TextField obligatorio por defecto, 
        # esta validación solo saltaría si permitieras blank=True.
        if self.estado == 'Resuelta' and not self.descripcion:
            raise ValidationError({
                'descripcion': "No se puede marcar como resuelta una incidencia sin descripción."
            })

        # 2. Validación de cambio de estado prohibido
        if self.pk:
            incidencia_original = Incidencia.objects.get(pk=self.pk)
            if incidencia_original.estado == 'Resuelta' and self.estado == 'Pendiente':
                raise ValidationError(
                    "Una incidencia resuelta no puede volver a estado pendiente."
                )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.titulo} ({self.estado})"
    